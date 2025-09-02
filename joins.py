import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ammar@#$",
    database = "practice"
)

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS courses")

cursor.execute("CREATE TABLE IF NOT EXISTS students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),city VARCHAR(50),course_id INT)")
cursor.execute("CREATE TABLE IF NOT EXISTS courses(id INT PRIMARY KEY,course_name VARCHAR(50),teacher VARCHAR(50))")

cursor.execute("""
INSERT INTO students (name, city, course_id) VALUES 
('Ali', 'Karachi', 101),
('Sara', 'Lahore', 102),
('Ahmed', 'Islamabad', NULL),
('Fatima', 'Karachi', NULL),
('Bilal', 'Lahore', 101),
('Ayesha', 'Multan', 104),
('Hamza', 'Karachi', NULL),
('Noor', 'Islamabad', 105)
""")

cursor.execute("""
INSERT INTO courses (id, course_name, teacher) VALUES
(101, 'Database', 'Sir Ali'),
(102, 'Python', 'Miss Sara'),
(103, 'Data Science', 'Sir Ahmed'),
(104, 'AI', 'Dr. Fatima'),
(106, 'Cyber Security', 'Sir Zain');
""")

cursor.execute("""SELECT s.name, c.course_name FROM students s INNER JOIN courses c ON s.course_id = c.id;""")
for i in cursor.fetchall():
    print(i)
cursor.execute("""
SELECT s.name, c.course_name, c.teacher
FROM students s
INNER JOIN courses c
ON  s.course_id = c.id;
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("""
SELECT s.name, c.course_name, s.city
FROM students s
INNER JOIN courses c ON s.course_id = c.id
WHERE s.city = 'Lahore';
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("""
SELECT s.name, c.course_name
FROM students s
INNER JOIN courses c ON s.course_id = c.id;
""")
for i in cursor.fetchall():
    print(i)

cursor.execute("""
SELECT c.course_name, COUNT(s.id) AS total_students
FROM students s
INNER JOIN courses c ON s.course_id = c.id
GROUP BY c.course_name;
""")
for i in cursor.fetchall():
    print(i)

print("\n Har student ka naam aur course (agar hai):")
cursor.execute("""
SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id;
""")
for i in cursor.fetchall():
    print(i)

print("\n Jo students ke paas course nahi hai:")
cursor.execute("""
SELECT s.name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id
WHERE c.id IS NULL;
""")
for i in cursor.fetchall():
    print(i)

print("\n Karachi ke students ke saath course:")
cursor.execute("""
SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id
WHERE s.city = 'Karachi';
""")
for i in cursor.fetchall():
    print(i)

print("\n Students + teacher (agar course linked hai):")
cursor.execute("""
SELECT s.name, c.teacher
FROM students s
LEFT JOIN courses c ON s.course_id = c.id;
""")
for i in cursor.fetchall():
    print(i)

print("\n Har student aur unke course ka naam sort by student:")
cursor.execute("""
SELECT s.name, c.course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.id
ORDER BY s.name ASC;
""")
for i in cursor.fetchall():
    print(i)

conn.commit()
