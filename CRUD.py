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
connect.commit()
