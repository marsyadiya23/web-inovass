<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

// Silabus cukup per program (trainings.brochure), bukan per jadwal.
return new class extends Migration
{
    public function up(): void
    {
        Schema::table('training_schedules', function (Blueprint $t) {
            $t->dropColumn('syllabus');
        });
    }

    public function down(): void
    {
        Schema::table('training_schedules', function (Blueprint $t) {
            $t->string('syllabus')->nullable()->after('note');
        });
    }
};
