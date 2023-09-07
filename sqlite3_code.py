# Create an sqlite3 database by reading data from a csv

import sqlite3
import csv

# Connect to the SQLite database (or create if it doesn't exist)
conn = sqlite3.connect('github_users.db')
cursor = conn.cursor()

# Create a table to store user data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        followers INTEGER,
        following INTEGER,
        repos INTEGER
    )
''')

# Read data from CSV and insert into the database
with open('github_user_data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        username, followers, following, repos = row
        cursor.execute('''
            INSERT INTO users (username, followers, following, repos)
            VALUES (?, ?, ?, ?)
        ''', (username, int(followers), int(following), int(repos)))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data has been stored in the database.")
