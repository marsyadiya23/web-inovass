<?php

namespace App\Filament\Pages;

use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;
use Filament\Support\Icons\Heroicon;

class ProdukContent extends EditPageContent
{
    protected static string $contentKey = 'produk';

    protected static ?string $title = 'Halaman Produk';

    protected static ?string $navigationLabel = 'Halaman Produk';

    protected static string | \BackedEnum | null $navigationIcon = Heroicon::OutlinedSquares2x2;

    protected static string | \UnitEnum | null $navigationGroup = 'Konten Website';

    protected static ?int $navigationSort = 3;

    protected function fields(): array
    {
        return [
            PageFields::hero('produk'),
            Section::make('Daftar produk')->collapsible()
                ->description('Isi produk diatur di menu Koleksi › Produk.')
                ->schema([TextInput::make('section_title')->label('Judul bagian')]),
            PageFields::cta(),
        ];
    }
}
