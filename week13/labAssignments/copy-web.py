#!/usr/bin/env python3
import requests

response = requests.get("https://notpurple.com")

print(f"{response.text}")

with open("my_web_file.html", "w") as jeff:
    jeff.write(response.text)

