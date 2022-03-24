#!/usr/bin/env python3
#Author: Alex Kunze
#Purpose: Converting Fahrenheit to Celsius


def F2C(Fahrenheit):

    Celsius = ((Fahrenheit - 32) * (5/9))
    return Celsius


def main():
    if __name__ == "__main__":
        global inputVar
        inputVar = float(input("Fahrenheit? "))
        print(f"Celsius {F2C(inputVar)}")

main()
