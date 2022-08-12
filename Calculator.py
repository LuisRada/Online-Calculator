import math
import string
from math import *

import datetime

import numpy as np
import matplotlib.pyplot as plt


def expo(n1, n2):
    return pow(n1, n2)


def raiz(n1):
    return sqrt(n1)


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def suma(n1, n2):
    return n1 + n2


def res(n1, n2):
    return n1 - n2


def inv(n1):
    return 1 / n1


def sin(n1):
    return math.sin(n1)


def cos(n1):
    return math.cos(n1)


def tan(n1):
    return math.tan(n1)


def ctg(n1):
    return 1 / math.tan(n1)


def sec(n1):
    return 1 / math.cos(n1)


def csc(n1):
    return 1 / math.sin(n1)


def asin(n1):
    return math.asin(n1)


def acos(n1):
    return math.acos(n1)


def atan(n1):
    return math.atan(n1)


def actg(n1):
    return math.atan(inv(n1))


def asec(n1):
    return math.acos(inv(n1))


def acsc(n1):
    return math.asin(inv(n1))


def hip(n1, n2):
    return sqrt(pow(n1, 2) + pow(n2, 2))


def cate(n1, n2):
    return sqrt(pow(n1, 2) - pow(n2, 2))


def sinla(n1, n2, n3):
    return math.asin((n3 * math.sin(math.radians(n1))) / n2) * 180 / math.pi


def sinll(n1, n2, n3):
    return (n2 * math.sin(math.radians(n3))) / math.sin(math.radians(n1))


def cosll(n1, n2, n3):
    return sqrt(n1 * n1 + n2 * n2 - 2 * n1 * n2 * math.cos(math.radians(n3)))


def cosla(n1, n2, n3):
    return math.acos((n1 * n1 - n2 * n2 - n3 * n3) / (-2 * n2 * n3)) * 180 / math.pi


def main():
    print("1- Sum\n"
          "2- Difference\n"
          "3- Multiplication\n"
          "4- Division\n"
          "5- Square root\n"
          "6- Exponential operation\n"
          "7- Trigonometry\n"
          "8- Matrix\n"
          "9- Polynomial operation\n")
    op = input("Enter the number of the operation you wanna make:\n")

    if op == "1":
        print("Let's make a sum")
        while True:
            try:
                n1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue

        while True:
            try:
                n2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        print(suma(n1, n2))

    elif op == "2":
        print("Let's make a subtraction")
        while True:
            try:
                n1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue

        while True:
            try:
                n2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        print(res(n1, n2))

    elif op == "3":
        print("Let's make a multiplication")
        while True:
            try:
                n1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue

        while True:
            try:
                n2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        print(mult(n1, n2))

    elif op == "4":
        print("Let's make a division")
        while True:
            try:
                n1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue

        while True:
            try:
                n2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        if n2 != 0:
            results = n1 / n2
        else:
            print("Division by Zero can't be done")
            results = ""

        print(results)

    elif op == "5":
        print("Let's make an square root")
        while True:
            try:
                n1 = float(input("Enter the base number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        print(raiz(n1))

    elif op == "6":
        print("Let's make an exponential operation")
        while True:
            try:
                n1 = float(input("Enter the base number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        while True:
            try:
                n2 = float(input("Enter the exponent number: "))
                break
            except ValueError:
                print("Please, enter the correct syntax")
                continue
        print(expo(n1, n2))

    elif op == "7":
        print("Let's make some trigonometric operations")
        print("1- Trigonometric functions\n"
              "2- Graphs\n"
              "3- Triangles\n")
        opt = input("Enter the number of the operation you wanna make:\n")

        def main7_1():
            global n1
            if opt == "1":
                menu1 = """
Welcome to the Trigonometric function's menu, here you can find some helpful operations 
related with trigonometric operations, such as:
1- Find the basic trigonometric functions
2- Convert Degrees - radians
3- Find the basic inverse trigonometric functions
            """
                print(menu1)
                opt1 = input("Enter the number of the operation you wanna make:\n")
                if opt1 == "1":
                    while True:
                        try:
                            n1 = float(input("Enter the base number: "))
                            break
                        except ValueError:
                            print("Please, enter the correct syntax")
                            continue
                    print("Sin = ", sin(n1))
                    print("Cos = ", cos(n1))
                    print("Tan = ", tan(n1))
                    print("Ctg = ", ctg(n1))
                    print("Sec = ", sec(n1))
                    print("Csc = ", csc(n1))

                elif opt1 == "2":
                    while True:
                        try:
                            n1 = float(input("Enter the degree number: "))
                            break
                        except ValueError:
                            print("Please, enter the correct syntax")
                            continue
                    rads = (n1 * math.pi) / 180
                    print(rads)

                elif opt1 == "3":
                    while True:
                        try:
                            n1 = float(input("Enter the base number: "))
                            break
                        except ValueError:
                            print("Please, enter the correct syntax")
                            continue
                    if -1 <= n1 <= 1:
                        print("Arc-Sin = ", asin(n1))
                    else:
                        print("Arc-Sin is not possible")

                    if -1 <= n1 <= 1:
                        print("Arc-Cos = ", acos(n1))
                    else:
                        print("Arc-Cos is not possible")

                    print("Arc-Tan = ", atan(n1))
                    print("Arc-Ctg = ", actg(n1))

                    if -1 < n1 < 1:
                        print("Arc-Sec and Arc-Csc are not possible")
                    else:
                        print("Arc-Sec = ", asec(n1))
                        print("Arc-Csc = ", acsc(n1))




                else:
                    print("That's not a valid option, Let's start again")
                    return main7_1()

        main7_1()

        def main7_2():
            if opt == "2":
                menu1 = """
Welcome to the Graph menu, here you can find some helpful operations 
related with trigonometric operations, such as:
1- Graph a function
2- Graph a trigonometric function
                """
                print(menu1)
                opt1 = input("Enter the number of the operation you wanna make:\n")
                if opt1 == "1":
                    while True:
                        try:
                            n1 = float(input("Enter the base number: "))
                            break
                        except ValueError:
                            print("Please, enter the correct syntax")
                            continue
                    print("Sin = ", sin(n1))
                    print("Cos = ", cos(n1))
                    print("Tan = ", tan(n1))
                    print("Ctg = ", ctg(n1))
                    print("Sec = ", sec(n1))
                    print("Csc = ", csc(n1))

                elif opt1 == "2":
                    while True:
                        try:
                            n1 = float(input("Enter the degree number: "))
                            break
                        except ValueError:
                            print("Please, enter the correct syntax")
                            continue
                    rads = (n1 * math.pi) / 180
                    print(rads)

                else:
                    print("That's not a valid option, Let's start again")
                    return main7_2()

        main7_2()

        def main7_3():
            if opt == "3":
                menu1 = """
Welcome to the Triangle's menu, here you can find some helpful operations 
related with trigonometric operations, such as:
1- Square triangles
2- Non square triangles
                        """
                print(menu1)
                opt1 = input("Enter the number of the operation you wanna make:\n")
                if opt1 == "1":
                    menu2 = """
Welcome to the Square triangle's menu, here you can find some helpful operations 
related with pythagora's theorem, such as:
1- find the hypotenuse
2- find the cathetus
                    """
                    print(menu2)
                    opt2 = input("Enter the number of the operation you wanna make:\n")
                    if opt2 == "1":
                        while True:
                            try:
                                n1 = float(input("Enter the first cathetus: "))
                                break
                            except ValueError:
                                print("Please, enter the correct syntax")
                                continue

                        while True:
                            try:
                                n2 = float(input("Enter the second cathetus: "))
                                break
                            except ValueError:
                                print("Please, enter the correct syntax")
                                continue
                        print(hip(n1, n2))

                    elif opt2 == "2":
                        while True:
                            try:
                                while True:
                                    try:
                                        n1 = float(input("Enter the hypotenuse: "))
                                        break
                                    except ValueError:
                                        print("Please, enter the correct syntax")
                                        continue

                                while True:
                                    try:
                                        n2 = float(input("Enter the cathetus: "))
                                        break
                                    except ValueError:
                                        print("Please, enter the correct syntax")
                                        continue

                                if n1 > n2:
                                    print("")
                                    break
                                else:
                                    print(
                                        "The value of the hypotenuse must be higher than the cathetus, please try again")
                            except ValueError:
                                print("")
                                continue

                        print(cate(n1, n2))

                elif opt1 == "2":
                    menu2 = """
Welcome to the Non square triangle's menu, here you can find some helpful operations 
related with Trigonometric operations, such as:
1- Use the Sin law
2- Use the Cos law
                                        """
                    print(menu2)
                    opt2 = input("Enter the number of the operation you wanna make:\n")
                    if opt2 == "1":
                        menu3 = """
Welcome to the Sin law menu, here you can find some helpful operations 
related with Trigonometric operations, such as:
1- find an angle of the triangle
2- find a side of the triangle
"""
                        print(menu3)
                        opt3 = input("Enter the number of the operation you wanna make:\n")
                        if opt3 == "1":
                            print("Please keep in mind the following structure for the Sin law =\n"
                                  "(Sin A)/a = (Sin B)/b == (Sin N1)/N2 = (Sin x)/N3")
                            while True:
                                try:
                                    n1 = float(input("Enter the first number (N1): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue

                            while True:
                                try:
                                    n2 = float(input("Enter the second number (N2): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            while True:
                                try:
                                    n3 = float(input("Enter the third number (N3): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            print(sinla(n1, n2, n3))

                        elif opt3 == "2":
                            print("Please keep in mind the following structure for the Sin law =\n"
                                  "(Sin A)/a = (Sin B)/b ==> (Sin N1)/N2 = (Sin N3)/x")
                            while True:
                                try:
                                    n1 = float(input("Enter the first number (N1): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue

                            while True:
                                try:
                                    n2 = float(input("Enter the second number (N2): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            while True:
                                try:
                                    n3 = float(input("Enter the third number (N3): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            print(sinll(n1, n2, n3))

                    elif opt2 == "2":
                        menu3 = """
Welcome to the Cos law menu, here you can find some helpful operations 
related with Trigonometric operations, such as:
1- find a side of the triangle
2- find an angle of the triangle
"""
                        print(menu3)
                        opt2 = input("Enter the number of the operation you wanna make:\n")
                        if opt2 == "1":
                            print("Please keep in mind the following structure for the Cos law =\n"
                                  "a^2 = b^2 + c^2 - 2*b*c*cos A  ==>  x = N1^2 + N2^2 - 2*N1*N2*cos N3 ")
                            while True:
                                try:
                                    n1 = float(input("Enter the first number (N1): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue

                            while True:
                                try:
                                    n2 = float(input("Enter the second number (N2): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            while True:
                                try:
                                    n3 = float(input("Enter the third number (N3): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            print(cosll(n1, n2, n3))

                        elif opt2 == "2":
                            print("Please keep in mind the following structure for the Cos law =\n"
                                  "a^2 = b^2 + c^2 - 2*b*c*cos A  ==>  x = Arc-cos((N1^2 - N2^2 - N3^2) / (-2*N2*N3)) ")
                            while True:
                                try:
                                    n1 = float(input("Enter the first number (N1): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue

                            while True:
                                try:
                                    n2 = float(input("Enter the second number (N2): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            while True:
                                try:
                                    n3 = float(input("Enter the third number (N3): "))
                                    break
                                except ValueError:
                                    print("Please, enter the correct syntax")
                                    continue
                            print(cosla(n1, n2, n3))


                else:
                    print("That's not a valid option, Let's start again")
                    return main7_3()

        main7_3()


    elif op == "8":
        print("Let's make some Matrix operations")
        print("1- Arithmetic operations\n"
              "2- Determinant\n"
              "3- Inverse matrix\n"
              "4- Adjunct matrix\n"
              "5- Range\n")
        opt = input("Enter the number of the operation you wanna make:\n")

    elif op == "9":
        print("Let's make some Polynomial operations")
        print("1- Trigonometric functions\n"
              "2- Graphs\n"
              "3- Triangles\n"
              "4- \n")
        opt = input("Enter the number of the operation you wanna make:\n")

    else:
        print("That's not a valid option, Let's start again")
        return main()


m = datetime.datetime.now()
time = m.hour

print("Welcome to the calculator")
name = input("What is your name? :")
print("Hello " + name + ", Let's make some calculations!!!")

end_program = False
while not end_program:
    main()
    _continue = True

    while _continue != False:
        _continue = input("Would you like to continue?: ").upper()
        if _continue == "NO":
            print(f"Thank you {name} for using this calculator, I hope to see you soon")
            if time < 12:
                print("Have a good Morning")
            elif time < 15:
                print("Have a good Afternoon")
            elif time < 20:
                print("Have a good Evening")
            else:
                print("Have a good Night")
            print(f"Bye!!!\n")
            end_program = True
            _continue = False
        elif _continue == "YES":
            print("Okay!!!, let´s do it again")
            _continue = False
        else:
            print("Bad input")

