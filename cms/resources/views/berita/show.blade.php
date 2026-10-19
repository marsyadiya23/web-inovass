@extends('layouts.site', [
    'title' => $article->title,
    'metaDescription' => $article->excerpt,
])

@push('styles')
<style>
  .page-hero-content h1 { font-size: clamp(2rem, 3.6vw, 3.4rem); max-width: 920px; }
  .berita-article { max-width: 820px; margin: 0 auto; padding: 0 1.5rem 5rem; }
  .berita-article .bi-bento-meta { margin-bottom: 1.5rem; }
  .berita-article .bi-date { color: #64748b; font-size: 0.8rem; }
  .berita-cover { width: 100%; border-radius: 20px; margin-bottom: 2.5rem; aspect-ratio: 16 / 9; object-fit: cover; }
  .berita-lead { font-size: 1.05rem; color: #1e3a8a; line-height: 1.8; font-weight: 500; margin-bottom: 2rem; }
  .berita-body { font-family: var(--font-sans); color: #475569; font-size: 0.98rem; line-height: 1.9; }
  .berita-body p { margin-bottom: 1.3rem; }
  .berita-body h2, .berita-body h3 { font-family: var(--font-serif); color: #1e3a8a; line-height: 1.3; margin: 2.2rem 0 1rem; }
  .berita-body h2 { font-size: 1.6rem; }
  .berita-body h3 { font-size: 1.25rem; }
  .berita-body ul, .berita-body ol { margin: 0 0 1.3rem 1.4rem; }
  .berita-body li { margin-bottom: 0.5rem; }
  .berita-body a { color: #00c278; }
  .berita-body img { max-width: 100%; height: auto; border-radius: 12px; }
  .berita-body blockquote { border-left: 3px solid #00c278; padding-left: 1.2rem; color: #1e3a8a; font-style: italic; }
  .berita-back { display: inline-block; margin-top: 2rem; color: #00c278; font-weight: 600; font-size: 0.85rem; text-decoration: none; }
  .berita-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
  .berita-grid .bi-bento-card { display: block; height: 320px; text-decoration: none; }
  @media (max-width: 900px) { .berita-grid { grid-template-columns: 1fr; } .berita-grid .bi-bento-card { height: 260px; } }
</style>
@endpush

@section('content')
  @php $badge = ['Insight' => 'bi-badge-blue', 'Pengumuman' => 'bi-badge-yellow'][$article->category] ?? 'bi-badge-green'; @endphp

  @include('partials.page-hero', [
      'heroTitle' => $article->title,
      'heroDesc' => null,
      'heroImage' => $article->cover,
      'crumbs' => [['Berita', url('berita')], [\Illuminate\Support\Str::limit($article->title, 40), null]],
  ])

  <article class="berita-article">
    <div class="bi-bento-meta">
      @if ($article->category)<span class="bi-badge {{ $badge }}">{{ $article->category }}</span>@endif
      <span class="bi-date">{{ $article->published_at?->locale('id')->translatedFormat('l, j F Y') }}</span>
    </div>

    @if ($article->cover)
      <img src="{{ media_url($article->cover) }}" alt="{{ $article->title }}" class="berita-cover" />
    @endif

    @if ($article->excerpt)<p class="berita-lead">{{ $article->excerpt }}</p>@endif

    <div class="berita-body">{!! $article->body !!}</div>

    <a href="{{ url('berita') }}" class="berita-back">← Kembali ke semua berita</a>
  </article>

  @if ($others->isNotEmpty())
    <section class="bi-section" style="background: #f7f9f8;">
      <div class="bi-inner">
        <div class="bi-header reveal">
          <p class="bi-eyebrow">BACA JUGA</p>
          <h2>Berita lainnya</h2>
        </div>
        <div class="berita-grid">
          @foreach ($others as $article)
            @include('berita.card')
          @endforeach
        </div>
      </div>
    </section>
  @endif

  @include('partials.cta')
@endsection
