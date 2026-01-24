# logando no site saucedemo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(5)

# preenchendo usuario
cpf_cnpj = driver.find_element(By.ID,"user-name")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("standard_user" + Keys.INSERT)
time.sleep(1)

# preenchendo senha
cpf_cnpj = driver.find_element(By.ID,"password")
cpf_cnpj.click()
time.sleep(1)
cpf_cnpj.send_keys("secret_sauce" + Keys.INSERT)
time.sleep(1)

clicando_botao_login = driver.find_element(By.ID,"login-button")
clicando_botao_login.click()
time.sleep(10)






