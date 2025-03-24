if __name__ == "__main__":
    
    class Restaurant:
        name = ""
        category = ""
        rating = 0.0
        delivery = False
    
    bobs_burgers = Restaurant()

    bobs_burgers.name = "Bob\'s Burgers"
    bobs_burgers.category = "American Diner"
    bobs_burgers.rating = "4.7"
    bobs_burgers.delivery = False

    zabas = Restaurant()

    zabas.name = "Zabas Mexican Grill"
    zabas.category = "Mexican Grill"
    zabas.rating = "4.5"
    zabas.delivery = True

    manna = Restaurant()

    manna.name = "Manna KBBQ"
    manna.category = "KBBQ"
    manna.rating = "5.0"
    manna.delivery = False

    print(vars(bobs_burgers))
    print(vars(zabas))
    print(vars(manna))