<?php

namespace App\Filament\Resources\Registrations\Pages;

use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\Registrations\Tables\RegistrationsTable;
use Filament\Actions\DeleteAction;
use Filament\Resources\Pages\EditRecord;

class EditRegistration extends EditRecord
{
    protected static string $resource = RegistrationResource::class;

    public function getSubheading(): ?string
    {
        return $this->record->code().' · '.$this->record->schedule?->training?->title.' · '.$this->record->participants.' peserta';
    }

    protected function getHeaderActions(): array
    {
        return [
            // Muat ulang halaman setelah pindah tahap agar form & Riwayat langsung menampilkan tahap baru
            RegistrationsTable::nextAction()->after(fn () => $this->redirect(RegistrationResource::getUrl('edit', ['record' => $this->record]))),
            RegistrationsTable::whatsappAction(),
            DeleteAction::make(),
        ];
    }
}
