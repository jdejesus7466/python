if __name__ == "__main__":

    earth_weight = float(input("Enter your weight: "))
    planet_number = int(input("Enter the planet number: "))

    if planet_number == 1:
        destination_weight = str(earth_weight * 0.38)
        print("Your weight on Mercury is: " + destination_weight)
    elif planet_number == 2:
        destination_weight = str(earth_weight * 0.91)
        print("Your weight on Venus is: " + destination_weight)
    elif planet_number == 3:
        destination_weight = str(earth_weight * 0.38)
        print("Your weight on Mars is: " + destination_weight)
    elif planet_number == 4:
        destination_weight = str(earth_weight * 2.53)
        print("Your weight on Jupiter is: " + destination_weight)
    elif planet_number == 5:
        destination_weight = str(earth_weight * 1.07)
        print("Your weight on Saturn is: " + destination_weight)
    elif planet_number == 6:
        destination_weight = str(earth_weight * 0.89)
        print("Your weight on Uranus is: " + destination_weight)
    elif planet_number == 7:
        destination_weight = str(earth_weight * 1.14)
        print("Your weight on Neptune is: " + destination_weight)
    else:
        print("Invalid Planet Number")


    