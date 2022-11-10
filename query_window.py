import sqlite3

# Connection Variable
conn = sqlite3.connect('customer.db')

# Create a Cursor
c = conn.cursor()

# Query the Database
c.execute("""
          SELECT rowid, * 
          FROM customers
          --WHERE last_name = 'West'
          """)
query = c.fetchall()
for _ in query:
    print(_)

# Commit our command
conn.commit()

# Close our connection 
conn.close()