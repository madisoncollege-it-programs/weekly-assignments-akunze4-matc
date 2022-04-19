#!/usr/bin/env python3
#Name: Alex Kunze

import socket

RHOST    = '192.168.1.5'
RPORT    = 5000
SND_DATA = ""
RCV_DATA = ""


C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

while True:
    x = input("Enter some data: ")
    if x == "exit":
        break
    else:
        SND_DATA = x
        C_SOCK.send(bytearray(SND_DATA, "utf8"))


RCV_DATA = C_SOCK.recv(1024)
print(RCV_DATA.decode())
C_SOCK.close()

