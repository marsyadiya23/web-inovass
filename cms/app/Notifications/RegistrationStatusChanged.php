<?php

namespace App\Notifications;

use App\Models\PageContent;
use App\Models\Registration;
use Illuminate\Notifications\Messages\MailMessage;
use Illuminate\Notifications\Notification;

/** Email ke pendaftar saat admin mengubah status ke Dikonfirmasi atau Batal (lihat Registration::booted). */
class RegistrationStatusChanged extends Notification
{
    public function __construct(public Registration $registration) {}

    public function via(object $notifiable): array
    {
        return ['mail'];
    }

    public function toMail(object $notifiable): MailMessage
    {
        $r = $this->registration->loadMissing('schedule.training');
        $schedule = $r->schedule;
        $label = $schedule->training->title.' ('.$schedule->dateLabel().') — '.$r->code();
        $s = PageContent::get('settings');

        $mail = (new MailMessage)->greeting('Halo '.$r->name.',')->salutation('Salam, Tim INOVASS');
        if (filled($s['email'] ?? null)) {
            $mail->replyTo($s['email'], 'INOVASS');
        }

        if ($r->status === 'batal') {
            return $mail->subject('Pendaftaran dibatalkan: '.$label)
                ->line('Pendaftaran Anda untuk **'.$label.'** telah dibatalkan.')
                ->line('Jika ini tidak sesuai atau Anda ingin mendaftar ke jadwal lain, silakan balas email ini.');
        }

        return $mail->subject('Pendaftaran dikonfirmasi: '.$label)
            ->line('Pendaftaran Anda untuk **'.$label.'** telah **dikonfirmasi**.')
            ->line('**Waktu:** '.$schedule->dateLabel().($schedule->time ? ', '.$schedule->time : ''))
            ->line('**Tempat:** '.$schedule->methodLabel().($schedule->location ? ' · '.$schedule->location : ''))
            ->line('**Jumlah peserta:** '.$r->participants)
            ->lineIf(filled($schedule->note), $schedule->note)
            ->line('Sampai jumpa di pelatihan.');
    }
}
