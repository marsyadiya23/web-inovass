@extends('layouts.site')

@push('styles')
  <link rel="stylesheet" href="{{ asset('assets/css/pelatihan.css') }}" />
@endpush

@php
    $s = \App\Models\PageContent::get('settings');
    $wa = preg_replace('/\D/', '', $s['whatsapp'] ?? '');
    $open = $schedules->filter->isOpen();
    $selected = (int) old('training_schedule_id', request('jadwal', $open->first()?->id));
    $ok = session('daftar_ok');
@endphp

@section('content')
  @include('partials.page-hero', [
      'heroTitle' => $training->title,
      'heroDesc' => $training->summary,
      'heroImage' => $training->image ?: 'legacy/Pelatihan Profesional.jpeg',
      'crumbs' => [['Program Pelatihan', route('pelatihan.index')], [$training->category->name, route('pelatihan.index').'#'.$training->category->slug]],
  ])

  <section class="pl-section">
    <div class="pl-container pl-detail">
      <div>
        <div class="pl-facts">
          <span>{{ $training->category->name }}</span>
          @if ($training->duration)<span>⏱ {{ $training->duration }}</span>@endif
          <span>📅 {{ $schedules->count() ? $schedules->count().' jadwal mendatang' : 'Jadwal menyusul' }}</span>
          @if ($training->brochure)<span><a href="{{ media_url($training->brochure) }}" target="_blank" rel="noopener">⬇ Unduh brosur</a></span>@endif
        </div>

        @if ($training->highlights)
          <div class="pl-highlights">
            @foreach ($training->highlights as $h)<div>{{ $h }}</div>@endforeach
          </div>
        @endif

        <h2 class="pl-heading">Jadwal <em>Tersedia</em></h2>
        @if ($schedules->isNotEmpty())
          <div class="pl-list" style="margin-bottom:2.5rem;">
            @foreach ($schedules as $schedule)
              @include('pelatihan._schedule', ['schedule' => $schedule->setRelation('training', $training), 'showTitle' => false])
            @endforeach
          </div>
        @else
          <div class="pl-empty" style="margin-bottom:2.5rem;">
            <p>Belum ada jadwal terbuka untuk pelatihan ini. Hubungi kami untuk jadwal berikutnya atau pelatihan in-house.</p>
          </div>
        @endif

        @if (filled(strip_tags((string) $training->description)))
          <div class="pl-body">{!! $training->description !!}</div>
        @endif
      </div>

      <aside class="pl-aside" id="daftar">
        <div class="pl-box">
          <h3>Daftar Pelatihan</h3>

          @if ($ok)
            <div class="pl-alert ok" role="status">
              <strong>Pendaftaran terkirim.</strong> Tim kami akan menghubungi Anda untuk konfirmasi.
              @if ($wa && $ok['wa'])
                <br /><a href="https://wa.me/{{ $wa }}?text={{ rawurlencode($ok['wa']) }}" target="_blank" rel="noopener">Konfirmasi via WhatsApp →</a>
              @endif
            </div>
          @endif
          @if ($errors->any())
            <div class="pl-alert err" role="alert">Mohon periksa kembali isian formulir.</div>
          @endif

          @if ($open->isEmpty())
            <p style="font-size:.88rem;color:#475569;">Pendaftaran online belum tersedia untuk pelatihan ini.</p>
            <a class="pl-btn" href="{{ $wa ? 'https://wa.me/'.$wa.'?text='.rawurlencode('Halo INOVASS, saya tertarik dengan '.$training->title.'. Kapan jadwal berikutnya?') : url('kontak.html') }}" target="_blank" rel="noopener">Tanya jadwal</a>
          @else
            <form method="POST" action="{{ route('pelatihan.daftar', $training->slug) }}">
              @csrf
              <div class="pl-hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off" /></label></div>

              <div class="pl-field">
                <label>Pilih jadwal</label>
                @foreach ($schedules as $schedule)
                  @php $isOpen = $schedule->isOpen(); @endphp
                  <label class="pl-opt {{ $isOpen ? '' : 'disabled' }}">
                    <input type="radio" name="training_schedule_id" value="{{ $schedule->id }}" @checked($selected === $schedule->id) @disabled(! $isOpen) required />
                    <strong>{{ $schedule->dateLabel() }}</strong> · {{ $schedule->methodLabel() }}{{ $schedule->location ? ', '.$schedule->location : '' }}
                    <br /><span style="margin-left:1.6rem;">{{ $schedule->priceLabel() }}{{ $isOpen ? '' : ' · '.$schedule->publicStatus() }}</span>
                  </label>
                @endforeach
                @error('training_schedule_id')<div class="pl-error">{{ $message }}</div>@enderror
              </div>

              @foreach ([
                  ['name', 'Nama lengkap', 'text', true],
                  ['email', 'Email', 'email', true],
                  ['phone', 'No. WhatsApp', 'tel', true],
                  ['organization', 'Instansi / perusahaan', 'text', false],
                  ['position', 'Jabatan', 'text', false],
              ] as [$field, $label, $type, $required])
                <div class="pl-field">
                  <label for="f-{{ $field }}">{{ $label }}{{ $required ? ' *' : '' }}</label>
                  <input id="f-{{ $field }}" type="{{ $type }}" name="{{ $field }}" value="{{ old($field) }}" @required($required) maxlength="255" />
                  @error($field)<div class="pl-error">{{ $message }}</div>@enderror
                </div>
              @endforeach

              <div class="pl-field">
                <label for="f-participants">Jumlah peserta *</label>
                <input id="f-participants" type="number" name="participants" min="1" max="100" value="{{ old('participants', 1) }}" required />
                @error('participants')<div class="pl-error">{{ $message }}</div>@enderror
              </div>
              <div class="pl-field">
                <label for="f-message">Pesan / pertanyaan</label>
                <textarea id="f-message" name="message" rows="3" maxlength="2000">{{ old('message') }}</textarea>
                @error('message')<div class="pl-error">{{ $message }}</div>@enderror
              </div>
              <button class="pl-btn" type="submit" style="width:100%;">Kirim pendaftaran</button>
            </form>
          @endif
        </div>
      </aside>
    </div>
  </section>

  @include('partials.cta')
@endsection
