#!/usr/bin/python3
import urllib.request
response = urllib.request.urlopen("https://unsplash.com/s/photos/ford-bronco")
print(response)

#print(response.status)
print(response.read)
