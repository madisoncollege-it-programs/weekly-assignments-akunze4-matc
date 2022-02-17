#!/usr/bin/env python3
#Author: Alex Kunze, #Purpose: Managing files practice


print("Question A below\n")


openFile = open("/etc/passwd", "r")

unifiedfileString = openFile.read()
print(f"Number of items in the single unified string - {len(unifiedfileString)}")
print("We want to use the read() function when we want to put all the contents of a given file into a string ")
print(f"\n")

openFile.close()



print("Question B below\n")


openFile = open("/etc/passwd", "r")

filenewlineString = openFile.readlines()
print(f"Number of lines within in /etc/passwd list - {len(filenewlineString)}")
print("We want to use the readlines() function, when we want to put the contents of a file into a list.")
print(f"\n")

openFile.close()


print("Question C below")


openFile = open("/etc/passwd", "r")
count = 0
for line in openFile:
    #print(f"{openFile.readline()}", end='')
    count += len(line)

print("\n")
print(f"Number of items within the /etc/passwd file - {count}")
print("We use this method when we need to loop over an extremely large file,")
print("without the need to open the entire file at once!")


openFile.close()
