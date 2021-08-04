import sqlite3
def connect_to_db(url_local_db='C:\\Users\\User\\db\\urloveLinks.db'):

    try:
        connection_string = sqlite3.connect(url_local_db)
        cursor=connection_string.cursor()
        cursor.execute('SELECT * from translateLink')
        for i in cursor:
            print('j')
            print(i)
    except:
        print('error')
connect_to_db()
# cursor.execute('select * from See')
# cursor.executescript('''
# CREATE TABLE days (
# idDay INTEGER NOT NULL PRIMARY KEY,
# name TEXT
# );
# insert into days(idDay,name) values(2, 'Monday');
# select * from days
# '''
#
# )
# cursor.execute('select * from days')
# for i in cursor:
#    print(i)
# connection_string.commit()