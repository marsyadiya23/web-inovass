<?php

namespace App\Filament\Widgets;

use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\Registrations\Tables\RegistrationsTable;
use App\Models\Registration;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Filament\Widgets\TableWidget;

class LatestRegistrations extends TableWidget
{
    protected static ?int $sort = 3;

    protected int|string|array $columnSpan = 'full';

    public function table(Table $table): Table
    {
        return $table
            ->heading('Pendaftar Terbaru')
            ->query(Registration::query()->with('schedule.training')->latest()->limit(5))
            ->paginated(false)
            ->columns([
                TextColumn::make('name')->label('Nama')->description(fn (Registration $r) => $r->organization),
                TextColumn::make('schedule.training.title')->label('Pelatihan')->wrap()->limit(60)
                    ->description(fn (Registration $r) => $r->schedule?->dateLabel()),
                TextColumn::make('participants')->label('Peserta'),
                TextColumn::make('status')->label('Status')->badge()
                    ->formatStateUsing(fn ($state) => Registration::STATUSES[$state] ?? $state)
                    ->color(fn ($state) => RegistrationsTable::COLORS[$state] ?? 'gray'),
                TextColumn::make('created_at')->label('Masuk')->since(),
            ])
            ->recordUrl(fn (Registration $record) => RegistrationResource::getUrl('edit', ['record' => $record]))
            ->emptyStateHeading('Belum ada pendaftar');
    }
}
