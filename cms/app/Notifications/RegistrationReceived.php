<?php

namespace App\Notifications;

use App\Models\PageContent;
use App\Models\Registration;
use Illuminate\Notifications\Messages\MailMessage;
use Illuminate\Notifications\Notification;

/** Email ke pendaftar sesaat setelah mendaftar lewat website. */
class RegistrationReceived extends Notification
{
    public function __construct(public Registration $registration, public string $scheduleLabel) {}

    public function via(object $notifiable): array
    {
        return ['mail'];
    }

    public function toMail(object $notifiable): MailMessage
    {
        $r = $this->registration;
        $s = PageContent::get('settings');
        $wa = preg_replace('/\D/', '', $s['whatsapp'] ?? '');

        $mail = (new MailMessage)
            ->subject('Pendaftaran diterima ('.$r->code().'): '.$this->scheduleLabel)
            ->greeting('Halo '.$r->name.',')
            ->line('Terima kasih, pendaftaran Anda untuk **'.$this->scheduleLabel.'** sudah kami terima.')
            ->line('**No. pendaftaran:** '.$r->code().' (sebutkan nomor ini saat menghubungi kami)')
            ->line('**Jumlah peserta:** '.$r->participants.($r->organization ? ' · **Instansi:** '.$r->organization : ''))
            ->line('Tim INOVASS akan menghubungi Anda melalui WhatsApp atau email maksimal 1×24 jam kerja untuk konfirmasi dan informasi pembayaran.')
            ->salutation('Salam, Tim INOVASS');

        if (filled($s['email'] ?? null)) {
            $mail->replyTo($s['email'], 'INOVASS');
        }

        return $wa ? $mail->action('Hubungi kami via WhatsApp', 'https://wa.me/'.$wa) : $mail;
    }
}
