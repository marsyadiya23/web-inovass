<?php

namespace App\Filament\Pages;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\Repeater;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\TextInput;
use Filament\Schemas\Components\Section;
use Filament\Support\Icons\Heroicon;

class HomeContent extends EditPageContent
{
    protected static string $contentKey = 'home';

    protected static ?string $title = 'Beranda';

    protected static ?string $navigationLabel = 'Beranda';

    protected static string | \BackedEnum | null $navigationIcon = Heroicon::OutlinedHome;

    protected static string | \UnitEnum | null $navigationGroup = 'Konten Website';

    protected static ?int $navigationSort = 1;

    /**
     * Ikon garis dari situs lama: key => [label, viewBox, isi SVG].
     * ponytail: daftar tetap; tambah entri di sini bila butuh ikon baru.
     */
    public const ICONS = [
        'mutu' => ['Mutu (kubus)', '0 0 28 28', '<path d="M14 3l10 5.5v7L14 21 4 15.5v-7L14 3z"/><path d="M14 21v4M4 15.5l4.5 2.5M23.5 15.5l-4.5 2.5"/>'],
        'k3' => ['K3 (penanda)', '0 0 28 28', '<path d="M14 2a5 5 0 0 1 5 5c0 4-5 8-5 8S9 11 9 7a5 5 0 0 1 5-5z"/><circle cx="14" cy="7" r="1.5" fill="#00c278"/><path d="M6 20h16M8 24h12"/>'],
        'lingkungan' => ['Lingkungan (bola)', '0 0 28 28', '<circle cx="14" cy="14" r="10"/><path d="M14 4C9 8 8 12 9 16c2 4 6 6 10 4"/><path d="M14 4c5 4 6 9 4 13-2 4-6 6-10 4"/>'],
        'lab' => ['Laboratorium (tas)', '0 0 28 28', '<rect x="3" y="8" width="22" height="14" rx="2"/><path d="M9 8V6a5 5 0 0 1 10 0v2"/><circle cx="14" cy="15" r="2"/>'],
        'keamanan' => ['Keamanan informasi', '0 0 28 28', '<rect x="4" y="4" width="20" height="20" rx="3"/><path d="M10 4v20M4 10h6M4 18h6"/><path d="M16 10l5 4-5 4"/>'],
        'energi' => ['Energi (matahari)', '0 0 28 28', '<path d="M14 3v6M5.5 6.5l4.2 4.2M3 14h6M5.5 21.5l4.2-4.2M14 25v-6M22.5 21.5l-4.2-4.2M25 14h-6M22.5 6.5l-4.2 4.2"/><circle cx="14" cy="14" r="3"/>'],
        'orang' => ['Orang', '0 0 22 22', '<circle cx="11" cy="8" r="4"/><path d="M3 20c0-4 3.6-7 8-7s8 3 8 7"/>'],
        'daftar' => ['Daftar centang', '0 0 22 22', '<path d="M3 5h16M3 11h10M3 17h6"/><polyline points="17 13 19 15 22 11"/>'],
        'grid' => ['Grid', '0 0 22 22', '<rect x="2" y="2" width="8" height="8" rx="1.5"/><rect x="12" y="2" width="8" height="8" rx="1.5"/><rect x="2" y="12" width="8" height="8" rx="1.5"/><rect x="12" y="12" width="8" height="8" rx="1.5"/>'],
        'jaringan' => ['Jaringan (target)', '0 0 22 22', '<circle cx="11" cy="11" r="8"/><path d="M2 11h3M17 11h3M11 2v3M11 17v3"/>'],
    ];

