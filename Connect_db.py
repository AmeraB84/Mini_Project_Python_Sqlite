import sqlite3

# Create database
db = sqlite3.connect('app.db')

# Setting Up CURSOR

cr = db.cursor()

# Create table and columns
cr.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER, name TEXT)')
cr.execute(
    'CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER,user_id INTEGER)')

# Fetch data
cr.execute('SELECT * FROM users')
# print(cr.fetchone())  # gives record if exists else return None
# print(cr.fetchall()) # gives a list of tuple
print(cr.fetchmany(1))  # gives n records a list of tuple


# my_list = ['Ahmed', 'Amel', 'Amera', 'Rym']
# cr.execute('INSERT INTO users(user_id,name) VALUES (1,"Ahmed")')
# cr.execute('INSERT INTO users(user_id,name) VALUES (2,"Amera")')
# cr.execute('INSERT INTO users(user_id,name) VALUES (3,"Ali")')
# for key, user in enumerate(my_list):
#     cr.execute(f'INSERT INTO users(user_id,name) VALUES ({key + 1},"{user}")')

# Save the changes
db.commit()

# Close connection
db.close()
