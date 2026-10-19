<?php

namespace App\Filament\Resources\Trainings\RelationManagers;

use App\Filament\Resources\TrainingSchedules\Schemas\TrainingScheduleForm;
use App\Filament\Resources\TrainingSchedules\Tables\TrainingSchedulesTable;
use Filament\Actions\CreateAction;
use Filament\Resources\RelationManagers\RelationManager;
use Filament\Schemas\Schema;
use Filament\Tables\Table;

class SchedulesRelationManager extends RelationManager
{
    protected static string $relationship = 'schedules';

    protected static ?string $title = 'Jadwal';

    protected static ?string $modelLabel = 'Jadwal';

    public function form(Schema $schema): Schema
    {
        return $schema->components(TrainingScheduleForm::fields(withTraining: false));
    }

    public function table(Table $table): Table
    {
        return TrainingSchedulesTable::base($table, withTraining: false)
            ->defaultSort('start_date', 'desc')
            ->headerActions([CreateAction::make()->label('Tambah jadwal')]);
    }
}
