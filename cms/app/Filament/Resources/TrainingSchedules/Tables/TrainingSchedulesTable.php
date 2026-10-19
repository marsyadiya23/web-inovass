<?php

namespace App\Filament\Resources\TrainingSchedules\Tables;

use App\Models\TrainingSchedule;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteAction;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Actions\ReplicateAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Filters\TernaryFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;

class TrainingSchedulesTable
{
    public const STATUS_COLORS = ['dibuka' => 'success', 'penuh' => 'warning', 'ditutup' => 'gray', 'batal' => 'danger'];

    public static function configure(Table $table): Table
    {
        return self::base($table, withTraining: true)
            ->filters([
                TernaryFilter::make('waktu')->label('Waktu')
                    ->trueLabel('Akan datang')->falseLabel('Sudah lewat')->default(true)
                    ->queries(
                        true: fn (Builder $query) => $query->whereRaw('COALESCE(end_date, start_date) >= ?', [today()->toDateString()]),
                        false: fn (Builder $query) => $query->whereRaw('COALESCE(end_date, start_date) < ?', [today()->toDateString()]),
                    ),
                SelectFilter::make('category')->label('Kategori')
                    ->relationship('training.category', 'name'),
                SelectFilter::make('method')->label('Metode')->options(TrainingSchedule::METHODS),
                SelectFilter::make('status')->label('Status')->options(TrainingSchedule::STATUSES),
            ]);
    }

    /** Kolom & aksi bersama untuk menu Jadwal dan relation manager di Program. */
    public static function base(Table $table, bool $withTraining): Table
    {
        return $table
            ->modifyQueryUsing(fn (Builder $query) => $query->with('training')->withSum(
                ['registrations as seats_taken' => fn (Builder $q) => $q->where('status', '!=', 'batal')], 'participants'))
            ->columns(array_filter([
                TextColumn::make('start_date')->label('Tanggal')->sortable()
                    ->formatStateUsing(fn ($state, TrainingSchedule $record) => $record->dateLabel())
                    ->description(fn (TrainingSchedule $record) => $record->time),
                $withTraining ? TextColumn::make('training.title')->label('Program')->searchable()->wrap()->limit(70) : null,
                TextColumn::make('method')->label('Metode')->badge()
                    ->formatStateUsing(fn ($state) => TrainingSchedule::METHODS[$state] ?? $state)
                    ->description(fn (TrainingSchedule $record) => $record->location),
                TextColumn::make('price')->label('Biaya')
                    ->state(fn (TrainingSchedule $record) => $record->effectivePrice())
                    ->money('IDR', locale: 'id')->placeholder('-'),
                TextColumn::make('seats_taken')->label('Peserta')
                    ->formatStateUsing(fn ($state, TrainingSchedule $record) => (int) $state.($record->quota ? ' / '.$record->quota : ''))
                    ->default(0),
                TextColumn::make('status')->label('Status')->badge()
                    ->formatStateUsing(fn ($state) => TrainingSchedule::STATUSES[$state] ?? $state)
                    ->color(fn ($state) => self::STATUS_COLORS[$state] ?? 'gray'),
            ]))
            ->defaultSort('start_date')
            ->recordActions([
                EditAction::make(),
                ReplicateAction::make()->label('Duplikat')
                    ->excludeAttributes(['seats_taken'])
                    ->successNotificationTitle('Jadwal diduplikat, silakan ubah tanggalnya'),
                DeleteAction::make(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([DeleteBulkAction::make()]),
            ]);
    }
}
