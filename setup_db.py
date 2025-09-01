import sqlite3
# help(sqlite3)
# connect to the database

conn = sqlite3.connect('rrtables.db')
cursor = conn.cursor()

# Table 1: Users (for punch-in/punch-out and privileges)
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('admin', 'tenant')),
    punch_in_time DATETIME,
    punch_out_time DATETIME,
    total_hours_worked REAL,
    date DATE
)
''')

# Table 2: Inventory (for production items)
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_name TEXT NOT NULL,
    lot_number TEXT NOT NULL UNIQUE,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity >= 0)
)
''')

# Table 3: Shopify Orders (for synced orders)
cursor.execute('''
CREATE TABLE IF NOT EXISTS shopify_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_location TEXT NOT NULL,
    order_date DATETIME NOT NULL,
    fulfillment_status TEXT NOT NULL CHECK(fulfillment_status IN ('fulfilled', 'pending')),
    payment_status TEXT NOT NULL CHECK(payment_status IN ('paid', 'unpaid')),
    total_amount REAL NOT NULL
)
''')

# Table 4: Picking List (for order fulfillment)
cursor.execute('''
CREATE TABLE IF NOT EXISTS picking_list (
    picking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    item_name TEXT NOT NULL,
    quantity_ordered INTEGER NOT NULL CHECK(quantity_ordered >= 0),
    location TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES shopify_orders(order_id),
    FOREIGN KEY (item_id) REFERENCES inventory(item_id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")