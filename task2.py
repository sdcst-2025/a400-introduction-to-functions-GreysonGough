"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
import random
import time

def title():
    print("Welcome to the guessing game!")
    time.sleep(1)
    print("This game involves you trying to guessing the number in few tries as possible.")
    time.sleep(1.4)
    print("The number is from 1 - 100")
    time.sleep(1)
    print("Good luck!")

def game():
    rnum = random.randint(1, 100)
    guess_count = 0

    while True:
        try:
            guess_count += 1
            guess = int(input(f"Enter your guess:"))

            if guess < 1 or guess > 100:
                print("Please guess within 1 - 100.")

            elif guess == rnum:
                print(f"congrats you won. {guess_count} guesses.")
                break

            elif guess < rnum:
                print("Too low! Please try again")

            elif guess > rnum:
                print("Too high! Please try again")

        except ValueError:
            print("Please enter a valid value.")
            guess_count += 1
         
        
if __name__ == "__main__":
    title()
    game()


