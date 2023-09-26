import sqlite3
db3= sqlite3.connect ('test2.db')
c=db3.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users(
name TEXT,
age INTEGER,
password TEXT )''')
c.execute('''INSERT INTO users VALUES('SHAHA', 23, 'sad2')''')
c.execute('''INSERT INTO users VALUES('alina', 18, 'vabdb')''')
c.execute('''INSERT INTO users VALUES('adi', 25, 'tey')''')

db3.commit()
db3.close()
