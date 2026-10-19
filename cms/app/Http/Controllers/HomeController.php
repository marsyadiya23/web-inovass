<?php

namespace App\Http\Controllers;

use App\Models\Article;
use App\Models\Client;
use App\Models\Faq;
use App\Models\PageContent;
use App\Models\Product;
use App\Models\Testimonial;
use App\Models\TrainingSchedule;

class HomeController extends Controller
{
    public function __invoke()
    {
        $h = PageContent::get('home');

        return view('home', [
            'homepage' => true,
            'h' => $h,
            'title' => trim(($h['hero']['title'] ?? '').' '.($h['hero']['title_em'] ?? '')) ?: null,
            'metaDescription' => $h['meta_description'] ?? null,
            'clients' => Client::published()->get(),
            'products' => Product::published()->get(),
            'articles' => Article::published()->take(3)->get(),
            'upcomingSchedules' => TrainingSchedule::visible()->with('training')->take(4)->get(),
            'testimonials' => Testimonial::published()->get(),
            'faqs' => Faq::published()->get(),
        ]);
    }
}
