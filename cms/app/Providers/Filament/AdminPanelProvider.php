<?php

namespace App\Providers\Filament;

use App\Filament\Pages\SiteSettings;
use App\Filament\Resources\Registrations\RegistrationResource;
use App\Filament\Resources\TrainingCategories\TrainingCategoryResource;
use App\Filament\Resources\Trainings\TrainingResource;
use App\Filament\Resources\TrainingSchedules\TrainingScheduleResource;
use App\Filament\Resources\Users\UserResource;
use Filament\Http\Middleware\Authenticate;
use Filament\Http\Middleware\AuthenticateSession;
use Filament\Http\Middleware\DisableBladeIconComponents;
use Filament\Http\Middleware\DispatchServingFilamentEvent;
use Filament\Pages\Dashboard;
use Filament\Navigation\NavigationGroup;
use Filament\Panel;
use Filament\PanelProvider;
use Filament\Support\Colors\Color;
use Filament\Widgets\AccountWidget;
use Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse;
use Illuminate\Cookie\Middleware\EncryptCookies;
use Illuminate\Foundation\Http\Middleware\PreventRequestForgery;
use Illuminate\Routing\Middleware\SubstituteBindings;
use Illuminate\Session\Middleware\StartSession;
use Illuminate\View\Middleware\ShareErrorsFromSession;

class AdminPanelProvider extends PanelProvider
{
    public function panel(Panel $panel): Panel
    {
        return $panel
            ->default()
            ->id('admin')
            ->path('admin')
            ->login()
            ->profile() // ganti nama/email/password admin; jangan pakai db:seed untuk ini (seed menimpa pengaturan)
            ->brandName('INOVASS CMS')
            ->brandLogo(asset('assets/img/logo.png'))
            ->brandLogoHeight('2.25rem')
            ->colors([
                'primary' => Color::hex('#00c278'),
                'gray' => Color::Slate,
            ])
            ->navigationGroups([
                NavigationGroup::make('Pelatihan'),
                NavigationGroup::make('Kotak Masuk'),
                NavigationGroup::make('Pengaturan')->collapsed(),
            ])
            ->sidebarCollapsibleOnDesktop()
            // ponytail: admin hanya untuk jadwal & pendaftaran. Resource/Page konten compro
            // (Beranda, Layanan, Berita, Pesan Masuk, dst.) masih ada di app/Filament tapi tidak didaftarkan.
            ->resources([
                TrainingScheduleResource::class,
                TrainingResource::class,
                TrainingCategoryResource::class,
                RegistrationResource::class,
                UserResource::class,
            ])
            ->pages([
                Dashboard::class,
                SiteSettings::class, // nomor WhatsApp untuk konfirmasi pendaftaran
            ])
            ->discoverWidgets(in: app_path('Filament/Widgets'), for: 'App\Filament\Widgets')
            ->widgets([
                AccountWidget::class,
            ])
            ->middleware([
                EncryptCookies::class,
                AddQueuedCookiesToResponse::class,
                StartSession::class,
                AuthenticateSession::class,
                ShareErrorsFromSession::class,
                PreventRequestForgery::class,
                SubstituteBindings::class,
                DisableBladeIconComponents::class,
                DispatchServingFilamentEvent::class,
            ])
            ->authMiddleware([
                Authenticate::class,
            ]);
    }
}
