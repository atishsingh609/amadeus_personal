import sqlite3

# Connect to your SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('identifier.sqllite')

# Open the .sql file and read its contents
with open('practice.sql', 'r') as file:
    sql_script = file.read()

# Execute the SQL script
try:
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    print("SQL script executed successfully.")
except Exception as e:
    print(f"Error: {e}")

# Commit and close the connection
conn.commit()
conn.close()
