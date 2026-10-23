<?php

namespace App\Filament\Resources\Registrations\Pages;

use App\Filament\Resources\Registrations\RegistrationResource;
use App\Models\Registration;
use Filament\Actions\CreateAction;
use Filament\Resources\Pages\ListRecords;
use Filament\Schemas\Components\Tabs\Tab;
use Illuminate\Database\Eloquent\Builder;

class ListRegistrations extends ListRecords
{
    protected static string $resource = RegistrationResource::class;

    protected function getHeaderActions(): array
    {
        return [
            CreateAction::make()->label('Tambah pendaftaran'), // untuk pendaftaran lewat telepon / WhatsApp
        ];
    }

    /** Tab per tahap alur kerja (URL: ?tab=baru). Bawaan: yang masih perlu ditindaklanjuti. */
    public function getTabs(): array
    {
        $counts = Registration::query()->selectRaw('status, count(*) as total')->groupBy('status')->pluck('total', 'status');

        $tabs = [
            'perlu' => Tab::make('Perlu ditindaklanjuti')->icon('heroicon-o-bell-alert')
                ->badge($counts->only(Registration::OPEN)->sum() ?: null)->badgeColor('warning')
                ->modifyQueryUsing(fn (Builder $query) => $query->whereIn('status', Registration::OPEN)),
        ];
        foreach (Registration::STATUSES as $key => $label) {
            $tabs[$key] = Tab::make($label)->badge($counts[$key] ?? null)
                ->modifyQueryUsing(fn (Builder $query) => $query->where('status', $key));
        }
        $tabs['semua'] = Tab::make('Semua');

        return $tabs;
    }

    public function getDefaultActiveTab(): string|int|null
    {
        return 'perlu';
    }
}
