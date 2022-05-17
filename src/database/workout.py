import json
import os

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
        return self.data["workouts"]
