<?php

namespace Database\Seeders;

use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingCategory;
use App\Models\TrainingSchedule;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

/**
 * Katalog awal pelatihan dari halaman pelatihan situs lama (database/seeders/data/layanan.json),
 * plus jadwal & pendaftar contoh di luar production supaya halaman jadwal bisa dilihat.
 */
class TrainingSeeder extends Seeder
{
    /** kategori pelatihan => [kategori layanan lama, slug induk lama...] */
    private const SOURCES = [
        'pelatihan-sertifikasi-iso' => ['Pelatihan Sertifikasi ISO', 'pelatihan-sertifikasi', ['public-training'],
            'Pelatihan standar sistem manajemen ISO/IEC/SNI untuk meningkatkan kompetensi personel organisasi.'],
        'pelatihan-akreditasi' => ['Pelatihan Akreditasi', 'pelatihan-akreditasi', ['public-training-akreditasi'],
            'Pelatihan standar akreditasi laboratorium, lembaga inspeksi, lembaga sertifikasi, dan penyelenggara uji profisiensi.'],
        'pranata-laboratorium' => ['Pranata Laboratorium', 'pranata-laboratorium', ['pranata-lab-mipa', 'pranata-lab-sosial', 'pranata-lab-kedokteran', 'pranata-lab-kesehatan'],
            'Pelatihan pranata laboratorium pendidikan sesuai standar akreditasi perguruan tinggi.'],
    ];

    public function run(): void
    {
        DB::transaction(function () {
            $this->catalog();
            if (app()->environment(['local', 'testing'])) {
                $this->demoSchedules();
            }
        });
    }

    private function catalog(): void
    {
        $services = json_decode(file_get_contents(database_path('seeders/data/layanan.json')), true)['services'];
        $sortCat = 0;

        foreach (self::SOURCES as $slug => [$name, $serviceCategory, $parents, $desc]) {
            $category = TrainingCategory::updateOrCreate(['slug' => $slug], [
                'name' => $name, 'description' => $desc, 'sort' => ++$sortCat, 'is_published' => true,
            ]);

            $sort = 0;
            foreach ($parents as $parent) {
                foreach ($services as $s) {
                    if ($s['category'] !== $serviceCategory || $s['parent'] !== $parent) {
                        continue;
                    }
                    // Situs lama menamai program per format ("Public Training ISO 9001"); katalog cukup "Pelatihan ...".
                    $title = trim(str_replace('Public Training ', '', $s['title']));
                    $title = Str::startsWith($title, 'Pelatihan') ? $title : 'Pelatihan '.$title;
                    $slugBase = Str::startsWith($s['slug'], 'public-training-')
                        ? 'pelatihan-'.Str::after($s['slug'], 'public-training-')
                        : $s['slug'];

                    Training::updateOrCreate(['slug' => $slugBase], [
                        'training_category_id' => $category->id,
                        'title' => $title,
                        'summary' => $s['summary'],
                        'highlights' => $s['highlights'] ?: null,
                        'description' => str_replace('Public Training', 'Pelatihan', (string) $s['body']),
                        'duration' => null,
                        'price' => null,
                        'sort' => ++$sort,
                        'is_published' => $s['is_published'] ?? true,
                    ]);
                }
            }
        }
    }

    private function demoSchedules(): void
    {
        if (TrainingSchedule::exists()) {
            return;
        }
        $note = 'Data contoh, hapus atau ubah sebelum dipakai.';
        $plan = [
            // [slug program, mulai +hari, lama hari, metode, lokasi, harga, kuota, status]
            ['pelatihan-iso-9001', 7, 2, 'offline', 'Bogor', 3500000, 20, 'dibuka'],
            ['pelatihan-iso-45001', 10, 2, 'online', 'Zoom Meeting', 2500000, null, 'dibuka'],
            ['pelatihan-iso-27001', 18, 3, 'hybrid', 'Jakarta & Zoom', 4500000, 25, 'dibuka'],
            ['pelatihan-iso-14001', 25, 2, 'offline', 'Jakarta', 3500000, 2, 'dibuka'],
            ['pelatihan-iso-9001', 40, 2, 'online', 'Zoom Meeting', 2500000, null, 'dibuka'],
            ['pelatihan-iso-37001', 47, 2, 'offline', 'Bandung', 3800000, 20, 'penuh'],
        ];
        foreach ($plan as [$slug, $in, $days, $method, $location, $price, $quota, $status]) {
            $training = Training::where('slug', $slug)->first() ?? Training::first();
            $start = today()->addDays($in);
            TrainingSchedule::create([
                'training_id' => $training->id,
                'start_date' => $start,
                'end_date' => $start->copy()->addDays($days - 1),
                'time' => '08.30 – 16.30 WIB',
                'method' => $method,
                'location' => $location,
                'price' => $price,
                'quota' => $quota,
                'registration_deadline' => $start->copy()->subDays(2),
                'status' => $status,
                'note' => $note,
            ]);
        }
        // Batch ISO 14001 berkuota 2 dibuat penuh oleh pendaftar contoh.
        $full = TrainingSchedule::where('quota', 2)->first();
        Registration::create(['training_schedule_id' => $full->id, 'name' => 'Contoh Peserta', 'email' => 'peserta@example.com',
            'phone' => '6281200000000', 'organization' => 'PT Contoh', 'position' => 'QHSE Officer', 'participants' => 2,
            'status' => 'dikonfirmasi', 'note' => $note]);
        Registration::create(['training_schedule_id' => TrainingSchedule::orderBy('start_date')->first()->id,
            'name' => 'Contoh Pendaftar Baru', 'email' => 'pendaftar@example.com', 'phone' => '6281300000000',
            'organization' => 'Universitas Contoh', 'participants' => 1, 'message' => 'Apakah ada sertifikat?', 'status' => 'baru']);
    }
}
