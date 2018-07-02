html = """
<html>
<head><title>The Dormous's story </title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time they were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elise --></a>,
<a href="http://exapmple.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of well.
</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
print(soup.title.name)
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
print(soup.p.string)
