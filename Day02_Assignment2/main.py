from dbconn import *
from create import *
from delete import *
from update import *
from retrieve import *

get_connection()
while 1:
    print("Select option:")
    print(" 1)Add \n 2)Delete \n 3)Update \n 4)Display all \n 5)Display employee for a given department \n 6)Display employee with highest salary \n 7)Display employee with lowest salary \n 8)Exit")
    choice = int(input("Enter your choice : "))
    if(choice==1):
        addemp()
    elif(choice==2):
        n=int(input("Enter the employee id to be deleted: "))
        delete_employee(n)
    elif(choice==3):
        id = int(input("Enter employee id for updation : "))
        e=input("Enter email ID to be updated: ")
        s=int(input("Enter new salary to be updated:"))
        update_employee(e,s,id)
    elif(choice==4):
        displayall()
    elif(choice==5):
        dep=input("Enter the department name: ")
        disdep(dep)
    elif(choice==6):
        print("Maximum salary: ")
        dismax()
    elif(choice==7):
        print("Minimum salary: ")
        dismin()
    elif(choice==8):
        print("Exiting.....")
        exit()