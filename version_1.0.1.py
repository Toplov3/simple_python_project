import requests
import os
import sys

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def check_urls(url):
	
	try:
		req = requests.get(url)
		if req.status_code == 200:
			print(f"[ + ] {url} : Live")
		elif re.status_code == 302:
			print(f"[ ! ] {url} : Rediredct ")
		else:
			print(f"[ - ] {url} : Dead")
	except:
		pass
urls = open(sys.argv[1],'r').readlines()

clear()
for url in urls:
	url = url.rstrip()
	check_urls(url)
