import os

def logo():
    print(r'''
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    ''')

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by 0"
    else:
        return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

calculator = True
calculator2 = True

while calculator:
    calculator2 = True
    logo()
    while True:
        try:
            n1 = float(input("What's the first number?: "))
            break
        except ValueError:
            print("That is not a valid number!")


    print('''
    +
    -
    *
    /
    ''')

    while calculator2:

        while True:
            operation = input("Pick an operation: ")
            if operation != "+" and operation != "-" and operation != "*" and operation != "/":
                print(f"{operation} is not a valid operation!")
            else:
                break

        while True:
            try:
                n2 = float(input("What's the next number?: "))
                break
            except ValueError:
                print(f"That is not a valid number!")

        result = operations[operation](n1, n2)

        print(f"{n1} {operation} {n2} = {result}")

        while True:
            decision = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation , or type 'e' to exit: ")
            if decision == "y" or decision == "n" or decision == "e":
                break
            else:
                print(f"{decision} is not a valid choice!")

        if decision == "y":
            n1 = result
        elif decision == "e":
            print("Goodbye!")
            calculator = False
        else:
            clear_console()
            calculator2 = False
            calculator2 = False