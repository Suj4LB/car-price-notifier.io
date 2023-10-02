import sqlite3

conn = sqlite3.connect('car_prices.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE cars (
        id INTEGER PRIMARY KEY,
        make TEXT,
        model TEXT,
        price INTEGER
    )
''')

dummy_data = [
    ('Swift', 'Dzire', 550000),
    ('Honda', 'City', 919000),
    ('Hyundai', 'Creta', 777000),
    ('Tata', 'Nexon', 886000)
]

cursor.executemany('INSERT INTO cars (make, model, price) VALUES (?, ?, ?)', dummy_data)

conn.commit()
conn.close()
