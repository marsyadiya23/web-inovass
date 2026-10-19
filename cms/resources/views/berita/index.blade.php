@extends('layouts.site', [
    'title' => 'Berita & Insight',
    'metaDescription' => 'Kabar terbaru, insight, dan pengumuman seputar standar ISO, akreditasi, dan pelatihan dari INOVASS.',
])

@push('styles')
<style>
  .berita-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; }
  .berita-grid .bi-bento-card { display: block; height: 360px; text-decoration: none; }
  .berita-grid .bi-bento-card h3 { font-size: 1.05rem; }
  .berita-empty { color: #64748b; font-size: 0.95rem; }
  .berita-pager { display: flex; justify-content: center; flex-wrap: wrap; gap: 0.5rem; margin-top: 3rem; }
  .berita-pager a, .berita-pager span { min-width: 42px; padding: 0.6rem 0.9rem; border-radius: 999px; border: 1px solid #e2e8f0; color: #1e3a8a; font-size: 0.85rem; font-weight: 600; text-align: center; text-decoration: none; }
  .berita-pager a:hover { border-color: #00c278; color: #00c278; }
  .berita-pager .is-active { background: #00c278; border-color: #00c278; color: #fff; }
  .berita-pager .is-disabled { opacity: 0.4; }
  @media (max-width: 900px) { .berita-grid { grid-template-columns: 1fr 1fr; } }
  @media (max-width: 580px) { .berita-grid { grid-template-columns: 1fr; } .berita-grid .bi-bento-card { height: 280px; } }
</style>
@endpush

@section('content')
  @include('partials.page-hero', [
      'heroTitle' => 'Berita &',
      'heroEm' => 'Insight',
      'heroDesc' => 'Kabar terbaru, insight, dan pengumuman seputar standar ISO, akreditasi, dan pelatihan dari INOVASS.',
      'crumbs' => [['Berita', null]],
  ])

  <section class="bi-section" style="padding-top: 0;">
    <div class="bi-inner">
      <div class="bi-header reveal">
        <p class="bi-eyebrow">BERITA &amp; INSIGHT</p>
        <h2>Update Terbaru dari INOVASS</h2>
      </div>

      @if ($articles->isEmpty())
        <p class="berita-empty">Belum ada berita yang diterbitkan.</p>
      @else
        <div class="berita-grid">
          @foreach ($articles as $article)
            @include('berita.card')
          @endforeach
        </div>

        @if ($articles->hasPages())
          <nav class="berita-pager" aria-label="Halaman berita">
            @if ($articles->onFirstPage())<span class="is-disabled">‹</span>@else<a href="{{ $articles->previousPageUrl() }}" rel="prev">‹</a>@endif
            @foreach ($articles->getUrlRange(1, $articles->lastPage()) as $page => $pageUrl)
              @if ($page === $articles->currentPage())<span class="is-active">{{ $page }}</span>@else<a href="{{ $pageUrl }}">{{ $page }}</a>@endif
            @endforeach
            @if ($articles->hasMorePages())<a href="{{ $articles->nextPageUrl() }}" rel="next">›</a>@else<span class="is-disabled">›</span>@endif
          </nav>
        @endif
      @endif
    </div>
  </section>

  @include('partials.cta')
@endsection
