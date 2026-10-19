<?php

namespace App\Filament\Pages;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;
use Filament\Support\Icons\Heroicon;

class TentangContent extends EditPageContent
{
    protected static string $contentKey = 'tentang';

    protected static ?string $title = 'Tentang Kami';

    protected static ?string $navigationLabel = 'Tentang Kami';

    protected static string | \BackedEnum | null $navigationIcon = Heroicon::OutlinedBuildingOffice2;

    protected static string | \UnitEnum | null $navigationGroup = 'Konten Website';

    protected static ?int $navigationSort = 2;

    protected function fields(): array
    {
        return [
            PageFields::hero('tentang'),
            Section::make('Profil perusahaan')->columns(2)->collapsible()->schema([
                TextInput::make('profile_title')->label('Judul'),
                TextInput::make('profile_em')->label('Judul baris kedua (hijau)'),
                Textarea::make('profile_text')->label('Teks profil')->helperText('Satu paragraf per baris')->rows(6)->columnSpanFull(),
                FileUpload::make('profile_image')->label('Gambar')->image()->disk('public')->directory('tentang')->columnSpanFull(),
                Repeater::make('stats')->label('Angka statistik')->columns(2)->defaultItems(0)->columnSpanFull()
                    ->schema([
                        TextInput::make('number')->label('Angka')->placeholder('20+')->required(),
                        TextInput::make('label')->label('Keterangan')->required(),
                    ]),
            ]),
            Section::make('Visi & Misi')->columns(2)->collapsible()->schema([
                TextInput::make('visi_title')->label('Judul'),
                TextInput::make('visi_em')->label('Judul baris kedua (hijau)'),
                Textarea::make('visi')->label('Visi')->rows(3)->columnSpanFull(),
                Repeater::make('misi')->label('Misi')->simple(TextInput::make('item')->required())->defaultItems(0)->columnSpanFull(),
                FileUpload::make('visi_image')->label('Gambar')->image()->disk('public')->directory('tentang')->columnSpanFull(),
            ]),
            Section::make('Mengapa memilih kami')->columns(2)->collapsible()->schema([
                TextInput::make('why_title')->label('Judul'),
                TextInput::make('why_em')->label('Judul baris kedua (hijau)'),
                Repeater::make('why_items')->label('Kartu')->columns(2)->defaultItems(0)->columnSpanFull()
                    ->itemLabel(fn (array $state) => $state['title'] ?? null)->collapsed()
                    ->schema([
                        TextInput::make('title')->label('Judul')->required(),
                        Select::make('icon')->label('Ikon')->options([
                            'users' => 'Orang', 'activity' => 'Grafik', 'grid' => 'Kotak', 'clock' => 'Jam', 'file' => 'Dokumen', 'shield' => 'Perisai',
                        ])->default('shield'),
                        Textarea::make('text')->label('Teks')->rows(2)->columnSpanFull(),
                    ]),
            ]),
            Section::make('Klien')->columns(2)->collapsible()
                ->description('Logo klien diatur di menu Koleksi › Klien.')
                ->schema([
                    TextInput::make('clients_title')->label('Judul'),
                    TextInput::make('clients_em')->label('Judul baris kedua (hijau)'),
                ]),
            PageFields::cta(),
        ];
    }
}
