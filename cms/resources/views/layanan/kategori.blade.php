@extends('layouts.site')

@section('content')
  @include('partials.page-hero', [
      'heroTitle' => 'Layanan',
      'heroEm' => 'Kami',
      'heroDesc' => 'Solusi konsultasi ISO profesional untuk membantu organisasi membangun, menerapkan, meningkatkan, dan memperoleh sertifikasi sistem manajemen sesuai standar nasional maupun internasional',
      'heroImage' => $category->image ?: 'legacy/layanan kami.jpeg',
      'crumbs' => [['Layanan', null]],
  ])

  <section class="nav-tabs-section" id="navTabsSection">
    <div class="nav-tabs-container">
      <div class="nav-tabs-card">
        @foreach ($categories as $cat)
          <a href="{{ $cat->url() }}" class="nav-tab-item {{ $cat->is($category) ? 'active' : '' }}">
            <span class="nav-tab-label">{{ $cat->name }}</span>
          </a>
        @endforeach
      </div>
    </div>
  </section>

  <section class="service-content-section">
    <div class="service-content-container">
      <div class="service-content-card active">
        <div class="service-intro">
          <h2>{{ $category->name }}</h2>
          @if (filled($category->intro))<p class="service-intro-desc">{{ $category->intro }}</p>@endif
        </div>

        <div class="service-grid">
          @forelse ($services as $service)
            <div class="service-item-card">
              <div class="service-item-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="#1e3a8a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
              </div>
              <h3>{{ $service->title }}</h3>
              @if (filled($service->summary))<p>{{ $service->summary }}</p>@endif
              <a href="{{ url("layanan/{$category->slug}/{$service->slug}.html") }}" class="service-item-btn">
                Lihat Detail
                <svg viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"/>
                </svg>
              </a>
            </div>
          @empty
            <p>Layanan untuk kategori ini segera hadir.</p>
          @endforelse
        </div>
      </div>
    </div>
  </section>

  @include('partials.cta')
@endsection
