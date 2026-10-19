<?php

namespace Tests\Feature;

use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\TrainingSchedule;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

/** Aturan bisnis pendaftaran: status, kuota, batas daftar, kepemilikan jadwal, honeypot, visibilitas. */
class TrainingRegistrationTest extends TestCase
{
    use RefreshDatabase;

    private Training $training;

    protected function setUp(): void
    {
        parent::setUp();
        $cat = TrainingCategory::create(['name' => 'Uji', 'slug' => 'uji']);
        $this->training = Training::create(['training_category_id' => $cat->id, 'title' => 'Pelatihan Uji', 'slug' => 'pelatihan-uji']);
    }

    private function schedule(array $attrs = []): TrainingSchedule
    {
        return $this->training->schedules()->create($attrs + ['start_date' => today()->addDays(10), 'status' => 'dibuka']);
    }

    /** Hitung pendaftar milik kategori uji saja (DB test bisa berisi data seed dari test lain). */
    private function regs(): int
    {
        return Registration::whereHas('schedule.training', fn ($q) => $q->where('training_category_id', $this->training->training_category_id))->count();
    }

    private function daftar(TrainingSchedule $s, array $extra = [])
    {
        return $this->post('/pelatihan/pelatihan-uji/daftar', $extra + [
            'training_schedule_id' => $s->id, 'name' => 'Budi', 'email' => 'budi@example.com',
            'phone' => '081234567890', 'participants' => 1,
        ]);
    }

    public function test_registers_on_open_schedule(): void
    {
        $s = $this->schedule(['quota' => 3]);
        $this->daftar($s)->assertRedirect()->assertSessionHas('daftar_ok');
        $this->assertSame(1, $this->regs());
        $this->assertSame('baru', Registration::latest('id')->first()->status);
        $this->assertSame(2, $s->fresh()->seatsLeft());
    }

    public function test_rejects_more_participants_than_seats_left(): void
    {
        $s = $this->schedule(['quota' => 2]);
        $this->daftar($s, ['participants' => 3])->assertSessionHasErrors('participants');
        $this->assertSame(0, $this->regs());
    }

    public function test_rejects_full_closed_past_deadline_or_foreign_schedule(): void
    {
        $full = $this->schedule(['quota' => 1]);
        $full->registrations()->create(['name' => 'A', 'email' => 'a@example.com', 'phone' => '0812', 'participants' => 1]);
        $closed = $this->schedule(['status' => 'ditutup']);
        $late = $this->schedule(['registration_deadline' => today()->subDay()]);
        $other = Training::create(['training_category_id' => $this->training->training_category_id, 'title' => 'Lain', 'slug' => 'lain'])
            ->schedules()->create(['start_date' => today()->addDays(5)]);

        foreach ([$full, $closed, $late, $other] as $s) {
            $this->daftar($s)->assertSessionHasErrors('training_schedule_id');
        }
        $this->assertSame(1, $this->regs());
    }

    public function test_cancelled_registrations_free_their_seats(): void
    {
        $s = $this->schedule(['quota' => 1]);
        $s->registrations()->create(['name' => 'A', 'email' => 'a@example.com', 'phone' => '0812', 'participants' => 1, 'status' => 'batal']);
        $this->assertTrue($s->isOpen());
    }

    public function test_honeypot_stores_nothing(): void
    {
        $this->daftar($this->schedule(), ['website' => 'http://spam.example'])->assertRedirect();
        $this->assertSame(0, $this->regs());
    }

    public function test_schedule_page_lists_only_upcoming_visible_batches(): void
    {
        $this->schedule(['start_date' => today()->addDays(3), 'location' => 'KOTA-MENDATANG']);
        $this->schedule(['start_date' => today()->subDays(3), 'location' => 'KOTA-LEWAT']);
        $this->schedule(['status' => 'batal', 'location' => 'KOTA-BATAL']);

        $this->get('/jadwal-pelatihan')->assertOk()
            ->assertSee('KOTA-MENDATANG')->assertDontSee('KOTA-LEWAT')->assertDontSee('KOTA-BATAL');

        $this->training->update(['is_published' => false]);
        $this->get('/jadwal-pelatihan')->assertOk()->assertDontSee('KOTA-MENDATANG');
        $this->get('/pelatihan/pelatihan-uji')->assertNotFound();
    }
}
