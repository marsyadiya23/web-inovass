<?php

namespace App\Filament\Resources\Registrations;

use App\Filament\Resources\Registrations\Pages\CreateRegistration;
use App\Filament\Resources\Registrations\Pages\EditRegistration;
use App\Filament\Resources\Registrations\Pages\ListRegistrations;
use App\Filament\Resources\Registrations\RelationManagers\ActivitiesRelationManager;
use App\Filament\Resources\Registrations\Schemas\RegistrationForm;
use App\Filament\Resources\Registrations\Tables\RegistrationsTable;
use App\Models\Registration;
use BackedEnum;
use Filament\Resources\Resource;
use Filament\Schemas\Schema;
use Filament\Support\Icons\Heroicon;
use Filament\Tables\Table;
use UnitEnum;

class RegistrationResource extends Resource
{
    protected static ?string $model = Registration::class;

    protected static string|BackedEnum|null $navigationIcon = Heroicon::OutlinedUserPlus;

    protected static string|UnitEnum|null $navigationGroup = null; // menu utama, tepat di bawah Dasbor

    protected static ?int $navigationSort = 1;

    protected static ?string $modelLabel = 'Pendaftaran';

    protected static ?string $pluralModelLabel = 'Pendaftaran';

    protected static ?string $navigationLabel = 'Pendaftaran';

    protected static ?string $recordTitleAttribute = 'name';

    public static function getNavigationBadge(): ?string
    {
        return Registration::whereIn('status', Registration::OPEN)->count() ?: null; // perlu ditindaklanjuti
    }

    public static function getNavigationBadgeColor(): ?string
    {
        return 'warning';
    }

    public static function form(Schema $schema): Schema
    {
        return RegistrationForm::configure($schema);
    }

    public static function table(Table $table): Table
    {
        return RegistrationsTable::configure($table);
    }

    public static function getRelations(): array
    {
        return [
            ActivitiesRelationManager::class,
        ];
    }

    public static function getPages(): array
    {
        return [
            'index' => ListRegistrations::route('/'),
            'create' => CreateRegistration::route('/create'),
            'edit' => EditRegistration::route('/{record}/edit'),
        ];
    }
}
