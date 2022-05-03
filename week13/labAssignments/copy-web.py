#!/usr/bin/env python3
#Name: Alex Kunze, Purpose: Using requests to download webpage
import requests

response = requests.get("https://notpurple.com")

print(f"{response.text}")

with open("my_web_file.html", "w") as jeff:
    jeff.write(response.text)

