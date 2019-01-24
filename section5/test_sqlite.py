# This is only to learn how to interact with SQLite

import sqlite3

connection = sqlite3.connect('data.db')

# A cursor allows you to select and start things
# Respondible for executing the query and storing the results
cursor = connection.cursor()

# Create the query
create_table = "CREATE TABLE users (id int, username text, password text)"

# Execute the query
cursor.execute(create_table)

# Store data in this database
user = (1, 'jose', 'asdf') # tuple
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# Insert and store many users
users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'asdf')
]
cursor.executemany(insert_query, users )

# Retrieve data from database
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# Save all the changes in the db file
connection.commit()

# Good habit to close the connection at the end
connection.close()
