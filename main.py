from fastapi import FastAPI

from src.controllers import workout_controller

app = FastAPI()

@app.get("/")
def root():
    return {"message": "It's working!"}

app.include_router(workout_controller.router)