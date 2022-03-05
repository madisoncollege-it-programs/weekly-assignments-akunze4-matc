#!/usr/bin/env python3
#Author: Alex Kunze, Purpose: Midterms file looping, and comparing lines.
print("Name: Alex Kunze")

openFile = open("Midterm-if.txt", "r")
lineNumber = 0
Total = 0

for line in openFile:
    lineNumber += 1
    if "gmeach18@ed.gov" in line:
        Total += lineNumber - 1
    elif "248.253.63.149" in line:
        Total += lineNumber - 1
    elif "Whiteland" in line:
        Total += lineNumber - 1
    elif "80.222.19.190" in line:
        Total += lineNumber - 1
    elif "Kayley" in line:
        Total += lineNumber - 1
    elif "dcassyqw@microsoft.com" in line:
        Total += lineNumber - 1

print(f"The total is: {Total}")


openFile.close()
