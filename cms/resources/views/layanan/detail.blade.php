@extends('layouts.site')

@push('styles')
  <link rel="stylesheet" href="{{ asset('assets/css/detail.css') }}" />
@endpush

@php
    $category = $service->category;
    $body = (string) $service->body;
    $highlightTitle = null;
    // Situs lama: judul kartu highlight = <h2> pertama di body. Ambil keluar agar tampil di atas kartu.
    if ($service->highlights && preg_match('#^\s*<h2>(.*?)</h2>#s', $body, $m)) {
        $highlightTitle = strip_tags($m[1]);
        $body = substr($body, strlen($m[0]));
    }
    $sep = 'style="color: rgba(255, 255, 255, 0.5) !important;"';
    $accents = ['accent-navy', 'accent-green', 'accent-yellow'];
@endphp

@section('content')
  <section class="detail-header-section">
    <div class="detail-header-container">
      <nav class="detail-breadcrumb-nav" style="font-size: 0.82rem !important;">
        <a href="{{ url('/') }}" class="breadcrumb-link" {!! $sep !!}>Beranda</a>
        <span class="breadcrumb-sep" {!! $sep !!}>›</span>
        <a href="{{ $category->url() }}" class="breadcrumb-link" {!! $sep !!}>{{ $category->name }}</a>
        @if ($service->parent)
          <span class="breadcrumb-sep" {!! $sep !!}>›</span>
          <a href="{{ url("layanan/{$category->slug}/{$service->parent->slug}.html") }}" class="breadcrumb-link" {!! $sep !!}>{{ $service->parent->title }}</a>
        @endif
        <span class="breadcrumb-sep" {!! $sep !!}>›</span>
        <span class="breadcrumb-current" style="color: #00e0a0 !important;">{{ \Illuminate\Support\Str::limit($service->title, 60) }}</span>
      </nav>
      <h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{{ $service->title }}</h1>
    </div>
  </section>

  <section class="iso-content-section">
    <div class="iso-content-container">
      @if ($service->highlights)
        <div class="iso-benefit-highlight">
          @if ($highlightTitle)<h2 class="benefit-highlight-title">{{ $highlightTitle }}</h2>@endif
          <div class="benefit-highlight-grid">
            @foreach ($service->highlights as $h)
              <div class="benefit-highlight-card"><p>{{ $h }}</p></div>
            @endforeach
          </div>
        </div>
      @endif

      @if (filled(trim(strip_tags($body))))
        <article class="cms-body">{!! $body !!}</article>
      @elseif ($children->isEmpty())
        <article class="cms-body"><h2>Konten Segera Hadir</h2><p>Informasi lengkap layanan ini sedang kami siapkan. Hubungi kami untuk konsultasi.</p></article>
      @endif

      @if ($children->isNotEmpty())
        <div class="cms-children product-details-grid">
          @foreach ($children as $i => $child)
            <a href="{{ url("layanan/{$category->slug}/{$child->slug}.html") }}" class="product-detail-item {{ $accents[$i % 3] }}" style="text-decoration: none; cursor: pointer;">
              <p>{{ $child->title }}</p>
            </a>
          @endforeach
        </div>
      @endif
    </div>
  </section>

  @include('partials.cta', ['ctaTitle' => 'Siap memulai', 'ctaEm' => 'proyek Anda?', 'ctaText' => 'Hubungi kami untuk konsultasi gratis dan penawaran terbaik untuk organisasi Anda.'])
@endsection
