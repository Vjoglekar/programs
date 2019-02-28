import sqlite3
connection = sqlite3.connect('test2.db')
cursor= connection.cursor()
query = 'select * from company;'
#query = 'create table company(id int, name text);'
cursor.execute(query)
print(cursor.fetchall())
connection.commit()
connection.close()
