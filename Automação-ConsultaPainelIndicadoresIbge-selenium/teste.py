# IBGE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.service import Service

# Define o nome da pasta
pasta_evidencias = 'Evidencias'
# Cria a pasta se ela não existir
if not os.path.exists(pasta_evidencias):
    os.makedirs(pasta_evidencias)

# Inicializa o driver (ex: Chrome)
driver = webdriver.Chrome()
driver.get("https://www.ibge.gov.br/")
time.sleep(5)

# # Exemplo: Encontrar um campo de texto pelo ID
# campo_cpf = driver.find_element(By.CLASS_NAME, "_1tmofjel")
# campo_cpf.click()
# time.sleep(5)

# campo_cpf = driver.find_element(By.ID, "f-cpf")
# campo_cpf.click()
# campo_cpf.send_keys("34795239860" + Keys.INSERT)
# time.sleep(1)


#  Exemplo: Encontrar um campo de texto pelo ID
# campo_data_nasc = driver.find_element(By.ID, "txtDataNascimento")
# campo_data_nasc.click()
# time.sleep(1)
# campo_data_nasc.send_keys("19121986" + Keys.INSERT)
# time.sleep(1)

# caminho_foto = os.path.join(pasta_evidencias, "evidencia_1.png")
# driver.save_screenshot(caminho_foto)
# print(f"Evidência salva em: {caminho_foto}")

# entrar = driver.find_element(By.ID, "checkbox")
# entrar.click()
# time.sleep(10)
# caminho_foto = os.path.join(pasta_evidencias, "evidencia_2.png")
# driver.save_screenshot(caminho_foto)
# print(f"Evidência salva em: {caminho_foto}")

# acesso_rapido_antecipacao = driver.find_element(By.ID,"b10-AntecipacaoDiv2")
# acesso_rapido_antecipacao.click()
# time.sleep(15)
# caminho_foto = os.path.join(pasta_evidencias, "evidencia_3.png")
# driver.save_screenshot(caminho_foto)
# print(f"Evidência salva em: {caminho_foto}")

# troca_estabelecimento = driver.find_element(By.ID,"b5-b3-$b2")
# troca_estabelecimento.click()
# time.sleep(15)

# caminho_foto = os.path.join(pasta_evidencias, "ultima_evidencia.png")
# driver.save_screenshot(caminho_foto)
# print(f"Evidência salva em: {caminho_foto}")

