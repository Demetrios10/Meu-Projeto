import time
from selenium import webdriver # type: ignore


browser = webdriver.Chrome()

browser.get("https://sicredi.qa.portaldocliente.fiserv.com/login?IsTimeout=True")
time.sleep(5)