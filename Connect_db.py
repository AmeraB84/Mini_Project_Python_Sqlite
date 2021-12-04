import sqlite3

# Create database
db = sqlite3.connect('app.db')

# Setting Up CURSOR

cr = db.cursor()

# Create table and columns
cr.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER, name TEXT)')
cr.execute(
    'CREATE TABLE IF NOT EXISTS skills (name TEXT, progress INTEGER,user_id INTEGER)')

my_list = ['Ahmed', 'Amel', 'Amera', 'Rym']
# cr.execute('INSERT INTO users(user_id,name) VALUES (1,"Ahmed")')
# cr.execute('INSERT INTO users(user_id,name) VALUES (2,"Amera")')
# cr.execute('INSERT INTO users(user_id,name) VALUES (3,"Ali")')
for key, user in enumerate(my_list):
    cr.execute(f'INSERT INTO users(user_id,name) VALUES ({key + 1},"{user}")')

# Save the changes
db.commit()

# Close connection
db.close()
