<?php

namespace Tests\Feature;

use App\Exports\RegistrationsExport;
use App\Filament\Resources\Registrations\Pages\ListRegistrations;
use App\Filament\Resources\TrainingSchedules\Pages\ListTrainingSchedules;
use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\User;
use Filament\Actions\Testing\TestAction;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;
use OpenSpout\Reader\XLSX\Reader;
use Tests\TestCase;

class RegistrationsExportTest extends TestCase
{
    use RefreshDatabase;

    public function test_xlsx_contains_header_and_rows_as_text(): void
    {
        $cat = TrainingCategory::create(['name' => 'Uji', 'slug' => 'uji']);
        $training = Training::create(['training_category_id' => $cat->id, 'title' => 'Pelatihan Ekspor', 'slug' => 'pelatihan-ekspor']);
        $schedule = $training->schedules()->create(['start_date' => today()->addDays(5), 'status' => 'dibuka', 'location' => 'Bogor']);
        $schedule->registrations()->create(['name' => 'Siti', 'email' => 's@example.com', 'phone' => '081200001111', 'participants' => 2, 'status' => 'dikonfirmasi']);

        $file = RegistrationsExport::download(Registration::where('email', 's@example.com'), 'x.xlsx')->getFile()->getPathname();
        $reader = new Reader;
        $reader->open($file);
        $rows = [];
        foreach ($reader->getSheetIterator() as $sheet) {
            foreach ($sheet->getRowIterator() as $row) {
                $rows[] = $row->toArray();
            }
        }
        $reader->close();

        $this->assertSame(RegistrationsExport::HEADINGS, $rows[0]);
        $this->assertSame(['Siti', '081200001111', 2, 'Dikonfirmasi', 'Pelatihan Ekspor', 'Bogor'],
            [$rows[1][1], $rows[1][4], $rows[1][6], $rows[1][7], $rows[1][8], $rows[1][11]]); // nomor HP tetap teks (0 di depan)
    }

    public function test_admin_export_buttons_download_xlsx(): void
    {
        $this->seed();
        $this->actingAs(User::first());
        $schedule = \App\Models\TrainingSchedule::with('training')->first();

        Livewire::test(ListRegistrations::class)
            ->callAction(TestAction::make('export')->table())
            ->assertFileDownloaded('pendaftar-'.now()->format('Y-m-d').'.xlsx');

        Livewire::test(ListTrainingSchedules::class)
            ->callAction(TestAction::make('export')->table($schedule))
            ->assertFileDownloaded('peserta-'.$schedule->training->slug.'-'.$schedule->start_date->format('Y-m-d').'.xlsx');
    }
}
