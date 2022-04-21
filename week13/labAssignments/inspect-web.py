#!/usr/bin/env python3
import requests,bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()
myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
# print(type(myHTML))
print(myHTML.title.text)
print(myHTML.find_all('a'))
