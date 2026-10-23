<?php

namespace App\Filament\Resources\Registrations\Tables;

use App\Exports\RegistrationsExport;
use App\Models\Registration;
use Filament\Actions\Action;
use Filament\Actions\BulkAction;
use Filament\Actions\BulkActionGroup;
use Filament\Actions\DeleteBulkAction;
use Filament\Actions\EditAction;
use Filament\Forms\Components\Select;
use Filament\Notifications\Notification;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Filters\SelectFilter;
use Filament\Tables\Table;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Support\Collection;

class RegistrationsTable
{
    public const COLORS = Registration::COLORS;

    public static function configure(Table $table): Table
    {
        return $table
            ->modifyQueryUsing(fn (Builder $query) => $query->with('schedule.training'))
            ->columns([
                TextColumn::make('created_at')->label('Masuk')->dateTime('d M Y H:i')->sortable()
                    ->description(fn (Registration $r) => $r->code().($r->isOverdue() ? ' · ⚠ belum dihubungi >24 jam' : '')),
                TextColumn::make('name')->label('Nama')->searchable()
                    ->description(fn (Registration $r) => trim($r->position.($r->position && $r->organization ? ', ' : '').$r->organization)),
                TextColumn::make('phone')->label('Kontak')->searchable()->description(fn (Registration $r) => $r->email),
                TextColumn::make('schedule.training.title')->label('Pelatihan')->wrap()->limit(60)
                    ->description(fn (Registration $r) => $r->schedule?->dateLabel()),
                TextColumn::make('participants')->label('Peserta'),
                self::statusColumn(),
            ])
            ->defaultSort('created_at', 'desc')
            ->filters([
                SelectFilter::make('training_schedule_id')->label('Jadwal')
                    ->relationship('schedule', 'id', fn (Builder $query) => $query->with('training')->orderByDesc('start_date'))
                    ->getOptionLabelFromRecordUsing(fn ($record) => $record->training->title.' — '.$record->dateLabel())
                    ->searchable()->preload(),
            ])
            ->headerActions([
                Action::make('export')->label('Ekspor Excel')->icon('heroicon-o-arrow-down-tray')->color('gray')
                    ->tooltip('Mengikuti tab & filter yang sedang aktif')
                    ->action(fn ($livewire) => RegistrationsExport::download(
                        $livewire->getFilteredSortedTableQuery(), 'pendaftar-'.now()->format('Y-m-d').'.xlsx')),
            ])
            ->recordActions([
                self::nextAction(),
                self::whatsappAction(),
                EditAction::make()->label('Detail'),
            ])
            ->toolbarActions([
                BulkActionGroup::make([
                    self::bulkStatusAction(),
                    DeleteBulkAction::make(),
                ]),
            ]);
    }

    public static function statusColumn(): TextColumn
    {
        return TextColumn::make('status')->label('Tahap')->badge()
            ->formatStateUsing(fn ($state) => Registration::STATUSES[$state] ?? $state)
            ->color(fn ($state) => Registration::COLORS[$state] ?? 'gray');
    }

    /** "→ Dihubungi", "→ Penawaran dikirim", dst. Konfirmasi dulu bila tahap berikutnya mengirim email ke pendaftar. */
    public static function nextAction(): Action
    {
        return Action::make('next')
            ->label(fn (Registration $record) => '→ '.Registration::STATUSES[Registration::NEXT[$record->status]])
            ->icon('heroicon-o-arrow-right-circle')->color('primary')
            ->visible(fn (Registration $record) => isset(Registration::NEXT[$record->status]))
            // Konfirmasi hanya saat ke "Dikonfirmasi" (mengirim email); tahap lain langsung pindah
            ->requiresConfirmation()
            ->modalHidden(fn (Registration $record) => Registration::NEXT[$record->status] !== 'dikonfirmasi')
            ->modalHeading('Konfirmasi pendaftaran?')
            ->modalDescription('Pendaftar akan menerima email "Pendaftaran dikonfirmasi".')
            ->action(function (Registration $record) {
                $record->update(['status' => Registration::NEXT[$record->status]]);
                Notification::make()->success()->title($record->code().': '.Registration::STATUSES[$record->status])->send();
            });
    }

    public static function whatsappAction(): Action
    {
        return Action::make('wa')->label('WhatsApp')->icon('heroicon-o-chat-bubble-left-right')->color('success')
            ->url(fn (Registration $r) => 'https://wa.me/'.preg_replace('/^0/', '62', preg_replace('/\D/', '', $r->phone))
                .'?text='.rawurlencode('Halo '.$r->name.', kami dari INOVASS terkait pendaftaran '.$r->code().'.'))
            ->openUrlInNewTab();
    }

    public static function bulkStatusAction(): BulkAction
    {
        return BulkAction::make('status')->label('Ubah tahap')->icon('heroicon-o-arrows-right-left')
            ->schema([Select::make('status')->label('Tahap baru')->options(Registration::STATUSES)->required()])
            ->modalDescription('Tahap "Dikonfirmasi" dan "Batal" mengirim email ke tiap pendaftar.')
            ->action(function (Collection $records, array $data) {
                $records->each->update(['status' => $data['status']]);
                Notification::make()->success()->title($records->count().' pendaftaran → '.Registration::STATUSES[$data['status']])->send();
            })
            ->deselectRecordsAfterCompletion();
    }
}
