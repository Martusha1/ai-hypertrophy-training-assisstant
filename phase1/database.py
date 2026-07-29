import sqlite3, json

def get_user_id(program_id):
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT user_id FROM program
    WHERE program_id = ?
""", (program_id,))
    
    user_id = cursor.fetchone()[0]
    
    conn.close()

    return user_id

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

    return cursor.lastrowid # gives back the ID that SQLite auto-generated after an INSERT

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

    return cursor.lastrowid # returns program_id

def get_programs():
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT program_id, program_name FROM program
""")
    
    all_programs = cursor.fetchall() # fetches multiple things
    conn.close()

    return all_programs # returns a list of all programs
    
def get_program_day(program_id):
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT raw_json from program
    WHERE program_id = ?
    """, (program_id,)) # , is needed because
    # execute expects 2nd arg to be a tuple or list
    
    rj = cursor.fetchone()[0] # because the result need to be
    # a tuple or list, we can also address which part of it we want
    conn.close()

    return json.loads(rj) # return raw json of program details for certain day

def log_session(program_id, user_id, day_number):
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO workout_sessions(program_id, user_id, day_number)
    VALUES (?,?,?)
""", (program_id, user_id, day_number))
    
    conn.commit()
    conn.close()

    return cursor.lastrowid # return workout_id

def save_set(workout_id, exercise_name, set_number, reps_done, weight_kg, rir):
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    weight_lbs = weight_kg * 2.20462

    cursor.execute("""
    INSERT INTO logged_sets (workout_id, exercise_name,
    set_number, reps_done, weight_kg, weight_lbs, rir)
    VALUES (?,?,?,?,?,?,?)
""",(workout_id, exercise_name, set_number, reps_done, weight_kg, weight_lbs, rir))
    
    conn.commit()
    conn.close()

    return cursor.lastrowid # return new set id

def check_progress(exercise_name):
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT workout_sessions.workout_id, logged_sets.exercise_name, logged_sets.set_number, logged_sets.reps_done, logged_sets.weight_kg, logged_sets.rir
    FROM logged_sets
    JOIN workout_sessions ON logged_sets.workout_id = workout_sessions.workout_id
    WHERE logged_sets.exercise_name = ?
    ORDER BY workout_sessions.session_date ASC
""", (exercise_name, ))
    
    sessions = cursor.fetchall() # returns a tuple of tuples
    
    ex_history = {}
    all_rir = []
    all_weights = []
    reps_per_set = []
    for w in sessions:
        if w[0] not in ex_history:
            ex_history[w[0]] = []
        ex_history[w[0]].append(w[2:6])
        all_rir.append(w[5])
        all_weights.append(w[4])
        reps_per_set.append(w[3])

    # ex_history dict approx. looks like this: {1:[(1,5,100,1)]}

    # conditions for trueness of progressive overload:
    # top set must improve, maintain or have more rir
    # no set can drop by more than 3 reps compared to the same set last session
    # big weight drops (over 20%) need low rir to count, otherwise it's junk volume
    
        


        



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