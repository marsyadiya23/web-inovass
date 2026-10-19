@extends('layouts.site', ['title' => 'Kontak', 'metaDescription' => $c['hero_desc'] ?? null])

@php
  $wa = preg_replace('/\D/', '', $s['whatsapp'] ?? '');
  $sent = session()->has('kontak_terkirim');
  $waText = session('kontak_terkirim');
@endphp

@push('styles')
  <style>
    /* Contact Section New Design */
    .contact-section-new {
      background: #f8fafc;
      padding: 5rem 2rem;
    }

    .contact-container-new {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 0.9fr 1.1fr;
      gap: 5rem;
      align-items: start;
    }

    /* Left Side: Contact Info */
    .contact-info-side {
      padding: 1rem 0;
    }

    .contact-title {
      color: #1e3a8a;
      font-size: 2.5rem;
      font-weight: 700;
      margin-bottom: 1.25rem;
      line-height: 1.15;
    }

    .contact-description {
      color: #475569;
      font-size: 1rem;
      line-height: 1.7;
      margin-bottom: 3rem;
    }

    .contact-info-list {
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }

    .contact-info-item {
      display: flex;
      align-items: flex-start;
      gap: 1.25rem;
      transition: transform 0.3s ease;
    }

    .contact-info-item:hover {
      transform: translateX(5px);
    }

    .contact-icon {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: #00e0a0;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      box-shadow: 0 4px 15px rgba(0, 224, 160, 0.2);
      transition: all 0.3s ease;
    }

    .contact-info-item:hover .contact-icon {
      transform: scale(1.1);
      box-shadow: 0 6px 20px rgba(0, 224, 160, 0.3);
      background: #1e3a8a;
    }

    .contact-icon svg {
      width: 22px;
      height: 22px;
      stroke: #ffffff;
      stroke-width: 2;
    }

    .contact-info-text h4 {
      color: #64748b;
      font-size: 0.8rem;
      font-weight: 600;
      margin: 0 0 0.35rem 0;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .contact-info-text p {
      color: #1e3a8a;
      font-size: 1rem;
      font-weight: 600;
      margin: 0;
      line-height: 1.6;
    }

    /* Right Side: Form */
    .contact-form-side {
      background: #ffffff;
      padding: 2.5rem;
      border-radius: 20px;
      box-shadow: 0 4px 30px rgba(30, 58, 138, 0.08);
    }

    .contact-form-new {
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }

    .form-row-double {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }

    .form-group-new {
      display: flex;
      flex-direction: column;
      gap: 0;
    }

    .form-group-new label {
      display: none;
    }

    .form-group-new input,
    .form-group-new textarea,
    .form-group-new select {
      padding: 1.25rem 1.5rem;
      border: 2px solid #e2e8f0;
      border-radius: 12px;
      font-size: 0.95rem;
      font-family: 'Plus Jakarta Sans', sans-serif;
      transition: all 0.3s ease;
      background: #f8fafc;
      color: #475569;
    }

    .form-group-new input::placeholder,
    .form-group-new textarea::placeholder {
      color: #94a3b8;
    }

    .form-group-new select {
      color: #94a3b8;
    }

    .form-group-new select option {
      color: #475569;
    }

    .form-group-new textarea {
      resize: vertical;
      min-height: 140px;
    }

    .form-group-new select {
      appearance: none;
      background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' stroke='%2394a3b8' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
      background-repeat: no-repeat;
      background-position: right 1.5rem center;
      padding-right: 3rem;
    }

    .form-group-new input:focus,
    .form-group-new textarea:focus,
    .form-group-new select:focus {
      outline: none;
      border-color: #00e0a0;
      background: #ffffff;
      box-shadow: 0 0 0 3px rgba(0, 224, 160, 0.1);
    }

    .submit-btn-new {
      background: transparent;
      color: #00e0a0;
      border: 2px solid #00e0a0;
      padding: 1.25rem 3.5rem;
      border-radius: 12px;
      font-size: 0.9rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      cursor: pointer;
      transition: all 0.3s ease;
      width: fit-content;
      margin-top: 0.5rem;
      text-transform: uppercase;
    }

    .submit-btn-new:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(0, 224, 160, 0.4);
      background: #00e0a0;
      color: #ffffff;
    }

    .submit-btn-new:active {
      transform: translateY(0);
    }

    /* Map Section */
    .map-section {
      width: 100%;
      max-width: 1200px;
      margin: 4rem auto 5rem;
      padding: 0 2rem;
      height: 450px;
      border-radius: 20px;
      overflow: hidden;
    }

    .map-section iframe {
      width: 100%;
      height: 100%;
      display: block;
      border-radius: 20px;
      box-shadow: 0 4px 30px rgba(30, 58, 138, 0.1);
    }

    /* Responsive */
    @media (max-width: 992px) {
      .contact-container-new {
        grid-template-columns: 1fr;
        gap: 3rem;
      }
      
      .contact-form-side {
        padding: 2rem;
      }
      
      .map-section {
        margin: 3rem auto 4rem;
        border-radius: 16px;
      }
      
      .map-section iframe {
        border-radius: 16px;
      }
    }

    @media (max-width: 640px) {
      .contact-section-new {
        padding: 3rem 1.5rem;
      }

      .contact-title {
        font-size: 2.25rem;
      }
      
      .contact-description {
        font-size: 1rem;
      }
      
      .form-row-double {
        grid-template-columns: 1fr;
      }
      
      .contact-form-side {
        padding: 1.75rem;
      }
      
      .form-group-new input,
      .form-group-new textarea,
      .form-group-new select {
        padding: 1.1rem 1.25rem;
      }

      .submit-btn-new {
        width: 100%;
        padding: 1.15rem 2rem;
      }
      
      .map-section {
        padding: 0 1.5rem;
        margin: 3rem auto 4rem;
        border-radius: 12px;
      }
      
      .map-section iframe {
        border-radius: 12px;
      }
    }
    .contact-info-text a { color: inherit; text-decoration: none; }
    .contact-info-text a:hover { color: #00c278; }

    .kontak-alert {
      border-radius: 12px;
      padding: 1.1rem 1.4rem;
      margin-bottom: 1.5rem;
      font-size: 0.95rem;
      line-height: 1.6;
    }
    .kontak-alert.success { background: #e9fbf3; border: 1px solid #00c278; color: #065f46; }
    .kontak-alert.error { background: #fef2f2; border: 1px solid #f87171; color: #991b1b; }
    .kontak-alert a.wa-link {
      display: inline-block;
      margin-top: 0.7rem;
      padding: 0.6rem 1.3rem;
      border-radius: 50px;
      background: #25d366;
      color: #ffffff;
      font-weight: 600;
      text-decoration: none;
    }
    .form-error { color: #dc2626; font-size: 0.82rem; margin-top: 0.4rem; }
    .form-hp { position: absolute; left: -9999px; width: 1px; height: 1px; overflow: hidden; }
  </style>
@endpush

@section('content')
  @include('partials.page-hero', [
    'heroTitle' => $c['hero_title'] ?? 'Hubungi',
    'heroEm' => $c['hero_em'] ?? 'Kami',
    'heroDesc' => $c['hero_desc'] ?? null,
    'heroImage' => $c['hero_image'] ?? null,
    'crumbs' => [['Hubungi Kami', null]],
  ])

  <!-- CONTACT SECTION -->
  <section class="contact-section-new">
    <div class="contact-container-new">

      <!-- Left Side: Contact Info -->
      <div class="contact-info-side">
        <h2 class="contact-title">{{ $c['title'] ?? 'Mari Wujudkan Solusi Bersama' }}</h2>
        <p class="contact-description">{{ $c['intro'] ?? '' }}</p>

        <div class="contact-info-list">
          @if (filled($s['phone'] ?? null))
            <div class="contact-info-item">
              <div class="contact-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
                </svg>
              </div>
              <div class="contact-info-text">
                <h4>Hubungi Kami</h4>
                <p>@if ($wa)<a href="https://wa.me/{{ $wa }}" target="_blank" rel="noopener">{{ $s['phone'] }}</a>@else{{ $s['phone'] }}@endif</p>
              </div>
            </div>
          @endif

          @if (filled($s['email'] ?? null))
            <div class="contact-info-item">
              <div class="contact-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                  <polyline points="22,6 12,13 2,6"/>
                </svg>
              </div>
              <div class="contact-info-text">
                <h4>Email Kami</h4>
                <p><a href="mailto:{{ $s['email'] }}">{{ $s['email'] }}</a></p>
              </div>
            </div>
          @endif

          @if (filled($s['address'] ?? null))
            <div class="contact-info-item">
              <div class="contact-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
              </div>
              <div class="contact-info-text">
                <h4>Kantor Kami</h4>
                <p>{!! nl2br(e($s['address'])) !!}</p>
              </div>
            </div>
          @endif
        </div>
      </div>

      <!-- Right Side: Contact Form -->
      <div class="contact-form-side" id="kontak-form">
        @if ($sent)
          <div class="kontak-alert success" role="status">
            <strong>Terima kasih, pesan Anda sudah kami terima.</strong> Tim INOVASS akan segera menghubungi Anda.
            @if ($wa && filled($waText))
              <br /><a class="wa-link" href="https://wa.me/{{ $wa }}?text={{ rawurlencode($waText) }}" target="_blank" rel="noopener">Lanjutkan via WhatsApp</a>
            @endif
          </div>
        @endif
        @if ($errors->any())
          <div class="kontak-alert error" role="alert">Mohon periksa kembali isian formulir Anda.</div>
        @endif

        <form class="contact-form-new" id="contactForm" method="POST" action="{{ route('kontak.kirim') }}">
          @csrf
          <div class="form-hp" aria-hidden="true">
            <label for="website">Website</label>
            <input type="text" id="website" name="website" tabindex="-1" autocomplete="off" />
          </div>

          <div class="form-row-double">
            <div class="form-group-new">
              <label for="nama">Nama Lengkap</label>
              <input type="text" id="nama" name="name" value="{{ old('name') }}" placeholder="Nama Lengkap" required maxlength="255" />
              @error('name')<span class="form-error">{{ $message }}</span>@enderror
            </div>

            <div class="form-group-new">
              <label for="email">Email</label>
              <input type="email" id="email" name="email" value="{{ old('email') }}" placeholder="Alamat Email" required maxlength="255" />
              @error('email')<span class="form-error">{{ $message }}</span>@enderror
            </div>
          </div>

          <div class="form-row-double">
            <div class="form-group-new">
              <label for="telepon">Nomor Telepon</label>
              <input type="tel" id="telepon" name="phone" value="{{ old('phone') }}" placeholder="Nomor Telepon" maxlength="50" />
              @error('phone')<span class="form-error">{{ $message }}</span>@enderror
            </div>

            <div class="form-group-new">
              <label for="organisasi">Organisasi / Perusahaan</label>
              <input type="text" id="organisasi" name="organization" value="{{ old('organization') }}" placeholder="Organisasi / Perusahaan" maxlength="255" />
              @error('organization')<span class="form-error">{{ $message }}</span>@enderror
            </div>
          </div>

          <div class="form-group-new">
            <label for="layanan">Keperluan</label>
            <select id="layanan" name="subject">
              <option value="">Pilih Keperluan</option>
              @foreach ($c['subjects'] ?? [] as $subject)
                <option value="{{ $subject }}" @selected(old('subject') === $subject)>{{ $subject }}</option>
              @endforeach
            </select>
            @error('subject')<span class="form-error">{{ $message }}</span>@enderror
          </div>

          <div class="form-group-new">
            <label for="pesan">Pesan</label>
            <textarea id="pesan" name="message" rows="5" placeholder="Tulis pesan Anda" required maxlength="3000">{{ old('message') }}</textarea>
            @error('message')<span class="form-error">{{ $message }}</span>@enderror
          </div>

          <button type="submit" class="submit-btn-new">
            Kirim Pesan
          </button>
        </form>
      </div>

    </div>
  </section>

  @if (filled($c['map_url'] ?? null))
    <!-- GOOGLE MAP SECTION -->
    <section class="map-section">
      <iframe
        src="{{ $c['map_url'] }}"
        title="Peta lokasi kantor INOVASS"
        width="100%"
        height="450"
        style="border:0;"
        allowfullscreen=""
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade">
      </iframe>
    </section>
  @endif
@endsection
