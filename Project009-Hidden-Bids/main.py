import os

bids_dic = {}


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


def winner(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

logo()
while True:

    while True:
        name = input("Enter your name: ").lower().strip()
        if name.isalpha():
            break
        else:
            print("Please enter a valid name")


    while True:
        try:
         bid = int(input("Enter your bid: $").strip())
         if bid < 0:
            raise ValueError
         else:
            break
        except ValueError:
            print("Please enter a number")

    bids_dic[name] = bid

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

winner(bids_dic)