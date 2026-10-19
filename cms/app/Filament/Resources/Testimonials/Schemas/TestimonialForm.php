<?php

namespace App\Filament\Resources\Testimonials\Schemas;

use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class TestimonialForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('Testimoni')->columns(2)->columnSpanFull()->schema([
                    Textarea::make('quote')->label('Kutipan')->required()->rows(4)->columnSpanFull(),
                    TextInput::make('name')->label('Nama')->required()->maxLength(255),
                    TextInput::make('position')->label('Jabatan')->placeholder('Mis. Kepala Lab')->maxLength(255),
                    TextInput::make('organization')->label('Organisasi')->placeholder('Mis. BBLK Jakarta')->maxLength(255),
                    Select::make('rating')->label('Rating')->required()->default(5)->selectablePlaceholder(false)
                        ->options([5 => '★★★★★ (5)', 4 => '★★★★ (4)', 3 => '★★★ (3)', 2 => '★★ (2)', 1 => '★ (1)']),
                    TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                    Toggle::make('is_published')->label('Tampilkan')->default(true),
                ]),
            ]);
    }
}
