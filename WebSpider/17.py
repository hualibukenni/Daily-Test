import http.cookiejar,urllib.request,ssl

ssl._create_default_https_context = ssl._create_unverified_context
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie1.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
try:
    response = opener.open('https://www.baidu.com')
except error.URLError as e:
    print(e.reason)
print(response.read().decode('utf-8'))
