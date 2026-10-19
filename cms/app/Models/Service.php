<?php

namespace App\Models;

use App\Models\Concerns\Publishable;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

class Service extends Model
{
    use Publishable;

    protected $guarded = ['id'];

    protected $casts = ['is_published' => 'boolean', 'highlights' => 'array'];

    public function category(): BelongsTo
    {
        return $this->belongsTo(ServiceCategory::class, 'service_category_id');
    }

    public function parent(): BelongsTo
    {
        return $this->belongsTo(Service::class, 'parent_id');
    }

    public function children(): HasMany
    {
        return $this->hasMany(Service::class, 'parent_id');
    }

    /** URL lama dipertahankan: /layanan/{kategori}/{slug}.html */
    public function url(): string
    {
        return url("layanan/{$this->category->slug}/{$this->slug}.html");
    }
}
