import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import csv

browser = webdriver.Edge(EdgeChromiumDriverManager().install())
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
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_MIPM.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
        
    elif "2023 MOC" in contacto:
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_MOC.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
    elif "2023 MIPM" in contacto:
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_MIPM.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
    elif "2023 MROM" in contacto:
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_MROM.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
    elif "2023 EICM" in contacto:
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_EIC.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
    elif "2023 EROM" in contacto:
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_MROM.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
    elif "2023 EICM" in contacto:
        send="En respuesta a su solicitud de información sobre nuestros postgrados le informo que se encuentra abierto el periodo de matrícula de los siguientes postgrados:"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Rehabilitación Oral y Estética Dental Integrada"
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Cirugía Bucal, Implantología y Periodoncia"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Máster en Ortodoncia Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Implantoprótesis Clínica"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Especialista en Odontología Conservadora"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send="Aprovecho la ocasión para invitarle a conocer las aulas de docencia Universitaria y el área clínica de nuestros Postgrados a través de los siguientes enlaces:  "		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" http://www.posgradoodontologia.es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.instagram.com/posgradoodontologia/?hl=es"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" https://www.facebook.com/odontologiauni1"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Para una Información Académica más detallada se recomienda contactar con el Coordinador de Postgrados, D. Antonio Sáez, en el teléfono:  (+34) 663 71 87 87 (Llamada o WhatsApp)"		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        send_message = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")		
        send=" Un cordial saludo."		
        send_message.send_keys(send)
        send_message.send_keys(Keys.ENTER)
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\ACCESO Y ADMISIÓN.pdf")
        time.sleep(7) 
        browser.find_element_by_class_name("_3wFFT").click() 
        time.sleep(2) 
        browser.find_element_by_css_selector("span[data-icon='clip']").click()
        browser.find_element_by_css_selector("input[type='file']").send_keys("C:\\Users\\34603\\Downloads\\Notepad\\Source\\Prueba\\Dossier_MIPM.pdf")
        time.sleep(12) 
        browser.find_element_by_class_name("_3wFFT").click()  
    
with open('Prueba.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        contacto = row['Telefono']
        time.sleep(1) 
        if contacto[0:2] == "52":
            buscar_contacto("521"+row['Telefono'][3:len(contacto)])
        else:
            buscar_contacto(row['Telefono'])
        time.sleep(2)
        chats = browser.find_elements_by_class_name("_8nE1Y")
        if len(chats)==0:
            browser.find_element_by_css_selector("span[data-icon='x-alt']").click()
        else:
            for i in range(len(chats)):
                separador = "\n"
                separado = chats[i].text.split(separador)
                enviar_mensaje(separado[0])
      
