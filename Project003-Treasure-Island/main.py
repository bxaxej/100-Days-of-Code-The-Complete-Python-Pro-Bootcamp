with open("logo.txt", "r", encoding="utf-8") as file:
    logo = file.read()

print(logo)

head = """
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a cross road. Where do you want to go? """

print(head)

while True:
    dec1 = (input("      Type 'left' or 'right'")).lower().strip()
    if dec1 == "left" or dec1 == "right":
        break
    else:
        print("Left or right!\n")

if dec1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    while True:
        dec2 = (input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")).lower().strip()
        if dec2 == "swim" or dec2 == "wait":
            break
        else:
            print("Type Swim or Wait!\n")

    if dec2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        while True:
            dec3 = (input("  One red, one yellow and one blue. Which colour do you choose?\n")).lower().strip()
            if dec3 == "red" or dec3 == "yellow" or dec3 == "blue":
                break
            else:
                print("Which colour do you choose?\n")

        if dec3 == "red":
            print("It's a room full of fire. Game Over.")
        elif dec3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
else:
    print("You fell into a hole. Game Over.")