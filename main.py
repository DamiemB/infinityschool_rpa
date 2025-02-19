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

    def bruteforce():
        token_brute_force = 9999
        while token_brute_force != 0:
            token_brute_force -= 1

    
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
    
    def acessandoPresenca():
        botao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Marcar presença')]")))
        botao.click()
        sleep(2)

    def marcandoPresenca():
        botao2 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Presença aula do curso')]")))
        botao2.click()
        sleep(2)
    
    def validacaotoken():
        token = driver.find_element(By.NAME, "token_validacao")
        token.send_keys("6666" + Keys.ENTER)
        validation_message = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "validation-message")))
        message_text = validation_message.text
        print(f'a mensagem de texto é >>> {message_text}')
        if message_text == "Token inválido!":
            print("Comparação de token invalida")
        else:
            print("comparação de token valida")


    system('clear')
    user_input()
    print('passou pelo input')
    acessandoSite()
    print('passou pela acessando site')
    login(credenciais["cpf"], credenciais["aniver"])
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