@extends('layouts.site')

@php
  $hero = $h['hero'] ?? [];
  $about = $h['about'] ?? [];
  $svc = $h['services'] ?? [];
  $prod = $h['products'] ?? [];
  $bp = $h['training'] ?? [];
  $wi = $h['why'] ?? [];
  $pw = $h['process'] ?? [];
  $bi = $h['news'] ?? [];
  $tm = $h['testimonials'] ?? [];
  $fq = $h['faq'] ?? [];
  $cta = $h['cta'] ?? [];
  $svcCards = array_values($svc['cards'] ?? []);
  $svcRight = array_slice($svcCards, 1);
  $clientRows = $clients->isEmpty() ? [] : $clients->split(2)->all();
  $fallbackImg = media_url('legacy/wallpaper 3.png');
@endphp

@section('content')

  <!-- HERO -->
  <section class="hero" id="hero">
    @if (filled($hero['image'] ?? null))
      <img src="{{ media_url($hero['image']) }}" alt="" class="hero-bg" />
    @endif
    <div class="hero-content">
      @if (filled($hero['eyebrow'] ?? null))<p class="hero-eyebrow">{{ $hero['eyebrow'] }}</p>@endif
      <h1>{{ $hero['title'] ?? '' }}@if (filled($hero['title_em'] ?? null))<br /><em>{{ $hero['title_em'] }}</em>@endif</h1>
      @if (filled($hero['description'] ?? null))<p class="hero-desc">{{ $hero['description'] }}</p>@endif
      @if (filled($hero['button_label'] ?? null))
        <div class="hero-buttons">
          <a href="{{ url($hero['button_url'] ?? '#tentang') }}" class="btn-hero">{{ $hero['button_label'] }}</a>
        </div>
      @endif
    </div>
  </section>

  <!-- TENTANG SINGKAT -->
  <section class="collections" id="tentang">
    <div class="about-brief-inner">
      <div class="about-brief-text reveal-left">
        <p class="about-brief-eyebrow">{{ $about['eyebrow'] ?? '' }}</p>
        <h2>{{ $about['title'] ?? '' }}@if (filled($about['title_em'] ?? null))<br /><em>{{ $about['title_em'] }}</em>@endif</h2>
        <p class="about-brief-desc">{{ $about['text'] ?? '' }}</p>
        <div class="about-brief-stats">
          @foreach ($about['stats'] ?? [] as $stat)
            <div class="about-stat reveal delay-{{ min($loop->iteration, 4) }}">
              <span class="about-stat-num" data-target="{{ (int) $stat['number'] }}" data-suffix="{{ $stat['suffix'] ?? '' }}">{{ number_format((int) $stat['number'], 0, ',', '.') }}{{ $stat['suffix'] ?? '' }}</span>
              <span class="about-stat-label">{{ $stat['label'] ?? '' }}</span>
            </div>
          @endforeach
        </div>
        @if (filled($about['button_label'] ?? null))
          <a href="{{ url($about['button_url'] ?? '/tentang.html') }}" class="about-brief-cta reveal delay-2">{{ $about['button_label'] }}</a>
        @endif
      </div>

      <div class="about-brief-cards reveal-right">
        @foreach ($about['values'] ?? [] as $val)
          <div class="about-val-card glow-card reveal delay-{{ min($loop->iteration, 4) }}">
            <div class="glow-border"></div>
            @if (filled($val['icon'] ?? null))
              <div class="about-val-icon">
                <img src="{{ media_url($val['icon']) }}" alt="{{ $val['title'] ?? '' }}" />
              </div>
            @endif
            <h4>{{ $val['title'] ?? '' }}</h4>
            <div class="val-divider"></div>
            <p>{{ $val['text'] ?? '' }}</p>
          </div>
        @endforeach
      </div>
    </div>
  </section>

  <!-- MARQUEE LOGO KLIEN -->
  @if ($clientRows)
    <section class="marquee-section">
      <p class="marquee-label">{{ $h['clients']['label'] ?? '' }}</p>
      @foreach ($clientRows as $row)
        <div class="marquee-wrap">
          <div class="marquee-track {{ $loop->first ? 'marquee-left' : 'marquee-right' }}">
            {{-- daftar diulang dua kali agar animasi berputar mulus --}}
            @foreach ([false, true] as $dup)
              @foreach ($row as $client)
                <div class="marquee-item" @if ($dup) aria-hidden="true" @endif><img src="{{ media_url($client->logo) }}" alt="{{ $dup ? '' : $client->name }}" /></div>
              @endforeach
            @endforeach
          </div>
        </div>
      @endforeach
    </section>
  @endif

  <!-- LAYANAN -->
  <section class="services-showcase" id="layanan-home">
    <div class="services-showcase-header reveal">
      <p class="about-brief-eyebrow">{{ $svc['eyebrow'] ?? '' }}</p>
      <h2>{{ $svc['title'] ?? '' }}@if (filled($svc['title_em'] ?? null))<br /><em>{{ $svc['title_em'] }}</em>@endif</h2>
    </div>

    @if ($svcCards)
      <div class="services-bento">
        @php $main = $svcCards[0]; @endphp
        <div class="svc-card svc-main reveal-left">
          <div class="svc-bg" style="background-image: url('{{ media_url($main['image'] ?? null) }}')"></div>
          <div class="svc-overlay"></div>
          <div class="svc-content">
            <h3>{{ $main['title'] ?? '' }}</h3>
            <p>{{ $main['text'] ?? '' }}</p>
            @if (filled($main['url'] ?? null))
              <a href="{{ url($main['url']) }}" class="svc-link">{{ $main['link_label'] ?? 'Pelajari Layanan →' }}</a>
            @endif
          </div>
        </div>

        @if ($svcRight)
          <div class="svc-right-grid">
            @foreach ($svcRight as $card)
              <div class="svc-card svc-small {{ $loop->last && count($svcRight) % 2 ? 'svc-wide' : '' }} reveal delay-{{ min($loop->iteration, 4) }}">
                <div class="svc-bg" style="background-image: url('{{ media_url($card['image'] ?? null) }}'); background-size: cover; background-position: center;"></div>
                <div class="svc-overlay svc-overlay-dark"></div>
                <div class="svc-content">
                  <h3>{{ $card['title'] ?? '' }}</h3>
                  <p>{{ $card['text'] ?? '' }}</p>
                  @if (filled($card['url'] ?? null))
                    <a href="{{ url($card['url']) }}" class="svc-link">{{ $card['link_label'] ?? 'Pelajari Layanan →' }}</a>
                  @endif
                </div>
              </div>
            @endforeach
          </div>
        @endif
      </div>
    @endif

    @if (filled($svc['button_label'] ?? null))
      <div class="services-cta reveal">
        <a href="{{ url($svc['button_url'] ?? '/layanan/sertifikasi-organisasi/index.html') }}" class="btn-outline">{{ $svc['button_label'] }}</a>
      </div>
    @endif
  </section>

  <!-- PRODUK -->
  @if ($products->isNotEmpty())
    <section class="products-showcase" id="produk-home">
      <div class="products-showcase-header reveal">
        <p class="prod-eyebrow">{{ $prod['eyebrow'] ?? '' }}</p>
        <h2>{{ $prod['title'] ?? '' }}@if (filled($prod['title_em'] ?? null))<br /><em>{{ $prod['title_em'] }}</em>@endif</h2>
        <p class="prod-subtitle">{{ $prod['subtitle'] ?? '' }}</p>
      </div>

      <div class="products-cards-row">
        @foreach ($products as $product)
          <div class="prod-card reveal delay-{{ min($loop->iteration, 4) }}" id="prodCard{{ $loop->iteration }}">
            <div class="prod-card-inner">
              <div class="prod-visual">
                <div class="prod-mockup-screen">
                  <img src="{{ media_url($product->image) ?? $fallbackImg }}" alt="{{ $product->name }}" />
                  <div class="prod-screen-overlay"></div>
                  <div class="prod-screen-ui">
                    <div class="prod-ui-dot active"></div>
                    <div class="prod-ui-dot"></div>
                    <div class="prod-ui-dot"></div>
                  </div>
                </div>
              </div>
              <div class="prod-info">
                <h3>{{ $product->name }}</h3>
                <p class="prod-desc">{{ $product->description }}</p>
                <a href="{{ url('kontak.html') }}" class="prod-cta-btn">{{ $product->button_label ?: 'Konsultasikan '.$product->name }}</a>
              </div>
            </div>
          </div>
        @endforeach
      </div>
    </section>
  @endif

  <!-- BIDANG PELATIHAN -->
  <section class="bp-section" id="bidang-pelatihan">
    <div class="bp-inner">
      <div class="bp-header reveal">
        <p class="bp-eyebrow">{{ $bp['eyebrow'] ?? '' }}</p>
        <h2>{{ $bp['title'] ?? '' }}@if (filled($bp['title_em'] ?? null))<br /><em>{{ $bp['title_em'] }}</em>@endif</h2>
      </div>
      <div class="bp-grid">
        @foreach ($bp['cards'] ?? [] as $card)
          <div class="bp-card reveal delay-{{ $loop->index % 3 + 1 }}">
            <div class="bp-icon">@include('home.icon', ['name' => $card['icon'] ?? null, 'size' => 28, 'stroke' => 1.8])</div>
            <h3>{{ $card['title'] ?? '' }}</h3>
            <p>{{ $card['text'] ?? '' }}</p>
          </div>
        @endforeach
      </div>
      @if (filled($bp['button_label'] ?? null))
        <div class="bp-cta reveal">
          <a href="{{ url($bp['button_url'] ?? '/layanan/pelatihan-sertifikasi/index.html') }}" class="btn-outline">{{ $bp['button_label'] }}</a>
        </div>
      @endif
    </div>
  </section>

  <!-- MENGAPA MEMILIH INOVASS -->
  @if ($upcomingSchedules->isNotEmpty())
    <section class="pl-home" id="jadwal-pelatihan">
      <div class="pl-container">
        <div class="pl-home-head">
          <div>
            <p class="pl-eyebrow">Jadwal Pelatihan</p>
            <h2 class="pl-heading">Jadwal Pelatihan <em>Terdekat</em></h2>
          </div>
          <a class="pl-btn ghost" href="{{ route('pelatihan.jadwal') }}">Lihat semua jadwal</a>
        </div>
        <div class="pl-list">
          @foreach ($upcomingSchedules as $schedule)
            @include('pelatihan._schedule', ['schedule' => $schedule])
          @endforeach
        </div>
      </div>
    </section>
  @endif

  <section class="wi-section" id="mengapa-inovass">
    <div class="wi-glow"></div>
    <div class="wi-inner">
      <div class="wi-left reveal-left">
        <p class="wi-eyebrow">{{ $wi['eyebrow'] ?? '' }}</p>
        <h2>{{ $wi['title'] ?? '' }}@if (filled($wi['title_em'] ?? null))<br /><em>{{ $wi['title_em'] }}</em>@endif</h2>
        <p class="wi-desc">{{ $wi['description'] ?? '' }}</p>
      </div>
      <div class="wi-right reveal-right">
        @foreach ($wi['cards'] ?? [] as $card)
          <div class="wi-card reveal delay-{{ min($loop->iteration, 4) }}">
            <div class="wi-card-icon">@include('home.icon', ['name' => $card['icon'] ?? null, 'size' => 22, 'stroke' => 1.7])</div>
            <h4>{{ $card['title'] ?? '' }}</h4>
            <p>{{ $card['text'] ?? '' }}</p>
          </div>
        @endforeach
      </div>
    </div>
  </section>

  <!-- PROSES KERJA -->
  <section class="pw-section" id="proses-kerja">
    <div class="pw-inner">
      <div class="pw-header reveal">
        <p class="pw-eyebrow">{{ $pw['eyebrow'] ?? '' }}</p>
        <h2>{{ $pw['title'] ?? '' }}</h2>
      </div>
      <div class="pw-steps">
        @foreach ($pw['steps'] ?? [] as $step)
          <div class="pw-step reveal delay-{{ min($loop->iteration, 4) }}">
            <div class="pw-step-num">{{ $loop->iteration }}</div>
            @unless ($loop->last)<div class="pw-connector" aria-hidden="true"></div>@endunless
            <div class="pw-step-body">
              <h3>{{ $step['title'] ?? '' }}</h3>
              <p>{{ $step['text'] ?? '' }}</p>
            </div>
          </div>
        @endforeach
      </div>
    </div>
  </section>

  <!-- BERITA & INSIGHT -->
  @if ($articles->isNotEmpty())
    <section class="bi-section" id="berita-insight">
      <div class="bi-inner">
        <div class="bi-header reveal">
          <p class="bi-eyebrow">{{ $bi['eyebrow'] ?? '' }}</p>
          <h2>{{ $bi['title'] ?? '' }}</h2>
        </div>
        <div class="bi-bento">
          @foreach ($articles as $article)
            <article class="bi-bento-card {{ $loop->first ? 'bi-bento-large' : '' }} reveal delay-{{ $loop->iteration }}">
              <img src="{{ media_url($article->cover) ?? $fallbackImg }}" alt="{{ $article->title }}" loading="lazy" />
              <div class="bi-bento-overlay"></div>
              <div class="bi-bento-content">
                <div class="bi-bento-meta">
                  @if ($article->published_at)<span class="bi-date">{{ $article->published_at->locale('id')->translatedFormat('j M Y') }}</span>@endif
                </div>
                <h3>{{ $article->title }}</h3>
                <p class="bi-bento-desc">{{ $article->excerpt }}</p>
                <a href="{{ $article->url() }}" class="bi-bento-link">Baca Selengkapnya →</a>
              </div>
            </article>
          @endforeach
        </div>
      </div>
    </section>
  @endif

  <!-- TESTIMONI -->
  @if ($testimonials->isNotEmpty())
    <section class="tm-section" id="testimoni">
      <div class="tm-header reveal">
        <p class="tm-eyebrow">{{ $tm['eyebrow'] ?? '' }}</p>
        <h2>{{ $tm['title'] ?? '' }}</h2>
      </div>
      <div class="tm-track-wrap">
        <div class="tm-track" id="tmTrack">
          {{-- dua kartu pertama diulang di akhir agar auto-scroll berputar mulus --}}
          @foreach ($testimonials->concat($testimonials->take(2)) as $t)
            @php $initial = collect(explode(' ', $t->name))->first(fn ($w) => ! str_ends_with($w, '.')) ?? $t->name; @endphp
            <div class="tm-card" @if ($loop->index >= $testimonials->count()) aria-hidden="true" @endif>
              <div class="tm-stars">{{ str_repeat('★', max(1, min(5, (int) $t->rating))) }}</div>
              <p>"{{ trim($t->quote, "\"“” \n") }}"</p>
              <div class="tm-author">
                <div class="tm-avatar">{{ mb_strtoupper(mb_substr($initial, 0, 1)) }}</div>
                <div>
                  <strong>{{ $t->name }}</strong>
                  <span>{{ trim($t->position.' '.$t->organization) }}</span>
                </div>
              </div>
            </div>
          @endforeach
        </div>
      </div>
    </section>
  @endif

  <!-- FAQ -->
  @if ($faqs->isNotEmpty())
    <section class="faq-section" id="faq">
      <div class="faq-inner">
        <div class="faq-header reveal">
          <p class="faq-eyebrow">{{ $fq['eyebrow'] ?? '' }}</p>
          <h2>{{ $fq['title'] ?? '' }}</h2>
        </div>
        <div class="faq-list">
          @foreach ($faqs as $faq)
            <div class="faq-item reveal delay-{{ $loop->index % 3 + 1 }}">
              <button class="faq-q" aria-expanded="false">
                <span>{{ $faq->question }}</span>
                <span class="faq-icon" aria-hidden="true">+</span>
              </button>
              <div class="faq-a">{!! $faq->answer !!}</div>
            </div>
          @endforeach
        </div>
      </div>
    </section>
  @endif

  <!-- CTA KONSULTASI -->
  <section class="cta-section" id="cta-konsultasi" style="padding: 6rem 5rem;">
    <div class="cta-glow" aria-hidden="true"></div>
    <div class="cta-inner reveal" style="max-width: 700px; margin: 0 auto;">
      <h2 style="font-family: var(--font-serif); font-size: clamp(1.5rem, 2.5vw, 2.2rem); font-weight: 700; color: #ffffff; line-height: 1.3; margin-bottom: 1.2rem; text-align: center;">{{ $cta['title'] ?? '' }}@if (filled($cta['title_em'] ?? null))<br /><em style="font-style: normal; color: #00e0a0;">{{ $cta['title_em'] }}</em>@endif</h2>
      <p style="font-size: 0.88rem; color: rgba(255, 255, 255, 0.7); line-height: 1.7; max-width: 560px; margin: 0 auto; text-align: center; margin-bottom: 32px;">{{ $cta['text'] ?? '' }}</p>
      <div class="cta-buttons" style="display: flex; align-items: center; justify-content: center; gap: 1.2rem; flex-wrap: wrap;">
        @if (filled($cta['primary_label'] ?? null))
          <a href="{{ url($cta['primary_url'] ?? '/kontak.html') }}" class="cta-btn-primary" style="font-family: var(--font-sans); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 0.95rem 2rem; background: #00e0a0; color: #1e3a8a; border: 2px solid #00e0a0; border-radius: 50px; text-decoration: none; transition: all 0.25s;">{{ $cta['primary_label'] }}</a>
        @endif
        @if (filled($cta['secondary_label'] ?? null))
          <a href="{{ url($cta['secondary_url'] ?? '/layanan/sertifikasi-organisasi/index.html') }}" class="cta-btn-secondary" style="font-family: var(--font-sans); font-size: 0.75rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; padding: 0.95rem 2rem; background: transparent; color: #ffffff; border: 2px solid rgba(255, 255, 255, 0.4); border-radius: 50px; text-decoration: none; transition: all 0.25s;">{{ $cta['secondary_label'] }}</a>
        @endif
      </div>
    </div>
  </section>

