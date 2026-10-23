<?php

namespace Tests\Feature;

use App\Filament\Resources\Users\Pages\ManageUsers;
use App\Models\User;
use Filament\Actions\Testing\TestAction;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Hash;
use Livewire\Livewire;
use Tests\TestCase;

class AdminUsersTest extends TestCase
{
    use RefreshDatabase;

    public function test_admin_can_add_admin_and_cannot_delete_self(): void
    {
        $me = User::factory()->create();
        $this->actingAs($me);

        Livewire::test(ManageUsers::class)
            ->callAction('create', ['name' => 'Andy', 'email' => 'andy@example.com', 'password' => 'rahasia-123'])
            ->assertHasNoActionErrors()
            ->assertActionHidden(TestAction::make('delete')->table($me));

        $new = User::where('email', 'andy@example.com')->first();
        $this->assertTrue(Hash::check('rahasia-123', $new->password));

        // Ubah tanpa isi password = password lama tetap
        Livewire::test(ManageUsers::class)
            ->callAction(TestAction::make('edit')->table($new), ['name' => 'Andy B', 'password' => ''])
            ->assertHasNoActionErrors();
        $this->assertTrue(Hash::check('rahasia-123', $new->fresh()->password));
        $this->assertSame('Andy B', $new->fresh()->name);
    }
}
