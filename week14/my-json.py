#!/usr/bin/env python3

import argparse
import sys
import requests
import json

parser = argparse.ArgumentParser(description="This is Alex Kunzes' script")

# parser.add_argument('-m', dest='Basic',type=str, help="Enter some text")
# parser.add_argument('-i', '--integer', dest='Integer',type=int,metavar="[an integer]", required=True, help="<required> Enter a simple Integer")
# parser.add_argument('-d', '--float', dest='Float', type=float,metavar="[a float]", help="Enter a simple float")
# parser.add_argument('-s', '--string', dest='String', type=str,metavar="[a string]", help="Enter a simple string")
parser.add_argument('-ip', '--ip-address', dest='Ip', type=str,metavar="[an ip address]", help="Enter an IP address")
# parser.add_argument('-l', dest='Strings', nargs='+',metavar="[strings]", help="Enter a list of strings (space delimited)")
# parser.add_argument('-t','--set-true', default=False, action='store_true', help='Toggle from default False to True')
# parser.add_argument('-f','--set-false', default=True,action='store_false', help='Toggle from default True to False')
# parser.add_argument('-v', '--version',action='version',version='1.0', help="shows program's version number and exit")

input_results = parser.parse_args()

# print(input_results)

# print(f"Basic entry: {input_results.Basic}")
# print(f"Integer Entry: {input_results.Integer}")
# print(f"Float Entry: {input_results.Float}")
# print(f"String Entry: {input_results.String}")
# print(f"Strings Entry: {input_results.Strings}")

newVar = input_results.Ip


# Create the url that we want to connect to
# url = f"http://ipinfo.io/{sys.argv[1]}/json"
url = f"http://ipinfo.io/{newVar}/json"

# Send the "get" request to the web server
jsonResp = requests.get(url)
# Convert the returned json formatted text to a dictionary
dictResp = json.loads(jsonResp.text) 

# for each key in the dictionary print the key and the data
for key in dictResp.keys():
    print(f"{key: <10}:{dictResp[key]: <10}")

