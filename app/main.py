import pandas as pd
from fastapi import FastAPI

app = FastAPI(title='Mi primer API',
            version='1.0.0')

@app.get("/")
async def read_root():
    return 'Funcionaaaa'


@app.get('/get_max_duration')
async def get_max_duration(anio:int, plataforma:str, duracion:str):
    df = pd.read_csv('Datasets\datos_titulos.csv')
    if duracion=='min':
        tipo='Movie'
    elif duracion =='season':
        tipo='TV Show'
    else:
        return 'No se entiende que desea buscar, por favor inserte min o season'
    max_duracion=(df.duration[((df['plataform']==plataforma)&(df['release_year']==anio)&(df['type'].str.contains(tipo)))].max())
    film_max=str(df.title[((df['plataform']==plataforma)&(df['duration']==max_duracion)&(df['type'].str.contains(tipo))&(df['release_year']==anio))].max())
    

    return 'El fim más largo es: ', film_max

@app.get('/get_count_plataforma')
async def get_count_plataforma(plataforma:str):
    df = pd.read_csv('Datasets\datos_titulos.csv')
    movie=((df['plataform']==plataforma)&(df['type'].str.contains('Movie'))).sum()
    show=((df['plataform']==plataforma)&(df['type'].str.contains('TV Show'))).sum()

    return f'Plataform: {plataforma} |Movies: {movie} |Tv show: {show}'

@app.get('/get_listedin')
async def get_listed_in(categoria:str):
    df = pd.read_csv('Datasets\datos_titulos.csv')    
    plataforma = ""
    plataformas = df.plataform.unique()
    max = 0
    for i in plataformas:
        if df[df.plataform==i].listed_in.str.count(categoria).sum() > max:
            max = df[df.plataform==i].listed_in.str.count(categoria).sum()
            plataforma = i
    return f"La plataforma con más titulos listados en el genero {categoria} es: {plataforma} con un total de {max} titulos"

@app.get('/get_actor')
def get_actor(plataforma:str, anio:int):
    df = pd.read_csv('Datasets\datos_titulos.csv')    
    lista_actores = df[(df['plataform'] ==plataforma) & (df['release_year'] == anio)].cast.str.split(',').dropna()  
    total_actores = []
    for actores in lista_actores:
        total_actores+= [(actor.strip(' ')) for actor in actores]
    conteo_actores=[total_actores.count(conteo) for conteo in total_actores]
    conteo_actores= dict(list(zip(total_actores, conteo_actores)))
    conteo_actores=[(conteo_actores[i], i) for i in conteo_actores]
    conteo_actores.sort(reverse=True)
    mayor=conteo_actores[0]
    mayor

    return f'En: {plataforma} en el año: {anio} el actor más mencionado es: {mayor[1]} en: {mayor[0]} apariciones'