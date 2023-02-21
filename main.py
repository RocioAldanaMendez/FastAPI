#Import libraries
from fastapi import FastAPI, Request, Form
import pandas as pd
import numpy as np
from flask import Flask, request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from typing import Optional
import pickle

app = FastAPI()


df= pd.read_csv('platforms_and_score.csv', sep=",")

# Configure a sample rate
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Loading information for the API
@app.get('/about')
async def about():
    return 'API created with FastAPI and Uvicorn'

#API 1) 
@app.get("/get_max_duration")
def get_max_duration(year: Optional[int] = None, platform: Optional[str] = None, duration_type: Optional[str] = None):
    # Convert year to integer if provided
    if year is not None and year != "":
        year = int(year)
    # Filter the DataFrame
    if duration_type is not None:
        filtered_df = df[df['duration_type'] == duration_type]
    else:
        filtered_df = df.copy()
    if year is not None:
        filtered_df = filtered_df[filtered_df['year'] == year]
    if platform is not None:
        filtered_df = filtered_df[filtered_df['platform'] == platform]
    # Sort the DataFrame and get the row with the maximum duration
    sorted_df = filtered_df.sort_values(by='duration_int', ascending=False)
    max_duration = sorted_df.iloc[0][['title']]

    return max_duration
"""
    This function calculates the Movie with the longest duration with optional filters of YEAR, PLATFORM and TYPE OF DURATION.
    (the function should be called get_max_duration(year, platform, duration_type))
"""  

#API 2)
@app.get("/get_score_count/")
def get_score_count(platform: str, scored: int, year:int):
    # Filter data based on conditions
    df_filtered = df[(df["platform"] == platform) & (df["scored"] >= scored) & (df["year"] == year)]
    # Count the number of rows that meet the conditions
    cantidad = len(df_filtered)
    # Return the number of times the condition is met
    return cantidad
"""
    This function calculates the number of movies by platform with a score greater than XX in a given year.
    (the function must be called get_score_count(platform, scored, year))
"""  

#API 3) 
@app.get('/get_count_platform')
def get_count_platform(platform=None):
    # if a platform is provided, filter the dataframe by that platform
    if platform:
        df_filtered = df[df['platform'] == platform]
    else:
        df_filtered = df
    
    # count the number of movies per platform
    count_by_platform = df_filtered['platform'].value_counts()
    
    # if the platform exists in the dataframe, return the amount as an integer
    if platform in count_by_platform.index:
        return int(count_by_platform[platform])
    
    # if no frame was provided, return the sum of all movies in the dataframe
    elif platform is None:
        return int(count_by_platform.sum())
    
    # if the platform does not exist in the dataframe, return 0
    else:
        return 0
"""
    The above function calculates the number of movies per platform with the PLATFORM filter.
    (The function should be called get_count_platform(platform))
""" 
#API 4)
@app.get('/get_actor')
def get_actor(platform:str, year:int):
    global df
    # Filter by year and platform
    filtered_df = df[(df['platform'] == platform) & (df['year'] == year)]

    # Count the number of times each actor appears in the 'cast' column
    actor_count = filtered_df['cast'].str.split(',').explode().str.strip().value_counts()

    # Return the actor that repeats the most
    if actor_count.empty:
        return None
    else:
        return actor_count.index[0]
"""
    The previous function identifies the Actor that is repeated the most according to platform and year.
    (The function should be called get_actor(platform, year))
"""  

def cargar_modelo():
    with open('C:/Users/rocio/OneDrive/Escritorio/FastAPI//modelo_recomendacion.pkl', 'rb') as archivo_modelo:
        model = pickle.load('modelo_recomendacion.pkl')
    return model

#API 5)
@app.get("/get_predictions")
async def get_predictions(userId: str, id: str):

    # Cargar el modelo desde un archivo
    with open('modelo_recomendacion.pkl', 'rb') as archivo:
        model = pickle.load(archivo)

    predictions = model.predict(userId, id)

    if predictions.est >= 4:
        mensaje = "Muy recomendada"
    elif predictions.est >=3 and predictions.est < 4:
        mensaje = "Recomendada"
    else:
        mensaje = "No te la recomiendo", predictions.est
    return {"mensaje": mensaje}

"""
    The previous code calculates if a movie can be liked or not by a user. 
    Receiving as a parameter the id of the user and the id of a movie.
""" 