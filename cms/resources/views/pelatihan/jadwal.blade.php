@extends('layouts.site')

@push('styles')
  <link rel="stylesheet" href="{{ asset('assets/css/pelatihan.css') }}" />
@endpush

@section('content')
  @include('partials.page-hero', [
      'heroTitle' => 'Jadwal',
      'heroEm' => 'Pelatihan',
      'heroDesc' => 'Jadwal pelatihan terbuka INOVASS yang akan datang. Pilih jadwal yang sesuai dan daftar langsung secara online.',
      'heroImage' => 'legacy/Pelatihan Profesional.jpeg',
      'crumbs' => [['Jadwal Pelatihan', null]],
  ])

  <section class="pl-section">
    <div class="pl-container">
      <form class="pl-filter" method="GET" action="{{ route('pelatihan.jadwal') }}">
        <div>
          <label for="f-bulan">Bulan</label>
          <select id="f-bulan" name="bulan" onchange="this.form.submit()">
            <option value="">Semua bulan</option>
            @foreach ($months as $m)
              <option value="{{ $m }}" @selected(($filters['bulan'] ?? '') === $m)>{{ \Carbon\Carbon::createFromFormat('Y-m', $m)->translatedFormat('F Y') }}</option>
            @endforeach
          </select>
        </div>
        <div>
          <label for="f-kategori">Kategori</label>
          <select id="f-kategori" name="kategori" onchange="this.form.submit()">
            <option value="">Semua kategori</option>
            @foreach ($categories as $c)
              <option value="{{ $c->slug }}" @selected(($filters['kategori'] ?? '') === $c->slug)>{{ $c->name }}</option>
            @endforeach
          </select>
        </div>
        <div>
          <label for="f-metode">Metode</label>
          <select id="f-metode" name="metode" onchange="this.form.submit()">
            <option value="">Semua metode</option>
            @foreach (\App\Models\TrainingSchedule::METHODS as $k => $v)
              <option value="{{ $k }}" @selected(($filters['metode'] ?? '') === $k)>{{ $v }}</option>
            @endforeach
          </select>
        </div>
        <noscript><button class="pl-btn" type="submit">Terapkan</button></noscript>
        @if (array_filter($filters))
          <a class="pl-reset" href="{{ route('pelatihan.jadwal') }}">Reset filter</a>
        @endif
      </form>

      @forelse ($schedules as $month => $items)
        <div class="pl-month">
          <h2 class="pl-month-title">{{ \Carbon\Carbon::createFromFormat('Y-m', $month)->translatedFormat('F Y') }}</h2>
          <div class="pl-list">
            @foreach ($items as $schedule)
              @include('pelatihan._schedule', ['schedule' => $schedule])
            @endforeach
          </div>
        </div>
      @empty
        <div class="pl-empty">
          <p><strong>Belum ada jadwal{{ array_filter($filters) ? ' yang sesuai filter' : '' }}.</strong></p>
          <p>Lihat <a href="{{ route('pelatihan.index') }}">katalog program pelatihan</a> atau hubungi kami untuk jadwal in-house.</p>
        </div>
      @endforelse

      <p style="margin-top:2rem;"><a class="pl-btn ghost" href="{{ route('pelatihan.index') }}">Lihat semua program pelatihan</a></p>
    </div>
  </section>

  @include('partials.cta', ['ctaTitle' => 'Butuh pelatihan', 'ctaEm' => 'in-house?', 'ctaText' => 'Kami dapat menyelenggarakan pelatihan khusus di lokasi dan jadwal organisasi Anda.'])
@endsection
