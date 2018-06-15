import requests

files = {'file':open('favicon.ico','rb')}
r = requests.post("http://httpbin.org/post",files=files)
print(type(r.text),r.text)
