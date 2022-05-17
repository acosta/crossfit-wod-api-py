from datetime import datetime
from typing import List, Optional
import uuid

from src.database.workout import WorkoutDB
from src.models.workout_models import Workout, WorkoutIn

class WorkoutService:
    def __init__(self) -> None:
        self.workout_db = WorkoutDB()

    def get_all_workouts(self) -> List[Workout]:
        all_workouts = []
        workouts = self.workout_db.get_all_workouts()

        for workout in workouts:
            all_workouts.append(Workout(**workout))

        return all_workouts

    def get_workout(self, id: str) -> Optional[Workout]:
        workouts = self.workout_db.get_all_workouts()

        for workout in workouts:
            if workout.get('id') == id:
                return Workout(**workout)

        return None

    def delete_workout(self, id: str) -> bool:
        workouts = self.workout_db.get_all_workouts()

        for index, workout in enumerate(workouts):
            if workout.get('id') == id:
                del workouts[index]
                return True

        return False

    def create_workout(self, workout: WorkoutIn) -> Optional[Workout]:
        id = uuid.uuid4()
        created_at = datetime.now().strftime("%d/%m/%y, %H:%M:%S %p")

        new_workout = Workout(id=str(id), name=workout.name, mode=workout.mode, equipment=workout.equipment, exercises=workout.exercises, createdAt=created_at, updatedAt=created_at, trainerTips=workout.trainerTips)
        if self.workout_db.create_workout(new_workout):
            return new_workout

        return None