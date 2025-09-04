import mysql.connector

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ammar@#$",
    database = "practice"
)
cursor = connect.cursor()
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
phone VARCHAR(20),
city VARCHAR(50)
)
""")

cursor.execute("INSERT INTO customers (name, email) VALUES (%s, %s)",("Ammar Anwer","ammar@gmail.com"))
cursor.execute("INSERT INTO customers (name, email) VALUES ('Anas','anas@gmail.com'),('danish','danish@gmail.com'),('Rahima','rahima@gmail.com')")
cursor.execute("INSERT INTO customers (name, email, phone, city) VALUES ('Farhan','farhan@gmail.com','03224387654','Karachi')")
cursor.execute("INSERT INTO customers (name, email, city) VALUES ('Faris','faris@gamail.com','Lahore')")
rows = [
    ("Imran malik", "imran@gmail.com","03202689355","Faislabad"),
    ("Irfan ", "irfan@gmail.com",None,"karachi"),
    ("Qasim Khan", "qasimkhan@gmail.com","03221234567","Peshawer")
]
cursor.executemany("INSERT INTO customers (name, email, phone, city) VALUES (%s,%s,%s,%s)",rows)

#SELECT queries
print("\n Acsess All Data from customers TABLE")
cursor.execute("SELECT * FROM customers")
for i in cursor.fetchall():
    print(i)

print("\n Select only specific columns (name, city)")
cursor.execute("SELECT name, city FROM customers")
for i in cursor.fetchall():
    print(i)

print("\n Select with WHERE condition (city = 'Karachi')")
cursor.execute("SELECT * FROM customers WHERE city = 'Karachi'")
for i in cursor.fetchall():
    print(i)

print("\n Order results by name ASC/DESC + LIMIT (top 5 customers)")
cursor.execute("SELECT * FROM customers ORDER BY name ASC LIMIT 5")
for i in cursor.fetchall():
    print(i)
print("\n Order results by name DESC")
cursor.execute("SELECT * FROM customers ORDER BY name DESC LIMIT 3")
for i in cursor.fetchall():
    print(i)

print("Update a single customers city")
cursor.execute("UPDATE customers SET city = 'Karachi' WHERE id = 5")
print("Update multiple fields at once (email + phone)")
cursor.execute("UPDATE customers SET email = 'muhammar@gmail.com', phone = '03009998888' WHERE id = 2;")
print("Update rows with condition (Karachi → Lahore)")
cursor.execute("UPDATE customers SET city = 'Lahore' WHERE city = 'Karachi'")
print("Update multiple rows at once (name LIKE 'A%' → city = 'Islamabad')")
cursor.execute("UPDATE customers SET city = 'Islamabad' WHERE name LIKE 'A%'")
print("Update using Python script (row selection with input)")
id = int(input("Enter customer ID to update: "))
new_city = input("Enter new city:")
cursor.execute("UPDATE customers SET city = %s WHERE id = %s", (new_city, id))
cursor.execute("SELECT * FROM customers")
for i in cursor.fetchall():
    print(i)

connect.commit()
