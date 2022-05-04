#!/usr/bin/env python3
#Author: Alex Kunze, Purpose Finals project

import argparse
import requests
import json
import bs4
import socket

parser = argparse.ArgumentParser(description="This is Alex Kunzes' script")

parser.add_argument('-f', '--function', dest='Func',type=int,metavar="[a number from 1-5]", required=True, help="<required> Enter a simple Integer")
parser.add_argument('-i', '--ipaddress', dest='Ip', type=str,metavar="[an ip address]", required=True, help="Enter an IP address")

input_results = parser.parse_args()

ipVar = input_results.Ip
funcVar = input_results.Func


url = f"http://{ipVar}/q{funcVar}"
print("Name: Alex Kunze")
print(url)



# Function 1
def get_response():
    res = requests.get(url)
    print(f"ANSWER: {res.text}")


# Function 2    
def parse_string():
    res = requests.get(url)
    myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
    links = myHTML.find_all('h3')
    WouldthisWork = str(links)
    aa = WouldthisWork[9]
    ab = WouldthisWork[11]
    ac = WouldthisWork[13]
    ad = WouldthisWork[15]
    ae = WouldthisWork[17]
    af = WouldthisWork[19]
    ag = WouldthisWork[21]
    ah = WouldthisWork[23]
    ai = WouldthisWork[25]
    total = aa + ab + ac + ad + ae + af + ag + ah + ai
    print(f"ANSWER: {total} Alex")


# Function 3    
def parse_header():
    res = requests.get(url)
    print(f"ANSWER: {res.headers['MATC-HEADER']}")
    myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
    links = myHTML.find_all('h3')


# Function 4 
def parse_json():

    jsonResp = requests.get(url)
    dictResp = json.loads(jsonResp.text) 
    for key in dictResp:
        for thing in dictResp[key]:
            if "The Shining" in str(thing):
                whatVar = str(thing)
                whutVar = whatVar.replace("{", "")
                whotVar = whutVar.replace("}", "")
                stunkVar = whotVar.split(",")
                for i in stunkVar:
                    if "publisher" in i:
                        lol = i.replace("publisher", "")
                        lool = lol.replace("'", "")
                        loool = lool.replace(":", "")
                        print(f"ANSWER: {loool.replace(' ', '')}")



# Function 5

def socket_client():

    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SND_DATA = "secret"
    RCV_DATA = ""

    list = []

    for port in range(5000,6000):

        try:
            C_SOCK.connect((ipVar, port))
            #list.append(port)
            C_SOCK.send(bytearray(SND_DATA, "utf8"))
            RCV_DATA = C_SOCK.recv(1024)
            print(f"ANSWER: {RCV_DATA.decode()}")

        except:
            pass

    #print(f"Open ports: {list}")




if input_results.Func == 1:
    get_response()

elif input_results.Func == 2:
    parse_string()

elif input_results.Func == 3:
    parse_header()

elif input_results.Func == 4:
    parse_json()

elif input_results.Func == 5:
    socket_client()

