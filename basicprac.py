import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$",
    database="practice"
)

cursor = con.cursor()

cursor.execute("DROP TABLE IF EXISTS student")

# Table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50),
    marks INT
)
""")
print("✅ Student table created")

# Data insert
students_data = [
    ("Ali", 18, "Karachi", 85),
    ("Sara", 20, "Lahore", 92),
    ("Ahmed", 19, "Islamabad", 76),
    ("Fatima", 22, "Karachi", 88),
    ("Bilal", 21, "Lahore", 67),
    ("Ayesha", 23, "Multan", 95),
    ("Hamza", 20, "Karachi", 72),
    ("Zain", 18, "Lahore", 81),
    ("Noor", 19, "Islamabad", 90),
    ("Usman", 22, "Karachi", 60),
]

cursor.executemany("INSERT INTO student(name, age, city, marks) VALUES (%s, %s, %s, %s)", students_data)
con.commit()
print("✅ Data inserted successfully")

print("\n Query 1: Marks > 80")
cursor.execute("SELECT name, city, marks FROM student WHERE marks > 80")
for i in cursor.fetchall():
    print(i)

print("\n Query 2: Lahore students")
cursor.execute("SELECT * FROM student WHERE city = 'Lahore';")
for row in cursor.fetchall():
    print(row)

print("\n Query 3: Karachi students marks DESC")
cursor.execute("SELECT name, city, marks FROM student WHERE city = 'Karachi' ORDER BY marks DESC;")
for i in cursor.fetchall():
    print(i)

print("\n Query 4: Top 3 students")
cursor.execute("SELECT name, marks ,city FROM student ORDER BY marks DESC LIMIT 3;")
for i in cursor.fetchall():
    print(i)

print("\n Query 5: Youngest 2 students")
cursor.execute("SELECT name, age, city, marks FROM student ORDER BY age ASC LIMIT 2;")
for i in cursor.fetchall():
    print(i)

print("\n Query 6: Marks between 60 and 85")
cursor.execute("SELECT name, age, city, marks FROM student WHERE marks BETWEEN 60 AND 85 ORDER BY marks ASC;")
for i in cursor.fetchall():
    print(i)

print("\n Query 7: Age > 20 students")
cursor.execute("SELECT name, age, city, marks FROM student WHERE age > 20;")
for i in cursor.fetchall():
    print(i)

print("\n Query 8: Lahore students alphabetical")
cursor.execute("SELECT name, age, city, marks FROM student WHERE city = 'Lahore' ORDER BY name ASC;")
for i in cursor.fetchall():
    print(i)

print("\n Query 9: Lowest marks in Karachi")
cursor.execute("SELECT name, age, city, marks FROM student WHERE city = 'Karachi' ORDER BY marks ASC LIMIT 1;")
for i in cursor.fetchall():
    print(i)

cursor.close()
con.close()
