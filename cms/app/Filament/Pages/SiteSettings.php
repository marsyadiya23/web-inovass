<?php

namespace App\Filament\Pages;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Support\Icons\Heroicon;

class SiteSettings extends EditPageContent
{
    protected static string $contentKey = 'settings';

    protected static ?string $title = 'Pengaturan Situs';

    protected static ?string $navigationLabel = 'Pengaturan Situs';

    protected static string | \BackedEnum | null $navigationIcon = Heroicon::OutlinedCog6Tooth;

    protected static string | \UnitEnum | null $navigationGroup = 'Pengaturan';

    protected static ?int $navigationSort = 99;

    protected function fields(): array
    {
        return [
            Section::make('Identitas')->columns(2)->schema([
                TextInput::make('site_name')->label('Nama situs')->required(),
                TextInput::make('tagline')->label('Tagline'),
                Textarea::make('description')->label('Deskripsi singkat (footer & meta)')->rows(3)->columnSpanFull(),
                FileUpload::make('logo')->label('Logo')->image()->disk('public')->directory('settings')->columnSpanFull(),
            ]),
            Section::make('Pelatihan')->schema([
                Toggle::make('show_prices')->label('Tampilkan harga pelatihan di website')
                    ->helperText('Mati = semua jadwal menampilkan "Hubungi kami"; harga tetap tersimpan dan tetap dikirim ke admin (email & Excel). Saat aktif, harga satu jadwal masih bisa disembunyikan di form jadwal.'),
            ]),
            Section::make('Kontak')->columns(2)->schema([
                TextInput::make('phone')->label('Telepon (tampilan)'),
                TextInput::make('whatsapp')->label('Nomor WhatsApp')->helperText('Format 62xxxxxxxxxx tanpa + atau spasi')->regex('/^62\d{8,13}$/'),
                TextInput::make('email')->label('Email')->email(),
                Textarea::make('address')->label('Alamat (satu baris per enter)')->rows(4),
            ]),
            Section::make('Media sosial')->schema([
                Repeater::make('socials')->hiddenLabel()->columns(2)->defaultItems(0)->schema([
                    Select::make('platform')->options([
                        'instagram' => 'Instagram', 'linkedin' => 'LinkedIn', 'youtube' => 'YouTube',
                        'facebook' => 'Facebook', 'tiktok' => 'TikTok', 'x' => 'X',
                    ])->required(),
                    TextInput::make('url')->label('URL')->url()->helperText('Kosongkan untuk menyembunyikan'),
                ]),
            ]),
            Section::make('Footer')->schema([
                TextInput::make('copyright')->label('Teks copyright')->helperText('{tahun} diganti tahun berjalan'),
            ]),
        ];
    }
}
