from fastapi import APIRouter
from src.database.workout import WorkoutDB


router = APIRouter(
    prefix="/api/v1/workouts",
    tags=['Workouts']
)

workout_db = WorkoutDB()

@router.get("/")
def get_all_workouts():
    workouts = workout_db.get_all_workouts()
    return workouts

@router.get("/{id}")
def get_workout(id: str):
    return {"message": f"Get workout {id}"}

@router.post("/")
def create_workout():
    return {"message": "Create a new workout"}

@router.patch("/{id}")
def update_workout(id: str):
    return {"message": f"Update workout {id}"}

@router.delete("/{id}")
def delete_workout(id: str):
    return {"message": f"Delete workout {id}"}
