# Import the sqlite3 module to work with SQLite databases.
import sqlite3

# Connect to or create a SQLite database file named 'car_prices.db'.
conn = sqlite3.connect('car_prices.db')

# Create a cursor object to interact with the database.
cursor = conn.cursor()

# Create a table named 'cars' in the database to store car-related data.
cursor.execute('''
    CREATE TABLE cars (
        id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        price INTEGER
    )
''')

# Define dummy data for cars, including make, model, and price.
dummy_data = [
    ('Swift', 'Dzire', 550000),
    ('Honda', 'City', 919000),
    ('Hyundai', 'Creta', 777000),
    ('Tata', 'Nexon', 886000)
]

# Insert the dummy data into the 'cars' table using a parameterized query.
cursor.executemany('INSERT INTO cars (make, model, price) VALUES (?, ?, ?)', dummy_data)

# Commit the changes to the database to save the data.
conn.commit()

# Close the database connection.
conn.close()
