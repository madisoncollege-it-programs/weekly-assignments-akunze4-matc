#!/usr/bin/env python3
#Author: Alex Kunze
#Purpose: Understanding subprocess module

import subprocess

myProc = subprocess.run(['ps','-axco', 'command']\
        ,stdout=subprocess.PIPE)

myProcString = myProc.stdout.decode()
myProcList = myProcString.strip().split('\n')


whatVar = myProcList[1::]
for i in whatVar:
    print(i)

lastVar = len(myProcList)
print(f"Total counted number of processes: {lastVar}")
