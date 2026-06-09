import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

while True:
    choice = input("What do you choose? Rock, Paper or Scissors?\n").lower().strip()
    if choice == "rock" or choice == "paper" or choice == "scissors":
        break
    else:
        clear_screen()
        print("Whoops! Try again.")


if choice == "rock":
    print(rock)
elif choice == "paper":
    print(paper)
elif choice == "scissors":
    print(scissors)
else:
    clear_screen()
    raise ValueError(f"Unexpected computer turn value: {choice}")

print("Computer chose:")

computer_turn = random.randint(1, 3)

if computer_turn == 1:
    computer_choice = "rock"
    print(rock)
elif computer_turn == 2:
    computer_choice = "paper"
    print(paper)
elif computer_turn == 3:
    computer_choice = "scissors"
    print(scissors)
else:
    clear_screen()
    raise ValueError(f"Unexpected computer turn value: {computer_turn}")


if choice == computer_choice:
    print("It's a draw!")
elif (choice == "rock" and computer_choice == "scissors") or \
     (choice == "paper" and computer_choice == "rock") or \
     (choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")

