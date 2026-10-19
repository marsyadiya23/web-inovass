@extends('layouts.site', ['title' => 'Produk', 'metaDescription' => $c['hero_desc'] ?? null])

@push('styles')
  <style>
    /* Product List Section */
    .product-list-section {
      background: #ffffff;
      padding: 5rem 5rem;
    }

    .section-title {
      text-align: center;
      font-family: var(--font-serif);
      font-size: clamp(2rem, 3.5vw, 3.2rem);
      font-weight: 700;
      color: #00c278;
      margin-bottom: 3rem;
      line-height: 1.3;
    }

    .product-item {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 5rem;
      max-width: 1200px;
      margin: 0 auto 5rem;
      align-items: center;
      min-height: 500px;
    }

    .product-item:last-child {
      margin-bottom: 0;
    }

    .product-item.reverse {
      direction: rtl;
    }

    .product-item.reverse > * {
      direction: ltr;
    }

    .product-item-image {
      width: 100%;
      height: 400px;
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }

    .product-item-image img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }

    .product-item:hover .product-item-image img {
      transform: scale(1.05);
    }

    .product-item-content h2 {
      font-family: var(--font-serif);
      font-size: clamp(1.8rem, 2.5vw, 2.2rem);
      font-weight: 700;
      color: #1e3a8a;
      margin-bottom: 1.2rem;
    }

    .product-item-content p {
      font-size: 1rem;
      color: #4a5568;
      line-height: 1.8;
      margin-bottom: 2rem;
    }

    .product-item-link {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      font-weight: 600;
      color: #00c278;
      background: transparent;
      text-decoration: none;
      padding: 0.9rem 2rem;
      border: 2px solid #00c278;
      border-radius: 50px;
      transition: all 0.3s ease;
    }

    .product-item-link:hover {
      background: #00c278;
      color: #ffffff;
      transform: translateY(-2px);
    }

    .product-item-link svg {
      width: 20px;
      height: 20px;
      transition: transform 0.3s;
    }

    .product-item-link:hover svg {
      transform: translateX(4px);
    }

    /* Responsive */
    @media (max-width: 900px) {


      .product-list-section {
        padding: 4rem 3rem;
      }

      .product-item {
        grid-template-columns: 1fr;
        gap: 2.5rem;
        margin-bottom: 4rem;
      }

      .product-item.reverse {
        direction: ltr;
      }

      .product-item-image {
        height: 320px;
      }
    }

    @media (max-width: 580px) {


      .product-list-section {
        padding: 3rem 1.5rem;
      }

      .product-item {
        gap: 2rem;
        margin-bottom: 3rem;
      }

      .product-item-image {
        height: 280px;
      }
    }

    .product-item-content .product-tagline {
      font-size: 0.85rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #00c278;
      margin: -0.6rem 0 1rem;
    }

    .product-item-content ul.product-features {
      list-style: none;
      padding: 0;
      margin: -0.8rem 0 2rem;
      display: grid;
      gap: 0.5rem;
    }

    .product-item-content ul.product-features li {
      position: relative;
      padding-left: 1.6rem;
      font-size: 0.95rem;
      color: #4a5568;
    }

    .product-item-content ul.product-features li::before {
      content: "";
      position: absolute;
      left: 0;
      top: 0.45em;
      width: 0.6rem;
      height: 0.6rem;
      border-radius: 50%;
      background: #00e0a0;
    }
  </style>
@endpush

@section('content')
  @include('partials.page-hero', [
    'heroTitle' => $c['hero_title'] ?? 'Produk',
    'heroEm' => $c['hero_em'] ?? 'Kami',
    'heroDesc' => $c['hero_desc'] ?? null,
    'heroImage' => $c['hero_image'] ?? null,
    'crumbs' => [['Produk', null]],
  ])

  <!-- PRODUCT LIST SECTION -->
  <section class="product-list-section">
    <h2 class="section-title">{{ $c['section_title'] ?? 'Solusi Digital INOVASS' }}</h2>

    @forelse ($products as $product)
      <div class="product-item {{ $loop->even ? 'reverse' : '' }} reveal" id="{{ $product->slug }}">
        <div class="product-item-image">
          @if ($src = media_url($product->image))<img src="{{ $src }}" alt="{{ $product->name }}" />@endif
        </div>
        <div class="product-item-content">
          <h2>{{ $product->name }}</h2>
          @if (filled($product->tagline))<p class="product-tagline">{{ $product->tagline }}</p>@endif
          <p>{{ $product->description }}</p>
          @if (! empty($product->features))
            <ul class="product-features">
              @foreach ($product->features as $feature)
                <li>{{ $feature }}</li>
              @endforeach
            </ul>
          @endif
          <a href="{{ url('kontak.html') }}" class="product-item-link">
            {{ $product->button_label ?: 'Hubungi Kami' }}
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14m-7-7l7 7-7 7"/>
            </svg>
          </a>
        </div>
      </div>
    @empty
      <p style="text-align:center;color:#4a5568;">Produk akan segera hadir.</p>
    @endforelse
  </section>

  <!-- CTA -->
  <section class="page-cta reveal">
    <h2>{{ $c['cta_title'] ?? 'Butuh solusi' }}<br /><em>{{ $c['cta_em'] ?? 'yang lebih spesifik?' }}</em></h2>
    <p>{{ $c['cta_text'] ?? '' }}</p>
    <a href="{{ url('kontak.html') }}" class="btn-outline">{{ $c['cta_button'] ?? 'Hubungi Kami' }}</a>
  </section>
@endsection
