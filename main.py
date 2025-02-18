from time import sleep
from os import system
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    
    credenciais = {
        "cpf" : "",
        "aniver" : ""
    }
    driver = webdriver.Firefox()
    
    def user_input():
        credenciais['cpf'] = input('Digite seu cpf; ')
        credenciais['aniver'] = input('Digite seu aniversario no seguinte modelo (xx/xx/xxxx); ')

    def acessandoSite():
        driver.get("https://infinityschool.app/")
        buttom = driver.find_element(By.CLASS_NAME, "button2")
        buttom.click()
        sleep(2)
    
    def login(cpf, aniversario):
        login = driver.find_element(By.NAME, "projectFilePath")
        login.send_keys(cpf)

        senha = driver.find_element(By.NAME, "data")
        senha.send_keys( aniversario + Keys.ENTER)
        sleep(2)
    
    def marcaPresença():
        botao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Marcar presença')]")))
        botao.click()
        sleep(2)

    system('clear')
    user_input()
    print('passou pelo input')
    acessandoSite()
    print('passou pela acessando site')
    login(credenciais["cpf"], credenciais["aniver"])
    print('passou pelo login')
    marcaPresença()
    print('passou pela presença')
    system('pause')
    
    driver.quit() 
main()