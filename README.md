![header](https://capsule-render.vercel.app/api?type=waving&height=300&section=header&text=%20Machine%20Learning%20Operations%20(MLOps)&fontSize=30&&color=15:92a8d1,100:f7cac9&desc=%20%20&fontColor=ff6347&fontAlignY=35)


## INDICE:
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#header">TÍTULO E IMAGEN DE PORTADA</a></li>
    <li><a href="#INDICE">ÍNDICE</a></li>
    <li><a href="#INTRODUCCIÓN">INTRODUCCIÓN</a></li>
    <li><a href="#OBJETIVO">OBJETIVO</a></li>
    <li><a href="#SCOPE-OF-WORK">SCOPE OF WORK</a></li>
    <li><a href="#ESTADO">ESTADO</a></li>
    <li><a href="#EDA-ETL">EDA - ETL</a></li>
    <li><a href="#FastAPI">FastAPI</a></li>
    <li><a href="#MINI-DEMO1">MINI-DEMO1</a></li>
    <li><a href="#MINI-DEMO2">MINI-DEMO2</a></li>
    <li><a href="#ACCESO-AL-PROYECTO">ACCESO AL PROYECTO</a></li>
    <li><a href="#TECNOLOGÍAS">TECNOLOGÍAS UTILIZADAS</a></li>
    <li><a href="#DESARROLLADORES">DESARROLLADORES DEL PROYECTO</a></li>
    <li><a href="#VIDEO">VIDEO</a></li>
  </ol>
</details>

## INTRODUCCIÓN
Este proyecto forma parte de la etapa Labs del curso de Data Science de la Academia Soy Henry.
En esta ocasión brinda fuentes de información asociadas a las plataformas de streaming, tales como:
- Amazon Prime Video
- Disney Plus
- Hulu
- Netflix

Y 8 datasets de ratings que contiene puntuaciones que usuarios otorgaron a ciertas peliculas.
## OBJETIVO
El proyecto consiste en una ingesta de datos, para aplicar transformaciones en los datasets que permitan realizar consultas a través de una API. Los archivos originales están disponibles en este repositorio:  [Datasets](https://github.com/HX-PRomero/PI_ML_OPS)


## SCOPE-OF-WORK
La propuesta de trabajo se llevará a cabo en las siguientes etapas:

1. Análisis de datos de exploración (EDA) . Link: (https://github.com/RocioAldanaMendez/FastAPI/blob/main/ETL-EDA/EDA_and_ETL_final.ipynb)
2. Extraer-Transformar y Cargar con Python. Link: (https://github.com/RocioAldanaMendez/FastAPI/blob/main/ETL-EDA/modelo2.ipynb)
3. Generación/Creación de una API con FastAPI Link: (https://github.com/RocioAldanaMendez/FastAPI/blob/main/main.py)
4. Ejecutar la API en un host local y ejecutar consultas, visualizando con Uvicorn.
5. Desarrollo de Modelo con Machine Learning. (https://github.com/RocioAldanaMendez/FastAPI/blob/main/archivo.modelo_recomendacion.gz )
6. Ajuste de parámetros del modelo
7. Realización de un deployment en Delta Space para las 4 consultas generadas.  Link: (https://deta.space/discovery/r/cdbdpvvwlphtxscn)
8. Realizacion de un deployment en Hugging Face Space utilizando Gradio.  Link: (https://huggingface.co/spaces/RoTesla/NISTELX)

![arquitectura](https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/structure.png)

## ESTADO:
<h4 align="center">
:white_check_mark: Proyecto finalizado :white_check_mark:
</h4>

## EDA-ETL
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/>  
Como paso inicial, los datos se cargarán utilizando la biblioteca pandas. En esta instancia, se realizará un análisis exploratorio de los datos y se realizarán las transformaciones necesarias para limpiar los datos. Para ver con más detalle el trabajo realizado con las ETD y ETL puede recurrir a la carpeta que contiene esos dos archivos. A continuación se adjunta una hoja de ruta que establecí para el desarrollo:

![EDA-ETL](https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/route_of_work.png)

## FastAPI
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/>
Para la creación de la API se utilizó el archivo main.py. Con eso, se construyó la API localmente y se configuraron las funciones para realizar consultas. La API carga el CSV ya transformado para realizar las consultas y devuelve los resultados esperados.

![DEMO-API](https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/DEMO-API.gif)

## MINI-DEMO1:
- `Funcionalidad 1`: Consultar película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

                    La consulta debe generarse con el siguiente formato: {year}/{platform}/{duration_type}: 200/netflix/min
                    
- `Funcionalidad 2`: Consultar cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

                   Formato: {platform}/{scored}/{year}: netflix/(numeros del 0 al 5)/2000
                    
- `Funcionalidad 3`: Consultar cantidad de películas por plataforma con filtro de PLATAFORMA

                    La consulta debe generarse con el siguiente formato: {platform}: netflix
                    
- `Funcionalidad 4`: Consultar actor que más se repite según plataforma y año.

                    La consulta debe generarse con el siguiente formato: {platform}/{year}/: netflix/2000
                    
  Donde plataforma puede ser: netflix, hulu, disney, amazon.
  
  Y duration_time puede ser: min o season.
  
- `Demo`: 

![demo](https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/DEMO1.gif)

Link deploy: https://deta.space/discovery/r/cdbdpvvwlphtxscn

## MINI-DEMO2:
- `Funcionalidad 1`: Consultar recomendación de pelicula ingresando id del usuario y el id de la pelicula.

                    La consulta debe generarse con el siguiente formato: {userId}/{id}: 123/ns123
                    
- `Demo`: 

![demo](https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/DEMO2.gif)

Link deploy: https://huggingface.co/spaces/RoTesla/NISTELX

## ACCESO-AL-PROYECTO
            ## 🛠️ Abre y ejecuta el proyecto
            -  Para correr la api completa es necesario descomprimir el archivo que contiene el modelo, para que la api consuma de ese archivo, y como se subió la carpeta donde se desarrolló la api completa, debe correr.
            -Para visualizar la salida final en los Deploys podes ir al link de punto 7 y 8 del scope of work, o ingresar al alrchivo txt que contiene todos los links.
            
 
## TECNOLOGÍAS
 <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/> 
<img src="https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/gradio-logo.svg" alt="gradio" width="80" height="40"/> </a>
<img src="https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/FAST.png" alt="fastapi" width="80" height="40"/></a>
<img src="https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/logo-hugging-face.png" alt="huggingface" width="90" height="40"/> 
<img src="https://github.com/RocioAldanaMendez/Meteorite-Landings/blob/main/assets/deta.png" alt="deta" width="40" height="40"/> 

## DESARROLLADORES

| [<img src="https://avatars.githubusercontent.com/u/83037176?v=4" width=115><br><sub>Rocío Méndez</sub>](https://github.com/RocioAldanaMendez) |
| :---: | 

## VIDEO
<img src="https://www.vectorlogo.zone/logos/youtube/youtube-ar21.svg"/> 
https://www.youtube.com/watch?v=xjuB7wzt12k

Gracias por ver este desarrollo, podes seguir los futuros cambios dandole una estrellita en la parte superior derecha del repositorio. Podes Clonarlo, y/o podes hacer un PullRequest ya que todo aporte es bienvenido. 


