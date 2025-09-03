import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ammar@#$",
)

cursor = conn.cursor()

cursor.execute("DROP DATABASE the_mart;")

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS the_mart")
cursor.execute("USE the_mart")


# Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(50),
    city VARCHAR(50)
)
""")

# Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL
)
""")

# Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Pending','Shipped','Delivered','Cancelled') DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
""")

# Order Items Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")
cursor.execute("INSERT INTO customers (name, email, phone, city) VALUES ('Ammar','ammar@gmail.com','03202595322','canada'),('Anas','anas@gmail.com','03221254664','karachi'),('Asim','asim@gmail.com','03220032030','Lahore')")
cursor.execute("SELECT * FROM customers")
for i in cursor.fetchall():
    print(i)

cursor.execute("INSERT INTO products (product_name, price, stock) VALUES ('Laptop', 120000, 10),('Mobile', 45000, 20),('Headphones', 3000, 50),('Keyboard', 1500, 30);")
cursor.execute("SELECT * FROM products")
for i in cursor.fetchall():
    print(i)

cursor.execute("INSERT INTO orders (customer_id, status) VALUES (1, 'Pending'),(2, 'Shipped'),(3,'Delivered')")
cursor.execute("SELECT * FROM orders")
for i in cursor.fetchall():
    print(i)
    
cursor.execute("INSERT INTO order_items (order_id,product_id, quantity,price) VALUES (1,1,1, 120000),(1,3,2, 6000)")
cursor.execute("SELECT * FROM order_items")
for i in cursor.fetchall():
    print(i)

conn.commit()

print("Sample customers & products added ✅")
