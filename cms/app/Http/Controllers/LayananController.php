<?php

namespace App\Http\Controllers;

use App\Models\Service;
use App\Models\ServiceCategory;

class LayananController extends Controller
{
    public function kategori(string $kategori)
    {
        $category = ServiceCategory::where('slug', $kategori)->where('is_published', true)->firstOrFail();

        return view('layanan.kategori', [
            'category' => $category,
            'categories' => ServiceCategory::published()->get(),
            'services' => $category->topServices()->published()->get(),
            'title' => $category->name,
            'metaDescription' => $category->meta_description ?: $category->intro,
        ]);
    }

    public function detail(string $kategori, string $slug)
    {
        $service = Service::with(['category', 'parent'])
            ->whereRelation('category', 'slug', $kategori)
            ->whereRelation('category', 'is_published', true)
            ->where('slug', $slug)->where('is_published', true)
            ->firstOrFail();

        return view('layanan.detail', [
            'service' => $service,
            'children' => $service->children()->published()->with('category')->get(),
            'title' => $service->title,
            'metaDescription' => $service->meta_description ?: $service->summary,
        ]);
    }
}
