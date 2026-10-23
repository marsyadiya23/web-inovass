<?php

namespace Tests\Feature;

use App\Filament\Resources\Registrations\Pages\ListRegistrations;
use App\Filament\Resources\TrainingSchedules\Pages\EditTrainingSchedule;
use App\Filament\Resources\TrainingSchedules\RelationManagers\RegistrationsRelationManager;
use App\Filament\Widgets\ActionItems;
use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\TrainingSchedule;
use App\Models\User;
use Filament\Actions\Testing\TestAction;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Notification;
use Livewire\Livewire;
use Tests\TestCase;

/** Alur kerja admin: tahap pendaftaran, riwayat, tab, aksi cepat, "Perlu tindakan", peserta per jadwal. */
class AdminWorkflowTest extends TestCase
{
    use RefreshDatabase;

    private TrainingSchedule $schedule;

    protected function setUp(): void
    {
        parent::setUp();
        Notification::fake();
        $cat = TrainingCategory::create(['name' => 'Alur', 'slug' => 'alur']);
        $training = Training::create(['training_category_id' => $cat->id, 'title' => 'Pelatihan Alur', 'slug' => 'pelatihan-alur']);
        $this->schedule = $training->schedules()->create(['start_date' => today()->addDays(10), 'status' => 'dibuka', 'quota' => 10]);
    }

    private function reg(string $status = 'baru', array $attrs = []): Registration
    {
        return $this->schedule->registrations()->create($attrs + [
            'name' => 'Peserta '.$status, 'email' => $status.'@example.com', 'phone' => '0812', 'participants' => 1, 'status' => $status,
        ]);
    }

    public function test_history_records_signup_and_stage_changes_with_actor(): void
    {
        $r = $this->reg();
        $this->assertSame('Mendaftar lewat website', $r->activities()->first()->description);

        $admin = User::factory()->create(['name' => 'Andy']);
        $this->actingAs($admin);
        $r->update(['status' => 'dihubungi', 'note' => 'sudah ditelepon']);

        $descs = $r->activities()->pluck('description')->all();
        $this->assertContains('Tahap: Baru → Dihubungi', $descs);
        $this->assertContains('Catatan internal diperbarui', $descs);
        $this->assertSame('Andy', $r->activities()->where('description', 'like', 'Tahap:%')->first()->user->name);
    }

    public function test_tabs_default_to_open_items_and_next_action_advances_stage(): void
    {
        $this->actingAs(User::factory()->create());
        $baru = $this->reg('baru');
        $selesai = $this->reg('selesai');

        Livewire::test(ListRegistrations::class)
            ->assertCanSeeTableRecords([$baru])
            ->assertCanNotSeeTableRecords([$selesai])
            ->callAction(TestAction::make('next')->table($baru))
            ->assertHasNoActionErrors();
        $this->assertSame('dihubungi', $baru->fresh()->status);

        Livewire::test(ListRegistrations::class, ['activeTab' => 'selesai'])
            ->assertCanSeeTableRecords([$selesai])->assertCanNotSeeTableRecords([$baru]);
    }

    public function test_bulk_stage_change(): void
    {
        $this->actingAs(User::factory()->create());
        $a = $this->reg('baru', ['email' => 'a@example.com']);
        $b = $this->reg('dihubungi', ['email' => 'b@example.com']);

        Livewire::test(ListRegistrations::class)
            ->selectTableRecords([$a, $b])
            ->callAction(TestAction::make('status')->table()->bulk(), ['status' => 'penawaran'])
            ->assertHasNoActionErrors();

        $this->assertSame(['penawaran', 'penawaran'], [$a->fresh()->status, $b->fresh()->status]);
    }

    public function test_action_items_flag_overdue_and_stale_schedules(): void
    {
        $old = $this->reg();
        $old->forceFill(['created_at' => now()->subDays(2)])->saveQuietly();
        $this->schedule->training->schedules()->create(['start_date' => today()->subDays(5), 'status' => 'dibuka']);

        $texts = array_column(ActionItems::items(), 1);
        $this->assertTrue(collect($texts)->contains(fn ($t) => str_contains($t, 'belum dihubungi lebih dari 24 jam')));
        $this->assertTrue(collect($texts)->contains(fn ($t) => str_contains($t, 'sudah lewat tetapi statusnya masih Dibuka')));
    }

    public function test_schedule_page_lists_its_registrations_and_exports(): void
    {
        $this->actingAs(User::factory()->create());
        $mine = $this->reg('baru');

        Livewire::test(RegistrationsRelationManager::class, ['ownerRecord' => $this->schedule, 'pageClass' => EditTrainingSchedule::class])
            ->assertCanSeeTableRecords([$mine])
            ->callAction(TestAction::make('export')->table())
            ->assertFileDownloaded('peserta-pelatihan-alur-'.$this->schedule->start_date->format('Y-m-d').'.xlsx');
    }
}
