import http.cookiejar,urllib.request

filename = 'cookies/cookie1.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)
# for item in cookie:
#     print(item.name+"="+item.value)
