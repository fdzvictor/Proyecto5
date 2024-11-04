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

warnings.filterwarnings("ignore")


#-----------------------------------------------------------------------------------
def sacar_historico(url_sproducto:str,pos_tabla = 0):

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

#Función para replacear comas por puntos, para poder pasar a float
def eliminar_comas(x):
    return x.replace(",",".")

#------------------------------------------------------------------------------------



# Función para eliminar puntos
def eliminar_puntos(x):
    return x.replace(".", "")


#------------------------------------------------------------------------------------
#Función que calcula el número más cercano al valor objetivo de una lista de valores 

def numero_mas_cercano(valor, lista_numeros):
    # Calcula la diferencia absoluta y encuentra el número más cercano
    numero_cercano = min(lista_numeros, key=lambda x: abs(x - valor))
    return numero_cercano

#--------------------------------------------------------------------
# Esta función devuelve un df con los 40 datos más relevantes en wallapop de un modelo de coche en concreto
# Por defecto la localización es la calle arturo soria 
def wallapop_coche (keywords, precio_max, latitud = 40.450381, longitud = -3.518064, precio_minimo: int = 0):
   
    url = "http://api.wallapop.com/api/v3/general/search"

    headers = {'Accept': '*/*', 'User-Agent': 'Wget/1.21.4',

    'Accept-Encoding': 'identity', 'X-DeviceOS': '0' }

    params = {"search_objects":[],
          # "from":0,
          # "to":10,
          "keywords": keywords,
          "min_sale_price" : precio_minimo,
          "max_sale_price" : precio_max,
          "order":"most_relevance",
          "search_point":{latitud,longitud},
          "type": "cars_search_cars",
          "category_ids" : 100,
          "brand": "",
          "model": "",
          "max_km": 1000000
        #   "spellcheck":null
        }
  
    res = requests.get(url, headers = headers, params = params)
    res.status_code
    dc_wallapop = res.json()

    #Sacamos los precios de la API
    lista_precios = []
    for i in dc_wallapop["search_objects"]:
      lista_precios.append(i["price"])

    #Sacamos el nombre
    lista_nombres = []
    for i in dc_wallapop["search_objects"]:
      lista_nombres.append(i["title"])

    #Sacamos el link
    lista_links = []
    for i in dc_wallapop["search_objects"]:
      lista_links.append("es.wallapop.com/item/" + i["web_slug"])

    #Sacamos localizacion
    lista_localiz = []
    for i in dc_wallapop["search_objects"]:
      lista_localiz.append(list(i["location"].values())[0])

    #Sacamos Código postal:
    lista_postal = []
    for i in dc_wallapop["search_objects"]:
      lista_postal.append(list(i["location"].values())[1])

  #Sacamos país:
    lista_pais = []
    for i in dc_wallapop["search_objects"]:
      lista_pais.append(list(i["location"].values())[-1])

  

    #Sacamos fecha
    lista_fecha = []
    for i in dc_wallapop["search_objects"]:
      lista_fecha.append(i["creation_date"])
      
    #Sacamos el df con todos los modelos detallados y el precio mediano 
    df_wallapop = pd.DataFrame(list(zip(lista_nombres,lista_precios,lista_localiz,lista_postal,lista_fecha,lista_links)), 
                           columns = ["Modelo","Precio","Localización","Código_postal","Fecha","Link_wallapop"])

    df_wallapop["Denominación"] = keywords
    #limpiamos df
    df_wallapop.drop_duplicates(inplace=True)
    df_wallapop["Link_wallapop"].astype(str)
    df_wallapop["Fecha"]
    df_wallapop["Fecha"] = pd.to_datetime(df_wallapop["Fecha"]).dt.strftime("%y-%m-%d")  
  
    return df_wallapop

#-------------------------------------------------------------------------------------------------

def coche_cerca_mediano(df):
# #Calculamos el precio que más se acerca al precio mediano
    valor_mediano = int(df["Precio"].median())
    precio_wallapop = numero_mas_cercano(valor_mediano,list(df["Precio"]))
    print(f"el precio del modelo que más se acerca al precio mediano es: {precio_wallapop}")

    #Extraemos valores para los coches más cerca de la mediana
    filtro = df[df["Precio"] == precio_wallapop]
    
    return filtro