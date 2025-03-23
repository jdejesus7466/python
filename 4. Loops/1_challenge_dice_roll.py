import random

if __name__ == "__main__":

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    total = dice1+dice2

    guess = int(input("What is the total (2-12)? "))

    while guess != total:
        print("What is the total (2-12)? ")
    
    print("You got it!")
    
