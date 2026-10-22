<?php

namespace Tests\Feature;

use App\Filament\Pages\SiteSettings;
use App\Models\PageContent;
use App\Models\User;
use Database\Seeders\DatabaseSeeder;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Livewire\Livewire;
use Tests\TestCase;

class SiteSettingsTest extends TestCase
{
    use RefreshDatabase;

    /** Menyimpan Pengaturan Situs tanpa mengubah apa pun tidak boleh menghapus logo / nomor WA. */
    public function test_save_without_changes_keeps_settings(): void
    {
        $this->seed(DatabaseSeeder::class);
        $before = PageContent::get('settings');
        $this->actingAs(User::first());

        Livewire::test(SiteSettings::class)->call('save')->assertHasNoErrors();

        $after = PageContent::get('settings');
        $this->assertSame($before['logo'], $after['logo']);
        $this->assertSame($before['whatsapp'], $after['whatsapp']);
    }
}
