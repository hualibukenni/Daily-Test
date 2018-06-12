import http.cookiejar,urllib.request,ssl

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
ssl._create_default_https_context = ssl._create_unverified_context
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)
