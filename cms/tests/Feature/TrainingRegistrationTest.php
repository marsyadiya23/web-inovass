<?php

namespace Tests\Feature;

use App\Models\PageContent;
use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\TrainingSchedule;
use App\Models\User;
use App\Notifications\NewRegistration;
use App\Notifications\RegistrationReceived;
use App\Notifications\RegistrationStatusChanged;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Notification;
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
        Notification::fake();
        $admin = User::factory()->create();
        $s = $this->schedule(['quota' => 3]);
        $res = $this->daftar($s, ['participants' => 2, 'participant_names' => "Ani\nCici"]);
        $reg = Registration::latest('id')->first();

        // Halaman terima kasih: tautan bertanda tangan, berisi nomor pendaftaran; tanpa tanda tangan ditolak
        $res->assertRedirectContains('/pelatihan/terima-kasih/'.$reg->id);
        $this->get($res->headers->get('Location'))->assertOk()->assertSee($reg->code())->assertSee('Pelatihan Uji');
        $this->get('/pelatihan/terima-kasih/'.$reg->id)->assertForbidden();

        Notification::assertSentTo($admin, NewRegistration::class);
        Notification::assertSentOnDemand(RegistrationReceived::class,
            fn ($n, $channels, $notifiable) => $notifiable->routes['mail'] === 'budi@example.com');
        $this->assertSame(1, $this->regs());
        $this->assertSame('baru', $reg->status);
        $this->assertSame("Ani\nCici", $reg->participant_names);
        $this->assertMatchesRegularExpression('/^REG-\d{4}-\d{4,}$/', $reg->code());
        $this->assertSame(1, $s->fresh()->seatsLeft());
    }

    public function test_participant_names_dropped_for_single_participant(): void
    {
        $this->daftar($this->schedule(), ['participants' => 1, 'participant_names' => 'Sisa isian']);
        $this->assertNull(Registration::latest('id')->first()->participant_names);
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

    public function test_status_change_emails_registrant_only_on_confirm_or_cancel(): void
    {
        $r = $this->schedule()->registrations()->create(['name' => 'Ani', 'email' => 'ani@example.com', 'phone' => '0812', 'participants' => 1, 'status' => 'baru']);
        Notification::fake();

        $r->update(['note' => 'sudah ditelepon']);
        Notification::assertNothingSent();

        $r->update(['status' => 'dikonfirmasi']);
        $r->update(['status' => 'batal']);
        Notification::assertSentOnDemandTimes(RegistrationStatusChanged::class, 2);
    }

    public function test_hidden_price_and_program_syllabus(): void
    {
        $this->training->update(['price' => 1750000, 'brochure' => 'brosur/program-uji.pdf']);
        $this->schedule(['location' => 'KOTA-A', 'price' => 2345678, 'hide_price' => true]);
        $this->schedule(['location' => 'KOTA-B', 'start_date' => today()->addDays(20)]);

        PageContent::put('settings', ['show_prices' => true]);
        $this->get('/jadwal-pelatihan')->assertOk()
            ->assertDontSee('2.345.678')->assertSee('Hubungi kami')   // harga jadwal ini disembunyikan
            ->assertSee('1.750.000')                                     // jadwal lain tetap pakai harga program
            ->assertSee('brosur/program-uji.pdf');                       // silabus program tampil di kartu jadwal

        PageContent::put('settings', ['show_prices' => false]);         // saklar Pengaturan Situs mati
        $this->get('/jadwal-pelatihan')->assertOk()->assertDontSee('1.750.000');
    }
}
