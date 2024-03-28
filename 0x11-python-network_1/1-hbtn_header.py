#!/usr/bin/python3
import urllib.request
import sys

# Check if a URL is provided as an argument
if len(sys.argv) < 2:
    print("Please provide a URL as an argument")
    sys.exit()

url = sys.argv[1]

# Send a request to the URL and retrieve the X-Request-Id value from the response header
try:
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"The value of X-Request-Id: {x_request_id}")
        else:
            print("X-Request-Id not found in the response header")
except urllib.error.URLError as e:
    print(f"Error accessing the URL: {e}")
