#!/usr/bin/env python3
#Name: Alex Kunze
#Purpose: Using Json

import argparse

parser = argparse.ArgumentParser(description="This is Alex Kunzes' script")

parser.add_argument('-ip', '--ip-address', dest='Ip', type=str,metavar="[a string]", help="Enter a simple string")

input_results = parser.parse_args()

newVar = input_results.Ip

import sys
import requests
import json

# Create the url that we want to connect to
# url = f"http://ipinfo.io/{sys.argv[1]}/json"
url = f"http://ipinfo.io/{newVar}/json"

# Send the "get" request to the web server
jsonResp = requests.get(url)
# Convert the returned json formatted text to a dictionary
dictResp = json.loads(jsonResp.text) 

# for each key in the dictionary print the key and the data
for key in dictResp.keys():
    print(f"{key: <10}: {dictResp[key]: <10}")

