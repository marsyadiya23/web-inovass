<?php

use Illuminate\Support\Facades\Storage;
use Illuminate\Support\Str;

if (! function_exists('media_url')) {
    /**
     * Path gambar dari DB ke URL publik.
     * "assets/..." = aset bawaan situs lama di public/, selain itu = upload Filament di disk public.
     */
    function media_url(?string $path): ?string
    {
        if (blank($path)) {
            return null;
        }
        if (Str::startsWith($path, ['http://', 'https://'])) {
            return $path;
        }
        if (Str::startsWith($path, 'assets/')) {
            return asset(str_replace(' ', '%20', $path));
        }

        return Storage::disk('public')->url($path);
    }
}
