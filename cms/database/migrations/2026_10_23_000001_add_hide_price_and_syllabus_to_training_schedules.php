<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('training_schedules', function (Blueprint $t) {
            $t->boolean('hide_price')->default(false)->after('price'); // true = website tampil "Hubungi kami"
            $t->string('syllabus')->nullable()->after('note');         // PDF/gambar; kosong = brosur program
        });
    }

    public function down(): void
    {
        Schema::table('training_schedules', function (Blueprint $t) {
            $t->dropColumn(['hide_price', 'syllabus']);
        });
    }
};
