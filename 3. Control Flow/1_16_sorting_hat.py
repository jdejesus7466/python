if __name__ == "__main__":

    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0

    ans1 =  int(input("Q1) Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n" ))

    if ans1 == 1:
        gryffindor += 1
        ravenclaw += 1
    elif ans1 == 2:
        hufflepuff += 1
        slytherin += 1
    else:
        print("Wrong Input")

    ans2 = int(input("Q2) When I’m dead, I want people to remember me as: \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n"))

    if ans2 == 1:
        hufflepuff += 2
    elif ans2 == 2:
        slytherin += 2
    elif ans2 == 3:
        ravenclaw += 2
    elif ans2 == 4:
        gryffindor += 2
    else:
        print("Wrong Input")

    ans3 = int(input("Q3) Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n"))

    if ans3 == 1:
        slytherin += 4
    elif ans3 == 2:
        hufflepuff += 4
    elif ans3 == 3:
        ravenclaw += 4
    elif ans3 == 4:
        gryffindor += 4
    else:
        print("Wrong Input")

    
    print("gryffindor: " + str(gryffindor))
    print("hufflepuff: " + str(hufflepuff))
    print("ravenclaw: " + str(ravenclaw))
    print("slytherin: " + str(slytherin))

    #BONUS: House with the most points...

    houses = {
        "Gryffindor": gryffindor,
        "Hufflepuff": hufflepuff,
        "Ravenclaw": ravenclaw,
        "Slytherin": slytherin
    }

    print("Your House Was...: " + str(max(houses, key=houses.get)))