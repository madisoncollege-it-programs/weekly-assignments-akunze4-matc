#!/usr/bin/env python3

'''
Name: Alex Kunze
Purpose: Acting as a client side for the file transfer
NOTE: I used to base for the client from the slides
'''

import socket

RHOST    = '192.168.1.5'
RPORT    = 5000
SND_DATA = ""
RCV_DATA = ""


C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

while True:
    x = input("Enter the name of the file in which shall be sent to the server: ")
    if x == "exit":
        break
    else:
        try:
            filePath = open(x, "rb")
            SND_DATA = filePath.read(1024)
            filePath.close()
            C_SOCK.send(SND_DATA)
            print("Ok... and? ...")
        except:
            print("Something went wrong..., the file probably doesn't exist")


RCV_DATA = C_SOCK.recv(1024)
print(RCV_DATA.decode())
C_SOCK.close()

