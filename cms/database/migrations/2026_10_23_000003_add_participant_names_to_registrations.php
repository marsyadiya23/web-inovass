<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    public function up(): void
    {
        Schema::table('registrations', function (Blueprint $t) {
            $t->text('participant_names')->nullable()->after('participants'); // nama peserta lain, satu per baris (untuk sertifikat)
        });
    }

    public function down(): void
    {
        Schema::table('registrations', function (Blueprint $t) {
            $t->dropColumn('participant_names');
        });
    }
};
