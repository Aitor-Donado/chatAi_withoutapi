from colorama import Fore, Back, Style

verde = Fore.GREEN
rojo = Fore.RED
amarillo = Fore.YELLOW
azul = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
blanco = Fore.WHITE

#Otros colores

naranja = Fore.LIGHTRED_EX
beige = Fore.LIGHTYELLOW_EX
celeste = Fore.LIGHTBLUE_EX
rosa = Fore.LIGHTMAGENTA_EX
turquesa = Fore.LIGHTCYAN_EX
gris = Fore.LIGHTWHITE_EX

#Colores de fondo

f_verde = Back.GREEN
f_rojo = Back.RED
f_amarillo = Back.YELLOW
f_azul = Back.BLUE
f_magenta = Back.MAGENTA
f_cyan = Back.CYAN
f_blanco = Back.WHITE

#Otros colores de fondo

f_naranja = Back.LIGHTRED_EX
f_beige = Back.LIGHTYELLOW_EX
f_celeste = Back.LIGHTBLUE_EX
f_rosa = Back.LIGHTMAGENTA_EX
f_turquesa = Back.LIGHTCYAN_EX
f_gris = Back.LIGHTWHITE_EX

def verde(texto):
    print(Fore.GREEN + texto + Fore.WHITE)

def rojo(texto):
    print(Fore.RED + texto + Fore.WHITE)

def amarillo(texto):
    print(Fore.YELLOW + texto + Fore.WHITE)

def azul(texto):
    print(Fore.BLUE + texto + Fore.WHITE)

def magenta(texto):
    print(Fore.MAGENTA + texto + Fore.WHITE)

def cyan(texto):
    print(Fore.CYAN + texto + Fore.WHITE)

def blanco(texto):
    print(Fore.WHITE + texto + Fore.WHITE)

def naranja(texto):
    print(Fore.LIGHTRED_EX + texto + Fore.WHITE)

def beige(texto):
    print(Fore.LIGHTYELLOW_EX + texto + Fore.WHITE)

def celeste(texto):
    print(Fore.LIGHTBLUE_EX + texto + Fore.WHITE)

def rosa(texto):
    print(Fore.LIGHTMAGENTA_EX + texto + Fore.WHITE)

def turquesa(texto):
    print(Fore.LIGHTCYAN_EX + texto + Fore.WHITE)

def gris(texto):
    print(Fore.LIGHTWHITE_EX + texto + Fore.WHITE)

def f_verde(texto):
    print(Back.GREEN + texto + Back.WHITE)

def f_rojo(texto):
    print(Back.RED + texto + Back.WHITE)

def f_amarillo(texto):
    print(Back.YELLOW + texto + Back.WHITE)

def f_azul(texto):
    print(Back.BLUE + texto + Back.WHITE)

def f_magenta(texto):
    print(Back.MAGENTA + texto + Back.WHITE)

#Ahora podremos usar las funciones en el programa principal
