import mysql.connector

con = mysql.connector.connect(
    host = "loclahost",
    user = "root",
    password = "Ammar@#$",
    database = "practice"
)

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT, city VARCHAR(50),marks INT")
print("Create Student table")

students_data = [
    (1, "Ali", 18, "Karachi", 85),
    (2, "Sara", 20, "Lahore", 92),
    (3, "Ahmed", 19, "Islamabad", 76),
    (4, "Fatima", 22, "Karachi", 88),
    (5, "Bilal", 21, "Lahore", 67),
    (6, "Ayesha", 23, "Multan", 95),
    (7, "Hamza", 20, "Karachi", 72),
    (8, "Zain", 18, "Lahore", 81),
    (9, "Noor", 19, "Islamabad", 90),
    (10, "Usman", 22, "Karachi", 60),
]