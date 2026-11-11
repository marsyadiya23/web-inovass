<?php

// Hanya menimpa batas payload; pengaturan Livewire lain tetap bawaan paket.
return [
    'payload' => [
        'max_size' => 1024 * 1024,
        // Bawaan 10 terlalu kecil untuk RichEditor: teks di dalam daftar/kutipan sudah 11+ level
        // (data.description.content.3.content.0.content.1.content.0.text) → form program gagal disimpan.
        'max_nesting_depth' => 30,
        'max_calls' => 50,
        'max_components' => 200,
    ],
];
