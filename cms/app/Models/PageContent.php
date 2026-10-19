<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * Konten singleton per key: settings, home, tentang, produk, kontak.
 * Pakai PageContent::get('home') di view/controller untuk array datanya.
 */
class PageContent extends Model
{
    protected $fillable = ['key', 'data'];

    protected $casts = ['data' => 'array'];

    private static array $memo = [];

    public static function get(string $key): array
    {
        return self::$memo[$key] ??= self::where('key', $key)->first()?->data ?? [];
    }

    public static function put(string $key, array $data): void
    {
        self::updateOrCreate(['key' => $key], ['data' => $data]);
        unset(self::$memo[$key]);
    }
}
