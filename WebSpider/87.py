from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
time.sleep(5)
input.send_keys('Iphone')
time.sleep(3)
input.clear()
time.sleep(5)
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()
