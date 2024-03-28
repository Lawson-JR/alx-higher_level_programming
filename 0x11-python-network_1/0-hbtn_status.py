#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':

  import urlib.request
  
  url = 'https://alx-intranet.hbtn.io/status'
  
  req = urlib.request.Request(url)
  with urllib.request.urlopen(req) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
