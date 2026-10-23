<?php

namespace App\Filament\Widgets;

use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\TrainingSchedules\TrainingScheduleResource;
use App\Models\Registration;
use App\Models\TrainingSchedule;
use Filament\Widgets\Widget;

/** Dasbor: daftar hal yang perlu dikerjakan admin hari ini, masing-masing dengan tautan langsung. */
class ActionItems extends Widget
{
    protected static ?int $sort = 0;

    protected static bool $isLazy = false; // bagian terpenting dasbor: tampil langsung, tidak menunggu dimuat

    protected int|string|array $columnSpan = 'full';

    protected string $view = 'filament.widgets.action-items';

    protected function getViewData(): array
    {
        return ['items' => self::items()];
    }

    /** @return list<array{0: 'danger'|'warning'|'gray', 1: string, 2: string}> [warna, teks, url] */
    public static function items(): array
    {
        $items = [];
        $regs = fn (string $tab) => RegistrationResource::getUrl('index', ['tab' => $tab]);
        $edit = fn (TrainingSchedule $s) => TrainingScheduleResource::getUrl('edit', ['record' => $s]);
        $name = fn (TrainingSchedule $s) => $s->training->title.' ('.$s->dateLabel().')';
        $past = fn ($q) => $q->whereRaw('COALESCE(end_date, start_date) < ?', [today()->toDateString()]);

        if ($n = Registration::where('status', 'baru')->where('created_at', '<', now()->subDay())->count()) {
            $items[] = ['danger', $n.' pendaftaran baru belum dihubungi lebih dari 24 jam', $regs('baru')];
        }

        foreach (TrainingSchedule::with('training')->upcoming()->where('status', 'dibuka')->get() as $s) {
            $left = $s->seatsLeft();
            if ($left !== null && $left > 0 && $left <= max(2, (int) ceil($s->quota * 0.2))) {
                $items[] = ['warning', $name($s).': sisa '.$left.' kursi', $edit($s)];
            }
            $deadline = $s->registration_deadline ?? $s->start_date;
            $days = (int) today()->diffInDays($deadline, false);
            if ($s->isOpen() && $days <= 3) {
                $items[] = ['warning', $name($s).': batas daftar '.match ($days) { 0 => 'hari ini', 1 => 'besok', default => $days.' hari lagi' }, $edit($s)];
            }
        }

        $soon = fn ($q) => $q->whereBetween('start_date', [today()->toDateString(), today()->addDays(7)->toDateString()]);
        if ($n = Registration::where('status', 'dikonfirmasi')->whereHas('schedule', $soon)->count()) {
            $items[] = ['warning', $n.' pendaftaran dikonfirmasi belum lunas, pelatihannya ≤ 7 hari lagi', $regs('dikonfirmasi')];
        }

        foreach (TrainingSchedule::with('training')->where('status', 'dibuka')->where($past)->get() as $s) {
            $items[] = ['gray', $name($s).': sudah lewat tetapi statusnya masih Dibuka', $edit($s)];
        }

        if ($n = Registration::whereIn('status', ['dikonfirmasi', 'lunas'])->whereHas('schedule', $past)->count()) {
            $items[] = ['gray', $n.' pendaftaran dari pelatihan yang sudah lewat belum ditandai Selesai', $regs('semua')];
        }

        return $items;
    }
}
