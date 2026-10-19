<?php

namespace Tests\Feature;

use App\Filament\Pages\HomeContent;
use App\Models\PageContent;
use App\Models\User;
use Database\Seeders\HomeSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;
use Tests\TestCase;

class HomeContentTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_edit_roundtrips_and_shows_on_homepage(): void
    {
        $this->seed(HomeSeeder::class);
        $before = PageContent::get('home');
        $this->actingAs(User::factory()->create());

        Livewire::test(HomeContent::class)
            ->assertOk()->assertSet('data.hero.title', 'The Maker of Innovation')
            ->set('data.hero.eyebrow', 'Eyebrow Baru')
            ->call('save')
            ->assertHasNoErrors();

        $after = PageContent::where('key', 'home')->first()->data;
        $this->assertSame('Eyebrow Baru', $after['hero']['eyebrow']);
        $after['hero']['eyebrow'] = $before['hero']['eyebrow'];
        $this->assertEquals($before, $after); // simpan tanpa ubah apa pun = data seeder utuh

        $this->get('/')->assertOk()->assertSee('Eyebrow Baru')->assertSee('Pertumbuhan Organisasi');
    }
}
