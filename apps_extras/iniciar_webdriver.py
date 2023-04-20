#Iniciar webdriver
import undetected_chromedriver as uc
import time

def iniciar_webdriver(headless=False, pos="maximizada"): #headless=False hace que se muestre el navegador
    """
    Inicia el webdriver de Chrome y devuelve el objeto WebDriver instanciado.
    pos: indica la posicion de la ventana del navegador
    """

    #instanciamos las opciones de Chrome
    options = uc.ChromeOptions()
    #desacrivamos el guardado de credenciales
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    #iniciamos el driver
    driver = uc.Chrome(
        options=options,
        headless=headless,
        log_level=3,
    )
    #posicionamos la ventana del navegador
    if not headless:
        #maximizamos la ventana
        driver.maximize_window()
        if pos != "maximizada":
            #obtenemos la resolucion de la ventana
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                #posicionamos la ventana en la esquina izquierda
                driver.set_window_rect(x=0, y=0, width=ancho//2, height=alto)
            elif pos == "derecha":
                driver.set_window_rect(x=ancho//2, y=0, width=ancho//2, height=alto)
    return driver

