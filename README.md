# Proyecto Machine Learning Operations (MLOps) 
# API de Recomendación de Juegos

Este proyecto implementa una API para disponibilizar y analizar datos de juegos de la plataforma Steam usando el framework FastAPI. También incluye un modelo de aprendizaje automático que aplica la similitud del coseno para proporcionar recomendaciones de juegos personalizadas a los usuarios.

## Requisitos

- Python 3.7 o superior
- FastAPI
- Uvicorn
- pandas
- numpy
- scikit-learn
- scipy

## Funcionalidades de la API

### 1. Developer Data
**Endpoint:** `/developer/{desarrollador}`

**Descripción:** Devuelve la cantidad de items y el porcentaje de contenido gratuito por año para una empresa desarrolladora especificada.

### 2. User Data
**Endpoint:** `/userdata/{User_id}`

**Descripción:** Devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendaciones basadas en reviews (`reviews.recommend`) y la cantidad de items.

### 3. User For Genre
**Endpoint:** `/UserForGenre/{genero}`

**Descripción:** Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

### 4. Best Developer of the Year
**Endpoint:** `/best_developer_year/{año}`

**Descripción:** Devuelve el top 3 de desarrolladores con juegos más recomendados por los usuarios para el año dado (considerando `reviews.recommend` = True y comentarios positivos).

### 5. Developer Reviews Analysis
**Endpoint:** `/developer_reviews_analysis/{desarrolladora}`

**Descripción:** Según el desarrollador, devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios categorizadas por análisis de sentimiento como positivo o negativo.

### 6. Recomendación de Usuario
**Endpoint:** `/recomendacion_usuario/{user_id}`

**Descripción:** Ingresando el ID de un usuario, devuelve una lista con 5 juegos recomendados para dicho usuario aplicando la similitud del coseno.

## Análisis Exploratorio de Datos (EDA)

El proyecto incluye un análisis exploratorio de los datos (EDA) para entender mejor las características y tendencias dentro del conjunto de datos de juegos. 

## Modelo de Aprendizaje Automático

El modelo de aprendizaje automático utilizado en este proyecto aplica la similitud del coseno para proporcionar recomendaciones personalizadas de juegos. La matriz usuario-item se crea a partir de los datos de revisión y se calcula la similitud del coseno entre usuarios para identificar juegos potencialmente interesantes para cada usuario.

## Render

El proyecto está desplegado y accesible en [Render](https://proyecto-pi01-dataft22.onrender.com/docs).


Para más información, puedes contactarme a través de:

- **Email:** [luchyescobedo@gmail.com](mailto:luchyescobedo@gmail.com)
- **LinkedIn:** [Lucía Escobedo](https://www.linkedin.com/in/lucia-escobedo-b76555202)





