import string

print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           ''')

program = True


def cesar(user_word, word_shift, decision):
    alphabet = string.ascii_lowercase
    coded_word = ""
    if decision == "encode":
        for letter in user_word:
            index = alphabet.index(letter)
            new_index = (index + word_shift) % 26
            coded_word += alphabet[new_index]
        print(f"Here's the encoded result: {coded_word}")
    else:
        for letter in user_word:
            index = alphabet.index(letter)
            new_index = (index - word_shift) % 26
            coded_word += alphabet[new_index]
        print(f"Here's the decoded result: {coded_word}")

while program:
    while True:
        decision = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
        if decision == "encode" or decision == "decode":
            break
        else:
            continue

    while True:
        user_word = input("Type your message:\n").lower().strip()
        if user_word.isalpha():
            break
        else:
            print("Please enter a valid word.")

    while True:
        try:
            word_shift = int(input("Type the shift number:\n"))
            if word_shift <= 0:
                print("Please enter a valid shift number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    cesar(user_word, word_shift, decision)

    while True:
        restart = input("Type 'yes' if you want to go restart. Otherwise type 'no'.\n")
        if restart == "yes" or restart == "no":
            break
        else:
            continue

    if restart == "yes":
        continue
    else:
        print("Goodbye!")
        program = False