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
    <li><a href="#DESCRIPCION">DESCRIPCIÓN</a></li>
    <li><a href="#ESTADO">ESTADO</a></li>
    <li><a href="#DEMOSTRACIÓNs">DEMOSTRACIÓN</a></li>
    <li><a href="#ACCESO">ACCESO AL PROYECTO</a></li>
    <li><a href="#TECNOLOGÍAS UTILIZADAS">TECNOLOGÍAS UTILIZADAS</a></li>
    <li><a href="#DESARROLLADORES">DESARROLLADORES DEL PROYECTO</a></li>
    <li><a href="#CONCLUSIÓN">CONCLUSIÓN</a></li>
  </ol>
</details>

## **INTRODUCCION**
Este proyecto forma parte de la etapa Labs del curso de Data Science de la Academia Soy Henry.
En esta ocasión brinda fuentes de información asociadas a las plataformas de streaming, tales como:
- Amazon Prime Video
- Disney Plus
- Hulu
- Netflix

## **OBJETIVO**
El proyecto consiste en una ingesta de datos de diversas fuentes entregados por la cátedra, para aplicar transformaciones en los datasets que permitan realizar consultas a través de una API. En el siguiente enlace tendrás acceso al repositorio del proyecto original:  [Statemet](https://github.com/RocioAldanaMendez/Streaming_Plataforms)
Los archivos originales están disponibles en este repositorio:  [Datasets](https://github.com/HX-PRomero/PI_ML_OPS)


## SCOPE OF WORK
La propuesta de trabajo se llevará a cabo en las siguientes etapas:

1. Análisis de datos de exploración (EDA) . Link: ![EDA-ETL-1](https://github.com/RocioAldanaMendez/FastAPI/blob/main/ETL-EDA/EDA_and_ETL_final.ipynb)
2. Extraer-Transformar y Cargar con Python. Link: ![EDA-ETL-2](https://github.com/RocioAldanaMendez/FastAPI/blob/main/ETL-EDA/modelo2.ipynb)
3. Generación/Creación de una API con FastAPI Link: ![main.py_API](https://github.com/RocioAldanaMendez/FastAPI/blob/main/main.py)
4. Ejecutar la API en un host local y ejecutar consultas, visualizando con Uvicorn.
5. Desarrollo de Modelo con Machine Learning. Link: ![ModeloML]( )
6. Ajuste de parámetros del modelo
7. Realización de un deployment en Delta Space para las 4 consultas generadas.  Link: ![Deploy_DETA](https://deta.space/discovery/r/cdbdpvvwlphtxscn)
8. Realizacion de un deployment en Hugging Face Space utilizando Gradio.  Link: ![Deploy_Gradio](https://huggingface.co/spaces/RoTesla/NISTELX)

![arquitectura](https://github.com/RocioAldanaMendez/FastAPI/blob/main/aseets/structure.png)

## ESTADO:
<h4 align="center">
:white_check_mark: Proyecto finalizado :white_check_mark:
</h4>

## EDA - ETL
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/>  
Como paso inicial, los datos se cargarán utilizando la biblioteca pandas. En esta instancia, se realizará un análisis exploratorio de los datos y se realizarán las transformaciones necesarias para limpiar los datos. transformaciones necesarias para la limpieza de datos. Para ver con más detalle el trabajo realizado con las ETD y ETL acceda al siguiente enlace: EDA/ETL

## FastAPI
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/>
Para la creación de la API se utilizó el archivo main.py. Con eso, se construyó la API localmente y se configuraron las funciones para realizar consultas. La API carga el CSV ya transformado para realizar las consultas y devuelve los resultados esperados.

Para este proyecto solo se solicitaron 4 tipos de consultas.

+ Duración máxima por tipo de película (película/serie), por plataforma y por año:
     La solicitud debe ser: get_max_duration(año, plataforma, [min o temporada]).

+ Número de películas y series (por separado) por plataforma.
     La solicitud debe ser: get_count_plataform(plataforma)
  
+ Número de veces que se repite un género y plataforma con más frecuencia del mismo género y plataforma.
     La solicitud debe ser: get_listedin('género')
     Como ejemplo de género, puede usar 'comedia', que debería devolver un coño de 2099 para la plataforma de Amazon.

+ Actor más repetido por plataforma y año.
   La solicitud debe ser: get_actor(plataforma, año)

## DEMOSTRACIÓN:
- `Funcionalidad 1`: Consultar película con mayor duración con filtros opcionales de Año, Plataforma y Tipo de duración.
- `Funcionalidad 2`: Consultar cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.
- `Funcionalidad 3`: Consultar cantidad de películas por plataforma con filtro de Plataforma.
- `Funcionalidad 4`: Consultar actor que más se repite según la Plataforma y Año.
- `Demo`: 

![demo](https://github.com/RocioAldanaMendez/Streaming_Platforms/blob/main/demo.gif)



## ACCESO AL PROYECTO
            \## 📁 Acceso al proyecto

            **Indica cómo se puede descargar o acceder al código fuente del proyecto, ya sea proyecto inicial o final**

            \## 🛠️ Abre y ejecuta el proyecto

            **Muestra las instrucciones necesarias para abrir y ejecutar el proyecto**

## TECNOLOGÍAS
 <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original-wordmark.svg" width=40px height=40px/><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width=40px height=40px/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" width=40px height=40px/> 

## DESARROLLADORES

| [<img src="https://avatars.githubusercontent.com/u/83037176?v=4" width=115><br><sub>Rocío Méndez</sub>](https://github.com/RocioAldanaMendez) |
| :---: | 

## VIDEO (<7 min)
<img src="https://www.vectorlogo.zone/logos/youtube/youtube-ar21.svg"/> 

## CONCLUSIÓN

