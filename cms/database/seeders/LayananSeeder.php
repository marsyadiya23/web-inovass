<?php

namespace Database\Seeders;

use App\Models\Service;
use App\Models\ServiceCategory;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

/** Impor 7 kategori + semua halaman layanan hasil ekstraksi situs lama (database/seeders/data/layanan.json). */
class LayananSeeder extends Seeder
{
    public function run(): void
    {
        DB::transaction(fn () => $this->import());
    }

    private function import(): void
    {
        $data = json_decode(file_get_contents(database_path('seeders/data/layanan.json')), true);

        $categories = [];
        foreach ($data['categories'] as $c) {
            $categories[$c['slug']] = ServiceCategory::updateOrCreate(['slug' => $c['slug']], [
                'name' => $c['name'],
                'short_description' => $c['short_description'] ?? null,
                'intro' => $c['intro'] ?? null,
                'image' => $c['image'] ?? null,
                'sort' => $c['sort'] ?? 0,
                'is_published' => true,
            ])->id;
        }

        // Dua putaran: level-3 dulu (parent null), lalu anak-anaknya.
        $ids = [];
        foreach ([false, true] as $children) {
            foreach ($data['services'] as $s) {
                if (filled($s['parent']) !== $children) {
                    continue;
                }
                $cat = $categories[$s['category']];
                $ids[$s['category'].'/'.$s['slug']] = Service::updateOrCreate(
                    ['service_category_id' => $cat, 'slug' => $s['slug']],
                    [
                        'parent_id' => $children ? $ids[($s['parent_category'] ?? $s['category']).'/'.$s['parent']] : null,
                        'title' => $s['title'],
                        'summary' => $s['summary'],
                        'highlights' => $s['highlights'] ?: null,
                        'body' => $s['body'],
                        'image' => $s['image'],
                        'sort' => $s['sort'] ?? 0,
                        'is_published' => $s['is_published'] ?? true,
                    ],
                )->id;
            }
        }
    }
}
