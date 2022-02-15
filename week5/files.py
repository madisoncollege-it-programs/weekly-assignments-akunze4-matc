#!/usr/bin/env python3
#Author: Alex Kunze, #Purpose: Managing files practice


# A


openFile = open("/etc/passwd", "r")

unifiedfileString = openFile.read()
print(f"Number of items in the single unified string - {len(unifiedfileString)}")
print("We want to use the read() function when we want to put all the contents of a given file into a string ")

openFile.close()


# B


print(f"\n\n")

openFile = open("/etc/passwd", "r")

filenewlineString = openFile.readlines()
print(f"Number of lines within in /etc/passwd list - {len(filenewlineString)}")
print("We want to use the readlines() function, when we want to put the contents of a file into a list.")

openFile.close()


# C


openFile = open("/etc/passwd", "r")

 fileonelineStringer = openFile.readline()

count = 0
for line in fileonelineStringer:
    count += 1
print(count)

openFile.close()





