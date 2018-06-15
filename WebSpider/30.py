import requests

r = requests.get("http://www.baisu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key+'='+value)
