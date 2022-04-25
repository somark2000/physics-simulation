#imports
import math

#quadratic equation solver for fall time:
def quad(a,b,c):
    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)
    print("quad")
    print(a)
    print(b)
    print(c)
    print(d)
    print("----")

    # find two solutions
    sol1 = float((-b - math.sqrt(d)) / (2 * a))
    sol2 = float((-b + math.sqrt(d)) / (2 * a))

    return max(sol1,sol2)