#!/usr/bin/python3
"""Display the X-Request-Id header of a request to a certain URL
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
