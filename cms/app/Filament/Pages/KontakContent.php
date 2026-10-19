<?php

namespace App\Filament\Pages;

use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;
use Filament\Support\Icons\Heroicon;

class KontakContent extends EditPageContent
{
    protected static string $contentKey = 'kontak';

    protected static ?string $title = 'Halaman Kontak';

    protected static ?string $navigationLabel = 'Halaman Kontak';

    protected static string | \BackedEnum | null $navigationIcon = Heroicon::OutlinedPhone;

    protected static string | \UnitEnum | null $navigationGroup = 'Konten Website';

    protected static ?int $navigationSort = 4;

    protected function fields(): array
    {
        return [
            PageFields::hero('kontak'),
            Section::make('Kontak & formulir')->collapsible()
                ->description('Telepon, WhatsApp, email, dan alamat diambil dari Pengaturan › Pengaturan Situs.')
                ->schema([
                    TextInput::make('title')->label('Judul'),
                    Textarea::make('intro')->label('Teks pengantar')->rows(3),
                    Repeater::make('subjects')->label('Pilihan "Keperluan" di formulir')
                        ->simple(TextInput::make('subject')->required())->defaultItems(0),
                    TextInput::make('map_url')->label('URL embed Google Maps')->url()
                        ->helperText('Google Maps › Bagikan › Sematkan peta › salin nilai src saja. Kosongkan untuk menyembunyikan peta.'),
                ]),
        ];
    }
}
