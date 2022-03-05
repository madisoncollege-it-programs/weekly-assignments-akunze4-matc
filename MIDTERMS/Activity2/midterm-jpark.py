#!/usr/bin/env python3
#Author: Alex Kunze, Purpose: Flow Control relating to Jurassic Park.

midDict = {
        "Username" : "dnedry",
        "Password" : "please"
        }

command_database = {
        "reboot"    : "OK. I will reboot all park systems",
        "shutdown"  : "OK. I will shut down all park systems.",
        "done"      : "I hate all this hacker stuff."
        }

white_rabbit_object = 0
counter = 0

while counter <= 3 and white_rabbit_object == 0:
    input_user = input("Username: > ")
    input_password = input("Password: > ")
    if input_password in midDict.values() and input_user in midDict.values():
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")
        white_rabbit_object = 1
        print(command_database.keys())
        input_command = input("Command: --> ")
        if input_command == "reboot":
            print(command_database["reboot"])
        elif input_command == "shutdown":
            print(command_database["shutdown"])
        elif input_command == "done":
            print(command_database["done"])
        else:
            print("The lysine Contigency has been put into effect.")
    else:
        print("Authentication Failure")
        counter += 1
        if counter == 3:
            annoyance = "You didn't say the magic word"
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
            print(annoyance)
        else:
            print(f"You didn' say the magic word {counter}")

