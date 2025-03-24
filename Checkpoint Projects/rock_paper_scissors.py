import random

if __name__ == "__main__":

    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================\n")

    print("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")

    list_choices = {
        "1" : "✊",
        "2" : "✋",
        "3" : "✌️",
        "4" : "🦎",
        "5" : "🖖"
    }

    choice = input("Pick a number: ")
    print("")
    cpu_choice = str(random.randint(1,5))

    print("You chose:", list_choices[choice])
    print("CPU chose:", list_choices[cpu_choice])
    
    if choice == "1":
        if cpu_choice == "2" or cpu_choice == "5":
            print("The CPU won!")
        elif cpu_choice == "3" or cpu_choice == "4":
            print("The Player won!")
        else:
            print("It's a tie!")
    elif choice == "2":
        if cpu_choice == "3" or cpu_choice == "4":
            print("The CPU won!")
        elif cpu_choice == "1" or cpu_choice == "5":
            print("The Player won!")
        else:
            print("It's a tie!")
    elif choice == "3":
        if cpu_choice == "1" or cpu_choice == "5":
            print("The CPU won!")
        elif cpu_choice == "2" or cpu_choice == "4":
            print("The Player won!")
        else:
            print("It's a tie!")
    elif choice == "4":
        if cpu_choice == "1" or cpu_choice == "3":
            print("The CPU won!")
        elif cpu_choice == "2" or cpu_choice == "5":
            print("The Player won!")
        else:
            print("It's a tie!")
    elif choice == "5":
        if cpu_choice == "2" or cpu_choice == "4":
            print("The CPU won!")
        elif cpu_choice == "1" or cpu_choice == "3":
            print("The Player won!")
        else:
            print("It's a tie!")
        