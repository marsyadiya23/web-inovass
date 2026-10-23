<?php

namespace App\Filament\Resources\TrainingSchedules\RelationManagers;

use App\Exports\RegistrationsExport;
use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\Registrations\Tables\RegistrationsTable;
use App\Models\Registration;
use Filament\Actions\Action;
use Filament\Actions\BulkActionGroup;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Tables\Columns\TextColumn;
use Filament\Tables\Table;

/** Daftar peserta di halaman detail jadwal: kuota terisi, tahap tiap pendaftaran, ekspor. */
class RegistrationsRelationManager extends RelationManager
{
    protected static string $relationship = 'registrations';

    protected static ?string $title = 'Pendaftar jadwal ini';

    public function table(Table $table): Table
    {
        $schedule = $this->getOwnerRecord();

        return $table
            ->description(fn () => 'Terisi '.$schedule->seatsTaken().($schedule->quota ? ' dari '.$schedule->quota.' kursi' : ' peserta (tanpa batas kuota)')
                .' · pendaftar Batal tidak dihitung')
            ->columns([
                TextColumn::make('created_at')->label('Masuk')->dateTime('d M Y')->sortable()
                    ->description(fn (Registration $r) => $r->code()),
                TextColumn::make('name')->label('Nama')->searchable()->description(fn (Registration $r) => $r->organization),
                TextColumn::make('phone')->label('Kontak')->description(fn (Registration $r) => $r->email),
                TextColumn::make('participants')->label('Peserta'),
                RegistrationsTable::statusColumn(),
            ])
            ->defaultSort('created_at', 'desc')
            ->recordUrl(fn (Registration $r) => RegistrationResource::getUrl('edit', ['record' => $r]))
            ->headerActions([
                Action::make('export')->label('Ekspor peserta')->icon('heroicon-o-arrow-down-tray')->color('gray')
                    ->action(fn () => RegistrationsExport::download($schedule->registrations()->getQuery()->orderBy('created_at'),
                        'peserta-'.$schedule->training->slug.'-'.$schedule->start_date->format('Y-m-d').'.xlsx')),
            ])
            ->recordActions([
                RegistrationsTable::nextAction(),
                RegistrationsTable::whatsappAction(),
            ])
            ->toolbarActions([
                BulkActionGroup::make([RegistrationsTable::bulkStatusAction()]),
            ]);
    }
}
