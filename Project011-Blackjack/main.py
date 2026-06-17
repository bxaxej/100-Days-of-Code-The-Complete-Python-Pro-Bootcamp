import random
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def logo():
    print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/           
    """)


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

while True:
    while True:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
        if play == "y" or play == "n":
            break

    if play == "n":
        print("Goodbye! 👋")
        break

    clear_console()
    your_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=1)

    your_current_score = sum(your_cards)
    computer_current_score = sum(computer_cards)
    logo()
    print(f"    Your cards: {your_cards}, current score: {your_current_score}")
    print(f"    Computer's first card: {computer_cards}")

    while True:
        if your_current_score >= 21:
            break

        while True:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
            if another_card == "y" or another_card == "n":
                break
            print("Please type 'y' or 'n'")

        if another_card == "y":
            your_cards += random.choices(cards, k=1)
            your_current_score = sum(your_cards)
            print(f"    Your cards: {your_cards}, current score: {your_current_score}")
        else:
            break

    if your_current_score <= 21:
        while computer_current_score < 22 and your_current_score > computer_current_score:
            computer_cards += random.choices(cards, k=1)
            computer_current_score = sum(computer_cards)

    print(f"   Your final hand: {your_cards}, final score: {your_current_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_current_score}")

    if your_current_score > 21:
        print("You went over. You lose 😭")
    elif computer_current_score > 21:
        print("Computer went over. You win! 😁")
    elif your_current_score > computer_current_score:
        print("You win! 😁")
    elif your_current_score < computer_current_score:
        print("You lose 😤")
    else:
        print("It's a draw! 🙃")

