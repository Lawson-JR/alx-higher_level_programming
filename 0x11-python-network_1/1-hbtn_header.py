#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

import urllib.request
import sys

# Check if a URL is provided as an argument
if len(sys.argv) < 2:
    print("Please provide a URL as an argument")
    sys.exit()

url = sys.argv[1]

# Send a request to the URL and retrieve the X-Request-Id value from the response header
req = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(dict(x_request_id))
    else:
        print("X-Request-Id not found in the response header")
