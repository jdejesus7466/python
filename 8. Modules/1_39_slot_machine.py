import random

if __name__ == "__main__":

    def play():
        choice = True
        while choice:

            symbols = ['🍒',' 🍇', '🍉', '7️⃣']

            results = random.choices(symbols, k=3)

            output = ""

            print(results[0] + " | " + results[1] + " | " + results[2])

            if results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣":
                print("Jackpot! 💰")
            else:
                print("Thanks for playing!")
            
            prompt = str(input("Keep Playing? (Y or N)"))

            if prompt == "Y" or prompt == "y":
                choice = True
            elif prompt == "N" or prompt == "n":
                choice = False
                print("Thanks for playing!")
            else:
                print("Wrong Input, stopping program...")
                choice = False
                print("Thanks for playing!")
        
    play()

