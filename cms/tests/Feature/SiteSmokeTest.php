<?php

namespace Tests\Feature;

use App\Models\Article;
use App\Models\Service;
use App\Models\ServiceCategory;
use App\Models\Training;
use App\Models\User;
use Filament\Facades\Filament;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

/**
 * Smoke test: seeder penuh, lalu setiap halaman publik & admin harus 200.
 * Dinamis: halaman/resource baru otomatis ikut dicek.
 */
class SiteSmokeTest extends TestCase
{
    use RefreshDatabase;

    // $seed = true hanya seed saat migrasi pertama; DB in-memory dipakai ulang antar test, jadi seed per test.
    protected function setUp(): void
    {
        parent::setUp();
        $this->seed();
    }

    public function test_public_pages_render(): void
    {
        $urls = ['/', '/tentang.html', '/produk.html', '/kontak.html', '/berita', '/jadwal-pelatihan', '/pelatihan', '/jadwal-pelatihan?metode=online'];
        $urls = array_merge(
            $urls,
            ServiceCategory::published()->get()->map(fn ($c) => parse_url($c->url(), PHP_URL_PATH))->all(),
            Service::with('category')->where('is_published', true)->get()->map(fn ($s) => parse_url($s->url(), PHP_URL_PATH))->all(),
            Article::published()->get()->map(fn ($a) => parse_url($a->url(), PHP_URL_PATH))->all(),
            Training::published()->get()->map(fn ($t) => parse_url($t->url(), PHP_URL_PATH))->all(),
        );

        foreach ($urls as $url) {
            $this->get($url)->assertOk();
        }
    }

    public function test_admin_pages_render(): void
    {
        $this->actingAs(User::first());
        $panel = Filament::getPanel('admin');

        $this->get('/admin')->assertOk();

        foreach ($panel->getPages() as $page) {
            $this->get($page::getUrl())->assertOk();
        }

        foreach ($panel->getResources() as $resource) {
            $this->get($resource::getUrl('index'))->assertOk();
            if ($resource::hasPage('create')) {
                $this->get($resource::getUrl('create'))->assertOk();
            }
            if ($resource::hasPage('edit') && ($record = $resource::getModel()::first())) {
                $this->get($resource::getUrl('edit', ['record' => $record]))->assertOk();
            }
        }
    }
}
