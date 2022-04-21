#!/usr/bin/env python3

'''
Name: Alex Kunze
Purpose: Acting as a server side for the file transfer
NOTE: I used to base for the server from the slides
'''

import socket

LHOST = ''
LPORT = 5000
RCV_DATA = ""         	

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind((LHOST, LPORT))

while True:
    	L_SOCK.listen(1)
    	L_CONN, addr = L_SOCK.accept()
    	print('Connected by', addr)
    	while True:
            RCV_DATA = L_CONN.recv(1024)
            if not RCV_DATA: break
            x = input("Enter filename to which the file shall be copied to: ")
            print("Thanks for your cooperation")
            weirdVar = open(x, "wb")
            weirdVar.write(RCV_DATA)
            weirdVar.close()
            # This line sends the data back to the client
            L_CONN.sendall(RCV_DATA)

    	L_CONN.close()

