import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.baidu.com')
time.sleep(2)
browser.get('https://www.taobao.com')
time.sleep(2)
browser.get('https://www.zhihu.com')
browser.back()
time.sleep(5)
browser.forward()

