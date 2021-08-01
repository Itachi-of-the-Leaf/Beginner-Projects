"""
This is a program that creates a simple calculator
We first define functions, then we ask the user for input and then we call the functions
"""
#This function adds two numbers
from os import kill
from typing import Type


def add(a , b):
    print("The sum of " , a , "and" , b , "is:" , a + b)

#This function subtracts two numbers
def subtract(a , b):
    print("The difference between" , a , "and" , b , "is:" , a-b)

#This function multiplies two numbers
def multiply(a , b):
    print("The product of" , a , "and" , b , "is:" ,  a*b)

#This function divides two numbers
def divide(a , b):
    try:
        print("The quotient obtained after dividing" , a , "by" , b , "is:" , a/b)
    except (ZeroDivisionError):
        print("Cannot divide by 0 (results: undefined)")

#This gives a raised to the power b
def exponent(a , b):
    print(a , "to the power" , b , "is:" , a ** b)

#This function gives us the multiplication table of a upto b.
def multiplication_table(a , b):
    for i in range(1 , b + 1):
        print(a , "x" , i , "=" , a*i)
    print("This was the multiplication table of" , a , "upto" , b)

#Now to ask the user for input
try:
    a = int(input("Please enter the first number: "))
except ValueError as VE:
    print("Please enter a number! Look at the error you've created!")
    raise
try:
    b = int(input("Please enter the second number: "))
except ValueError as VE:
    print("Please enter a number! Look at the error you've created!")
    raise
print("Would you like to add(1) , subtract(2), multiply(3), divide(4), get exponent(5) or get the multiplication table(6) of the numbers?")
choice = input("Enter your choice: (1/2/3/4/5/6): ")
#Implementing functions based on the input.
if choice == "1":
    add(a , b)
elif choice == "2":
    subtract(a , b)
elif choice == "2":
    subtract(a , b)
elif choice == "3":
    multiply(a , b)
elif choice == "4":
    try:
        divide(a , b)
    except ZeroDivisionError():
        print("Cannot divide by zero!")
elif choice == "5":
    exponent(a , b)
elif choice == "6":
    multiplication_table(a , b)
#Big brain move to handle all errors in case user enters the wrong input
else:
    print("Please enter a valid choice!")