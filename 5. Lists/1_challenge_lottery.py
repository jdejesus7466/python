import random

if __name__ == "__main__":

    my_numbers = []
    winning_numbers = []

    for i in range(0, 5):
        my_numbers.append(random.randint(1,69))
        winning_numbers.append(random.randint(1,69))
    
    my_numbers.append(random.randint(1,26))
    winning_numbers.append(random.randint(1,26))

    print(my_numbers)
    print(winning_numbers)
