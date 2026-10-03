import sqlite3
 
# Create/connect to database
conn = sqlite3.connect("tution.db")
 
# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT,
        dob TEXT,
        age INTEGER,
        gender TEXT,
        mobile_number INTEGER,
        email_address TEXT,
        password TEXT,
        preferred_language TEXT,
        school_college_name TEXT,
        class_grade TEXT,
        borad_curriculum TEXT,
        academic_year INTEGER,
        subjects_for_tution TEXT,
        current_level_per_subject TEXT,
        area_topics_needing_help TEXT
    )
""")


# Save changes       
conn.commit()

# Close connection
conn.close()
 
print("Database created successfully!")