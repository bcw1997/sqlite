import sqlite3

# Connection Variable
conn = sqlite3.connect('customer.db')

# Create a Cursor
c = conn.cursor()

# Update Records in Table
c.execute("""
          UPDATE customers 
          SET first_name = "Master"
          WHERE first_name = 'John'
          """)

# Commit our command
conn.commit()

# Close our connection 
conn.close()