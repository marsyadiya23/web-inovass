<?php

namespace App\Models;

use App\Notifications\RegistrationStatusChanged;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;
use Illuminate\Support\Facades\Notification;

class Registration extends Model
{
    /** Tahap alur kerja admin, berurutan. "batal" di luar urutan. */
    public const STATUSES = [
        'baru' => 'Baru',
        'dihubungi' => 'Dihubungi',
        'penawaran' => 'Penawaran dikirim',
        'dikonfirmasi' => 'Dikonfirmasi',
        'lunas' => 'Lunas',
        'selesai' => 'Selesai',
        'batal' => 'Batal',
    ];

    /** Tahap berikutnya untuk tombol "Lanjut" di admin. */
    public const NEXT = [
        'baru' => 'dihubungi',
        'dihubungi' => 'penawaran',
        'penawaran' => 'dikonfirmasi',
        'dikonfirmasi' => 'lunas',
        'lunas' => 'selesai',
    ];

    /** Masih perlu ditindaklanjuti admin sebelum terkonfirmasi. */
    public const OPEN = ['baru', 'dihubungi', 'penawaran'];

    public const COLORS = [
        'baru' => 'warning', 'dihubungi' => 'info', 'penawaran' => 'info',
        'dikonfirmasi' => 'primary', 'lunas' => 'success', 'selesai' => 'success', 'batal' => 'gray',
    ];

    protected $fillable = ['training_schedule_id', 'name', 'email', 'phone', 'organization', 'position', 'participants', 'participant_names', 'message', 'status', 'note'];

    protected $casts = ['participants' => 'integer'];

    protected static function booted(): void
    {
        static::created(fn (Registration $r) => $r->log(auth()->check() ? 'Ditambahkan oleh admin' : 'Mendaftar lewat website'));

        static::updated(function (Registration $r) {
            if ($r->wasChanged('status')) {
                $r->log('Tahap: '.(self::STATUSES[$r->getOriginal('status')] ?? $r->getOriginal('status')).' → '.(self::STATUSES[$r->status] ?? $r->status));
                // Pendaftar diberi tahu otomatis saat dikonfirmasi / dibatalkan. Email gagal tidak menggagalkan simpan.
                if (in_array($r->status, ['dikonfirmasi', 'batal'], true)) {
                    rescue(fn () => Notification::route('mail', $r->email)->notify(new RegistrationStatusChanged($r)));
                }
            }
            if ($r->wasChanged('note')) {
                $r->log('Catatan internal diperbarui');
            }
        });
    }

    /** Catat ke riwayat; pelaku = admin yang sedang login (kosong = pendaftar/sistem). */
    public function log(string $description): void
    {
        $this->activities()->create(['description' => $description, 'user_id' => auth()->id()]);
    }

    /** Pendaftaran baru yang belum dihubungi lebih dari 24 jam. */
    public function isOverdue(): bool
    {
        return $this->status === 'baru' && $this->created_at?->lt(now()->subDay());
    }

    /** Nomor pendaftaran untuk pendaftar & admin, mis. REG-2026-0042 (dari id, tanpa kolom tambahan). */
    public function code(): string
    {
        return 'REG-'.($this->created_at ?? now())->format('Y').'-'.str_pad((string) $this->id, 4, '0', STR_PAD_LEFT);
    }

    /** Harga per peserta × jumlah peserta; null bila jadwal/program belum punya harga. Untuk admin. */
    public function estimatedTotal(): ?int
    {
        $price = $this->schedule?->effectivePrice();

        return $price === null ? null : $price * $this->participants;
    }

    public function schedule(): BelongsTo
    {
        return $this->belongsTo(TrainingSchedule::class, 'training_schedule_id');
    }

    public function activities(): HasMany
    {
        return $this->hasMany(RegistrationActivity::class)->latest('id');
    }
}
