if __name__ == "__main__":

    number = int(input("Input an integer: "))
    total = 0

    for i in range(1, number + 1):
        total += i ** 2
    
    print(total)
