from time import sleep
from os import system
from random import randint
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    
    credenciais = {
        "user_cpf" : "",
        "user_date" : "",
        "user_token" : ""
    }
    driver = webdriver.Firefox()
    
    def user_input():
        credenciais['user_cpf'] = input('Digite seu cpf; ')
        credenciais['user_date'] = input('Digite seu aniversario no seguinte modelo (xx/xx/xxxx); ')
        credenciais['user_token'] = input('Digite o Token do dia: ')

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
    
    def acessandoPresenca():
        botao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Marcar presença')]")))
        botao.click()
        sleep(2)

    def marcandoPresenca():
        botao2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Presença aula do curso')]")))
        botao2.click()
        sleep(2)
    
    def validacaotoken():
        token = driver.find_element(By.NAME, "token_validacao")
        token.send_keys(credenciais['user_token'] + Keys.ENTER)
        validation_message = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "validation-message")))
        confirmar_presença_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Concluir presença')]")))
        message_text = validation_message.text
        print(f'a mensagem de texto é >>> {message_text}')
        if message_text == "Token inválido!":
            print("Comparação de token invalida")
            while menssage_text == "Token Inválido":
                random = randint()
                
                confirmar_presença_button.click()
        else:
            print("comparação de token valida")
            


    system('clear')
    user_input()
    print('passou pelo input')
    acessandoSite()
    print('passou pela acessando site')
    login(credenciais["user_cpf"], credenciais["user_date"])
    print('passou pelo login')
    acessandoPresenca()
    print('passou pela presença')
    marcandoPresenca()
    print('Passou no marcando presença')
    validacaotoken()
    print('Passou Token')
    sleep(30)
    
    
    driver.quit() 
main()