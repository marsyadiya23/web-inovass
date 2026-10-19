<?php

namespace App\Models\Concerns;

use Illuminate\Database\Eloquent\Builder;

trait Publishable
{
    public function scopePublished(Builder $q): Builder
    {
        return $q->where('is_published', true)->orderBy('sort')->orderBy('id');
    }
}
