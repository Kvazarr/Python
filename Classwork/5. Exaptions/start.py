from math import sqrt
import sys

# try:
#     number = int(input("Enter number: "))
#     square = sqrt(number)
#     print(f"Square of number: {square}")
# except ValueError:
#     print("Not valid number")
# except SyntaxError:
#     print("Invalid Syntax")
# except OSError as err:
#     print(f"Error! :{err}")



# def Func(number):
#     return sqrt(number)

# try:
#     number = int(input("Enter number: "))
#     Func(number)
#     print(f"Square of number: {Func(number)}")
# except ValueError:
#     print("Not valid number")
# except SyntaxError:
#     print("Invalid Syntax")

dict = {}
exit = False

def Func(dict,exit):
    while exit != True:
        choice = int(input(f"1)Add value; 0)Exit;\nEnter ur choice: "))
        if choice == 1:
            key = input("Enter key: ")
            value = input("Enter value: ")
            dict[key]=value
        elif choice == 0:
            exit = True
Func(dict,exit)

def Func2(choice, dict):
    if choice == 1:
        print(dict)
    # elif choice == 2:
    # elif choice == 3:
    # elif choice == 4:
    # elif choice == 5:

while exit !=True:
    try:
        choice = int(input(f"1)Show all; 2)Search value; 3)Change value; 4)Show by key; 5)Delete by key; \nEnter your choice: "))
        Func2(choice,dict)
        exit = True
    except ValueError:
        print("Not valid value.")
