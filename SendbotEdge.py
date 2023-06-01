import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriver
import csv

browser = webdriver.Edge("msedgedriver")
browser.get("https://web.whatsapp.com/")
print("Escaneando codigo")
input()
print("Logeados")
time.sleep(1)
def buscar_contacto(contacto):
    search_contact = browser.find_element_by_xpath("//*[@id='side']/div[1]/div/div/div[2]/div/div[1]/p")
    search_contact.send_keys(contacto)
    search_contact.send_keys(Keys.ENTER)
    
def enviar_mensaje(contacto):
    send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    
    if "2023 Programador" in contacto:
        send="Hola buenas" 
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(1) 
        browser.find_element_by_class_name("_3wFFT").click()  
    elif "2023 MOC" in contacto:
        send="Hola buenas" 
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(1) 
        browser.find_element_by_class_name("_3wFFT").click()
    elif "2023 MIPM" in contacto:
        send="Hola buenas" 
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(1) 
        browser.find_element_by_class_name("_3wFFT").click()
    elif "2023 MROM" in contacto:
        send="Hola buenas" 
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(1) 
        browser.find_element_by_class_name("_3wFFT").click()
    elif "2023 EICM" in contacto:
        send="Hola buenas" 
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(1) 
        browser.find_element_by_class_name("_3wFFT").click()
    elif "2023 EROM" in contacto:
        send="Hola buenas" 
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(1) 
        browser.find_element_by_class_name("_3wFFT").click()
    
 
    
with open('Prueba.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        buscar_contacto(row['Telefono'])
        chats = browser.find_elements_by_class_name("_8nE1Y")
        for i in range(len(chats)):
            separador = "\n"
            separado = chats[i].text.split(separador)
            enviar_mensaje(separado[0])
