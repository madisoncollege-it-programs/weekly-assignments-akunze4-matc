#!/usr/bin/env python3
import requests

# The get function will go to the specified URL and get the HTML
response = requests.get("https://madisoncollege.edu")

# Raise an exception if we did not get a good response code
try:
    response.raise_for_status()

    # Inspect the response object we get back
    print(type(response))
    print(f"Status Code: {response.status_code}")
    print(f"Text: {response.text[:250]}")
except Exception as exc:
    print(f"There was an error {exc}")
    

