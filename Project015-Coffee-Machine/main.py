cofee_machine = {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0
    }

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

program = True

while program:

    welcome = input("What would you like? (espresso/latte/cappuccino): ")

    if welcome == "espresso" or welcome == "latte" or welcome == "cappuccino" or welcome == "report" or welcome == "off":
        if welcome == "espresso" or welcome == "latte" or welcome == "cappuccino":

            while True:
                try:
                    quarters = int(input("How many quarters? "))
                    quarters *= 0.01
                    break
                except ValueError:
                    print("Sorry, you must enter an integer")

            while True:
                try:
                    dimes = int(input("How many dimes? "))
                    dimes *= 0.10
                    break
                except ValueError:
                    print("Sorry, you must enter an integer")

            while True:
                try:
                    nickles = int(input("How many nickles? "))
                    nickles *= 0.05
                    break
                except ValueError:
                    print("Sorry, you must enter an integer")

            while True:
                try:
                    pennies = int(input("How many pennies? "))
                    pennies *= 0.25
                    break
                except ValueError:
                    print("Sorry, you must enter an integer")

            cofee_machine['money'] += quarters + dimes + nickles + pennies

            drink_cost = menu[welcome]["cost"]
            drink_water = menu[welcome]["ingredients"]["water"]
            drink_milk = menu[welcome]["ingredients"]["milk"]
            drink_coffee = menu[welcome]["ingredients"]["coffee"]

            water = cofee_machine['water']
            milk = cofee_machine['milk']
            coffee = cofee_machine['coffee']
            money = cofee_machine['money']


            if money < drink_cost:
                print("Sorry, you don't have enough money")
            elif water < drink_water:
                print("Sorry, we ran of water")
            elif coffee < drink_coffee:
                print("Sorry, we ran of coffee")
            else:
                print(f"Here is your {welcome}. Enjoy")
                cofee_machine['water'] -= drink_water
                cofee_machine['coffee'] -= drink_coffee
                cofee_machine['milk'] -= drink_milk
                cofee_machine['money'] -= drink_cost
        elif welcome == 'report':
            print(f'''
Money: {cofee_machine['money']:.2f} $
Water: {cofee_machine['water']} ml
Milk: {cofee_machine['milk']} ml
Coffee: {cofee_machine['coffee']} g
                ''')
        elif welcome == 'off':
            print("Goodbye!")
            program = False
    else:
        print(f"{welcome} is invalid input")


