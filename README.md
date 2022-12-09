# <h1 align=center> **Diego Cortez** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
</p>

¡Bienvenidos al primer proyecto individual de la etapa de labs! En esta ocasión, deberán hacer un trabajo situándose en el rol de un ***Data Engineer***.  

<hr>  

## **ETL**

El trabajo consistió en la limpieza de datos, uní los 4 datasets proporcionados en un dataframe con todos los datos necesarios, eliminé las columnas no necesarias para las consultas, la columna Duration la pasé a int y utilicé la columna type para tomar las variables por min o por season según si es Movie o TV Show.

También creé un código el cuál toma cada Film y en caso de estar repetido el Film entre plataformas normaliza sus valores(en caso de hulu que no tenía valores en la columna Cast ayudó a completar algunos de esos datos faltantes).


## **Querys y FastAPI**

Generé las preguntas, en total 4 preguntas:
    + Cantidad de Films por plataforma separado en Movie y TV Show.
    + Actores con más apariciones según el año y la plataforma.
    + Plataforma con más apariciones de Films según el género.
    + Movie ó Show con más min o seasons según plataforma y año.

Luego con FastAPI generé una intro al nombre de 'Funcionaaa' y las 4 preguntas ya antes mencionadas, todo esto en un archivo llamado main.py con el cual corre la API. Gracias a ello tenía lo necesario para generar mi entorno en Docker.

## **Docker**

En docker lo primero en hacerse fue el Dockerfile con un requirements que contiene lo necesario para descargar dentro de mi entorno. con ello cree la imagen de mi docker y luego el conteiner con puerto 80:80 e Ip 0.0.0.0.

De ahí corrió en el local host mi Api y le hice las preguntas requeridas para testear su funcionamiento.

## **Video demostrativo**

