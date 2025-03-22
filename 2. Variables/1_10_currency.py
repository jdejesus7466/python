if __name__ == "__main__":

    pesos = int(input("What do you have left in pesos? "))
    soles = int(input("What do you have left in soles? "))
    reais = int(input("What do you have left in reais? "))

    usd = (pesos * 0.00024) + (soles * 0.28) + (reais * 0.21)

    print(usd)