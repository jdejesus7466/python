import math

if __name__ == "__main__":
    
    a = int(input())
    b = int(input())
    c = int(input())

    quad_plus = (-b + math.sqrt( (b**2) - (4*a*c))) / (2 * a)
    quad_minus = (-b - math.sqrt( (b**2) - (4*a*c))) / (2 * a)

    print(quad_plus)
    print(quad_minus)