import sqlite3
con = sqlite3.connect('employee.db')

cursor = con.cursor()

b = 1
while b:
    print("menu :")
    print("1. add employees ")
    print("2. view employees ")
    print("3. exit ")
    a = int(input("enter ur selection : "))

    if a == 1:
        num = int(input("Enter no of employees "))
        for i in range(num):
            eid = int(input("enter employee id : "))
            code = int(input("Enter employee code : "))
            name = input("Enter employee  name: ")
            salary = int(input("Enter salary : "))
            desig = (input("Enter designation : "))
            insert_query = f"INSERT INTO empdata VALUES('{eid}','{code}','{name}','{salary}','{desig}')"
            cursor.execute(insert_query)
            con.commit()

    elif a ==2:
        sq = "SELECT * FROM empdata"
        cursor.execute(sq)
        r = cursor.fetchall()
        for j in r:
            print('emp id : ',j[0])
            print('emp code :',j[1])
            print('Name :',j[2])
            print('salary:',j[3])
            print('designation :',j[4])
            con.commit()
    else :
        print("exit")
        b=0