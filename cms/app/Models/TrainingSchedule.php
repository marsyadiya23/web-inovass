<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class TrainingSchedule extends Model
{
    public const METHODS = ['offline' => 'Tatap muka', 'online' => 'Online', 'hybrid' => 'Hybrid'];

    public const STATUSES = ['dibuka' => 'Dibuka', 'penuh' => 'Penuh', 'ditutup' => 'Ditutup', 'batal' => 'Batal'];

    protected $guarded = ['id'];

    protected $casts = [
        'start_date' => 'date',
        'end_date' => 'date',
        'registration_deadline' => 'date',
        'price' => 'integer',
        'quota' => 'integer',
    ];

    public function training(): BelongsTo
    {
        return $this->belongsTo(Training::class);
    }

    public function registrations(): HasMany
    {
        return $this->hasMany(Registration::class);
    }

    /** Belum lewat (tanggal selesai/mulai >= hari ini), tidak batal, program tampil. */
    public function scopeUpcoming(Builder $q): Builder
    {
        return $q->where('status', '!=', 'batal')
            ->whereRaw('COALESCE(end_date, start_date) >= ?', [today()->toDateString()])
            ->orderBy('start_date');
    }

    public function scopeVisible(Builder $q): Builder
    {
        return $q->upcoming()->whereHas('training', fn ($t) => $t->where('is_published', true)
            ->whereHas('category', fn ($c) => $c->where('is_published', true)));
    }

    public function effectivePrice(): ?int
    {
        return $this->price ?? $this->training?->price;
    }

    public function priceLabel(): string
    {
        $p = $this->effectivePrice();

        return match (true) {
            $p === null => 'Hubungi kami',
            $p === 0 => 'Gratis',
            default => 'Rp '.number_format($p, 0, ',', '.'),
        };
    }

    /** Peserta terdaftar (tidak termasuk yang batal). */
    public function seatsTaken(): int
    {
        return (int) $this->registrations()->where('status', '!=', 'batal')->sum('participants');
    }

    public function seatsLeft(): ?int
    {
        return $this->quota === null ? null : max(0, $this->quota - $this->seatsTaken());
    }

    /** Bisa daftar: status dibuka, belum lewat batas daftar / tanggal mulai, kuota belum habis. */
    public function isOpen(): bool
    {
        $deadline = $this->registration_deadline ?? $this->start_date;

        return $this->status === 'dibuka'
            && today()->lte($deadline)
            && ($this->seatsLeft() === null || $this->seatsLeft() > 0);
    }

    /** Label status untuk publik, termasuk status turunan (kuota habis / pendaftaran tutup). */
    public function publicStatus(): string
    {
        if ($this->status !== 'dibuka') {
            return self::STATUSES[$this->status] ?? $this->status;
        }
        if ($this->seatsLeft() === 0) {
            return 'Penuh';
        }

        return $this->isOpen() ? 'Dibuka' : 'Pendaftaran ditutup';
    }

    public function dateLabel(): string
    {
        $s = $this->start_date;
        $e = $this->end_date;
        if (! $e || $e->isSameDay($s)) {
            return $s->translatedFormat('j F Y');
        }
        if ($s->isSameMonth($e)) {
            return $s->format('j').'–'.$e->translatedFormat('j F Y');
        }

        return $s->translatedFormat('j M').' – '.$e->translatedFormat('j M Y');
    }

    public function methodLabel(): string
    {
        return self::METHODS[$this->method] ?? $this->method;
    }
}
