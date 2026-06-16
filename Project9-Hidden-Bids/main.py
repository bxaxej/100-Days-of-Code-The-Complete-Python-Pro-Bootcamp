import os

names = []
bids = []


def logo():
    print(r'''

                         ___________
                                  /
                          )_______(
                          |"""""""|_.-._.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\ 
    ''')

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def winner():
    winner_bid = max(bids)

    winners = [names[i] for i in range(len(bids)) if bids[i] == winner_bid]

    if len(winners) > 1:
        print(f"It's a tie! The winners are {', '.join(winners)} with a bid of ${winner_bid}")
    else:
        print(f"The winner is {winners[0]} with a bid of ${winner_bid}")

logo()
while True:

    while True:
        name = input("Enter your name: ").lower().strip()
        if name.isalpha():
            names.append(name)
            break
        else:
            print("Please enter a valid name")


    while True:
        try:
         bid = int(input("Enter your bid: $").strip())
         if bid < 0:
            raise ValueError
         else:
            bids.append(bid)
            break

        except ValueError:
            print("Please enter a number")

    while True:
        bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower().strip()
        if bidders == "yes":
            clear_console()
            logo()
            break
        elif bidders == "no":
            break
        else:
            print("Please enter 'yes' or 'no'")

    if bidders == "no":
        break
    else:
        continue

winner()