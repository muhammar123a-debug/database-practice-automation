import mysql.connector


connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$",
    database="practice"
)

cursor = connect.cursor()
cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute(
    """CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE)"""
    )
print("Employees table created")

sql = "INSERT INTO Employees (name, department, salary, hire_date) VALUES (%s, %s, %s, %s)"
values = [
    ("Ayesha Ahmed", "HR", 60000.00, "2025-08-01"),
    ("Bilal Shah", "Finance", 75000.00, "2025-07-15"),
    ("Sara Malik", "Marketing", 55000.00, "2025-06-20")
]

cursor.executemany(sql, values)   # ✅ multiple rows insert
connect.commit()

print("✅", cursor.rowcount, "records inserted")


