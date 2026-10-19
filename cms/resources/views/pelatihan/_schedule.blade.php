{{-- Kartu satu jadwal. Props: $schedule (with training), $showTitle (default true) --}}
@php
    $status = $schedule->publicStatus();
    $badge = $schedule->isOpen() ? 'open' : ($status === 'Penuh' ? 'full' : 'closed');
    $left = $schedule->seatsLeft();
    $training = $schedule->training;
@endphp
<div class="pl-card">
  <div class="pl-date">
    <span class="d">{{ $schedule->start_date->format('d') }}</span>
    <span class="m">{{ $schedule->start_date->translatedFormat('M Y') }}</span>
  </div>
  <div>
    @if ($showTitle ?? true)
      <h3><a href="{{ $training->url() }}">{{ $training->title }}</a></h3>
    @endif
    <div class="pl-meta">
      <span>📅 {{ $schedule->dateLabel() }}</span>
      @if ($schedule->time)<span>🕘 {{ $schedule->time }}</span>@endif
      <span>📍 {{ $schedule->methodLabel() }}{{ $schedule->location ? ' · '.$schedule->location : '' }}</span>
      @if ($left !== null && $schedule->isOpen())<span>👥 Sisa {{ $left }} kursi</span>@endif
    </div>
    @if ($schedule->note)<div class="pl-note">{{ $schedule->note }}</div>@endif
  </div>
  <div class="pl-side">
    <span class="pl-badge {{ $badge }}">{{ $status }}</span>
    <div class="pl-price">{{ $schedule->priceLabel() }}</div>
    @if ($schedule->isOpen())
      <a class="pl-btn" href="{{ $training->url() }}?jadwal={{ $schedule->id }}#daftar">Daftar</a>
    @else
      <a class="pl-btn ghost" href="{{ $training->url() }}">Detail</a>
    @endif
  </div>
</div>
