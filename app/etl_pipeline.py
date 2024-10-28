import pandas as pd
import sqlite3

# Load the Netflix dataset
df = pd.read_csv('data/netflix_series.csv')

# Data Cleaning (handle missing values)
df = df.dropna(subset=['title', 'listed_in', 'rating'])


# SQLite connection
conn = sqlite3.connect('netflix.db')
cursor = conn.cursor()

# Create a table in SQLite if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS netflix_series (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    genre TEXT,
    description TEXT,
    rating FLOAT,
    release_year INTEGER
)
''')

# Insert data into the table
df.to_sql('netflix_series', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("Data ingestion and cleaning completed.")
