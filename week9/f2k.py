#!/usr/bin/env python3
#Author: Alex Kunze
#Purpose: Converting Fahrenheit to Celsius


def F2C(Fahrenheit):

    Kelvin = (5/9 * (Fahrenheit - 32) + 273.15)
    return Kelvin
# K = 5/9(F - 32) + 273.15

def main():
    global inputVar
    inputVar = float(input("Fahrenheit? "))
    if __name__ == "__main__":
        print(f"Kelvin = {F2C(inputVar):^.1f}")

main()
