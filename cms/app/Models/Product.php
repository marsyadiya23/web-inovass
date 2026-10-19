<?php

namespace App\Models;

use App\Models\Concerns\Publishable;
use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    use Publishable;

    protected $guarded = ['id'];

    protected $casts = ['is_published' => 'boolean', 'features' => 'array'];
}
