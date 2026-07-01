import sqlite3

def init_db():
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER NOT NULL,
        training_experience TEXT,
        training_days_per_week INTEGER NOT NULL,
        session_length INTEGER NOT NULL,
        available_equipment TEXT,
        goal TEXT,
        created_at DATE          
        );
 """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS program (
        program_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        program_name TEXT,
        weeks INTEGER NOT NULL,
        raw_json TEXT,
        created_at DATE,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_sessions (
        workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
        program_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        session_date DATE,
        day_number INTEGER NOT NULL,
        notes TEXT,
        FOREIGN KEY (program_id) REFERENCES program(program_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logged_sets (
        sets_id INTEGER PRIMARY KEY AUTOINCREMENT,
        workout_id INTEGER NOT NULL,
        exercise_name TEXT,
        set_number INTEGER,
        reps_done INTEGER,
        weight_kg REAL,
        weight_lbs REAL,
        rir INTEGER,
        FOREIGN KEY (workout_id) REFERENCES workout_sessions(workout_id)
        );
""")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()