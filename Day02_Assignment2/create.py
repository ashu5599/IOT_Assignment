import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)

def addemp():
    empid = int(input("Enter employee ID : "))
    name = input("Enter name : ")
    department = input("Enter department name : ")
    email = input("Enter email address :")
    salary = int(input("Enter salary : "))
    DOJ = input("Enter your date of joining : ")
    
    query = f"insert into employee values({empid}, '{name}', '{department}', '{email}', '{salary}', '{DOJ}');"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
