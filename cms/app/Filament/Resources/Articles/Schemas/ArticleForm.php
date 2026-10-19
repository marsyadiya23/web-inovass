<?php

namespace App\Filament\Resources\Articles\Schemas;

use Filament\Forms\Components\DateTimePicker;
use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\RichEditor;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Group;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Set;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class ArticleForm
{
    public const CATEGORIES = ['Berita' => 'Berita', 'Insight' => 'Insight', 'Pengumuman' => 'Pengumuman'];

    public static function configure(Schema $schema): Schema
    {
        return $schema
            ->columns(3)
            ->components([
                Group::make()->columnSpan(['lg' => 2])->schema([
                    Section::make('Isi berita')->schema([
                        TextInput::make('title')->label('Judul')->required()->maxLength(255)
                            ->live(onBlur: true)
                            ->afterStateUpdated(fn (?string $state, Set $set, string $operation) => $operation === 'create' ? $set('slug', Str::slug($state ?? '')) : null),
                        TextInput::make('slug')->required()->maxLength(255)->unique(ignoreRecord: true)->alphaDash()
                            ->prefix(url('berita').'/'),
                        Textarea::make('excerpt')->label('Ringkasan')->rows(3)->maxLength(500)
                            ->helperText('Tampil di kartu berita dan sebagai deskripsi meta.'),
                        RichEditor::make('body')->label('Isi')
                            ->fileAttachmentsDisk('public')->fileAttachmentsDirectory('articles'),
                    ]),
                ]),
                Group::make()->columnSpan(['lg' => 1])->schema([
                    Section::make('Publikasi')->schema([
                        Toggle::make('is_published')->label('Tampilkan')->default(true),
                        DateTimePicker::make('published_at')->label('Tanggal terbit')->required()->default(now())->native(false)
                            ->helperText('Berita dengan tanggal di masa depan baru tampil pada tanggal tersebut.'),
                        Select::make('category')->label('Kategori')->options(self::CATEGORIES)->default('Berita'),
                        FileUpload::make('cover')->label('Gambar sampul')->image()->disk('public')->directory('articles'),
                    ]),
                ]),
            ]);
    }
}
