import mysql.connector

connect = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ammar@#$",
    database = "practice"
)

cursor = connect.cursor()
#DROP TABLE IF EXISTS IN DATABASE
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS customers")

# --- Create customers table ---
cursor.execute("""
CREATE TABLE customers(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(50)
)
""")

# --- Create products table ---
cursor.execute("""
CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL            
)
""")

# --- Create orders table ---
cursor.execute("""
CREATE TABLE orders(
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")


# --- Insert customers ---
cursor.executemany("""
INSERT INTO customers (name, email, phone, city)
VALUES (%s, %s, %s, %s)
""", [
    ("Ammar Anwer", "ammar@gmail.com", "0322000001", "Karachi"),
    ("Anas", "anas@gmail.com", "0322000002", "Lahore"),
    ("Danish", "danish@gmail.com", "0322000003", "Islamabad"),
    ("Rahima", "rahima@gmail.com", None, "Karachi"),
    ("Farhan", "farhan@gmail.com", "0322000004", "Faisalabad"),
    ("Faris", "faris@gmail.com", None, "Lahore")
])

# --- Insert products ---
cursor.executemany("""
INSERT INTO products (product_name, price)
VALUES (%s, %s)
""", [
    ("Laptop", 80000),
    ("Mobile", 40000),
    ("Tablet", 25000),
    ("Headphones", 5000),
    ("Smartwatch", 15000)
])

# --- Insert orders ---
cursor.executemany("""
INSERT INTO orders (customer_id, product_id, order_date, quantity)
VALUES (%s, %s, %s, %s)
""", [
    (1, 1, "2025-09-01", 1),   
    (2, 2, "2025-09-02", 2),   
    (3, 3, "2025-09-03", 1),   
    (1, 4, "2025-09-03", 3),   
    (5, 5, "2025-09-04", 1),   
    (6, 2, "2025-09-04", 1)    
])



print("Tables created successfully.")

connect.commit()
