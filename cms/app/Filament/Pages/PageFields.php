<?php

namespace App\Filament\Pages;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;

/** Bagian form yang sama di halaman Tentang/Produk/Kontak (hero + CTA band). */
class PageFields
{
    public static function hero(string $dir): Section
    {
        return Section::make('Hero (bagian atas)')->columns(2)->collapsible()->schema([
            TextInput::make('hero_title')->label('Judul')->required(),
            TextInput::make('hero_em')->label('Judul baris kedua (hijau)'),
            Textarea::make('hero_desc')->label('Deskripsi')->helperText('Juga dipakai sebagai meta description')->rows(2)->columnSpanFull(),
            FileUpload::make('hero_image')->label('Gambar latar')->image()->disk('public')->directory($dir)->columnSpanFull(),
        ]);
    }

    public static function cta(): Section
    {
        return Section::make('Ajakan (CTA) bawah halaman')->columns(2)->collapsible()->schema([
            TextInput::make('cta_title')->label('Judul'),
            TextInput::make('cta_em')->label('Judul baris kedua (hijau)'),
            TextInput::make('cta_text')->label('Teks')->columnSpanFull(),
            TextInput::make('cta_button')->label('Label tombol (menuju halaman Kontak)'),
        ]);
    }
}
