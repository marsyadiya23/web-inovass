<?php

namespace App\Filament\Resources\ContactMessages\Tables;

use App\Filament\Resources\ContactMessages\ContactMessageResource;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;

class ContactMessagesTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('created_at')->label('Diterima')->dateTime('d M Y H:i')->sortable(),
                TextColumn::make('name')->label('Nama')->searchable()->description(fn ($record) => $record->organization),
                TextColumn::make('email')->label('Email')->searchable()->copyable(),
                TextColumn::make('phone')->label('Telepon')->searchable()->toggleable(),
                TextColumn::make('subject')->label('Keperluan')->searchable(),
                TextColumn::make('message')->label('Pesan')->limit(60)->searchable()->toggleable(),
                TextColumn::make('status')->badge()
                    ->formatStateUsing(fn (string $state) => ContactMessageResource::STATUSES[$state] ?? $state)
                    ->color(fn (string $state) => ContactMessageResource::COLORS[$state] ?? 'gray'),
            ])
            ->defaultSort('created_at', 'desc')
            ->filters([
                SelectFilter::make('status')->options(ContactMessageResource::STATUSES),
            ])
            ->recordActions([
                EditAction::make()->label('Buka'),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    DeleteBulkAction::make(),
                ]),
            ]);
    }
}
