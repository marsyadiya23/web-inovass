<?php

namespace App\Filament\Resources\Articles\Tables;

use App\Filament\Resources\Articles\Schemas\ArticleForm;
use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\ImageColumn;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\ToggleColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;

class ArticlesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                ImageColumn::make('cover')->label('Sampul')->disk('public'),
                TextColumn::make('title')->label('Judul')->searchable()->wrap()->limit(80),
                TextColumn::make('category')->label('Kategori')->badge(),
                TextColumn::make('published_at')->label('Terbit')->dateTime('d M Y H:i')->sortable(),
                ToggleColumn::make('is_published')->label('Tampil'),
            ])
            ->defaultSort('published_at', 'desc')
            ->filters([
                SelectFilter::make('category')->label('Kategori')->options(ArticleForm::CATEGORIES),
            ])
            ->recordActions([
                Action::make('lihat')->label('Lihat')->icon('heroicon-o-arrow-top-right-on-square')
                    ->url(fn ($record) => $record->url())->openUrlInNewTab(),
                EditAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ]);
    }
}
