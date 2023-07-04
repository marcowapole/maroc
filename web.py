# pip install requests
#method 1
import urllib.request
from urllib.request import Request, urlopen
req = Request('https://medium.com/@codedev101', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).getcode()
print(webpage) # 200
# method 2
import requests
r = requests.get("https://medium.com/@codedev101")
print(r.status_code) # 200
