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
      <div class="pl-search">
        <label class="pl-search-box">
          <span class="pl-sr">Cari program pelatihan</span>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
          <input type="search" id="plSearch" value="{{ request('q') }}" autocomplete="off" placeholder="Cari pelatihan, mis. ISO 9001, 17025, audit internal…" />
        </label>
        <a class="pl-btn" href="{{ route('pelatihan.jadwal') }}">Lihat jadwal terdekat</a>
      </div>
      <p class="pl-search-meta" id="plSearchMeta" aria-live="polite"></p>
      <div class="pl-search-empty" id="plSearchEmpty" hidden>
        Tidak ada program yang cocok. Coba kata lain, atau <a href="{{ url('/kontak.html') }}">hubungi kami</a>, kami bisa menyiapkan pelatihan sesuai kebutuhan.
      </div>

      @foreach ($categories as $category)
        @continue($category->trainings->isEmpty())
        <div class="pl-cat" id="{{ $category->slug }}">
          <p class="pl-eyebrow"><span class="pl-cat-count">{{ $category->trainings->count() }}</span> program</p>
          <h2 class="pl-heading">{{ $category->name }}</h2>
          @if ($category->description)<p class="pl-lead">{{ $category->description }}</p>@endif
          <div class="pl-grid">
            @foreach ($category->trainings as $training)
              <a class="pl-prog" href="{{ $training->url() }}" data-search="{{ $training->title }} {{ $training->summary }} {{ $category->name }}">
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

  <script>
    // Saring katalog di browser (semua program sudah ada di halaman). Semua kata harus cocok; ?q= bisa dibagikan.
    (function () {
      var input = document.getElementById('plSearch'), meta = document.getElementById('plSearchMeta'), empty = document.getElementById('plSearchEmpty');
      var cards = [].slice.call(document.querySelectorAll('.pl-prog[data-search]'));
      var norm = function (s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim(); };
      cards.forEach(function (c) { c._h = ' ' + norm(c.dataset.search); });

      function apply() {
        var q = norm(input.value), words = q ? q.split(' ') : [], total = 0;
        cards.forEach(function (c) {
          var ok = words.every(function (w) { return c._h.indexOf(' ' + w) !== -1; }); // awal kata: "9001" ≠ "39001"
          c.style.display = ok ? '' : 'none';
          if (ok) total++;
        });
        document.querySelectorAll('.pl-cat').forEach(function (cat) {
          var n = cat.querySelectorAll('.pl-prog[data-search]:not([style*="none"])').length;
          cat.style.display = n ? '' : 'none';
          cat.querySelector('.pl-cat-count').textContent = n;
        });
        meta.textContent = q ? total + ' program ditemukan' : '';
        empty.hidden = !q || total > 0;
        var url = new URL(location.href);
        q ? url.searchParams.set('q', input.value.trim()) : url.searchParams.delete('q');
        history.replaceState(null, '', url);
      }

      var timer;
      input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(apply, 100); });
      input.addEventListener('keydown', function (e) { if (e.key === 'Escape') { input.value = ''; apply(); } });
      if (input.value) apply();
    })();
  </script>

  @include('partials.cta', ['ctaTitle' => 'Tidak menemukan', 'ctaEm' => 'pelatihan yang dicari?', 'ctaText' => 'Ceritakan kebutuhan pelatihan organisasi Anda, tim kami akan menyiapkan programnya.'])
@endsection
