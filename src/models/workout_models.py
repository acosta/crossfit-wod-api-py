from datetime import datetime
from pydantic import BaseModel
from typing import List

class Workout(BaseModel):
    id: str
    name: str
    mode: str
    equipment: List[str] = []
    exercises: List[str] = []
    createdAt: str
    updatedAt: str
    trainer_tips: List[str] = []
