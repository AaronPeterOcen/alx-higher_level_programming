#!/usr/bin/python3
"""
fetches alx url
"""
import urllib.request

# response = urllib.request.urlopen("https://unsplash.com/s/photos/ford-bronco")
# print(response)

# #print(response.status)
# print(response.read)

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read().decode("utf-8")

    for line in body.splitlines():
        print("\t- {}".format(line))
