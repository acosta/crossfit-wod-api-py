from typing import List

from src.database.workout import WorkoutDB
from src.models.workout_models import Workout

class WorkoutService:
    def __init__(self) -> None:
        self.workout_db = WorkoutDB()

    def get_all_workouts(self) -> List[Workout]:
        all_workouts = []
        workouts = self.workout_db.get_all_workouts()

        for workout in workouts:
            all_workouts.append(Workout(**workout))

        return all_workouts