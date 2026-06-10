print("Welcome to the Band Name Generator")
city_name = input("What's the name of the city you grew up in? ")
pet_name = input("What's your pet's name? ")
favorite_color = input("What's your favorite color? ")
print("Your Band Name could be:\n", favorite_color, city_name, pet_name)

length = len(city_name) + len(favorite_color) + len(pet_name)

print(f"Your brand has {length} characters")