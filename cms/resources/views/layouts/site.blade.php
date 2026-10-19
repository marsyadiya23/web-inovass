@php
    $s = \App\Models\PageContent::get('settings');
    $nav = [
        ['label' => 'Beranda', 'url' => url('/'), 'active' => request()->is('/', 'index.html')],
        ['label' => 'Layanan', 'url' => url('layanan/sertifikasi-organisasi/index.html'), 'active' => request()->is('layanan/*')],
        ['label' => 'Jadwal Pelatihan', 'url' => route('pelatihan.jadwal'), 'active' => request()->is('jadwal-pelatihan', 'pelatihan*')],
        ['label' => 'Produk', 'url' => url('produk.html'), 'active' => request()->is('produk.html')],
        ['label' => 'Tentang Kami', 'url' => url('tentang.html'), 'active' => request()->is('tentang.html')],
    ];
    $wa = preg_replace('/\D/', '', $s['whatsapp'] ?? '');
@endphp
<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{ isset($title) ? $title.' — ' : '' }}{{ $s['site_name'] ?? 'INOVASS' }}</title>
  <meta name="description" content="{{ $metaDescription ?? ($s['description'] ?? '') }}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{{ asset('assets/css/style.css') }}" />
  @unless($homepage ?? false)
    <link rel="stylesheet" href="{{ asset('assets/css/pages.css') }}" />
  @endunless
  @stack('styles')
</head>
<body>

  <nav class="navbar">
    <a href="{{ url('/') }}" class="nav-logo">
      <img src="{{ media_url($s['logo'] ?? null) ?? asset('assets/img/logo.png') }}" alt="{{ $s['site_name'] ?? 'INOVASS' }} Logo" class="nav-logo-img" />
    </a>
    <div class="nav-menu">
      @foreach ($nav as $item)
        <a href="{{ $item['url'] }}" class="nav-link {{ $item['active'] ? 'active' : '' }}">{{ $item['label'] }}</a>
      @endforeach
    </div>
    <div class="nav-right">
      <a href="{{ url('kontak.html') }}" class="nav-cta">Hubungi Kami</a>
      <button class="nav-hamburger" aria-label="Menu" id="hamburgerBtn">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
  <div class="mobile-menu" id="mobileMenu">
    @foreach ($nav as $item)
      <a href="{{ $item['url'] }}" class="mobile-link {{ $item['active'] ? 'active' : '' }}">{{ $item['label'] }}</a>
    @endforeach
    <a href="{{ url('kontak.html') }}" class="mobile-cta">Hubungi Kami</a>
  </div>

  @yield('content')

  <footer class="footer" style="background: #0a1628 !important;">
    <div class="footer-top">
      <div class="footer-brand reveal-left">
        <a href="{{ url('/') }}" class="footer-logo-link">
          <img src="{{ media_url($s['logo'] ?? null) ?? asset('assets/img/logo.png') }}" alt="{{ $s['site_name'] ?? 'INOVASS' }} Logo" class="nav-logo-img" />
        </a>
        <p class="footer-tagline">{{ $s['tagline'] ?? '' }}</p>
        <p class="footer-desc">{{ $s['description'] ?? '' }}</p>
        @php $socials = collect($s['socials'] ?? [])->filter(fn ($x) => filled($x['url'] ?? null)); @endphp
        @if ($socials->isNotEmpty())
          <div class="footer-socials" style="margin-top:1.5rem;">
            @foreach ($socials as $soc)
              <a href="{{ $soc['url'] }}" target="_blank" rel="noopener">{{ strtoupper($soc['platform']) }}</a>
            @endforeach
          </div>
        @endif
      </div>
      <div class="footer-links reveal-right">
        <div class="footer-col">
          <h4>Kantor</h4>
          <ul>
            @foreach (preg_split('/\r?\n/', $s['address'] ?? '') as $line)
              @if (filled($line))<li>{{ $line }}</li>@endif
            @endforeach
          </ul>
        </div>
        <div class="footer-col">
          <h4>Hubungi Kami</h4>
          <ul>
            @if ($wa)<li><a href="https://wa.me/{{ $wa }}">{{ $s['phone'] ?? $wa }}</a></li>@endif
            @if (filled($s['email'] ?? null))<li><a href="mailto:{{ $s['email'] }}">{{ $s['email'] }}</a></li>@endif
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <p>{{ str_replace('{tahun}', date('Y'), $s['copyright'] ?? '© {tahun} INOVASS. Hak cipta dilindungi undang-undang.') }}</p>
    </div>
  </footer>

  <script src="{{ asset('assets/js/script.js') }}"></script>
  @stack('scripts')
</body>
</html>
