from fastapi import FastAPI
from schemas import Workout

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет, это мой первый API"}

@app.post("/workouts")
def create_workout(workout: Workout):
    return {"received": workout}