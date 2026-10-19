<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

// ponytail: satu migrasi untuk semua tabel konten v0. Pecah per tabel saat skema PRD penuh masuk.
return new class extends Migration
{
    public function up(): void
    {
        // Konten singleton (pengaturan situs, beranda, tentang, produk, kontak) disimpan sebagai JSON per key.
        Schema::create('page_contents', function (Blueprint $t) {
            $t->id();
            $t->string('key')->unique();
            $t->json('data')->nullable();
            $t->timestamps();
        });

        Schema::create('service_categories', function (Blueprint $t) {
            $t->id();
            $t->string('name');
            $t->string('slug')->unique();
            $t->text('short_description')->nullable();
            $t->text('intro')->nullable();
            $t->string('image')->nullable();
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->string('meta_description')->nullable();
            $t->timestamps();
        });

        Schema::create('services', function (Blueprint $t) {
            $t->id();
            $t->foreignId('service_category_id')->constrained()->cascadeOnDelete();
            $t->foreignId('parent_id')->nullable()->constrained('services')->nullOnDelete();
            $t->string('title');
            $t->string('slug');
            $t->text('summary')->nullable();
            $t->json('highlights')->nullable();
            $t->longText('body')->nullable();
            $t->string('image')->nullable();
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->string('meta_description')->nullable();
            $t->timestamps();
            $t->unique(['service_category_id', 'slug']);
        });

        Schema::create('products', function (Blueprint $t) {
            $t->id();
            $t->string('name');
            $t->string('slug')->unique();
            $t->string('tagline')->nullable();
            $t->text('description')->nullable();
            $t->json('features')->nullable();
            $t->string('image')->nullable();
            $t->string('button_label')->nullable();
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->timestamps();
        });

        Schema::create('clients', function (Blueprint $t) {
            $t->id();
            $t->string('name');
            $t->string('logo');
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->timestamps();
        });

        Schema::create('testimonials', function (Blueprint $t) {
            $t->id();
            $t->text('quote');
            $t->string('name');
            $t->string('position')->nullable();
            $t->string('organization')->nullable();
            $t->unsignedTinyInteger('rating')->default(5);
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->timestamps();
        });

        Schema::create('faqs', function (Blueprint $t) {
            $t->id();
            $t->string('question');
            $t->text('answer');
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->timestamps();
        });

        Schema::create('articles', function (Blueprint $t) {
            $t->id();
            $t->string('title');
            $t->string('slug')->unique();
            $t->string('category')->nullable();
            $t->text('excerpt')->nullable();
            $t->string('cover')->nullable();
            $t->longText('body')->nullable();
            $t->timestamp('published_at')->nullable();
            $t->boolean('is_published')->default(true);
            $t->timestamps();
        });

        Schema::create('contact_messages', function (Blueprint $t) {
            $t->id();
            $t->string('name');
            $t->string('email');
            $t->string('phone')->nullable();
            $t->string('organization')->nullable();
            $t->string('subject')->nullable();
            $t->text('message');
            $t->string('status')->default('baru');
            $t->text('note')->nullable();
            $t->timestamps();
        });
    }

    public function down(): void
    {
        foreach (['contact_messages', 'articles', 'faqs', 'testimonials', 'clients', 'products', 'services', 'service_categories', 'page_contents'] as $table) {
            Schema::dropIfExists($table);
        }
    }
};
