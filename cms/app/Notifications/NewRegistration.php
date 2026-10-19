<?php

namespace App\Notifications;

use App\Models\Registration;
use Illuminate\Notifications\Messages\MailMessage;
use Illuminate\Notifications\Notification;

/** Email ke semua akun admin setiap ada pendaftar baru. */
class NewRegistration extends Notification
{
    public function __construct(public Registration $registration, public string $scheduleLabel) {}

    public function via(object $notifiable): array
    {
        return ['mail'];
    }

    public function toMail(object $notifiable): MailMessage
    {
        $r = $this->registration;

        return (new MailMessage)
            ->subject('Pendaftar baru: '.$r->name.' — '.$this->scheduleLabel)
            ->replyTo($r->email, $r->name)
            ->greeting('Pendaftar baru')
            ->line('**Pelatihan:** '.$this->scheduleLabel)
            ->line('**Nama:** '.$r->name)
            ->line('**Instansi:** '.($r->organization ?: '-').' · **Jabatan:** '.($r->position ?: '-'))
            ->line('**WhatsApp:** '.$r->phone.' · **Email:** '.$r->email)
            ->line('**Jumlah peserta:** '.$r->participants)
            ->lineIf(filled($r->message), '**Pesan:** '.$r->message)
            ->action('Proses di admin', url('/admin/registrations/'.$r->id.'/edit'))
            ->salutation('Balas email ini untuk langsung menghubungi pendaftar.');
    }
}
