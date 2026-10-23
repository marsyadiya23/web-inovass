<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class RegistrationActivity extends Model
{
    protected $fillable = ['registration_id', 'user_id', 'description'];

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}
