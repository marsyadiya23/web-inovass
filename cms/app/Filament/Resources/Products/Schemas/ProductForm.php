<?php

namespace App\Filament\Resources\Products\Schemas;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Set;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class ProductForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('Produk')->columns(2)->columnSpanFull()->schema([
                    TextInput::make('name')->label('Nama produk')->required()->maxLength(255)
                        ->live(onBlur: true)
                        ->afterStateUpdated(fn (?string $state, Set $set, string $operation) => $operation === 'create' ? $set('slug', Str::slug($state ?? '')) : null),
                    TextInput::make('slug')->required()->maxLength(255)->unique(ignoreRecord: true)->alphaDash(),
                    TextInput::make('tagline')->label('Nama lengkap / tagline')->helperText('Mis. Document Control System (DCS)')->maxLength(255),
                    TextInput::make('button_label')->label('Label tombol')->placeholder('Hubungi Kami')->maxLength(255),
                    Textarea::make('description')->label('Deskripsi')->rows(4)->columnSpanFull(),
                    Repeater::make('features')->label('Fitur')->simple(TextInput::make('feature')->required())
                        ->defaultItems(0)->reorderable()->columnSpanFull(),
                    FileUpload::make('image')->label('Gambar / screenshot')->image()->disk('public')->directory('products')->columnSpanFull(),
                    TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                    Toggle::make('is_published')->label('Tampilkan')->default(true),
                ]),
            ]);
    }
}
