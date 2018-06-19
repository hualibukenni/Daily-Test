import requests

def get_one_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_11_4)AppleWebKit/537.36(KHTML,like Gecko) chrome/52.0.2743.116 Safari/537.36'
    }

    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    # print(html)

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(pattern,html)
    print(items)

main()
