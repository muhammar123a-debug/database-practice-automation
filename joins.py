import mysql.connector

connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$"
)

cursor = connect.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS practice")
cursor.execute("USE practice")
print("Database created")

# Delete old tables if exists
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS classes")

# Create tables
cursor.execute("""
CREATE TABLE classes(
    id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(50)
)
""")

cursor.execute("""
CREATE TABLE students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    class_id INT,
    FOREIGN KEY (class_id) REFERENCES classes(id)
)
""")
print("✅ Tables Created")

# Step 1: Insert classes first
cursor.executemany("INSERT INTO classes (class_name) VALUES (%s)", [
    ("Computer Science",),
    ("Mathematics",),
    ("Physics",)
])

# Step 2: Insert students (now class_id exists)
cursor.executemany("INSERT INTO students (name, class_id) VALUES (%s,%s)", [
    ("Ali", 1),
    ("Farooq", 2),
    ("Hasim", 3),
    ("Hina", None)  # None = NULL
])

connect.commit()
print("✅ Data Inserted")

# INNER JOIN
print("\n🔹 INNER JOIN Result:")
cursor.execute("""
SELECT students.name, classes.class_name
FROM students
INNER JOIN classes ON students.class_id = classes.id
""")
for row in cursor.fetchall():
    print(row)

cursor.close()
connect.close()
