import random
import os

game_data = [
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 635,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 504,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 424,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 396,
        'description': 'Media person_ality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 394,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 376,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 360,
        'description': 'Media person_ality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 317,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 306,
        'description': 'Media person_ality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 293,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 291,
        'description': 'Model and media person_ality',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 284,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'National Geographic',
        'follower_count': 281,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 222,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 250,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 228,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 214,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 205,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 181,
        'description': 'Actress and Musician',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 178,
        'description': 'Comedian and Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 165,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 154,
        'description': 'Musician and Actress',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 159,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 88,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 72,
        'description': 'Musician',
        'country': 'Canada'
    }
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    print(r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/    
    """)

def higer_lower(person_a, person_b):
    score = 0
    game = True
    who = ""

    while game:
        logo()
        name1 = person_a['name']
        follower_count1 = person_a['follower_count']
        description1 = person_a['description']
        country1 = person_a['country']

        name2 = person_b['name']
        follower_count2 = person_b['follower_count']
        description2 = person_b['description']
        country2 = person_b['country']

        if score != 0:
            print(f"You're right! Current score: {score}.")

        print(f"Compare A: {name1}, a {description1}, from {country1}.")
        print(r"""
                 _    __    
                | |  / /____
                | | / / ___/
                | |/ (__  ) 
                |___/____(_)
                """)
        print(f"Against B: {name2}, a {description2}, from {country2}.")

        while game:
            who = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
            if who == "a" or who == "b":
                break
            else:
                print("Type 'A' or 'B'.")

        if who == "a":
            if follower_count1 > follower_count2:
                score += 1
                clear()
                person_a = person_b
                person_b = random.choice(game_data)
                while person_b == person_a:
                    person_b = random.choice(game_data)
            else:
                clear()
                logo()
                print(f"Sorry, that's wrong. Final score: {score}")
                game = False
        elif who == "b":
            if follower_count2 > follower_count1:
                score += 1
                clear()
                person_a = person_b
                person_b = random.choice(game_data)
                while person_b == person_a:
                    person_b = random.choice(game_data)
            else:
                clear()
                logo()
                print(f"Sorry, that's wrong. Final score: {score}")
                game = False



game1 = True

while game1:
    clear()
    person1 = random.choice(game_data)
    person2 = random.choice(game_data)

    while person1 == person2:
        person2 = random.choice(game_data)

    higer_lower(person1, person2)
    while True:
        again = input("Would you like to play again? (y/n): ").lower().strip()
        if again == "y":
            break
        elif again == "n":
            clear()
            print("Goodbye!")
            game1 = False
            break
        else:
            print("Type 'y' or 'n'.")
