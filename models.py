from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class WorkoutDB(Base):
    __tablename__= "workouts"


    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)


    sets = relationship("WorkoutSetDB", back_populates="workout")



class WorkoutSetDB(Base):
    __tablename__ = "workout_sets"

    id = Column(Integer, primary_key=True, index=True)
    exercise_name = Column(String)
    weight_kg = Column(Float)
    reps = Column(Integer)
    workout_id = Column(Integer, ForeignKey("workouts.id"))

    workout = relationship("WorkoutDB", back_populates="sets")