import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('a.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS login
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT)''')

# Insert data into the table
users_data = [
    ('user1','pass1'),
    ('angela','123abc'),
    ('qwerty','qwe_rty'),
    ('blueprint','fellowship'),
    ('reghan','h29xl'),
    ('william','2938j'),
    ('aparna','3ioej')
]

cursor.executemany('INSERT INTO login (username, password) VALUES (?, ?)', users_data)

# cursor.execute("INSERT INTO login(username, password)VALUE(?,?)",("user1","pass1"))

# Commit the changes and close the conenction
conn.commit()
conn.close()
