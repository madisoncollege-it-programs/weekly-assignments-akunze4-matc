#!/usr/bin/env python3
#Author: Alex Kunze
#Purpose: Messing with Dictonaries

#1
myDict = {
        "server1.testlab.com": "192.168.1.10",
        "server2.testlab.com": "192.168.1.11",
        "server3.testlab.com": "192.168.1.12",
        "server4.testlab.com": "192.168.1.13",
        "server5.testlab.com": "192.168.1.14",
        "server6.testlab.com": "192.168.1.15"
}

#2
# print(myDict.keys())

#3
# for item in sorted(myDict):
#     print(myDict[item])

#4
# print(myDict.items())

#5
myDict["server7.testlab.com"] = "192.168.1.16"
myDict["server8.testlab.com"] = "192.168.1.17"

#6
# print("server7.testlab.com" in myDict.keys())

#7
print("server10.testlab.com" in myDict.keys())
