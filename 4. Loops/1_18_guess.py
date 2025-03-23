if __name__ == "__main__":

    guess = 0
    tries = 0

    while guess != 6:
        guess = int(input("Guess the number:  "))
        tries += 1

    print("You got it!")
    print("Tries: ", tries)