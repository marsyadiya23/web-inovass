<?php

namespace App\Filament\Widgets;

use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\TrainingSchedules\TrainingScheduleResource;
use App\Models\Registration;
use App\Models\TrainingSchedule;
use Filament\Support\Icons\Heroicon;
use Filament\Widgets\StatsOverviewWidget;
use Filament\Widgets\StatsOverviewWidget\Stat;
use Illuminate\Support\Facades\DB;

class StatsOverview extends StatsOverviewWidget
{
    protected static ?int $sort = 1;

    protected function getStats(): array
    {
        $open = Registration::whereIn('status', Registration::OPEN)->count();
        $overdue = Registration::where('status', 'baru')->where('created_at', '<', now()->subDay())->count();
        $upcoming = TrainingSchedule::upcoming()->count();
        $schedulesThisMonth = TrainingSchedule::upcoming()->whereBetween('start_date', [today(), today()->endOfMonth()])->count();
        $month = today()->translatedFormat('F');
        $participants = (int) Registration::where('status', '!=', 'batal')
            ->whereBetween('created_at', [today()->startOfMonth(), now()])->sum('participants');
        // Peserta terkonfirmasi/lunas/selesai × harga efektif, untuk jadwal yang mulai bulan ini
        $revenue = (int) DB::table('registrations as r')
            ->join('training_schedules as s', 's.id', '=', 'r.training_schedule_id')
            ->join('trainings as t', 't.id', '=', 's.training_id')
            ->whereIn('r.status', ['dikonfirmasi', 'lunas', 'selesai'])
            ->whereBetween('s.start_date', [today()->startOfMonth()->toDateString(), today()->endOfMonth()->toDateString()])
            ->sum(DB::raw('r.participants * COALESCE(s.price, t.price, 0)'));

        return [
            Stat::make('Perlu ditindaklanjuti', $open)
                ->description($overdue ? $overdue.' belum dihubungi >24 jam' : ($open ? 'Baru, dihubungi, atau menunggu penawaran' : 'Semua sudah tertangani'))
                ->color($overdue ? 'danger' : ($open ? 'warning' : 'success'))
                ->icon(Heroicon::OutlinedBellAlert)
                ->url(RegistrationResource::getUrl('index', ['tab' => 'perlu'])),
            Stat::make('Jadwal mendatang', $upcoming)
                ->description($schedulesThisMonth.' jadwal bulan ini')
                ->icon(Heroicon::OutlinedCalendarDays)
                ->url(TrainingScheduleResource::getUrl()),
            Stat::make('Peserta mendaftar ('.$month.')', $participants)
                ->description('Tidak termasuk yang batal')
                ->icon(Heroicon::OutlinedUserGroup)
                ->url(RegistrationResource::getUrl('index', ['tab' => 'semua'])),
            Stat::make('Perkiraan pemasukan ('.$month.')', 'Rp '.number_format($revenue, 0, ',', '.'))
                ->description('Jadwal bulan ini, sudah dikonfirmasi')
                ->icon(Heroicon::OutlinedBanknotes),
        ];
    }
}
