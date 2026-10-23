<?php

namespace App\Filament\Resources\Trainings\Schemas;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\RichEditor;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Group;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Set;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class TrainingForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->columns(3)->components([
            Group::make()->columnSpan(['lg' => 2])->schema([
                Section::make('Program')->schema([
                    TextInput::make('title')->label('Nama pelatihan')->required()->maxLength(255)
                        ->live(onBlur: true)
                        ->afterStateUpdated(fn (?string $state, Set $set, string $operation) => $operation === 'create' ? $set('slug', Str::slug($state ?? '')) : null),
                    TextInput::make('slug')->required()->alphaDash()->unique(ignoreRecord: true)->prefix(url('pelatihan').'/'),
                    Textarea::make('summary')->label('Ringkasan')->rows(3)
                        ->helperText('Tampil di kartu katalog dan daftar jadwal.'),
                    TagsInput::make('highlights')->label('Poin utama')->placeholder('Ketik lalu Enter'),
                    RichEditor::make('description')->label('Deskripsi lengkap (materi, manfaat, peserta)')
                        ->fileAttachmentsDisk('public')->fileAttachmentsDirectory('pelatihan'),
                ]),
            ]),
            Group::make()->columnSpan(['lg' => 1])->schema([
                Section::make('Pengaturan')->schema([
                    Select::make('training_category_id')->label('Kategori')->relationship('category', 'name')
                        ->required()->preload()
                        ->createOptionForm([
                            TextInput::make('name')->label('Nama kategori')->required()
                                ->live(onBlur: true)->afterStateUpdated(fn (?string $state, Set $set) => $set('slug', Str::slug($state ?? ''))),
                            TextInput::make('slug')->required()->unique('training_categories', 'slug'),
                        ]),
                    TextInput::make('duration')->label('Durasi')->placeholder('2 hari (16 jam)'),
                    TextInput::make('price')->label('Harga default per peserta')->numeric()->minValue(0)->prefix('Rp')
                        ->helperText('Bisa diganti per jadwal. Kosongkan = "Hubungi kami".'),
                    Toggle::make('is_published')->label('Tampilkan di website')->default(true),
                    TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                ]),
                Section::make('Media')->collapsed()->schema([
                    FileUpload::make('image')->label('Gambar')->image()->disk('public')->directory('pelatihan'),
                    FileUpload::make('brochure')->label('Silabus (PDF atau gambar)')->helperText('Tampil sebagai tombol "Silabus" di halaman program dan di setiap jadwalnya.')->acceptedFileTypes(['application/pdf', 'image/*'])
                        ->maxSize(10240)->disk('public')->directory('brosur'),
                    TextInput::make('meta_description')->label('Meta description (SEO)')->maxLength(255),
                ]),
            ]),
        ]);
    }
}
