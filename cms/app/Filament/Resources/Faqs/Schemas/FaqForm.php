<?php

namespace App\Filament\Resources\Faqs\Schemas;

use Filament\Forms\Components\RichEditor;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class FaqForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->components([
                Section::make('FAQ')->columns(2)->columnSpanFull()->schema([
                    TextInput::make('question')->label('Pertanyaan')->required()->maxLength(255)->columnSpanFull(),
                    RichEditor::make('answer')->label('Jawaban')->required()->columnSpanFull()
                        ->toolbarButtons([['bold', 'italic', 'link'], ['bulletList', 'orderedList'], ['undo', 'redo']]),
                    TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                    Toggle::make('is_published')->label('Tampilkan')->default(true),
                ]),
            ]);
    }
}
