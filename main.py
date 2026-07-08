from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import Workout, WorkoutOut
from database import SessionLocal
import database
import models

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Привет, это мой первый API"}

@app.post("/workouts")
def create_workout(workout: Workout, db: Session = Depends(get_db)):
    db_workout = models.WorkoutDB(date=workout.date)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)

    for s in workout.sets:
        db_set = models.WorkoutSetDB(
            exercise_name=s.exercise_name,
            weight_kg=s.weight_kg,
            reps=s.reps,
            workout_id=db_workout.id
        )
        db.add(db_set)
    db.commit()

    return {"id": db_workout.id, "message": "Тренировка сохранена"}

@app.get("/workouts", response_model=list[WorkoutOut])
def get_workouts(db: Session = Depends(get_db)):
    return db.query(models.WorkoutDB).all()