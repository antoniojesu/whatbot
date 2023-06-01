import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriver


browser = webdriver.Edge("msedgedriver")

browser.get("https://web.whatsapp.com/")
print("Escaneando codigo")
input()
print("Logeados")
time.sleep(5)
def buscar_contacto(contacto):
    search_contact = browser.find_element_by_xpath("//*[@id='side']/div[1]/div/div/div[2]/div/div[1]/p")
    search_contact.send_keys(contacto)
    search_contact.send_keys(Keys.ENTER)
    
def enviar_mensaje(message,contacto):
    send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
    
    if "Hola" in message:
        send= "Hola que desea"
    elif ("Rehabilitacion" in message or "Rehabilitación" in message 
          or "rehabilitación" in message or "rehabilitacion" in message):
        send="Usted quiere Rehabilitacion"
    
    elif ("periodoncia"  in message or "Periodoncia"  in message 
          or "implantologia"  in message or "Implantologia"  in message
          or "implantología"  in message or "Implantología"  in message):
        send="Usted quiere Periodoncia"
         
    elif "Ortodoncia" in message or "ortodoncia" in message:
        send="Usted quiere Ortodoncia" 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\bmi.jpg")
        time.sleep(5) 
        browser.find_element_by_class_name("_3wFFT").click()
          
    elif ("Implantoprotesis"  in message or "Implantoprótesis"  in message 
          or "implantoprotesis"  in message or "implantoprótesis"  in message):
        send="Usted quiere Implantoprotesis"
        
    elif ("informacion" in message or "información" in message 
          or "Informacion" in message or "Información" in message):
        send="Que informacion quiere tenemos lo siguiente:\n1a\n2b\n3c"
    
    
    send_message.send_keys(send)
    send_message.send_keys(Keys.ENTER)
    

bucle = True
while bucle:
    chats = browser.find_elements_by_class_name("_8nE1Y")
    for i in range(len(chats)):
        resultado = browser.find_elements_by_class_name("_2H6nH")
        print(len(resultado))
        if len(resultado) >0:
            if "_2H6nH" in chats[i].get_attribute("outerHTML"):
                separador = "\n"
                separado = chats[i].text.split(separador)
                buscar_contacto(separado[0])
                enviar_mensaje(separado[len(separado)-1],separado[0]) 
