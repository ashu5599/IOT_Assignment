import mysql.connector

def open_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="sunbeam",
        password="sunbeam",
        database="iotdb"
    )

def displayall():
    query = "SELECT * FROM employee;"

    with open_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        cursor.close()

def disdep(department_name):
    query = "SELECT name FROM employee WHERE department = %s;"

    with open_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, (department_name,))
        records = cursor.fetchall()
        print(records)
        cursor.close()

def dismax():
    query = "SELECT * FROM employee WHERE salary = (SELECT MAX(salary) FROM employee);"

    with open_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        cursor.close()

def dismin():
    query = "SELECT * FROM employee WHERE salary = (SELECT MIN(salary) FROM employee);"

    with open_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)
        cursor.close()
