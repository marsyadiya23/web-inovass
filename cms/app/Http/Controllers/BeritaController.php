<?php

namespace App\Http\Controllers;

use App\Models\Article;

class BeritaController extends Controller
{
    public function index()
    {
        return view('berita.index', ['articles' => Article::published()->paginate(9)]);
    }

    public function show(string $slug)
    {
        $article = Article::published()->where('slug', $slug)->firstOrFail();

        return view('berita.show', [
            'article' => $article,
            'others' => Article::published()->whereKeyNot($article->id)->take(3)->get(),
        ]);
    }
}
