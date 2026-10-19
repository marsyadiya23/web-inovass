<?php

namespace App\Models;

use App\Models\Concerns\Publishable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class TrainingCategory extends Model
{
    use Publishable;

    protected $guarded = ['id'];

    protected $casts = ['is_published' => 'boolean'];

    public function trainings(): HasMany
    {
        return $this->hasMany(Training::class);
    }
}
