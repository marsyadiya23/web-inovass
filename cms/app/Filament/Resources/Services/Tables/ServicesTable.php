<?php

namespace App\Filament\Resources\Services\Tables;

use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\ToggleColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Filters\TernaryFilter;
use Filament\Tables\Table;

class ServicesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn ($query) => $query->with(['category', 'parent']))
            ->columns([
                TextColumn::make('title')->label('Judul')->searchable()->wrap()->limit(90),
                TextColumn::make('category.name')->label('Kategori')->badge(),
                TextColumn::make('parent.title')->label('Induk')->limit(40)->placeholder('Layanan utama')->color('gray'),
                TextColumn::make('sort')->label('Urutan')->sortable(),
                ToggleColumn::make('is_published')->label('Tampil'),
            ])
            ->defaultSort(fn ($query) => $query->orderBy('service_category_id')->orderBy('parent_id')->orderBy('sort'))
            ->filters([
                SelectFilter::make('service_category_id')->label('Kategori')->relationship('category', 'name'),
                TernaryFilter::make('level')->label('Level')
                    ->trueLabel('Layanan utama')->falseLabel('Sub-layanan')
                    ->queries(
                        true: fn ($query) => $query->whereNull('parent_id'),
                        false: fn ($query) => $query->whereNotNull('parent_id'),
                    ),
                SelectFilter::make('parent_id')->label('Induk')
                    ->relationship('parent', 'title', fn ($query) => $query->whereNull('parent_id'))->searchable()->preload(),
                TernaryFilter::make('is_published')->label('Status tampil'),
            ])
            ->recordActions([
                Action::make('lihat')->label('Lihat')->icon('heroicon-o-arrow-top-right-on-square')
                    ->url(fn ($record) => $record->url())->openUrlInNewTab(),
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([DeleteBulkAction::make()]),
            ]);
    }
}
