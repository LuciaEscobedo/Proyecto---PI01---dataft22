#Usaremos el framework FastAPI 
#Importamos Librerias
from fastapi import FastAPI
from funciones import developer, userdata, UserForGenre, best_developer_year, developer_reviews_analysis, recomendacion_usuario

app = FastAPI ()

@app.get('/developer/{desarrollador}')
def get_developer(desarrollador: str):
    resultado = developer(desarrollador)
    return resultado

@app.get('/userdata/{user_id}')
def get_userdata(user_id: str):
    resultado = userdata(user_id)
    return resultado

@app.get('/UserForGenre/ {genero}')
def get_UserForGenre(genero:str):
    resultado = UserForGenre(genero)
    return resultado

@app.get('/best_developer_year/ {year}')
def get_best_developer_year(year:int):
    resultado = best_developer_year(year)
    return resultado

@app.get('/developer_reviews_analysis/ {desarrollador}')
def get_developer_reviews_analysis(desarrollador:str):
    resultado = developer_reviews_analysis(desarrollador)
    return resultado

@app.get('/recomendacion_usuario/ {user_id}')
def get_recomendacion_usuario(user_id:str):
    resultado = recomendacion_usuario(user_id)
    return resultado

