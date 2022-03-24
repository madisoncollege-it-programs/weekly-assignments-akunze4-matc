#!/usr/bin/env python3
#Author: Alex Kunze
#Purpose: Converting Celsius to Fahrenheit


def C2F(Celsius):

    Fahrenheit = ((Celsius * (9/5)) + 32)
    return Fahrenheit


def main():
    if __name__ == "__main__":
        global inputVar
        inputVar = float(input("Celsius? "))
        print(f"Fahrenheit {C2F(inputVar)}")

main()
