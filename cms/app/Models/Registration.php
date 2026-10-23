<?php

namespace App\Models;

use App\Notifications\RegistrationStatusChanged;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Notification;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Registration extends Model
{
    public const STATUSES = ['baru' => 'Baru', 'dikonfirmasi' => 'Dikonfirmasi', 'batal' => 'Batal'];

    protected $fillable = ['training_schedule_id', 'name', 'email', 'phone', 'organization', 'position', 'participants', 'message', 'status', 'note'];

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

    public function schedule(): BelongsTo
    {
        return $this->belongsTo(TrainingSchedule::class, 'training_schedule_id');
    }
}
