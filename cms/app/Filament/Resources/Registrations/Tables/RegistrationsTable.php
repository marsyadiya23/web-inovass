<?php

namespace App\Filament\Resources\Registrations\Tables;

use App\Exports\RegistrationsExport;
use App\Models\Registration;
use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;

class RegistrationsTable
{
    public const COLORS = ['baru' => 'warning', 'dikonfirmasi' => 'success', 'batal' => 'gray'];

    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn (Builder $query) => $query->with('schedule.training'))
            ->columns([
                TextColumn::make('created_at')->label('Masuk')->dateTime('d M Y H:i')->sortable(),
                TextColumn::make('name')->label('Nama')->searchable()
                    ->description(fn (Registration $r) => trim($r->position.($r->position && $r->organization ? ', ' : '').$r->organization)),
                TextColumn::make('phone')->label('Kontak')->searchable()->description(fn (Registration $r) => $r->email),
                TextColumn::make('schedule.training.title')->label('Pelatihan')->wrap()->limit(60)
                    ->description(fn (Registration $r) => $r->schedule?->dateLabel()),
                TextColumn::make('participants')->label('Peserta'),
                TextColumn::make('status')->label('Status')->badge()
                    ->formatStateUsing(fn ($state) => Registration::STATUSES[$state] ?? $state)
                    ->color(fn ($state) => self::COLORS[$state] ?? 'gray'),
            ])
            ->defaultSort('created_at', 'desc')
            ->filters([
                SelectFilter::make('status')->label('Status')->options(Registration::STATUSES),
                SelectFilter::make('training_schedule_id')->label('Jadwal')
                    ->relationship('schedule', 'id', fn (Builder $query) => $query->with('training')->orderByDesc('start_date'))
                    ->getOptionLabelFromRecordUsing(fn ($record) => $record->training->title.' — '.$record->dateLabel())
                    ->searchable()->preload(),
            ])
            ->headerActions([
                Action::make('export')->label('Ekspor Excel')->icon('heroicon-o-arrow-down-tray')->color('gray')
                    ->tooltip('Mengikuti filter yang sedang aktif (status, jadwal)')
                    ->action(fn ($livewire) => RegistrationsExport::download(
                        $livewire->getFilteredSortedTableQuery(), 'pendaftar-'.now()->format('Y-m-d').'.xlsx')),
            ])
            ->recordActions([
                Action::make('wa')->label('WhatsApp')->icon('heroicon-o-chat-bubble-left-right')->color('success')
                    ->url(fn (Registration $r) => 'https://wa.me/'.preg_replace('/^0/', '62', preg_replace('/\D/', '', $r->phone)))
                    ->openUrlInNewTab(),
                EditAction::make()->label('Proses'),
            ])
            ->toolbarActions([
                BulkActionGroup::make([DeleteBulkAction::make()]),
            ]);
    }
}
