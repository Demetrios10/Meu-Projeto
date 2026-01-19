import time
from selenium import webdriver # type: ignore


browser = webdriver.Chrome()

browser.get("https://google.com")
time.sleep(5)