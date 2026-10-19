<?php

namespace App\Filament\Resources\TrainingCategories\Tables;

use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\ToggleColumn;
use Filament\Tables\Table;

class TrainingCategoriesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('name')->label('Kategori')->searchable(),
                TextColumn::make('trainings_count')->label('Jumlah program')->counts('trainings'),
                ToggleColumn::make('is_published')->label('Tampil'),
            ])
            ->reorderable('sort')
            ->defaultSort('sort')
            ->recordActions([EditAction::make()]);
    }
}
