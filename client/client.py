#!/usr/bin/env python3

# client.py
import os
import requests

import time

def get_secret_message():
    url = os.environ["SECRET_URL"]
    response = requests.get(url)
    print(f"The secret message is: {response.text}")

if __name__ == "__main__":
    
    while True:
        time.sleep( 10 )