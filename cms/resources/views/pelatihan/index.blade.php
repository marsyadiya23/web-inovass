@extends('layouts.site')

@push('styles')
  <link rel="stylesheet" href="{{ asset('assets/css/pelatihan.css') }}" />
@endpush

@section('content')
  @include('partials.page-hero', [
      'heroTitle' => 'Program',
      'heroEm' => 'Pelatihan',
      'heroDesc' => 'Program pelatihan berbasis standar internasional untuk meningkatkan kompetensi personel organisasi Anda.',
      'heroImage' => 'legacy/Pelatihan Profesional.jpeg',
      'crumbs' => [['Program Pelatihan', null]],
  ])

  <section class="pl-section">
    <div class="pl-container">
      <p style="margin-bottom:2rem;"><a class="pl-btn" href="{{ route('pelatihan.jadwal') }}">Lihat jadwal terdekat</a></p>

      @foreach ($categories as $category)
        @continue($category->trainings->isEmpty())
        <div class="pl-cat" id="{{ $category->slug }}">
          <p class="pl-eyebrow">{{ $category->trainings->count() }} program</p>
          <h2 class="pl-heading">{{ $category->name }}</h2>
          @if ($category->description)<p class="pl-lead">{{ $category->description }}</p>@endif
          <div class="pl-grid">
            @foreach ($category->trainings as $training)
              <a class="pl-prog" href="{{ $training->url() }}">
                <div>
                  <h3>{{ $training->title }}</h3>
                  @if ($training->summary)<p>{{ \Illuminate\Support\Str::limit($training->summary, 130) }}</p>@endif
                </div>
                @if ($training->upcoming_count)
                  <span class="pl-next">● {{ $training->upcoming_count }} jadwal tersedia</span>
                @else
                  <span class="pl-next none">Jadwal menyusul, hubungi kami</span>
                @endif
              </a>
            @endforeach
          </div>
        </div>
      @endforeach
    </div>
  </section>

  @include('partials.cta', ['ctaTitle' => 'Tidak menemukan', 'ctaEm' => 'pelatihan yang dicari?', 'ctaText' => 'Ceritakan kebutuhan pelatihan organisasi Anda, tim kami akan menyiapkan programnya.'])
@endsection
