<?php

namespace Tests\Feature;

use App\Models\ContactMessage;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ContactFormTest extends TestCase
{
    use RefreshDatabase;

    // Seed juga di sini: RefreshDatabase hanya migrate (+seed) sekali per proses, jadi test pertama menentukan.
    protected $seed = true;

    private array $valid = [
        'name' => 'Budi Santoso',
        'email' => 'budi@contoh.co.id',
        'phone' => '081234567890',
        'organization' => 'PT Contoh',
        'subject' => 'Konsultasi ISO',
        'message' => 'Kami ingin konsultasi ISO 9001.',
    ];

    public function test_valid_post_stores_message(): void
    {
        $this->post(route('kontak.kirim'), $this->valid)
            ->assertRedirect()
            ->assertSessionHas('kontak_terkirim');

        $this->assertDatabaseHas('contact_messages', ['email' => 'budi@contoh.co.id', 'status' => 'baru']);
    }

    public function test_honeypot_post_stores_nothing(): void
    {
        $before = ContactMessage::count();

        $this->post(route('kontak.kirim'), $this->valid + ['website' => 'http://spam.example'])
            ->assertRedirect()
            ->assertSessionHas('kontak_terkirim');

        $this->assertSame($before, ContactMessage::count());
    }

    public function test_missing_email_fails_validation(): void
    {
        $before = ContactMessage::count();

        $this->post(route('kontak.kirim'), ['email' => ''] + $this->valid)
            ->assertSessionHasErrors('email');

        $this->assertSame($before, ContactMessage::count());
    }
}
