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

@app.get("/programs")
def http_get_programs():
    programs = database.get_programs()
    return {"Programs": programs}

@app.post("/session/log/{program_id}/{user_id}/{day_number}")
def http_log_session(program_id: int, user_id: int, day_number: int):
    workout_id = database.log_session(program_id, user_id, day_number)
    return {"Workout logged": workout_id}

