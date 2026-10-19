<?php

namespace App\Filament\Resources\TrainingCategories\Schemas;

use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Set;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class TrainingCategoryForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components([
            Section::make()->columnSpanFull()->columns(2)->schema([
                TextInput::make('name')->label('Nama kategori')->required()->maxLength(255)
                    ->live(onBlur: true)
                    ->afterStateUpdated(fn (?string $state, Set $set, string $operation) => $operation === 'create' ? $set('slug', Str::slug($state ?? '')) : null),
                TextInput::make('slug')->required()->alphaDash()->unique(ignoreRecord: true),
                Textarea::make('description')->label('Deskripsi')->rows(3)->columnSpanFull(),
                TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                Toggle::make('is_published')->label('Tampilkan')->default(true),
            ]),
        ]);
    }
}
