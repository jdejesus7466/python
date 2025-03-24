def welcome():
    print("Hi Welcome to BurgerMart, here is our menu!\n"
          "1) 🍔 Cheeseburger\n"
          "2) 🍟 Fries\n"
          "3) 🥤 Soda\n"
          "4) 🍦 Ice Cream\n"
          "5) 🍪 Cookie")
    
def get_item(item):
    return food_menu[item]

if __name__ == "__main__":

    food_menu = {
        1 : "🍔 Cheeseburger",
        2 : "🍟 Fries",
        3 : "🥤 Soda",
        4 : "🍦 Ice Cream",
        5 : "🍪 Cookie"
    }

    welcome()

    choice = int(input("What would you like today? "))

    print("Here is your food, thank you!", get_item(choice))



