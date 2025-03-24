from math import pi
from random import choice

if __name__ == "__main__":

    planets = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Saturn'
    ]

    random_planet = choice(planets)
    area = 0

    if random_planet == "Mercury":
        area = 4 * pi * 2440
    elif random_planet == "Venus":
        area = 4 * pi * 6052
    elif random_planet == "Earth":
        area = 4 * pi * 6371
    elif random_planet == "Mars":
        area = 4 * pi * 3390
    elif random_planet == "Saturn":
        area = 4 * pi * 58232
    else:
        print("Oops! An error occurred.")
    
    print(random_planet + ": " + str(round(area, 2)))