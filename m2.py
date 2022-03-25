import sqlite3
con = sqlite3.connect('pms.db')

cursor = con.cursor()

b = 1
while b:
    print("menu :")
    print("1. add a patient ")
    print("2. view patients ")
    print("3. exit ")
    a = int(input("enter ur selection : "))

    if a == 1:
        num = int(input("Enter no of patient "))
        for i in range(num):
            pcode = int(input("Enter code : "))
            pname = input("Enter patient name: ")
            padd = input("Enter the Address: ")
            pph = int(input("Enter the phone No: "))
            insert_query = f"INSERT INTO patient VALUES('{pcode}','{pname}','{padd}','{pph}')"
            cursor.execute(insert_query)
            con.commit()

    elif a ==2:
        sq = "SELECT * FROM patient"
        cursor.execute(sq)
        r = cursor.fetchall()
        for j in r:
            print('patient code :',j[0])
            print('Name of the patient:',j[1])
            print('Address of patient :',j[2])
            print('phone no :',j[3])

            con.commit()
    else :
        print("exit")
        b=0