
# This is a simple loop calculator that performs addition, subtraction, multiplication, and division.

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    if b == 0:
        return "error: can't divide by zero!"
    return a / b

while True:
    print("\n select operator:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    choice = input("enter your choice (1/2/3//4/5) : ")

    if choice == "5":
        break

    num1 =int(input("enter your first number: "))
    num2 =int(input("enter your second number: "))

    if choice == "1":
        print(add(num1 , num2))
    elif choice == "2":
        print(subtract(num1 , num2))
    elif choice == "3":
        print(multiply(num1 , num2))
    elif choice == "4":
        print(divide(num1 , num2))
    else:
        print("invalid input! please try again.")

