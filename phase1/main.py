from fastapi import FastAPI
from phase1 import database

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hypertrophy API running"}

@app.get("/progress/{exercise_name}")
def get_progress(exercise_name: str):
    result = database.check_progress(exercise_name)
    return {"Result": result}