<?php

use App\Http\Controllers\BeritaController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\LayananController;
use App\Http\Controllers\PageController;
use App\Http\Controllers\PelatihanController;
use Illuminate\Support\Facades\Route;

// URL lama situs statis (.html) dipertahankan apa adanya.
Route::get('/', HomeController::class)->name('home');
Route::redirect('/index.html', '/', 301);

Route::get('/tentang.html', [PageController::class, 'tentang'])->name('tentang');
Route::get('/produk.html', [PageController::class, 'produk'])->name('produk');
Route::get('/kontak.html', [PageController::class, 'kontak'])->name('kontak');
Route::post('/kontak.html', [PageController::class, 'kirimKontak'])->middleware('throttle:5,1')->name('kontak.kirim');

Route::get('/layanan/{kategori}/', [LayananController::class, 'kategori']);
Route::get('/layanan/{kategori}/index.html', [LayananController::class, 'kategori'])->name('layanan.kategori');
Route::get('/layanan/{kategori}/{slug}.html', [LayananController::class, 'detail'])->name('layanan.detail');

Route::get('/berita', [BeritaController::class, 'index'])->name('berita.index');
Route::get('/berita/{slug}', [BeritaController::class, 'show'])->name('berita.show');

// Inti CMS: jadwal & katalog pelatihan.
Route::get('/jadwal-pelatihan', [PelatihanController::class, 'jadwal'])->name('pelatihan.jadwal');
Route::get('/pelatihan', [PelatihanController::class, 'index'])->name('pelatihan.index');
Route::get('/pelatihan/{slug}', [PelatihanController::class, 'show'])->name('pelatihan.show');
Route::post('/pelatihan/{slug}/daftar', [PelatihanController::class, 'daftar'])->middleware('throttle:5,1')->name('pelatihan.daftar');
