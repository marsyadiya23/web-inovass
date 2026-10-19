<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    
    protected $guarded = ['id'];

    public function scopePublished(Builder $q): Builder
    {
        return $q->where('is_published', true)->where('published_at', '<=', now())->latest('published_at');
    }

    public function url(): string
    {
        return url("berita/{$this->slug}");
    }

    protected $casts = ['is_published' => 'boolean', 'published_at' => 'datetime'];
}
