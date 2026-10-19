<?php

namespace App\Filament\Resources\ServiceCategories\Tables;

use Filament\Actions\Action;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\ToggleColumn;
use Filament\Tables\Table;

class ServiceCategoriesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('name')->label('Kategori')->searchable(),
                TextColumn::make('slug')->color('gray'),
                TextColumn::make('services_count')->label('Jumlah layanan')->counts('services'),
                ToggleColumn::make('is_published')->label('Tampil'),
            ])
            ->reorderable('sort')
            ->defaultSort('sort')
            ->recordActions([
                Action::make('lihat')->label('Lihat')->icon('heroicon-o-arrow-top-right-on-square')
                    ->url(fn ($record) => $record->url())->openUrlInNewTab(),
                EditAction::make(),
            ]);
    }
}
