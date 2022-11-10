import sqlite3

# Connection Variable
conn = sqlite3.connect('customer.db')

# Create a Cursor
c = conn.cursor()

# Create a Table

c.execute("""
          CREATE TABLE customers
          (first_name DATATYPE TEXT,
          last_name DATATYPE TEXT,
          email DATATYPE TEXT
          )""")

# Create cursor to add row to table
c.execute("INSERT INTO customers VALUES ('Bob', 'Builder', 'bobthebuilder@gmail.com')")

# Add multiple customers to table (python list)
many_customers = [
                ('Theodore','Roosevelt','teddyroos@gmail.com'),
                ('Franklin','Roosevelt','Frank@gmail.com'),
                ('John','Chief','john117@gmail.com')
                  ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Commit our command
conn.commit()

# Close our connection 
conn.close()