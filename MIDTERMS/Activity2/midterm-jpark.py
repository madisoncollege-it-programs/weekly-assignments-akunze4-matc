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
input_user = input("Username: > ")
input_password = input("Password: > ")

while white_rabbit_object == 0 and counter <= 3:
    for thing in midDict.values():
        if input_user == thing:
            for thang in midDict.values():
                if input_password == thang:
                    print("Loogin Sucessful")
                    white_rabbit_object = 1
                    print(command_database.keys())
                    input_command = input("Command > ")
                    if input_command == "reboot":
                        print(command_database["reboot"])
                    if input_command == "shutdown":
                        print(command_database["shutdown"])
                    if input_command == "done":
                        print(command_database["done"])
                    else:
                        print("The Lysine Contigency has been put into effect.")
        else:
            if white_rabbit_object != 1:
                print("Loogin Failure")
            white_rabbit_object = 1
            counter + 1
