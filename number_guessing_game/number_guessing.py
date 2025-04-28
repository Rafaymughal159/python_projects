import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = int(input("guess a number between 1 to 10 : "))
    if guess < number: 
        print("too low")
    elif guess > number:
     print("too high")
    elif guess == number:
     print("congratulatins, you got it!")
