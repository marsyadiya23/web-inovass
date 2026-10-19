<?php

namespace App\Filament\Resources\Services\Schemas;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\RichEditor;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TagsInput;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Group;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Get;
use Filament\Schemas\Components\Utilities\Set;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;
use Illuminate\Validation\Rules\Unique;

class ServiceForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->columns(3)->components([
            Group::make()->columnSpan(['lg' => 2])->schema([
                Section::make('Isi layanan')->schema([
                    TextInput::make('title')->label('Judul')->required()->maxLength(255)
                        ->live(onBlur: true)
                        ->afterStateUpdated(fn (?string $state, Set $set, string $operation) => $operation === 'create' ? $set('slug', Str::slug($state ?? '')) : null),
                    TextInput::make('slug')->required()->alphaDash()->suffix('.html')
                        ->unique(ignoreRecord: true, modifyRuleUsing: fn (Unique $rule, Get $get) => $rule->where('service_category_id', $get('service_category_id')))
                        ->helperText('Bagian akhir URL. Harus unik dalam satu kategori.'),
                    Textarea::make('summary')->label('Ringkasan')->rows(3)
                        ->helperText('Tampil di kartu daftar layanan dan sebagai deskripsi meta.'),
                    TagsInput::make('highlights')->label('Poin highlight')->placeholder('Ketik lalu Enter')
                        ->helperText('Kartu kecil di atas isi (biasanya 3 poin). Kosongkan jika tidak perlu.'),
                    RichEditor::make('body')->label('Isi halaman')
                        ->fileAttachmentsDisk('public')->fileAttachmentsDirectory('layanan'),
                ]),
            ]),
            Group::make()->columnSpan(['lg' => 1])->schema([
                Section::make('Penempatan')->schema([
                    Select::make('service_category_id')->label('Kategori')->relationship('category', 'name')
                        ->required()->live()->afterStateUpdated(fn (Set $set) => $set('parent_id', null)),
                    Select::make('parent_id')->label('Induk layanan')
                        ->relationship('parent', 'title', fn ($query, Get $get) => $query
                            ->whereNull('parent_id')->where('service_category_id', $get('service_category_id')))
                        ->searchable()->preload()
                        ->helperText('Kosongkan untuk layanan utama (tampil di halaman kategori).'),
                    TextInput::make('sort')->label('Urutan')->numeric()->default(0),
                    Toggle::make('is_published')->label('Tampilkan')->default(true),
                ]),
                Section::make('Lainnya')->collapsed()->schema([
                    FileUpload::make('image')->label('Gambar')->image()->disk('public')->directory('layanan'),
                    TextInput::make('meta_description')->label('Meta description (SEO)')->maxLength(255),
                ]),
            ]),
        ]);
    }
}
