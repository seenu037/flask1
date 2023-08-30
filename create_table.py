import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE parking (flat_name TEXT, availability TEXT)')
print("Created table successfully!")

conn.close()
