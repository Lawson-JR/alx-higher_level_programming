#!/usr/bin/pyhton3

import urllib.request
import urllib.parse
import sys

def main(url, email):
  # Encode the email parameter
  data = urllib.parse.urlencode({'email': email}.encode('utf-8'))

  # Make a POST request to the URl with email as a parameter
  req = urllib.request.Request(url, data=data, method='POST')
  with urllib.request.urlopen(req) as response:
    # Decode an display the body of the response
    print(response.read().decode('utf-8'))

if __name__ == "__main__":
  # Get URL and email from command ine arguments
  url = sys.argv[1]
  email = sys.argv[2]

  main(url, email)
