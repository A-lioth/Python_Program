
import random

def guess_number():
    num = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == num:
            print("Congratulations! You guessed the number.")
            break
        elif guess < num:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

guess_number()
