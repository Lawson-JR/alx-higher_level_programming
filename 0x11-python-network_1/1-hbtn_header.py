#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL and displays the value
- of the X-Request-Id variable found in the header ofthe response.
"""

import urllib.request
import sys


if __name__ == '__main__':
    # Check if a URL is provided as an argument
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument")
        sys.exit()
    
    url = sys.argv[1]
    
    # Send a request to the URL and retrieve the X-Request-Id value from the response header
    req = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get('X-request-Id'))    
