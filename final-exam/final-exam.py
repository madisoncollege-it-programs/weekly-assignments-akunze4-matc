#!/usr/bin/env python3
#Author: Alex Kunze, Purpose Finals project

import argparse
import requests
import json
import bs4

parser = argparse.ArgumentParser(description="This is Alex Kunzes' script")

parser.add_argument('-f', '--function', dest='Func',type=int,metavar="[a function from 1-5]", required=True, help="<required> Enter a simple Integer")
parser.add_argument('-i', '--ipaddress', dest='Ip', type=str,metavar="[an ip address]", required=True, help="Enter an IP address")

input_results = parser.parse_args()

# print(input_results)

ipVar = input_results.Ip
funcVar = input_results.Func


# Create the url that we want to connect to
# url = f"http://ipinfo.io/{sys.argv[1]}/json"
url = f"http://{ipVar}/q{funcVar}"
print("Name: Alex Kunze")
print(url)

# # # Forest of Functions

# Function 1
def get_response():
    res = requests.get(url)
    print(f"ANSWER: {res.text}")

# Function 2    
def parse_string():
    res = requests.get(url)
    # res.raise_for_status()
    myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
    # print(type(myHTML))
    #p rint(f"Title: {myHTML.title.text}")
    links = myHTML.find_all('h3')
    # links = myHTML.select('a')
    WouldthisWork = str(links)
    aa = WouldthisWork[9]
    ab = WouldthisWork[11]
    ac = WouldthisWork[13]
    ad = WouldthisWork[15]
    ae = WouldthisWork[17]
    af = WouldthisWork[19]
    ag = WouldthisWork[21]
    ah = WouldthisWork[23]
    total = aa + ab + ac + ad + ae + af + ag + ah
    print(f"ANSWER: {total} Alex")

# Function 3    
def parse_header():
    res = requests.get(url)
    print(f"ANSWER: {res.headers['MATC-HEADER']}")
    # res.raise_for_status()
    myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
    # print(type(myHTML))
    #p rint(f"Title: {myHTML.title.text}")
    links = myHTML.find_all('h3')
    # links = myHTML.select('a')
    # print(f"ANSWER: {Unknown} Alex")


# Function 4 
def parse_json():

    # url = f"http://ipinfo.io/{newVar}/json"

    # Send the "get" request to the web server
    jsonResp = requests.get(url)
    # Convert the returned json formatted text to a dictionary
#     dictResp = json.loads(jsonResp.text) 
    print(json.dumps(jsonResp.text))

    # for each key in the dictionary print the key and the data
#     for key in dictResp.keys():
#         print(f"{key: <10}:{dictResp[key]: <10}")





if input_results.Func == 1:
    get_response()

elif input_results.Func == 2:
    parse_string()

elif input_results.Func == 3:
    parse_header()

elif input_results.Func == 4:
    parse_json()



