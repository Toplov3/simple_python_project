import requests
import sys


url = input("[ + ] Enter Url to check it: ")
req = requests.get(url)

if req.status_code == 200:
	print("[ + ] Url is Live")
else:
	print("[ - ] Url is Not Available")
