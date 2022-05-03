#!/usr/bin/env python3
#Name: Alex Kunze, Purpose: Web scraping with beautiful soup
import requests,bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()
myHTML = bs4.BeautifulSoup(res.text,features="html.parser")
# print(type(myHTML))
print(f"Title: {myHTML.title.text}")
links = myHTML.find_all('a')
# links = myHTML.select('a')
print(f"First Link: {links[0]['href']}")
print(f"Second Link: {links[1]['href']}")

