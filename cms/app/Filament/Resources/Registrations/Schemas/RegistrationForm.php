<?php

namespace App\Filament\Resources\Registrations\Schemas;

use App\Models\Registration;
use App\Models\TrainingSchedule;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Components\Group;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class RegistrationForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->columns(3)->components([
            Group::make()->columnSpan(['lg' => 2])->schema([
                Section::make('Data pendaftar')->columns(2)->schema([
                    Select::make('training_schedule_id')->label('Jadwal')->columnSpanFull()
                        ->relationship('schedule', 'id')
                        ->getOptionLabelFromRecordUsing(fn (TrainingSchedule $record) => $record->training->title.' — '.$record->dateLabel())
                        ->searchable(['id'])->preload()->required(),
                    TextInput::make('name')->label('Nama')->required(),
                    TextInput::make('email')->label('Email')->email()->required(),
                    TextInput::make('phone')->label('No. WhatsApp')->tel()->required(),
                    TextInput::make('organization')->label('Instansi / perusahaan'),
                    TextInput::make('position')->label('Jabatan'),
                    TextInput::make('participants')->label('Jumlah peserta')->numeric()->minValue(1)->default(1)->required(),
                    Textarea::make('participant_names')->label('Nama peserta lain (satu per baris)')->rows(3)->columnSpanFull(),
                    Textarea::make('message')->label('Pesan dari pendaftar')->rows(3)->columnSpanFull(),
                ]),
            ]),
            Section::make('Tindak lanjut')->columnSpan(['lg' => 1])->schema([
                Select::make('status')->label('Tahap')->options(Registration::STATUSES)->default('baru')->required()
                    ->helperText('Urutan: Baru → Dihubungi → Penawaran dikirim → Dikonfirmasi → Lunas → Selesai. "Dikonfirmasi" dan "Batal" otomatis mengirim email ke pendaftar. "Batal" tidak dihitung ke kuota.'),
                Textarea::make('note')->label('Catatan internal')->rows(4),
            ]),
        ]);
    }
}
