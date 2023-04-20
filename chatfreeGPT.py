#modulos de python
import os
import sys
import time 
import pickle
import tempfile
#modulos de python para webscraping
from selenium.webdriver.common.by import By #para buscar elementos por atributos
from selenium.webdriver.support.ui import WebDriverWait #para esperar a que cargue un elemento
from selenium.webdriver.support import expected_conditions as ec #para esperar a que cargue un elemento
from selenium.webdriver.common.keys import Keys #para simular teclas

#modulos propios
from config import *
from apps_extras.colores import *
from apps_extras.cursor_arriba import cursor_arriba
from apps_extras.iniciar_webdriver import iniciar_webdriver

class ChatGpt:
    def __init__(self, user, password):
        """
        Iniciamos el web driver y nos logueamos en ChatGPT
        """
        self.OPENAI_USER = user
        self.OPENAI_PASS = password
        self.COOKIES_FILE = f"{tempfile.gettempdir()}/openai.cookies"
        azul("Iniciando webdriver...")
        self.driver = iniciar_webdriver(headless=False, pos="izquierda")
        azul("Webdriver iniciado")
        self.wait = WebDriverWait(self.driver, 30)
        login = self.login_openai()
        print()
        if not login:
            rojo("No se pudo iniciar sesion en OpenAI")
            sys.exit(1)

    def login_openai(self):
        """
        Realiza login en OpenAI por cookies o desde cero
        """
        azul("Logueando en OpenAI...")
        print("Cargando ChatGPT...")
        self.driver.get("https://chat.openai.com/auth/login")
        cursor_arriba()

        time.sleep(3)
        print("Click en login")
        boton_login = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[text()='Log in']")))
        boton_login.click()
        cursor_arriba()

        #Introducimos el usuario
        time.sleep(3)
        print("Introduciendo usuario")
        input_usuario = self.wait.until(ec.element_to_be_clickable((By.ID, "username")))
        input_usuario.send_keys(OPENAI_USER)


