import random
import string

print("Welcome to the PyPassword Generator!")
# Program zadziała sprawdza czy input ma wartość 0 lub większą i jest cyfrą
# Pętla od ilości znaków w haśle
while True:
    user_letters = input("How many letters would you like in your password?\n")

    try:
        nr_letters = int(user_letters)

        if nr_letters > 0:
            break
        else:
            print("It cannot be less than 0!!\n")

    except ValueError:
        print("Whoops! That's not a valid number. Try again.\n")

# Pętla od ilości symboli w haśle, sprawdza czy użytkownik nie przekracza ilości znaków
while True:
    user_symbols = input("How many symbols would you like?\n")

    try:
        nr_symbols = int(user_symbols)

        if nr_symbols > nr_letters:
            print(f"You cant have {nr_symbols} symbols in only {nr_letters} letters \n")
        elif nr_symbols >= 0:
            break
        else:
            print("It cannot be less than 0!\n")

    except ValueError:
        print("Whoops! That's not a valid number. Try again.\n")

# Zmienna licząca ile znaków jeszcze możemy dać dla cyfr
space_left = nr_letters - nr_symbols

# Pętla od ilości cyfr w haśle, sprawdza czy się zmieszczą w haśle
while True:
    user_numbers = input("How many numbers would you like?\n")

    try:
        nr_numbers = int(user_numbers)

        if nr_numbers > space_left:
            print(f"You have only {space_left} letters left! \n")
        elif nr_numbers >= 0:
            break
        else:
            print("It cannot be less than 0!\n")

    except ValueError:
        print("Whoops! That's not a valid number. Try again.\n")

# liczymy jaka część hasła będzie na litery
p_letters = nr_letters - (nr_symbols + nr_numbers)

# Tworzymy tablice liter
password_letters = random.choices(string.ascii_letters, k=p_letters)

# Tworzymy tablice symboli
password_symbols = random.choices(string.punctuation, k=nr_symbols)

# Tworzymy tablice cyfr
password_numbers = random.choices(string.digits, k=nr_numbers)

# Łączymy je w jedną tymczasową
password_temp = password_letters + password_symbols + password_numbers
print(password_temp)
# Mieszamy kolejność
random.shuffle(password_temp)
print(password_temp)

# Z listy tworzymy napis
password_final = "".join(password_temp)
print(f"Your password is: {password_final}")
