<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Registration extends Model
{
    public const STATUSES = ['baru' => 'Baru', 'dikonfirmasi' => 'Dikonfirmasi', 'batal' => 'Batal'];

    protected $fillable = ['training_schedule_id', 'name', 'email', 'phone', 'organization', 'position', 'participants', 'message', 'status', 'note'];

    protected $casts = ['participants' => 'integer'];

    public function schedule(): BelongsTo
    {
        return $this->belongsTo(TrainingSchedule::class, 'training_schedule_id');
    }
}
