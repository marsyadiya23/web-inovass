@extends('layouts.site', ['title' => 'Tentang Kami', 'metaDescription' => $c['hero_desc'] ?? null])

@php
  // Ikon kartu "Mengapa Memilih" (SVG asli situs lama), dipilih per kartu di admin.
  $icons = [
    'users' => '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path>',
    'activity' => '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>',
    'grid' => '<rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect>',
    'clock' => '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
    'file' => '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline>',
    'shield' => '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>',
  ];
  $paragraphs = array_filter(preg_split('/\R+/',$c['profile_text'] ?? ''), 'filled');
  $rows = $clients->split(2); // dua baris marquee seperti situs lama
@endphp

@section('content')
  @include('partials.page-hero', [
    'heroTitle' => $c['hero_title'] ?? 'Tentang',
    'heroEm' => $c['hero_em'] ?? 'Kami',
    'heroDesc' => $c['hero_desc'] ?? null,
    'heroImage' => $c['hero_image'] ?? null,
    'crumbs' => [['Tentang Kami', null]],
  ])

  <!-- PROFIL PERUSAHAAN -->
  <section class="page-section about-profile">
    <div class="about-grid">
      <div class="about-image reveal-left">
        @if ($src = media_url($c['profile_image'] ?? null))<img src="{{ $src }}" alt="Profil {{ $c['profile_title'] ?? 'INOVASS' }}" />@endif
      </div>
      <div class="about-text reveal-right">
        <h2>{{ $c['profile_title'] ?? '' }}@if (filled($c['profile_em'] ?? null))<br /><em>{{ $c['profile_em'] }}</em>@endif</h2>
        @foreach ($paragraphs as $p)
          <p>{{ $p }}</p>
        @endforeach
        @if (! empty($c['stats']))
          <div class="about-stats">
            @foreach ($c['stats'] as $stat)
              <div class="stat-item">
                <span class="stat-num">{{ $stat['number'] ?? '' }}</span>
                <span class="stat-label">{{ $stat['label'] ?? '' }}</span>
              </div>
            @endforeach
          </div>
        @endif
      </div>
    </div>
  </section>

  <!-- VISI MISI -->
  <section class="page-section about-visi-misi">
    <div class="about-grid">
      <div class="about-text reveal-left">
        <h2>{{ $c['visi_title'] ?? 'Visi dan Misi' }}@if (filled($c['visi_em'] ?? null))<br /><em>{{ $c['visi_em'] }}</em>@endif</h2>
        <div class="visi-misi-content">
          <div class="visi-block">
            <h3>Visi</h3>
            <p>{{ $c['visi'] ?? '' }}</p>
          </div>
          <div class="misi-block">
            <h3>Misi</h3>
            <ul>
              @foreach ($c['misi'] ?? [] as $item)
                <li>{{ $item }}</li>
              @endforeach
            </ul>
          </div>
        </div>
      </div>
      <div class="about-image reveal-right">
        @if ($src = media_url($c['visi_image'] ?? null))<img src="{{ $src }}" alt="Visi Misi INOVASS" />@endif
      </div>
    </div>
  </section>

  <!-- MENGAPA MEMILIH KAMI -->
  @if (! empty($c['why_items']))
    <section class="page-section about-why-us">
      <div class="section-header reveal">
        <h2>{{ $c['why_title'] ?? '' }}@if (filled($c['why_em'] ?? null))<br /><em>{{ $c['why_em'] }}</em>@endif</h2>
      </div>
      <div class="why-us-grid">
        @foreach ($c['why_items'] as $i => $card)
          <div class="why-card reveal delay-{{ $i % 6 + 1 }}">
            <div class="why-icon">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00e0a0" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{!! $icons[$card['icon'] ?? ''] ?? $icons['shield'] !!}</svg>
            </div>
            <div class="why-card-content">
              <h3>{{ $card['title'] ?? '' }}</h3>
              <p>{{ $card['text'] ?? '' }}</p>
            </div>
          </div>
        @endforeach
      </div>
    </section>
  @endif

  <!-- TELAH MELAYANI & BERKOLABORASI -->
  @if ($clients->isNotEmpty())
    <section class="page-section about-clients">
      <div class="section-header reveal">
        <h2>{{ $c['clients_title'] ?? 'Telah Melayani & Berkolaborasi' }}@if (filled($c['clients_em'] ?? null))<br /><em>{{ $c['clients_em'] }}</em>@endif</h2>
      </div>
      @foreach ($rows as $r => $row)
        <div class="clients-marquee-wrap">
          <div class="clients-marquee-track {{ $r % 2 ? 'clients-marquee-right' : 'clients-marquee-left' }}">
            {{-- Daftar dirender dua kali agar marquee berputar tanpa jeda. --}}
            @foreach ([$row, $row] as $copy)
              @foreach ($copy as $client)
                <div class="client-logo-item"><img src="{{ media_url($client->logo) }}" alt="{{ $client->name }}" loading="lazy" /></div>
              @endforeach
            @endforeach
          </div>
        </div>
      @endforeach
    </section>
  @endif

  <!-- CTA -->
  <section class="page-cta reveal">
    <h2>{{ $c['cta_title'] ?? 'Bergabunglah dengan' }}<br /><em>{{ $c['cta_em'] ?? 'perjalanan kami.' }}</em></h2>
    <p>{{ $c['cta_text'] ?? '' }}</p>
    <a href="{{ url('kontak.html') }}" class="btn-outline">{{ $c['cta_button'] ?? 'Hubungi Kami' }}</a>
  </section>
@endsection
