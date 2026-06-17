import random

print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ ''')

hangman = [
    r'''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', r'''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

count = 0
score = 0
lives = 6
game = True

def hangman_state():
    print(hangman[lives])

def lives_info():
    print(f"****************************{lives}/6 LIVES LEFT****************************")

def word_to_guess():
    print(f"Your word is: {"" .join(blank)}")


word_list = ["apple", "banana", "cobweb", "python"]
chosen_word = random.choice(word_list)

word_len = len(chosen_word)

blank = []
for char in chosen_word:
    blank.append('_')

print(f"Your word is: {"" .join(blank)}")

while game:

    while True:
        answer = input("Guess the letter: ").lower().strip()

        if len(answer) == 1 and answer.isalpha():
            break
        else:
            print("Error! Only one letter allowed.")

    for i in range(word_len):
            if chosen_word[i] == answer:
                blank[i] = answer
                count += 1

    if count > 0:
        score += 1
        count = 0
        if lives == 0:
            game = False
            print(f'***********************IT WAS {chosen_word}! YOU LOSE**********************')
            break
        elif "_" not in blank:
            game = False
            word_to_guess()
            print("Congratulations! You guessed the word!")
        else:
            word_to_guess()
            hangman_state()
            lives_info()
    else:
        count = 0
        lives -= 1
        if lives == 0:
            print(f"You guessed {answer}, that's not ine the word. You lose a life.")
            hangman_state()
            print(f'***********************IT WAS {chosen_word}! YOU LOSE**********************')
            game = False
        elif "_" not in blank:
            game = False
            word_to_guess()
            print("Congratulations! You guessed the word!")
        else:
            print(f"You guessed {answer}, that's not ine the word. You lose a life.")
            hangman_state()
            word_to_guess()
            lives_info()


