<?php

namespace App\Filament\Resources\Clients\Schemas;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class ClientForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('Klien')->columns(2)->columnSpanFull()->schema([
                    TextInput::make('name')->label('Nama organisasi')->required()->maxLength(255)->columnSpanFull(),
                    FileUpload::make('logo')->label('Logo')->image()->disk('public')->directory('clients')->required()->columnSpanFull(),
                    TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                    Toggle::make('is_published')->label('Tampilkan')->default(true),
                ]),
            ]);
    }
}
