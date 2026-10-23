<?php

namespace App\Models;

use App\Notifications\RegistrationStatusChanged;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Notification;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Registration extends Model
{
    public const STATUSES = ['baru' => 'Baru', 'dikonfirmasi' => 'Dikonfirmasi', 'batal' => 'Batal'];

    protected $fillable = ['training_schedule_id', 'name', 'email', 'phone', 'organization', 'position', 'participants', 'participant_names', 'message', 'status', 'note'];

    protected $casts = ['participants' => 'integer'];

    protected static function booted(): void
    {
        // Pendaftar diberi tahu otomatis saat admin mengonfirmasi / membatalkan. Email gagal tidak menggagalkan simpan.
        static::updated(function (Registration $r) {
            if ($r->wasChanged('status') && in_array($r->status, ['dikonfirmasi', 'batal'], true)) {
                rescue(fn () => Notification::route('mail', $r->email)->notify(new RegistrationStatusChanged($r)));
            }
        });
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
}
