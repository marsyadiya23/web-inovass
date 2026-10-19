{{-- Hero halaman dalam. Props: $heroTitle, $heroEm (opsional, baris miring), $heroDesc, $heroImage, $crumbs = [[label, url|null], ...] --}}
<section class="page-hero page-hero-img">
  <img src="{{ media_url($heroImage ?? null) ?? asset('assets/img/layanan%20kami.jpeg') }}" alt="{{ $heroTitle }}" class="page-hero-bg" />
  <div class="page-hero-overlay"></div>
  <div class="page-hero-content">
    <nav class="page-breadcrumb" aria-label="Breadcrumb">
      <a href="{{ url('/') }}">Beranda</a>
      @foreach ($crumbs ?? [] as [$label, $href])
        <span>›</span>
        @if ($href)<a href="{{ $href }}">{{ $label }}</a>@else<span>{{ $label }}</span>@endif
      @endforeach
    </nav>
    <h1>{{ $heroTitle }}@if (filled($heroEm ?? null))<br /><em>{{ $heroEm }}</em>@endif</h1>
    @if (filled($heroDesc ?? null))<p class="page-desc">{{ $heroDesc }}</p>@endif
  </div>
</section>
