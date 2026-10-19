<?php

namespace App\Filament\Widgets;

use App\Filament\Resources\TrainingSchedules\Tables\TrainingSchedulesTable;
use App\Filament\Resources\TrainingSchedules\TrainingScheduleResource;
use App\Models\TrainingSchedule;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;
use Filament\Widgets\TableWidget;

class UpcomingSchedules extends TableWidget
{
    protected static ?int $sort = 2;

    protected int|string|array $columnSpan = 'full';

    public function table(Table $table): Table
    {
        return $table
            ->heading('Jadwal Terdekat')
            ->query(TrainingSchedule::upcoming()->with('training')
                ->withSum(['registrations as seats_taken' => fn ($q) => $q->where('status', '!=', 'batal')], 'participants')
                ->limit(6))
            ->paginated(false)
            ->columns([
                TextColumn::make('start_date')->label('Tanggal')
                    ->formatStateUsing(fn ($state, TrainingSchedule $record) => $record->dateLabel()),
                TextColumn::make('training.title')->label('Program')->wrap()->limit(70),
                TextColumn::make('method')->label('Metode')->badge()
                    ->formatStateUsing(fn ($state) => TrainingSchedule::METHODS[$state] ?? $state),
                TextColumn::make('seats_taken')->label('Peserta')->default(0)
                    ->formatStateUsing(fn ($state, TrainingSchedule $record) => (int) $state.($record->quota ? ' / '.$record->quota : '')),
                TextColumn::make('status')->label('Status')->badge()
                    ->formatStateUsing(fn ($state) => TrainingSchedule::STATUSES[$state] ?? $state)
                    ->color(fn ($state) => TrainingSchedulesTable::STATUS_COLORS[$state] ?? 'gray'),
            ])
            ->recordUrl(fn (TrainingSchedule $record) => TrainingScheduleResource::getUrl('edit', ['record' => $record]))
            ->emptyStateHeading('Belum ada jadwal mendatang');
    }
}
