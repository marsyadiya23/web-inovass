<?php

namespace App\Filament\Pages;

use App\Models\PageContent;
use Filament\Actions\Action;
use Filament\Notifications\Notification;
use Filament\Pages\Page;
use Filament\Schemas\Components\Actions;
use Filament\Schemas\Components\EmbeddedSchema;
use Filament\Schemas\Components\Form;
use Filament\Schemas\Schema;

/**
 * Base halaman admin untuk konten singleton (satu baris page_contents per key).
 * Turunan cukup isi $contentKey dan fields(); simpan otomatis ke PageContent::put().
 */
abstract class EditPageContent extends Page
{
    protected static string $contentKey;

    public ?array $data = [];

    /** @return array<\Filament\Schemas\Components\Component|\Filament\Forms\Components\Field> */
    abstract protected function fields(): array;

    public function mount(): void
    {
        $this->form->fill(PageContent::get(static::$contentKey));
    }

    public function form(Schema $schema): Schema
    {
        return $schema->components($this->fields())->statePath('data');
    }

    public function content(Schema $schema): Schema
    {
        return $schema->components([
            Form::make([EmbeddedSchema::make('form')])
                ->id('form')
                ->livewireSubmitHandler('save')
                ->footer([
                    Actions::make([
                        Action::make('save')->label('Simpan')->submit('save')->keyBindings(['mod+s']),
                    ]),
                ]),
        ]);
    }

    public function save(): void
    {
        PageContent::put(static::$contentKey, $this->form->getState());

        Notification::make()->success()->title('Tersimpan')->send();
    }
}
