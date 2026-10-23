<?php

namespace App\Filament\Resources\Registrations\RelationManagers;

use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

/** Riwayat pendaftaran (hanya baca): kapan daftar, siapa mengubah tahap, kapan. */
class ActivitiesRelationManager extends RelationManager
{
    protected static string $relationship = 'activities';

    protected static ?string $title = 'Riwayat';

    public function isReadOnly(): bool
    {
        return true;
    }

    public function table(Table $table): Table
    {
        return $table
            ->columns([
                TextColumn::make('created_at')->label('Waktu')->dateTime('d M Y H:i'),
                TextColumn::make('description')->label('Kejadian')->wrap(),
                TextColumn::make('user.name')->label('Oleh')->default('Pendaftar / sistem'),
            ])
            ->paginated([10, 25]);
    }
}
