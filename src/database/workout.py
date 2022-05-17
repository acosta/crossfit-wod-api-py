import json
import os

from src.models.workout_models import Workout

class WorkoutDB:
    def __init__(self) -> None:
        self.data = None
        self.load_file()

    def load_file(self) -> None:
        json_file_path = os.path.join(os.path.dirname(__file__), "workout_db.json")
        f = open(json_file_path)
        self.data = json.load(f)
        f.close()

    def get_all_workouts(self) -> list:
        return self.data["workouts"] if self.data is not None else []

    def create_workout(self, new_workout: Workout) -> bool:
        if self.data is not None:
            self.data["workouts"].append(new_workout.dict())
            return True

        return False

    def delete_workout(self, id: str) -> bool:
        if self.data:
            for index, workout in enumerate(self.data.get("workouts", [])):
                if workout.get('id') == id:
                    del self.data.get("workouts")[index]
                    return True

        return False
