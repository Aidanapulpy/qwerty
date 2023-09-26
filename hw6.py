import sqlite3
db3= sqlite3.connect ('test.db3')
c=db3.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users(
name TEXT,
age INTEGER,
password TEXT )''')
c.execute('''INSERT INTO users VALUES('SHAHA', 23, 'sad2')''')


db3.commit()
db3.close()
