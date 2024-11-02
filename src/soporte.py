# Importamos las librerías que necesitamos:

# Beautifulsoup
from bs4 import BeautifulSoup

# Requests
import requests

# Importar librerías para automatización de navegadores web con Selenium
# -----------------------------------------------------------------------
from selenium import webdriver  # Selenium es una herramienta para automatizar la interacción con navegadores web.
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriverManager gestiona la instalación del controlador de Chrome.
from selenium.webdriver.common.keys import Keys  # Keys es útil para simular eventos de teclado en Selenium.
from selenium.webdriver.support.ui import Select  # Select se utiliza para interactuar con elementos <select> en páginas web.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException # Excepciones comunes de selenium que nos podemos encontrar 


# Importar librerías para pausar la ejecución
# -----------------------------------------------------------------------
from time import sleep  # Sleep se utiliza para pausar la ejecución del programa por un número de segundos.

# Librerías para tratamiento de datos
# -----------------------------------------------------------------------
import pandas as pd
import numpy as np

#Librerias de soporte
#-------------------------------------------------------------------------
import warnings
import sys
sys.path.append("../")
from src import soporte
import json
from tqdm import tqdm
warnings.filterwarnings("ignore")


#-----------------------------------------------------------------------------------
def sacar_historico(url_sproducto,pos_tabla):

#Sacar histórico de precios, empecemos con una url: 
    
    res_producto = requests.get(url_sproducto)
    print(res_producto)

#Creamos bs4, buscamos aquellos elementos que sean tablas y seleccionamos la que queremos en concreto
    sopa_producto = BeautifulSoup(res_producto.content,"html.parser")
    tablas = sopa_producto.find_all("table")

    tablasweb = []
    for n in tablas:
        tablasweb.append(n)
#Puesto que hay webs que tienen varias tablas, cogemos siempre aquella con datos del año, la primera

    tabla = tablasweb[pos_tabla]
    headers = []
    for i in tabla.findAll("th"):
        headers.append(i.getText())
    
    datos = []
    for fila in tabla.find_all('tr'):
        columnas = fila.find_all('td')
        # Extraer el texto de cada columna y limpiar
        datos_fila = [columna.getText(strip=True) for columna in columnas]
        if datos_fila:  # Evitar filas vacías
            datos.append(datos_fila)

    df = pd.DataFrame(datos, columns= headers)
    

    return df


#-----------------------------------------------------------------------------------