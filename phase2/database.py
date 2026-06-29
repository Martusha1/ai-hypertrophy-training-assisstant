import sqlite3

def init_db():
    conn = sqlite3.connect("hypertrophy.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age int,
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
        user_id int NOT NULL,
        program_name TEXT,
        weeks int NOT NULL,
        raw_json TEXT,
        created_at DATE,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
        );
""")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()