import sqlite3

con = sqlite3.connect('pms.db')

cursor = con.cursor()
sq = '''CREATE TABLE patient(
               code INTEGER PRIMARY KEY,
               name TEXT ,
               address TEXT,
               phone TEXT)'''

cursor.execute(sq)

print('table is created successfully')

con.commit()
con.close()
