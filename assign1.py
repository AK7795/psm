import sqlite3

con = sqlite3.connect('employee.db')

cursor = con.cursor()
sq = '''CREATE TABLE empdata(
               id INTEGER ,
               empcode INTEGER,
               empname TEXT ,
               empsalary INTEGER,
               designation TEXT)'''

cursor.execute(sq)

print('table is created successfully')

con.commit()
con.close()
