from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,built_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
  result = opener.open(url)
  html = result.read().decode('utf-8')
  print(html)
except URLError as e:
  print(e.reason)
