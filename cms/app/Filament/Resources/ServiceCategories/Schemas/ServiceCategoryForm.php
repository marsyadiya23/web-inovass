<?php

namespace App\Filament\Resources\ServiceCategories\Schemas;

use Filament\Forms\Components\FileUpload;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Forms\Components\Toggle;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Components\Utilities\Set;
use Filament\Schemas\Schema;
use Illuminate\Support\Str;

class ServiceCategoryForm
{
    public static function configure(Schema $schema): Schema
    {
        return $schema->columns(3)->components([
            Section::make('Kategori')->columnSpan(['lg' => 2])->schema([
                TextInput::make('name')->label('Nama kategori')->required()->maxLength(255)
                    ->live(onBlur: true)
                    ->afterStateUpdated(fn (?string $state, Set $set, string $operation) => $operation === 'create' ? $set('slug', Str::slug($state ?? '')) : null),
                TextInput::make('slug')->required()->alphaDash()->unique(ignoreRecord: true)
                    ->prefix(url('layanan').'/')->suffix('/index.html')
                    ->helperText('Mengubah slug akan mengubah URL semua layanan di kategori ini.'),
                Textarea::make('intro')->label('Intro (tampil di bawah judul kategori)')->rows(4),
                TextInput::make('short_description')->label('Deskripsi singkat'),
            ]),
            Section::make('Tampilan')->columnSpan(['lg' => 1])->schema([
                Toggle::make('is_published')->label('Tampilkan')->default(true),
                TextInput::make('sort')->label('Urutan tab')->numeric()->default(0),
                FileUpload::make('image')->label('Gambar hero')->image()->disk('public')->directory('layanan'),
                TextInput::make('meta_description')->label('Meta description (SEO)')->maxLength(255),
            ]),
        ]);
    }
}
