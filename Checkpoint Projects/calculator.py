import math

if __name__ == "__main__":

    print("==================")
    print("Area Calculator 📐")
    print("==================\n")

    print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit\n")

    choice = int(input("Which Shape: "))

    if choice == 1:
        height = int(input("Height: "))
        base = int(input("Base: "))
        print("The area is", ((height*base)/2) )
    elif choice == 2:
        length = int(input("Length: "))
        width = int(input("Width: "))
        print("The area is", (length*width) )
    elif choice == 3:
        side = int(input("Side: "))
        print("The area is", (side ** 2) )
    elif choice == 4:
        radius = int(input("Radius: "))
        print("The area is", (math.pi * (radius ** 2) ))
    else:
        print("Goodbye!")
        quit
        

    
