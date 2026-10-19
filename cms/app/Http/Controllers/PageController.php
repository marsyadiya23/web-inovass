<?php

namespace App\Http\Controllers;

use App\Models\Client;
use App\Models\ContactMessage;
use App\Models\PageContent;
use App\Models\Product;
use Illuminate\Http\Request;

class PageController extends Controller
{
    public function tentang()
    {
        return view('pages.tentang', ['c' => PageContent::get('tentang'), 'clients' => Client::published()->get()]);
    }

    public function produk()
    {
        return view('pages.produk', ['c' => PageContent::get('produk'), 'products' => Product::published()->get()]);
    }

    public function kontak()
    {
        return view('pages.kontak', ['c' => PageContent::get('kontak'), 's' => PageContent::get('settings')]);
    }

    public function kirimKontak(Request $request)
    {
        // Honeypot: bot mengisi field tersembunyi -> pura-pura sukses tanpa menyimpan.
        if (filled($request->input('website'))) {
            return redirect()->to(route('kontak').'#kontak-form')->with('kontak_terkirim', '');
        }

        $data = $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255',
            'phone' => 'nullable|string|max:50',
            'organization' => 'nullable|string|max:255',
            'subject' => 'nullable|string|max:255',
            'message' => 'required|string|max:3000',
        ]);

        ContactMessage::create($data + ['status' => 'baru']);

        // Teks untuk tombol "Lanjutkan via WhatsApp" (perilaku form situs lama).
        $wa = implode("\n", array_filter([
            'Halo INOVASS, saya ingin berkonsultasi.',
            'Nama: '.$data['name'],
            'Email: '.$data['email'],
            filled($data['phone'] ?? null) ? 'Telepon: '.$data['phone'] : null,
            filled($data['organization'] ?? null) ? 'Organisasi: '.$data['organization'] : null,
            filled($data['subject'] ?? null) ? 'Keperluan: '.$data['subject'] : null,
            '',
            $data['message'],
        ], fn ($line) => $line !== null));

        return redirect()->to(route('kontak').'#kontak-form')->with('kontak_terkirim', $wa);
    }
}
