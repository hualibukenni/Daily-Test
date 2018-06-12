import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
response = urllib.request.Request(url = 'http://1024.917rbb.info/pw/',headers = headers)
rs = urllib.request.urlopen(response).read()
print(rs)
# # print (rs.status)
# print(rs.getheaders())
# print(rs.getheader('Server'))
# print(type(response))
