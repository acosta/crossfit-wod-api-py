from fastapi import APIRouter
from typing import List

from src.models.workout_models import Workout
from src.services.workout_service import WorkoutService

router = APIRouter(
    prefix="/api/v1/workouts",
    tags=['Workouts']
)

workout_service = WorkoutService()

@router.get("/", response_model=List[Workout])
def get_all_workouts():
    return workout_service.get_all_workouts()

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