    protected function fields(): array
    {
        $icons = array_map(fn ($i) => $i[0], self::ICONS);
        $heading = fn (string $prefix, bool $em = true) => array_filter([
            TextInput::make("$prefix.eyebrow")->label('Label kecil (eyebrow)'),
            TextInput::make("$prefix.title")->label('Judul'),
            $em ? TextInput::make("$prefix.title_em")->label('Judul baris hijau') : null,
        ]);
        $link = fn (string $prefix, string $label = 'Tombol') => [
            TextInput::make("{$prefix}_label")->label("$label: teks"),
            TextInput::make("{$prefix}_url")->label("$label: tautan")->helperText('Contoh: /kontak.html, /layanan/sertifikasi-organisasi/index.html, #tentang'),
        ];
        $iconCards = fn (string $name) => Repeater::make($name)->label('Kartu')->columns(2)->collapsible()
            ->itemLabel(fn (array $state) => $state['title'] ?? null)->schema([
                Select::make('icon')->label('Ikon')->options($icons),
                TextInput::make('title')->label('Judul')->required(),
                Textarea::make('text')->label('Teks')->rows(2)->columnSpanFull(),
            ]);

        return [
            Section::make('Hero')->columns(2)->collapsible()->schema([
                TextInput::make('hero.eyebrow')->label('Label kecil (eyebrow)'),
                TextInput::make('hero.title')->label('Judul')->required(),
                TextInput::make('hero.title_em')->label('Judul baris hijau'),
                Textarea::make('hero.description')->label('Deskripsi')->rows(2),
                ...$link('hero.button'),
                FileUpload::make('hero.image')->label('Gambar latar')->image()->disk('public')->directory('home')->columnSpanFull(),
            ]),
            Section::make('Tentang singkat')->columns(2)->collapsible()->collapsed()->schema([
                ...$heading('about'),
                Textarea::make('about.text')->label('Teks')->rows(3)->columnSpanFull(),
                ...$link('about.button'),
                Repeater::make('about.stats')->label('Angka statistik')->columns(3)->columnSpanFull()->collapsible()
                    ->itemLabel(fn (array $state) => trim(($state['number'] ?? '').($state['suffix'] ?? '').' '.($state['label'] ?? '')))->schema([
                        TextInput::make('number')->label('Angka')->numeric()->integer()->required(),
                        TextInput::make('suffix')->label('Akhiran')->placeholder('+'),
                        TextInput::make('label')->label('Keterangan')->required(),
                    ]),
                Repeater::make('about.values')->label('Kartu nilai')->columns(2)->columnSpanFull()->collapsible()
                    ->itemLabel(fn (array $state) => $state['title'] ?? null)->schema([
                        TextInput::make('title')->label('Judul')->required(),
                        FileUpload::make('icon')->label('Ikon (gambar)')->image()->disk('public')->directory('home'),
                        Textarea::make('text')->label('Teks')->rows(2)->columnSpanFull(),
                    ]),
            ]),
            Section::make('Logo klien')->collapsible()->collapsed()
                ->description('Logonya diatur di menu Koleksi › Klien.')->schema([
                    TextInput::make('clients.label')->label('Teks di atas logo'),
                ]),
            Section::make('Layanan')->columns(2)->collapsible()->collapsed()->schema([
                ...$heading('services'),
                ...$link('services.button'),
                Repeater::make('services.cards')->label('Kartu layanan (kartu pertama tampil besar)')->columns(2)->columnSpanFull()->collapsible()
                    ->itemLabel(fn (array $state) => $state['title'] ?? null)->schema([
                        TextInput::make('title')->label('Judul')->required(),
                        TextInput::make('url')->label('Tautan')->helperText('Contoh: /layanan/akreditasi-organisasi/index.html'),
                        Textarea::make('text')->label('Teks')->rows(2),
                        TextInput::make('link_label')->label('Teks tautan')->placeholder('Pelajari Layanan →'),
                        FileUpload::make('image')->label('Gambar latar')->image()->disk('public')->directory('home')->columnSpanFull(),
                    ]),
            ]),
            Section::make('Produk')->columns(2)->collapsible()->collapsed()
                ->description('Kartu produk diatur di menu Koleksi › Produk.')->schema([
                    ...$heading('products'),
                    Textarea::make('products.subtitle')->label('Subjudul')->rows(2),
                ]),
            Section::make('Bidang pelatihan')->columns(2)->collapsible()->collapsed()->schema([
                ...$heading('training'),
                ...$link('training.button'),
                $iconCards('training.cards')->columnSpanFull(),
            ]),
            Section::make('Mengapa INOVASS')->columns(2)->collapsible()->collapsed()->schema([
                ...$heading('why'),
                Textarea::make('why.description')->label('Deskripsi')->rows(2),
                $iconCards('why.cards')->columnSpanFull(),
            ]),
            Section::make('Proses kerja')->columns(2)->collapsible()->collapsed()->schema([
                ...$heading('process', false),
                Repeater::make('process.steps')->label('Langkah (nomor otomatis)')->columns(2)->columnSpanFull()->collapsible()
                    ->itemLabel(fn (array $state) => $state['title'] ?? null)->schema([
                        TextInput::make('title')->label('Judul')->required(),
                        Textarea::make('text')->label('Teks')->rows(2),
                    ]),
            ]),
            Section::make('Judul bagian Berita, Testimoni, FAQ')->columns(2)->collapsible()->collapsed()
                ->description('Isinya diatur di menu Koleksi (Berita, Testimoni, FAQ).')->schema([
                    ...$heading('news', false),
                    ...$heading('testimonials', false),
                    ...$heading('faq', false),
                ]),
            Section::make('Ajakan konsultasi (CTA)')->columns(2)->collapsible()->collapsed()->schema([
                TextInput::make('cta.title')->label('Judul'),
                TextInput::make('cta.title_em')->label('Judul baris hijau'),
                Textarea::make('cta.text')->label('Teks')->rows(2)->columnSpanFull(),
                ...$link('cta.primary', 'Tombol utama'),
                ...$link('cta.secondary', 'Tombol kedua'),
            ]),
            Section::make('SEO')->collapsible()->collapsed()->schema([
                Textarea::make('meta_description')->label('Meta description')->rows(2)->maxLength(300),
            ]),
        ];
    }
}
