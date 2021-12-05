import sqlite3


def get_all_data():

    try:
        # Create a connexion and database
        db = sqlite3.connect('app.db')
        print('connect to data base succefuly')

        # Create a cursor to execute query
        cr = db.cursor()
        cr.execute('SELECT * FROM users')
        results = cr.fetchall()
        print(f'The numbers of rows is {len(results)}')

        print('Show data : ')
        for row in results:
            print(f'User ID ==> {row[0]} ,', end=' ')
            print(f'User name ==> {row[1]}')

    # Errors
    except sqlite3.Error as er:
        print(f'Errors reading data {er}')

    finally:  # exeution what ever
        if (db):
            # Close database
            db.close()
            print('Connection to database is closed')


get_all_data()
