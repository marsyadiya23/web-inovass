<?php

namespace App\Filament\Resources\ContactMessages\Schemas;

use App\Filament\Resources\ContactMessages\ContactMessageResource;
use Filament\Forms\Components\Select;
use Filament\Forms\Components\TextInput;
use Filament\Forms\Components\Textarea;
use Filament\Schemas\Components\Section;
use Filament\Schemas\Schema;

class ContactMessageForm
{
    public static function configure(Schema $schema): Schema
    {
        // ponytail: field pengirim disabled = tampil read-only dan tidak ikut tersimpan.
        return $schema
            ->components([
                Section::make('Pesan')->columns(2)->schema([
                    TextInput::make('name')->label('Nama')->disabled(),
                    TextInput::make('email')->label('Email')->disabled(),
                    TextInput::make('phone')->label('Telepon')->disabled(),
                    TextInput::make('organization')->label('Organisasi')->disabled(),
                    TextInput::make('subject')->label('Keperluan')->disabled(),
                    TextInput::make('created_at')->label('Diterima')->disabled()
                        ->formatStateUsing(fn ($state) => $state ? \Illuminate\Support\Carbon::parse($state)->timezone(config('app.timezone'))->translatedFormat('d M Y H:i') : null),
                    Textarea::make('message')->label('Isi pesan')->rows(8)->disabled()->columnSpanFull(),
                ]),
                Section::make('Tindak lanjut')->schema([
                    Select::make('status')->options(ContactMessageResource::STATUSES)->required()->native(false),
                    Textarea::make('note')->label('Catatan internal')->rows(4),
                ]),
            ]);
    }
}
