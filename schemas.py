from pydantic import BaseModel
from datetime import date
from typing import List

class WorkoutSet(BaseModel):
    exercise_name: str
    weight_kg: float
    reps: int

class Workout(BaseModel):
    date: date
    sets: List[WorkoutSet]

class WorkoutSetOut(WorkoutSet):
    id: int

    class Config:
        from_attributes = True

class WorkoutOut(BaseModel):
    id: int
    date: date
    sets: List[WorkoutSetOut]

    class Config:
        from_attributes = True