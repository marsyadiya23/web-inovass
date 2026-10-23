@extends('layouts.site')

@push('styles')
  <link rel="stylesheet" href="{{ asset('assets/css/pelatihan.css') }}" />
  <meta name="robots" content="noindex" />
@endpush

@php
    $s = \App\Models\PageContent::get('settings');
    $wa = preg_replace('/\D/', '', $s['whatsapp'] ?? '');
    $r = $registration;
    $training = $schedule->training;
    $waText = implode("\n", array_filter([
        'Halo INOVASS, saya sudah mendaftar pelatihan.',
        'No. pendaftaran: '.$r->code(),
        $training->title.' ('.$schedule->dateLabel().')',
        'Nama: '.$r->name,
        $r->organization ? 'Instansi: '.$r->organization : null,
        'Jumlah peserta: '.$r->participants,
    ]));
@endphp

@section('content')
  <section class="pl-section">
    <div class="pl-container pl-thanks">
      <div class="pl-box">
        <div class="pl-eyebrow">Pendaftaran diterima</div>
        <h1 class="pl-heading">Terima kasih, <em>{{ $r->name }}</em></h1>
        <p class="pl-code">No. pendaftaran <strong>{{ $r->code() }}</strong></p>

        <dl class="pl-summary">
          <dt>Pelatihan</dt><dd>{{ $training->title }}</dd>
          <dt>Jadwal</dt><dd>{{ $schedule->dateLabel() }}{{ $schedule->time ? ', '.$schedule->time : '' }}</dd>
          <dt>Tempat</dt><dd>{{ $schedule->methodLabel() }}{{ $schedule->location ? ' · '.$schedule->location : '' }}</dd>
          <dt>Jumlah peserta</dt><dd>{{ $r->participants }}</dd>
          @if ($schedule->priceVisible())
            <dt>Perkiraan biaya</dt><dd>{{ $r->participants }} × Rp {{ number_format($schedule->effectivePrice(), 0, ',', '.') }} = <strong>Rp {{ number_format($r->estimatedTotal(), 0, ',', '.') }}</strong></dd>
          @endif
        </dl>

        <h3>Langkah berikutnya</h3>
        <ol class="pl-steps">
          <li>Email tanda terima dikirim ke <strong>{{ $r->email }}</strong>. Cek juga folder Spam.</li>
          <li>Tim INOVASS menghubungi Anda maksimal <strong>1×24 jam kerja</strong> untuk konfirmasi{{ $schedule->priceVisible() ? '' : ', rincian biaya,' }} dan pembayaran.</li>
          <li>Ingin lebih cepat? Konfirmasi lewat WhatsApp dengan menyebutkan nomor pendaftaran di atas.</li>
        </ol>

        <div class="pl-actions">
          @if ($wa)
            <a class="pl-btn" href="https://wa.me/{{ $wa }}?text={{ rawurlencode($waText) }}" target="_blank" rel="noopener">Konfirmasi via WhatsApp</a>
          @endif
          <a class="pl-btn ghost" href="{{ route('pelatihan.jadwal') }}">Lihat jadwal lain</a>
        </div>
      </div>
    </div>
  </section>
@endsection
