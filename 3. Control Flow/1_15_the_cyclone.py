if __name__ == "__main__":

    height = input("How tall are you (in cm)? ")
    credits = input("How many credits do you have? ")

    if int(height) >= 137 and int(credits) >= 10:
        print("Enjoy the ride!")
    elif int(height) < 137:
        print("You are not tall enough to ride.")
    elif int(credits) < 10:
        print("You don't have enough credits.")
    else:
        print("You don't have enough credits nor are you tall enough to ride.")

