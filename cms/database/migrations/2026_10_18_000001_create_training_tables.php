<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

// Inti CMS: katalog pelatihan, jadwal (batch), dan pendaftar.
return new class extends Migration
{
    public function up(): void
    {
        Schema::create('training_categories', function (Blueprint $t) {
            $t->id();
            $t->string('name');
            $t->string('slug')->unique();
            $t->text('description')->nullable();
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->timestamps();
        });

        Schema::create('trainings', function (Blueprint $t) {
            $t->id();
            $t->foreignId('training_category_id')->constrained()->restrictOnDelete();
            $t->string('title');
            $t->string('slug')->unique();
            $t->text('summary')->nullable();
            $t->json('highlights')->nullable();
            $t->longText('description')->nullable();
            $t->string('duration')->nullable();          // "2 hari (16 jam)"
            $t->unsignedBigInteger('price')->nullable();  // harga default, rupiah
            $t->string('image')->nullable();
            $t->string('brochure')->nullable();           // PDF
            $t->unsignedInteger('sort')->default(0);
            $t->boolean('is_published')->default(true);
            $t->string('meta_description')->nullable();
            $t->timestamps();
        });

        Schema::create('training_schedules', function (Blueprint $t) {
            $t->id();
            $t->foreignId('training_id')->constrained()->cascadeOnDelete();
            $t->date('start_date');
            $t->date('end_date')->nullable();
            $t->string('time')->nullable();               // "08.30 – 16.30 WIB"
            $t->string('method')->default('offline');     // offline | online | hybrid
            $t->string('location')->nullable();           // kota/venue, atau "Zoom"
            $t->unsignedBigInteger('price')->nullable();  // kosong = harga program
            $t->unsignedInteger('quota')->nullable();     // kosong = tanpa batas
            $t->date('registration_deadline')->nullable();
            $t->string('status')->default('dibuka');      // dibuka | penuh | ditutup | batal
            $t->text('note')->nullable();
            $t->timestamps();
            $t->index('start_date');
        });

        Schema::create('registrations', function (Blueprint $t) {
            $t->id();
            $t->foreignId('training_schedule_id')->constrained()->cascadeOnDelete();
            $t->string('name');
            $t->string('email');
            $t->string('phone');
            $t->string('organization')->nullable();
            $t->string('position')->nullable();
            $t->unsignedInteger('participants')->default(1);
            $t->text('message')->nullable();
            $t->string('status')->default('baru');        // baru | dikonfirmasi | batal
            $t->text('note')->nullable();                 // catatan internal admin
            $t->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('registrations');
        Schema::dropIfExists('training_schedules');
        Schema::dropIfExists('trainings');
        Schema::dropIfExists('training_categories');
    }
};
