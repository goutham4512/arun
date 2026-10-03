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
cursor.execute("""
insert into students values(
   003,
  'goutham surendran kp',
   20,
  'MALE',
  9400698312,           
  'goutham.gmail.com',
  'english',
  'ilahia arts and science',
  'A',
  'BCA',
  2025-2029,
  'c,python,java',
  'tution centerl',
  'c,python,java',
  'beginner,beginner,beginner',
  'non'
  )
""")
# Save changes       
conn.commit()

# Close connection
conn.close()
 
print("Database created successfully!")