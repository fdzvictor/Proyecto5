# Análisis del Mercado de Coches en España

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar el mercado de coches en España, tanto en términos de matriculaciones históricas como en el contexto del mercado de segunda mano. Utilizando varias técnicas de scraping y APIs, hemos recopilado y analizado datos de diversas fuentes, incluyendo Wallapop, Datosmacro y la Dirección General de Tráfico (DGT), para crear una base de datos completa de los modelos de coches más populares en el país. Con estos datos, se han llevado a cabo análisis de estacionalidad y de las características del mercado de segunda mano.

## Fuentes de Datos
1. **API de Wallapop**: Obtenemos información de Wallapop para realizar un análisis de precios y disponibilidad de coches en el mercado de segunda mano.
2. **Datosmacro**: Se ha scrapeado la tabla de matriculaciones históricas en España, una fuente clave para conocer la evolución de la demanda de diferentes modelos.
3. **Dirección General de Tráfico (DGT)**: Usamos web scraping para acceder a los microdatos del parque móvil en 2023, permitiendo un análisis detallado de los modelos más populares en circulación.

## Tecnologías y Librerías Utilizadas
- **Python**: Lenguaje principal para el procesamiento y análisis de datos.
- **Librerías de Scraping**:
  - `requests`: Para hacer llamadas HTTP a la API de Wallapop.
  - `BeautifulSoup` (bs4): Para extraer datos de HTML en el scraping de Datosmacro y la DGT.
  - `Selenium`: Para el scraping dinámico de sitios que requieren interacción avanzada.
- **Pandas**: Para manipulación y análisis de datos en DataFrames.
- **psycopg2**: Conexión y manejo de bases de datos PostgreSQL para almacenar los datos obtenidos y realizar consultas.
  
## Proceso de Obtención y Análisis de Datos
1. **Llamada a la API de Wallapop**: Para obtener datos de coches en venta en el mercado de segunda mano, fue necesario averiguar los parámetros y headers correctos de la API de Wallapop. La API permitió obtener hasta 40 elementos por modelo de coche, lo que nos ayudó a construir una base de datos de precios y características para realizar análisis de mercado.
  
2. **Scraping de Datosmacro**: Se scrapeó la tabla de matriculaciones históricas de Datosmacro para analizar la evolución en la popularidad de diferentes modelos de coche en España.
  
3. **Web Scraping de la DGT**: A través de scraping, se obtuvieron microdatos del parque móvil español para 2023, lo que permitió identificar los modelos más comunes y analizar su distribución geográfica y características de emisiones.

4. **Creación de Base de Datos**: Se organizó toda la información en una base de datos en PostgreSQL, donde se estructuraron las tablas para realizar consultas de los modelos más populares y sus características en el mercado de segunda mano.

5. **Análisis de Estacionalidad**: Utilizando los datos de Wallapop, se realizó un análisis estacional para observar las fluctuaciones de precio y disponibilidad de los modelos en función de la época del año, así como otros detalles relevantes del mercado de segunda mano.

## Resultados
El análisis permitió extraer conclusiones sobre:
- **Modelos de coches más populares**: Identificación de los modelos más vendidos y en circulación en España.
- **Tendencias del mercado de segunda mano**: Análisis de precios y disponibilidad de los coches más populares en Wallapop.
- **Estacionalidad**: Variaciones en la oferta y demanda a lo largo del año, lo que ayuda a entender mejor las tendencias en el mercado de segunda mano de automóviles.

## Cómo Ejecutar el Proyecto
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio
