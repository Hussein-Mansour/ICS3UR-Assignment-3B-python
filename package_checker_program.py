#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Wed/May5/2021
# This program is a package checker program


def main():
    # this function checks if the package is accepted or not
    print("Hello and Welcome, our company wants to ask you for some information before entering!")
    print("")
    # input
    print("Weight of package:")
    weight_package = int(input("please enter the weight(kg):"))
    print("")
    print("Volume of package:")
    lenght_package = int(input("please enter the length (cm):"))
    width_package = int(input("please enter the width (cm):"))
    height_package = int(input("please enter the height (cm):"))

    # process 1
    volume = lenght_package * width_package * height_package

    # process 2 & output
    if ((weight_package <= 27) and (volume <= 10000)):
        print("\nyour package is accepted, you can enter.")
    elif ((weight_package >= 27) and (volume >= 10000)):
        print("\nyour package is not accepted")
        print("your weight should not be larger than 27 (kg).")
        print("your volume should not be larger than 10,000 cubic cm.")
    elif (weight_package >= 27):
        print("\nyour package is not accepted")
        print("your weight should not be larger than 27 (kg).")
    elif (volume >= 10000):
        print("\nyour package is not accepted")
        print("your volume should not be larger than 10,000 cubic cm.")
    else:
        print("please check your info again!")


if __name__ == "__main__":
    main()
