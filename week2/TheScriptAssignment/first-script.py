#!/usr/bin/env python3
first_name = "Alex"
last_name = "Kunze"
print(f"My name is {first_name} {last_name}")

x = input("Would you like to see what I learned this week in python scripting?, Yes/No > ")
xy = x.lower()
if xy == "yes":
    print("I learned how to do the special formatting, with the print command")
    print("I also learned about using end =' ' which basically allows you to print multiple lines")
    print("of code on the same line!")
elif xy == "no":
    print(" Sad Face ")


