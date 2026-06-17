import random
import os

def logo():
    print(r"""  
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
    """)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

game = True

while game:
    logo()
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
    """)
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == "easy":
            chances = 10
            break
        elif difficulty == "hard":
            chances = 5
            break
        else:
            print("Type 'easy' or 'hard'!")

    number = random.randint(1, 100)
    answer = 0

    while number != answer:
        if chances == 0:
            print(f"You lost! The number was {number}.")
            break
        else:
            print(f"You have {chances} attempts remaining to guess the number.")

            try:
                answer = int(input("Make a guess: "))
            except ValueError:
                print("That is not a valid number! Try again.")
                continue

            if number > answer:
                print("Too low!")
                chances -= 1
            elif number < answer:
                print("Too high!")
                chances -= 1
            else:
                print(f"You got it! The answer was {number}.")

    while True:
        again = input("Would you like to play again? (y/n): ")
        if again == "y":
            clear()
            break
        else:
            game = False
            print("Thank you for playing!")
            break