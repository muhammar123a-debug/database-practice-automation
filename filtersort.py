import mysql.connector
connect = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$",
    database="practice"
)

cursor = connect.cursor()

#drop old table if exists
cursor.execute("DROP TABLE IF EXISTS employees")

#create table
cursor.execute("CREATE TABLE employees(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50) NOT NULL,department VARCHAR(50) NOT NULL,salary DECIMAL(10,2), hire_date DATE)")
print("Employee table created")

#insert sample data
employee_data =[
    ("Ammar", "IT", 60000, "2023-01-15"),
    ("Ali", "HR", 45000, "2022-12-01"),
    ("Sara", "Finance", 75000, "2023-03-10"),
    ("Zain", "IT", 50000, "2023-06-21"),
    ("Hina", "Finance", 82000, "2022-11-05"),
    ("Bilal", "HR", 40000, "2023-04-17"),
    ("Usman", "IT", 95000, "2021-09-30")
]

cursor.executemany("INSERT INTO employees (name, department, salary, hire_date) VALUES (%s,%s,%s,%s)", employee_data)
connect.commit()
print("Sample data inserted")


# -------------Filtering---------
print("\n Employees in IT Department")
cursor.execute("SELECT * FROM employees WHERE department = 'IT'")
for i in cursor.fetchall():
    print(i)

print("\n Employees with salary > 50000")
cursor.execute("SELECT * FROM employees WHERE salary > 50000")
for i in cursor.fetchall():
    print(i)

print("\n Employees hired between 2022-12-01 and 2023-06-30:")
cursor.execute("SELECT * FROM employees WHERE hire_date BETWEEN '2022-12-01' AND '2023-06-30'")
for i in cursor.fetchall():
    print(i)

print("\n Employees who names starts with 'A':")
cursor.execute("SELECT * FROM employees WHERE name LIKE 'A%'")
for i in cursor.fetchall():
    print(i)

# -----------------SORTING-----------------
print("\n Employees Sort by salary (DSEC)")
cursor.execute("SELECT * FROM employees ORDER BY salary DESC")
for i in cursor.fetchall():
    print(i)

print("\n Employees Sorted by hire_date (ASC)")
cursor.execute("SELECT * FROM employees ORDER BY hire_date ASC")
for i in cursor.fetchall():
    print(i)

# --------------Aggregation ------------

print("\n Total number of Employees")
cursor.execute("SELECT COUNT(*) FROM employees")
print(cursor.fetchone()[0])

print("\n Average Salary of Employees")
cursor.execute("SELECT AVG(salary) FROM employees")
print(cursor.fetchone()[0])

print("\n MAX salary in IT department")
cursor.execute("SELECT MAX(salary) FROM employees WHERE department = 'IT'")
print(cursor.fetchone()[0])

print("\n Salary Sum per department (GROUP BY)")
cursor.execute("SELECT department, SUM(salary) FROM employees GROUP BY department")
for i in cursor.fetchall():
    print(i)

print("\n Salary AVG per departemt:")
cursor.execute("SELECT department, AVG(salary) FROM employees GROUP BY department")
for i in cursor.fetchall():
    print(i)

cursor.close()
connect.close()