from pywebio import *
from pywebio.output import *
from pywebio.input import *
def add(a,b):
    put_text("Answer is = ",a+b)
def sub(a,b):
    put_text("Answer is = ",a-b)
def mul(a,b):
    put_text("Answer is = ",a*b)
def div(a,b):
    put_text("Answer is = ",a//b)

num1 = int(input("Enter first number= "))
num2 = int(input("Enter second number= "))

put_text("Enter the operation you want to perform: ")
put_text("a:Addition\nb:Subtraction\nc:Multiplication\nd:Division\n")

operation = input("")
operation = operation.lower()
match operation:
    case 'addition':
        add(num1,num2)
    case 'subtraction':
        sub(num1,num2)
    case 'multiplication':
        mul(num1,num2)
    case 'division':
        div(num1,num2)
