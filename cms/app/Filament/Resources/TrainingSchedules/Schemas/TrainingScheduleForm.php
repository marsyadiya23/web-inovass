<?php

namespace App\Filament\Resources\TrainingSchedules\Schemas;

use App\Models\Training;
use App\Models\TrainingSchedule;
use Filament\Forms\Components\DatePicker;
use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Schemas\Schema;

class TrainingScheduleForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->components(self::fields(withTraining: true));
    }

    /** Dipakai juga oleh relation manager di halaman Program Pelatihan (tanpa pilihan program). */
    public static function fields(bool $withTraining): array
    {
        return [
            Section::make('Jadwal')->columns(2)->columnSpanFull()->schema(array_filter([
                $withTraining ? Select::make('training_id')->label('Program pelatihan')
                    ->relationship('training', 'title')->searchable()->preload()->required()->columnSpanFull() : null,
                DatePicker::make('start_date')->label('Tanggal mulai')->required()->native(false)->displayFormat('d M Y')->live(),
                DatePicker::make('end_date')->label('Tanggal selesai')->native(false)->displayFormat('d M Y')
                    ->afterOrEqual('start_date')->helperText('Kosongkan jika hanya 1 hari.'),
                TextInput::make('time')->label('Jam')->placeholder('08.30 – 16.30 WIB'),
                DatePicker::make('registration_deadline')->label('Batas pendaftaran')->native(false)->displayFormat('d M Y')
                    ->beforeOrEqual(fn (Get $get) => $get('end_date') ?: $get('start_date'))
                    ->helperText('Kosongkan = sampai tanggal mulai.'),
            ])),
            Section::make('Tempat & biaya')->columns(2)->columnSpanFull()->schema([
                Select::make('method')->label('Metode')->options(TrainingSchedule::METHODS)->default('offline')->required(),
                TextInput::make('location')->label('Lokasi')->placeholder('Bogor / Zoom Meeting'),
                TextInput::make('price')->label('Biaya per peserta')->numeric()->minValue(0)->prefix('Rp')
                    ->helperText(fn (Get $get) => 'Kosongkan = pakai harga program'.(($p = Training::find($get('training_id'))?->price) ? ' (Rp '.number_format($p, 0, ',', '.').')' : '').'.'),
                Toggle::make('hide_price')->label('Sembunyikan harga di website')
                    ->helperText('Website menampilkan "Hubungi kami". Harga tetap tersimpan.')->inline(false),
                TextInput::make('quota')->label('Kuota peserta')->numeric()->minValue(1)->helperText('Kosongkan = tanpa batas.'),
                Select::make('status')->label('Status')->options(TrainingSchedule::STATUSES)->default('dibuka')->required()
                    ->helperText('Otomatis tampil "Penuh" bila kuota habis, dan hilang dari website setelah tanggal lewat.'),
                Textarea::make('note')->label('Catatan (tampil di website)')->rows(2),
            ]),
            Section::make('Silabus')->columnSpanFull()->schema([
                FileUpload::make('syllabus')->label('File silabus (PDF atau gambar)')
                    ->acceptedFileTypes(['application/pdf', 'image/*'])->maxSize(10240)
                    ->disk('public')->directory('silabus')->openable()->downloadable()
                    ->helperText('Maks. 10 MB. Tampil sebagai tombol "Silabus" di website. Kosongkan = pakai brosur program.'),
            ]),
        ];
    }
}
