<?php

namespace App\Filament\Widgets;

use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\Trainings\TrainingResource;
use App\Filament\Resources\TrainingSchedules\TrainingScheduleResource;
use App\Models\Registration;
use App\Models\Training;
use App\Models\TrainingSchedule;
use Filament\Support\Icons\Heroicon;
use Filament\Widgets\StatsOverviewWidget;
use Filament\Widgets\StatsOverviewWidget\Stat;

class StatsOverview extends StatsOverviewWidget
{
    protected static ?int $sort = 1;

    protected function getStats(): array
    {
        $upcoming = TrainingSchedule::upcoming()->count();
        $thisMonth = TrainingSchedule::upcoming()->whereBetween('start_date', [today(), today()->endOfMonth()])->count();
        $newRegs = Registration::where('status', 'baru')->count();

        return [
            Stat::make('Jadwal mendatang', $upcoming)
                ->description($thisMonth.' jadwal bulan ini')
                ->icon(Heroicon::OutlinedCalendarDays)
                ->url(TrainingScheduleResource::getUrl()),
            Stat::make('Pendaftar baru', $newRegs)
                ->description($newRegs ? 'Perlu dikonfirmasi' : 'Semua sudah diproses')
                ->color($newRegs ? 'warning' : 'success')
                ->icon(Heroicon::OutlinedUserPlus)
                ->url(RegistrationResource::getUrl()),
            Stat::make('Program pelatihan aktif', Training::where('is_published', true)->count())
                ->icon(Heroicon::OutlinedAcademicCap)
                ->url(TrainingResource::getUrl()),
        ];
    }
}
