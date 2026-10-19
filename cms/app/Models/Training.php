<?php

namespace App\Models;

use App\Models\Concerns\Publishable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Training extends Model
{
    use Publishable;

    protected $guarded = ['id'];

    protected $casts = ['is_published' => 'boolean', 'highlights' => 'array', 'price' => 'integer'];

    public function category(): BelongsTo
    {
        return $this->belongsTo(TrainingCategory::class, 'training_category_id');
    }

    public function schedules(): HasMany
    {
        return $this->hasMany(TrainingSchedule::class);
    }

    /** Jadwal yang belum lewat dan tidak dibatalkan, urut tanggal. */
    public function upcomingSchedules(): HasMany
    {
        return $this->schedules()->upcoming();
    }

    public function url(): string
    {
        return route('pelatihan.show', $this->slug);
    }
}
