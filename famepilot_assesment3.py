import math
from math import sqrt
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c= int(input("enter value of c: "))


def find_roots(a,b,c):
    if a == 0:
        print("a cant be zero")
    else:
        value = b**2 - 4*a*c
        root_value = math.sqrt(abs(value))

        if value > 0:
            root_1 = ((-b + root_value)/(2*a))
            root_2 = ((-b - root_value)/(2*a))
            print("this one")
            result = root_1,root_2

        elif value== 0:
            root_1 = (-b/(2*a))
            result = (root_1,0)


        else:
            root_1 = (str((-b/(2*a)))+(" +i"+str(root_value)))
            root_2 = (str((-b/(2*a)))+("-i"+str(root_value)))
            result = (root_1,root_2)

    print(result)


find_roots(a,b,c)