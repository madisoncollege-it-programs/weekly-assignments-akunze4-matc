#!/usr/bin/env python3

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#Question 1
print(f"Hello {varName: ^0s}")

#Question 2 
print(f"{varRed:-<4s}{varGreen:-<6s}{varBlue: ^s}")

#Question 3 
print(f"Is this {varGreen.lower(): ^0s} or {varBlue.lower(): ^0s}?")

#Question 4
print(f"My name is {varName.upper(): ^0s}")

#Question 5
print(f"[{varRed:+^7s}]")

#Question 6
print(f"[{varGreen.lower():=<7}]")

#Question 7
print(f"[{varBlue.lower():*>9s}]")

#Question 8
print(f"{varBlue*10: ^0s}")

#Question 9
print(f"{varLoot: ^0f}")

#Question 10
print(f"{varLoot: ^.1f}")

#Question 11
print(f"I have ${varLoot: ^.2f}")

#Question 12
print(f"[{varRed:$^9s}$] [{varGreen:$^10s}$] [{varBlue:$^11s}]")

#Question 13
print(f"[{varRed[::-1]: ^7s}] [{varGreen: ^7s}] [{varBlue[::-1]: ^7s}]")

#Question 14 
print(f"First Color:[{varRed: ^0s}] Second Color:[{varGreen: ^0s}] Third Color:[{varBlue: ^0s}]")
