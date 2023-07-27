from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
global driver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("http://aps-dev.coppel.io/intranet/capturahoras/login")

boton = driver.find_element(By.XPATH, "//button[contains(text(), ' Inicia sesión con Colaborador Digital ')]")
boton.click()

username_field = driver.find_element(By.NAME, "logonId")
username_field.send_keys("angelsebastian80@pruebas.com")

password_field = driver.find_element(By.NAME, "logonPassword")
password_field.send_keys("########")

try:
    botonIngresar = driver.find_element(By.XPATH, "//button[contains(text(), 'Ingresar')]")
    botonIngresar.click()
except Exception as e:
    print("El error es: ",e)

try:
    botonIngresar = driver.find_element(By.XPATH, "//button[contains(text(), 'Ingresar')]")
    botonIngresar.click()
except Exception as e:
    print("Por si falla en donde sea ",e)

driver.close()
