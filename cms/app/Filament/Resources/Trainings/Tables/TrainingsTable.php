<?php

namespace App\Filament\Resources\Trainings\Tables;

use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Columns\ToggleColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Filters\TernaryFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;

class TrainingsTable
{
    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn (Builder $query) => $query->with('category')->withCount(['schedules as upcoming_count' => fn (Builder $q) => $q
                ->where('status', '!=', 'batal')->whereRaw('COALESCE(end_date, start_date) >= ?', [today()->toDateString()])]))
            ->columns([
                TextColumn::make('title')->label('Pelatihan')->searchable()->wrap()->limit(90),
                TextColumn::make('category.name')->label('Kategori')->badge(),
                TextColumn::make('upcoming_count')->label('Jadwal mendatang')->sortable()
                    ->badge()->color(fn ($state) => $state ? 'success' : 'gray'),
                TextColumn::make('price')->label('Harga')->money('IDR', locale: 'id')->placeholder('-'),
                ToggleColumn::make('is_published')->label('Tampil'),
            ])
            ->defaultSort(fn (Builder $query) => $query->orderBy('training_category_id')->orderBy('sort'))
            ->filters([
                SelectFilter::make('training_category_id')->label('Kategori')->relationship('category', 'name'),
                TernaryFilter::make('punya_jadwal')->label('Jadwal')
                    ->trueLabel('Ada jadwal mendatang')->falseLabel('Belum ada jadwal')
                    ->queries(
                        true: fn (Builder $query) => $query->whereHas('schedules', fn (Builder $q) => $q->upcoming()),
                        false: fn (Builder $query) => $query->whereDoesntHave('schedules', fn (Builder $q) => $q->upcoming()),
                    ),
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
