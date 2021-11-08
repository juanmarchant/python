# **2) ¿Eres capaz de desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora actual? Hazlo en un script llamado reloj.py y 
# ejecútalo en la terminal.**

# *Ayudas: El módulo **time** integra una función llamada **sleep(segundos)** que puede pausar la ejecución de un programa durante un tiempo. Así mismo el módulo 
# **os** integra la función **system('cls')** y **system('clear')** para limpiar la pantalla de la terminal en sistemas Windows y Linux/Unix respecticamente.*

import time
import datetime 
import os

while True:
    hora = datetime.datetime.now()
    print(f"{hora.hour}:{hora.minute}:{hora.second}")
    time.sleep(1)
    os.system('clear')
    