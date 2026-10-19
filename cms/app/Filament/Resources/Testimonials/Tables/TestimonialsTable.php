<?php

namespace App\Filament\Resources\Testimonials\Tables;

use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\ToggleColumn;
use Filament\Tables\Table;

class TestimonialsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('name')->label('Nama')->searchable()
                    ->description(fn ($record) => collect([$record->position, $record->organization])->filter()->join(' · ')),
                TextColumn::make('quote')->label('Kutipan')->limit(70)->searchable()->wrap(),
                TextColumn::make('rating')->label('Rating')->formatStateUsing(fn ($state) => str_repeat('★', (int) $state)),
                ToggleColumn::make('is_published')->label('Tampil'),
            ])
            ->reorderable('sort')
            ->defaultSort('sort')
            ->recordActions([
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ]);
    }
}
