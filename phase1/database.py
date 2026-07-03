import sqlite3, json

def save_user(user):
    conn = sqlite3.connect("hypertrophy.db")
    # opens a connection to the database; if it doesn't exist,
    # SQLite creates it
    cursor = conn.cursor()
    # runs SQL statements through the connection

    cursor.execute("""
        INSERT INTO users (name, age, training_experience,
        training_days_per_week, session_length,
        available_equipment, goal) VALUES (?,?,?,?,?,?,?)
    """, (user["name"], user["age"], user["training experience"], user["training days per week"],
    user["session length"],user["available equipment"], user["goal"]))

    # sends SQL statements to DB through the cursor
    # but doesn't save anything, it just queues them up

    conn.commit()
    # saves everything you've inserted/updated/deleted until now
    conn.close()
    # closes the connection

    return cursor.lastrowid
# gives back the ID that SQLite auto-generated after an INSERT

def save_program(user_id, formatted_program):
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    raw_json = json.dumps(formatted_program)
    
    cursor.execute("""
        INSERT INTO program (user_id, program_name,
        weeks, raw_json) VALUES (?,?,?,?)
    """, (user_id, formatted_program["program_name"], formatted_program["weeks"], raw_json))

    conn.commit()
    conn.close()

    return cursor.lastrowid

def get_programs():
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT program_id, program_name FROM program
""")
    
    all_programs = cursor.fetchall()
    conn.close()

    return all_programs
    

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