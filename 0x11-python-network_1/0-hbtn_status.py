#!/usr/bin/python3
import urlib.request

url = 'https://alx-intranet.hbtn.io/status'

req = urlib.request.Request(url)
with urllib.request.urlopen(req) as response:
  body = response.read()
  print("Body response:")
  print("\t- type:", type(body))
  print("\t- content:", body)
  print("\t- utf8 content:", body.decode('utf-8'))
