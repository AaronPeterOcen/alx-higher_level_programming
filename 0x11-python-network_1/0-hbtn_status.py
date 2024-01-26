#!/usr/bin/python3
"""
fetches alx url from  https://alx-intranet.hbtn.io/status
"""
import urllib.request

# response = urllib.request.urlopen("https://unsplash.com/s/photos/ford-bronco")
# print(response)

# #print(response.status)
# print(response.read)

if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
