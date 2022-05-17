from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/workouts",
    tags=['Workouts']
)

@router.get("/")
def get_all_workouts():
    return {"message": "Get all workouts"}

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
