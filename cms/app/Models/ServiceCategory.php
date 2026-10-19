<?php

namespace App\Models;

use App\Models\Concerns\Publishable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\HasMany;

class ServiceCategory extends Model
{
    use Publishable;

    protected $guarded = ['id'];

    protected $casts = ['is_published' => 'boolean'];

    public function services(): HasMany
    {
        return $this->hasMany(Service::class);
    }

    /** Layanan level 3 (tanpa parent) yang tampil di hub kategori. */
    public function topServices(): HasMany
    {
        return $this->services()->whereNull('parent_id');
    }

    public function url(): string
    {
        return url("layanan/{$this->slug}/index.html");
    }
}
