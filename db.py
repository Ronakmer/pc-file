import sqlite3

con = sqlite3.connect('students.db')


def insertData(name, age, city):
    qry = "insert into students (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry, (name, age, city))
    con.commit()
    print("User Details Added")


def updateData(name, age, city, id):
    qry = "update students set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry, (name, age, city, id))
    con.commit()
    print("User Details Updated")


def deleteData(id):
    qry = "delete from students where id=?;"
    con.execute(qry, (id,))
    con.commit()
    print("User Details Deleted")


def viewData():
    qry = "select * from students"
    result = con.execute(qry)
    for row in result:
        print(row)


def partial_name(name, id):
    qry = "update students set NAME=? where id=?;"
    con.execute(qry, (name, id))
    con.commit()
    print("User Details Updated")


def partial_age(age, id):
    qry = "update students set AGE=? where id=?;"
    con.execute(qry, (age, id))
    con.commit()
    print("User Details Updated")


def partial_city(city, id):
    qry = "update students set CITY=? where id=?;"
    con.execute(qry, (city, id))
    con.commit()
    print("User Details Updated")


print("""
1.Insert
2.Update
3.Delete
4.view
5.partial update
""")

ch = 1
while ch == 1:


    c = int(input("Select Your Choice : "))
    if c == 1:
        print("Add New Record")
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        city = input("Enter City : ")
        insertData(name, age, city)
    elif c == 2:
        print("Edit A Record")
        id = input("Enter ID : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        updateData(name, age, city, id)
    elif c == 3:
        print("Delete A Record")
        id = input("Enter ID : ")
        deleteData(id)
    elif c == 4:
        print("Print All Record")
        viewData()
    elif c == 5:
        print("1.name 2.age 3.city")
        demo = int(input("select any one: "))

        if demo == 1:
            id = input("Enter ID : ")
            name = input("enter name: ")
            partial_name(name, id)
        elif demo == 2:
            id = input("Enter ID : ")
            age = int(input("enter age: "))
            partial_age(age, id)
        elif demo == 3:
            id = input("Enter ID : ")
            city = input("enter city: ")
            partial_city(city, id)
    else:
        print("Invalid Selection")
    ch = int(input("Enter 1 To Continue : "))

con.close()
print("Thank You")
