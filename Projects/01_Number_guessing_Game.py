import random

n = random.randrange(1,10)
guess = int(input("Enter any number from 1 to 9 : "))

print(" Welcome to the Number Guessing Game!")

while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("you guesses it right !!")