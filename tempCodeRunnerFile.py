
import sqlite3

# connect to the database
conn = sqlite3.connect('public_art.db')

# create a cursor object
c = conn.cursor()

# execute a query
c.execute('SELECT * FROM public_art')

# fetch the results
rows = c.fetchall()

# print the results
for row in rows:
    print(row)

# close the cursor and connection
c.close()
conn.close()

