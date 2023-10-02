import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('car_prices.db')
cursor = conn.cursor()

# Create a table to store car information
cursor.execute('''
    CREATE TABLE cars (
        id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        price INTEGER
    )
''')

# Insert some dummy data
dummy_data = [
    ('Honda', 'Civic', 18000),
    ('Toyota', 'Corolla', 19000),
    ('Ford', 'Focus', 17000),
    ('Chevrolet', 'Cruze', 16000)
]

cursor.executemany('INSERT INTO cars (make, model, price) VALUES (?, ?, ?)', dummy_data)

# Commit changes and close the connection
conn.commit()
conn.close()
