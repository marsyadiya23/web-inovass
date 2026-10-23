<?php

namespace App\Http\Controllers;

use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\TrainingSchedule;
use App\Models\User;
use App\Notifications\NewRegistration;
use App\Notifications\RegistrationReceived;
use Carbon\Carbon;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Notification;
use Illuminate\Support\Facades\URL;
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

        // Honeypot: bot mengisi field tersembunyi -> pura-pura sukses tanpa menyimpan.
        if (filled($request->input('website'))) {
            return redirect()->to($training->url());
        }

        $data = $request->validate([
            'training_schedule_id' => ['required', 'integer'],
            'name' => ['required', 'string', 'max:255'],
            'email' => ['required', 'email', 'max:255'],
            'phone' => ['required', 'string', 'max:30', 'regex:/^[0-9+\-\s()]{8,}$/'],
            'organization' => ['nullable', 'string', 'max:255'],
            'position' => ['nullable', 'string', 'max:255'],
            'participants' => ['required', 'integer', 'min:1', 'max:100'],
            'participant_names' => ['nullable', 'string', 'max:5000'],
            'message' => ['nullable', 'string', 'max:2000'],
        ], [], [
            'training_schedule_id' => 'jadwal', 'name' => 'nama', 'phone' => 'nomor WhatsApp',
            'participants' => 'jumlah peserta', 'participant_names' => 'nama peserta lain', 'message' => 'pesan',
        ]);
        if ($data['participants'] < 2) {
            $data['participant_names'] = null;
        }

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
        rescue(fn () => Notification::route('mail', $registration->email)->notify(new RegistrationReceived($registration, $label)));

        // Halaman terima kasih terpisah (form tidak tampil lagi -> tidak dobel). Tautan bertanda tangan:
        // berisi data pendaftar, jadi tidak bisa dibuka dengan menebak nomor.
        return redirect()->to(URL::temporarySignedRoute('pelatihan.terima-kasih', now()->addDays(7), ['registration' => $registration->id]));
    }

    public function terimaKasih(Registration $registration)
    {
        $registration->load('schedule.training');

        return view('pelatihan.terima-kasih', [
            'title' => 'Pendaftaran diterima',
            'registration' => $registration,
            'schedule' => $registration->schedule,
        ]);
    }
}
