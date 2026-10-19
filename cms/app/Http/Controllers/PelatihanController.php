<?php

namespace App\Http\Controllers;

use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\TrainingSchedule;
use App\Models\User;
use App\Notifications\NewRegistration;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Notification;
use Illuminate\Validation\ValidationException;

class PelatihanController extends Controller
{
    /** Daftar semua jadwal mendatang, filter bulan / kategori / metode. */
    public function jadwal(Request $request)
    {
        $filters = $request->validate([
            'bulan' => ['nullable', 'date_format:Y-m'],
            'kategori' => ['nullable', 'string', 'max:100'],
            'metode' => ['nullable', 'in:'.implode(',', array_keys(TrainingSchedule::METHODS))],
        ]);

        $query = TrainingSchedule::visible()->with('training.category')
            ->withSum(['registrations as seats_taken' => fn ($q) => $q->where('status', '!=', 'batal')], 'participants');

        if ($bulan = $filters['bulan'] ?? null) {
            $month = Carbon::createFromFormat('Y-m', $bulan)->startOfMonth();
            $query->whereBetween('start_date', [$month, $month->copy()->endOfMonth()]);
        }
        if ($kategori = $filters['kategori'] ?? null) {
            $query->whereHas('training.category', fn ($q) => $q->where('slug', $kategori));
        }
        if ($metode = $filters['metode'] ?? null) {
            $query->where('method', $metode);
        }

        // Pilihan bulan: bulan-bulan yang memang punya jadwal.
        $months = TrainingSchedule::visible()->pluck('start_date')
            ->map(fn ($d) => $d->format('Y-m'))->unique()->values();

        return view('pelatihan.jadwal', [
            'title' => 'Jadwal Pelatihan',
            'metaDescription' => 'Jadwal pelatihan ISO, akreditasi, dan pranata laboratorium INOVASS yang akan datang.',
            'schedules' => $query->get()->groupBy(fn ($s) => $s->start_date->format('Y-m')),
            'months' => $months,
            'categories' => TrainingCategory::published()->get(),
            'filters' => $filters,
        ]);
    }

    public function index()
    {
        return view('pelatihan.index', [
            'title' => 'Program Pelatihan',
            'metaDescription' => 'Katalog program pelatihan INOVASS.',
            'categories' => TrainingCategory::published()->with(['trainings' => fn ($q) => $q->published()
                ->withCount(['schedules as upcoming_count' => fn ($s) => $s->upcoming()])])->get(),
        ]);
    }

    public function show(string $slug)
    {
        $training = Training::with('category')->where('slug', $slug)->where('is_published', true)->firstOrFail();

        return view('pelatihan.show', [
            'title' => $training->title,
            'metaDescription' => $training->meta_description ?: $training->summary,
            'training' => $training,
            'schedules' => $training->upcomingSchedules()->get(),
        ]);
    }

    public function daftar(Request $request, string $slug)
    {
        $training = Training::where('slug', $slug)->where('is_published', true)->firstOrFail();
        $back = redirect()->to($training->url().'#daftar');

        // Honeypot: bot mengisi field tersembunyi -> pura-pura sukses tanpa menyimpan.
        if (filled($request->input('website'))) {
            return $back->with('daftar_ok', ['schedule' => '', 'wa' => '']);
        }

        $data = $request->validate([
            'training_schedule_id' => ['required', 'integer'],
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'email', 'max:255'],
            'phone' => ['required', 'string', 'max:30', 'regex:/^[0-9+\-\s()]{8,}$/'],
            'organization' => ['nullable', 'string', 'max:255'],
            'position' => ['nullable', 'string', 'max:255'],
            'participants' => ['required', 'integer', 'min:1', 'max:100'],
            'message' => ['nullable', 'string', 'max:2000'],
        ], [], [
            'training_schedule_id' => 'jadwal', 'name' => 'nama', 'phone' => 'nomor WhatsApp',
            'participants' => 'jumlah peserta', 'message' => 'pesan',
        ]);

        $schedule = $training->schedules()->find($data['training_schedule_id']);
        if (! $schedule || ! $schedule->isOpen()) {
            throw ValidationException::withMessages(['training_schedule_id' => 'Jadwal ini sudah tidak menerima pendaftaran.']);
        }
        if (($left = $schedule->seatsLeft()) !== null && $data['participants'] > $left) {
            throw ValidationException::withMessages(['participants' => "Sisa kuota jadwal ini {$left} peserta."]);
        }

        $registration = Registration::create($data + ['status' => 'baru']);

        $label = $training->title.' ('.$schedule->dateLabel().')';
        // Email gagal (SMTP mati, dll.) tidak boleh menggagalkan pendaftaran; error tetap tercatat di laravel.log.
        rescue(fn () => Notification::send(User::all(), new NewRegistration($registration, $label)));
        $wa = implode("\n", array_filter([
            'Halo INOVASS, saya sudah mendaftar pelatihan:',
            $label,
            'Nama: '.$data['name'],
            filled($data['organization'] ?? null) ? 'Instansi: '.$data['organization'] : null,
            'Jumlah peserta: '.$data['participants'],
        ]));

        return $back->with('daftar_ok', ['schedule' => $label, 'wa' => $wa]);
    }
}
