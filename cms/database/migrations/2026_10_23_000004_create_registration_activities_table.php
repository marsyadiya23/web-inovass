<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        // Riwayat per pendaftaran: daftar, perubahan tahap, catatan. user_id kosong = pendaftar/sistem.
        Schema::create('registration_activities', function (Blueprint $t) {
            $t->id();
            $t->foreignId('registration_id')->constrained()->cascadeOnDelete();
            $t->foreignId('user_id')->nullable()->constrained()->nullOnDelete();
            $t->string('description');
            $t->timestamps();
        });
    }

    public function down(): void
    {
        Schema::dropIfExists('registration_activities');
    }
};
