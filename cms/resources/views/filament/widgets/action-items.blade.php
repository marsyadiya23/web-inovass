{{-- Gaya inline: kelas Tailwind di luar bawaan Filament tidak ikut terkompilasi di panel --}}
<x-filament-widgets::widget>
    <x-filament::section heading="Perlu tindakan" icon="heroicon-o-bell-alert">
        @forelse ($items as [$color, $text, $url])
            <a href="{{ $url }}" style="display:flex;align-items:center;gap:.75rem;padding:.6rem 0;text-decoration:none;color:inherit;{{ $loop->last ? '' : 'border-bottom:1px solid rgba(127,127,127,.18);' }}">
                <span style="flex:none;width:.6rem;height:.6rem;border-radius:999px;background:{{ ['danger' => '#ef4444', 'warning' => '#f59e0b', 'gray' => '#94a3b8'][$color] }}"></span>
                <span style="flex:1;font-size:.9rem">{{ $text }}</span>
                <span style="flex:none;font-size:.8rem;font-weight:600;color:#00a066">Buka →</span>
            </a>
        @empty
            <p style="font-size:.9rem;opacity:.75">Tidak ada yang perlu ditindaklanjuti saat ini.</p>
        @endforelse
    </x-filament::section>
</x-filament-widgets::widget>
