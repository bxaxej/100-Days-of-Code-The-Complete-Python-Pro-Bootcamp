print("Welcome to the tip calculator!")

while True:
    try:
        total_bill = float(input("Please enter a valid total bill? $"))

        if total_bill > 0:
            break
        else:
            print("The bill cannot be 0 or less")

    except ValueError:
        print("Please enter a valid number of total bill.")


while True:
    try:

        tip = float(input("How much tip would you like to give? 10, 12, or 15? %"))

        if tip > 0:
            break
        else:
            print("Error: The tip cannot be less than 0!")

    except ValueError:
        print("Please enter a valid number of tip.")


while True:
    try:
        split = float(input("How many people to split the bill? "))

        if split > 0:
            break
        else:
            print("Error: The split cannot be 0 or less!")

    except ValueError:
        print("Please enter a valid number of split.")


tip_perc = total_bill * (tip / 100)
total_bill_with_tip = total_bill + tip_perc
result = total_bill_with_tip / split

print(f"Each person should pay:{result}$\n")
print(f"The total bill is {total_bill}$")
print(f"The tip was {int(tip)}%, which gives us: {tip_perc}$")
print(f"Summing tip and bill is {total_bill_with_tip}$")
print(f"Split for {int(split)} person/s, gives us {result:.2f}$")