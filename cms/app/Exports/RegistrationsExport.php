<?php

namespace App\Exports;

use App\Models\Registration;
use Illuminate\Database\Eloquent\Builder;
use OpenSpout\Common\Entity\Row;
use OpenSpout\Writer\XLSX\Writer;
use Symfony\Component\HttpFoundation\BinaryFileResponse;

/** Daftar pendaftar ke .xlsx (PRD US-05): tabel Pendaftar (ikut filter aktif) & aksi "Ekspor peserta" per jadwal. */
class RegistrationsExport
{
    public const HEADINGS = [
        'Tanggal daftar', 'Nama', 'Instansi', 'Jabatan', 'WhatsApp', 'Email', 'Jumlah peserta', 'Status',
        'Program', 'Tanggal pelatihan', 'Metode', 'Lokasi', 'Pesan pendaftar', 'Catatan internal',
    ];

    /** @return list<list<string|int|null>> */
    public static function rows(Builder $query): array
    {
        // ponytail: get() sekaligus; cukup untuk ribuan baris. Pakai lazy() bila sampai puluhan ribu.
        return $query->with('schedule.training')->get()->map(fn (Registration $r) => [
            $r->created_at?->format('Y-m-d H:i'),
            $r->name,
            $r->organization,
            $r->position,
            $r->phone,
            $r->email,
            $r->participants,
            Registration::STATUSES[$r->status] ?? $r->status,
            $r->schedule?->training?->title,
            $r->schedule?->dateLabel(),
            $r->schedule?->methodLabel(),
            $r->schedule?->location,
            $r->message,
            $r->note,
        ])->all();
    }

    public static function download(Builder $query, string $filename): BinaryFileResponse
    {
        $path = tempnam(sys_get_temp_dir(), 'xlsx');
        $writer = new Writer;
        $writer->openToFile($path);
        $writer->addRow(Row::fromValues(self::HEADINGS));
        foreach (self::rows($query) as $row) {
            $writer->addRow(Row::fromValues($row));
        }
        $writer->close();

        return response()->download($path, $filename)->deleteFileAfterSend();
    }
}
