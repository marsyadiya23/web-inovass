{{-- Ikon SVG garis hijau dari daftar tetap HomeContent::ICONS. Props: $name, $size, $stroke --}}
@php $icon = \App\Filament\Pages\HomeContent::ICONS[$name ?? ''] ?? null; @endphp
@if ($icon)
<svg width="{{ $size }}" height="{{ $size }}" viewBox="{{ $icon[1] }}" fill="none" stroke="#00c278" stroke-width="{{ $stroke }}" stroke-linecap="round" stroke-linejoin="round">{!! $icon[2] !!}</svg>
@endif
