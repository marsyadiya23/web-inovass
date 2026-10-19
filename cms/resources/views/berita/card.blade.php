{{-- Kartu berita (kelas bi-bento-* dari section Berita & Insight beranda). Props: $article --}}
@php $badge = ['Insight' => 'bi-badge-blue', 'Pengumuman' => 'bi-badge-yellow'][$article->category] ?? 'bi-badge-green'; @endphp
<a href="{{ $article->url() }}" class="bi-bento-card reveal">
  <img src="{{ media_url($article->cover) ?? media_url('legacy/wallpaper 3.png') }}" alt="{{ $article->title }}" loading="lazy" />
  <div class="bi-bento-overlay"></div>
  <div class="bi-bento-content">
    <div class="bi-bento-meta">
      @if ($article->category)<span class="bi-badge {{ $badge }}">{{ $article->category }}</span>@endif
      <span class="bi-date">{{ $article->published_at?->locale('id')->translatedFormat('j M Y') }}</span>
    </div>
    <h3>{{ $article->title }}</h3>
    @if ($article->excerpt)<p class="bi-bento-desc">{{ $article->excerpt }}</p>@endif
    <span class="bi-bento-link">Baca Selengkapnya →</span>
  </div>
</a>
