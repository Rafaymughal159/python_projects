def add (a , b):
    return a + b

def subtract (a , b):
    return a - b

def multiply (a , b):
    return a * b

def divide (a , b):
    if b == 0:
        return "can't divide by zero"
    return a / b
print("select operation : +, -, *, /")
choice = input("enter operation : ")

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

if choice == "+":
    print(add(num1,num2))
elif choice == "-":
    print(subtract(num1,num2))
elif choice == "*":
    print(multiply(num1,num2))
elif choice == "/":
    print(divide(num1,num2))
else:
    print("invalid input")