@endsection

@push('styles')
  <link rel="stylesheet" href="{{ asset('assets/css/pelatihan.css') }}" />
@endpush

@push('scripts')
  <script>
    // ── FAQ Accordion ──
    document.querySelectorAll('.faq-q').forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.faq-item');
        const answer = item.querySelector('.faq-a');
        const icon = btn.querySelector('.faq-icon');
        const isOpen = btn.getAttribute('aria-expanded') === 'true';

        document.querySelectorAll('.faq-item').forEach(other => {
          if (other !== item) {
            other.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
            other.querySelector('.faq-a').style.maxHeight = null;
            other.querySelector('.faq-icon').textContent = '+';
            other.classList.remove('faq-open');
          }
        });

        btn.setAttribute('aria-expanded', String(!isOpen));
        answer.style.maxHeight = isOpen ? null : answer.scrollHeight + 'px';
        icon.textContent = isOpen ? '+' : '×';
        item.classList.toggle('faq-open', !isOpen);
      });
    });

    // ── Testimoni Auto-scroll ──
    (function() {
      const tmTrack = document.getElementById('tmTrack');
      if (!tmTrack) return;
      let tmSpeed = 0.9, tmPaused = false, tmDragging = false, tmStartX = 0, tmStartScroll = 0;

      function tmScroll() {
        if (!tmPaused && !tmDragging) {
          tmTrack.scrollLeft += tmSpeed;
          if (tmTrack.scrollLeft >= tmTrack.scrollWidth - tmTrack.clientWidth - 2) tmTrack.scrollLeft = 0;
        }
        requestAnimationFrame(tmScroll);
      }
      requestAnimationFrame(tmScroll);

      tmTrack.addEventListener('mouseenter', () => { tmPaused = true; });
      tmTrack.addEventListener('mouseleave', () => { tmPaused = false; });
      tmTrack.addEventListener('mousedown', e => {
        tmDragging = true;
        tmStartX = e.pageX - tmTrack.offsetLeft;
        tmStartScroll = tmTrack.scrollLeft;
        tmTrack.style.cursor = 'grabbing';
      });
      window.addEventListener('mousemove', e => {
        if (!tmDragging) return;
        tmTrack.scrollLeft = tmStartScroll - (e.pageX - tmTrack.offsetLeft - tmStartX);
      });
      window.addEventListener('mouseup', () => { tmDragging = false; tmTrack.style.cursor = 'grab'; });
      tmTrack.addEventListener('touchstart', e => {
        tmStartX = e.touches[0].pageX;
        tmStartScroll = tmTrack.scrollLeft;
        tmPaused = true;
      }, { passive: true });
      tmTrack.addEventListener('touchmove', e => {
        tmTrack.scrollLeft = tmStartScroll - (e.touches[0].pageX - tmStartX);
      }, { passive: true });
      tmTrack.addEventListener('touchend', () => { setTimeout(() => { tmPaused = false; }, 1200); });
    })();

    // ── Counter statistik saat masuk viewport ──
    function animateCounter(el, target, suffix, duration = 1800) {
      const startTime = performance.now();
      function update(now) {
        const progress = Math.min((now - startTime) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = (progress < 1 ? Math.floor(eased * target) : target).toLocaleString('id-ID') + suffix;
        if (progress < 1) requestAnimationFrame(update);
      }
      requestAnimationFrame(update);
    }
    const counterObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        animateCounter(entry.target, parseInt(entry.target.dataset.target), entry.target.dataset.suffix || '');
        counterObserver.unobserve(entry.target);
      });
    }, { threshold: 0.5 });
    document.querySelectorAll('.about-stat-num[data-target]').forEach(el => counterObserver.observe(el));

    // ── Glow cards mengikuti pointer ──
    (function() {
      const cards = document.querySelectorAll('.glow-card');
      document.addEventListener('pointermove', e => {
        cards.forEach(card => {
          const r = card.getBoundingClientRect();
          const inArea = e.clientX > r.left - 64 && e.clientX < r.right + 64 && e.clientY > r.top - 64 && e.clientY < r.bottom + 64;
          if (!inArea) { card.style.setProperty('--active', '0'); return; }
          const angle = Math.atan2(e.clientY - (r.top + r.height / 2), e.clientX - (r.left + r.width / 2)) * (180 / Math.PI) + 90;
          card.style.setProperty('--active', '1');
          card.style.setProperty('--start', String(angle));
          card.style.setProperty('--spread', '40');
          card.style.setProperty('--mx', ((e.clientX - r.left) / r.width) * 100 + '%');
          card.style.setProperty('--my', ((e.clientY - r.top) / r.height) * 100 + '%');
        });
      }, { passive: true });
      document.addEventListener('scroll', () => cards.forEach(card => card.style.setProperty('--active', '0')), { passive: true });
    })();
  </script>
@endpush
