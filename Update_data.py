import sqlite3


def Update_date():

    try:
        # Create connection
        db = sqlite3.connect('app.db')
        print('The connection to database is a succes !')

        # Create cursor
        cr = db.cursor()

        # Update data
        cr.execute('UPDATE users SET name = "Amel" WHERE user_id = 1 ')

        # Commit a changes
        db.commit()

        # Fetch data
        cr.execute('SELECT * FROM users')

        # Showing data
        print(cr.fetchall())

    except sqlite3.Error as er:
        # print errors
        print(f'Erros reading data {er}')

    finally:

        if (db):
            # Close connection to database
            db.close()
            print('The connection to database is closed !')


Update_date()
