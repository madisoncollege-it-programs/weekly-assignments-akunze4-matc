#!/usr/bin/env python3
#Author: Alex Kunze, Purpose: Midterms file looping, and comparing lines.
print("Name: Alex Kunze")

openFile = open("Midterm-if.txt", "r")
Total = 0

for line in openFile:

    if "gmeach18@ed.gov" in line:
        Total += int(line.split(",")[0])

    elif "248.253.63.149" in line:
        Total += int(line.split(",")[0])

    elif "Whiteland" in line:
        Total += int(line.split(",")[0])

    elif "80.222.19.190" in line:
        Total += int(line.split(",")[0])

    elif "Kayley" in line:
        Total += int(line.split(",")[0])

    elif "dcassyqw@microsoft.com" in line:
        Total += int(line.split(",")[0])


print(f"The total is: {Total}")


openFile.close()
