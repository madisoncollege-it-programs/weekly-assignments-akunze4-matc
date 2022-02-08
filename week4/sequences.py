#!/usr/bin/env python3

"""
Author: Alex Kunze
Purpose: Messing with lists, and  strings.
"""

#1
varString = "Here is a nice string to slice"
varList = ["Here", "is", "a", "nice", "list", "to", "slice"]

#2
print(f"{varString[3::]}\n {varString[0:3]}\n {varString[3:12]}\n {varString[::2]}\n {varString[::-1]}")

#3
print(f"{varList[::-1]}")
print(f"{varList[2::-1]}")
print(f"{varList[2:4]}")
print(f"{varList[::3]}")
print(f"{varList[1::]}")

#4
for i in varString.split(" "):
    print(f"{i}\n")

#5
for i in varList:
    print(f"{i}\n")
