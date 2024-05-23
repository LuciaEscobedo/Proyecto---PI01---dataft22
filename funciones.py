import pandas as pd

# def developer( desarrollador : str ): 
# Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

# Funcion Developer
def developer(desarrollador: str):
    # Cargar el Dataset
    df_desarrolladores = pd.read_parquet('./Datasets/def_developer.parquet')


    # Filtrar los datos para el desarrollador dado
    desarrollador_data = df_desarrolladores[df_desarrolladores['publisher'] == desarrollador]

    if not desarrollador_data.empty:
        # Filtrar los juegos gratuitos
        juegos_gratuitos = desarrollador_data[desarrollador_data['price'] == 0]

        # Inicializar el diccionario para contener la información
        items_x_anio = {}

        # Recorrer las filas de datos del desarrollador 
        for _, row in desarrollador_data.iterrows():
            year = row['release_date']  # Usar directamente el año de la columna release_date
            items_x_anio.setdefault(year, {"Cantidad_items": 0, "Cantidad_contenido_free": 0})
            items_x_anio[year]["Cantidad_items"] += 1

        # Actualizar la cantidad de contenido gratuito por año
        for _, row in juegos_gratuitos.iterrows():
            year = row['release_date']  # Usar directamente el año de la columna release_date
            items_x_anio[year]["Cantidad_contenido_free"] += 1

        # Generar la respuesta para cada año
        respuesta = []
        for year, data in items_x_anio.items():
            Cantidad_items = data["Cantidad_items"]
            Cantidad_contenido_free = data["Cantidad_contenido_free"]
            total_items = Cantidad_items + Cantidad_contenido_free
            Contenido_free_porcentaje = f"{(Cantidad_contenido_free / total_items) * 100:.2f}%"
            respuesta.append(
                {
                    "Año": year,
                    "Cantidad de Items": Cantidad_items,
                    "Porcentaje de Contenido Free": Contenido_free_porcentaje,
                }
            )
        return respuesta 
    else:
        return {"error": "Desarrollador no encontrado"}


#def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas 
# para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.


# Función Userdata
def userdata(User_id: str):

    # Cargar el Dataset
    df_combined = pd.read_parquet('./Datasets/def_userdata.parquet')

    # Filtrar el DataFrame combinado por el User_id dado
    user_data = df_combined[df_combined['user_id'] == User_id].copy()  # Copiamos el DataFrame para evitar SettingWithCopyWarning
    
    if user_data.empty:
        return {"error": "Usuario no encontrado"}
    
    # Filtrar los precios que sean de tipo float
    user_data_float_prices = user_data[user_data['price'].apply(lambda x: isinstance(x, float))]
    
    # Calcular la cantidad de dinero gastado por el usuario
    total_money_spent = user_data_float_prices['price'].sum()
    
    # Calcular el porcentaje de recomendación positiva
    num_positive_recommendations = user_data[user_data['recommend']].shape[0]  # Usamos directamente valores booleanos
    
    if len(user_data) > 0:
        recommend_percentage = (num_positive_recommendations / len(user_data)) * 100
    else:
        recommend_percentage = 0
    
    # Calcular la cantidad de items del usuario
    total_items = len(user_data)
    
    return {
        "Usuario": User_id,
        "Dinero gastado": f"${total_money_spent:.2f}",
        "% de recomendación positiva": f"{recommend_percentage:.2f}%",
        "Cantidad de items": total_items
    }

import pandas as pd

# def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas 
# para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

#Funcion UserForGenre
def UserForGenre(genero: str):
    # Cargar el Dataset
    df_combined = pd.read_parquet('./Datasets/def_userforgenre.parquet')

    # Filtrar las filas que contienen el género especificado en alguna parte del texto
    filtered_df = df_combined[df_combined['genres'].str.contains(genero, case=False, na=False)]
    
    if filtered_df.empty:
        return {"error": "No se encontraron registros para el género especificado"}
    
    # Calcular la suma de horas jugadas por usuario para el género dado
    user_hours_sum = filtered_df.groupby('user_id')['playtime_forever'].sum().reset_index()
    
    # Encontrar al usuario con más horas jugadas para el género dado
    user_max_hours = user_hours_sum.loc[user_hours_sum['playtime_forever'].idxmax(), 'user_id']
    
    
    # Calcular la acumulación de horas jugadas por año de lanzamiento
    hours_per_year = filtered_df.groupby(filtered_df['release_date'])['playtime_forever'].sum().reset_index()
    hours_per_year = hours_per_year.rename(columns={'release_date': 'Año', 'playtime_forever': 'Horas'})
    hours_per_year = hours_per_year.to_dict(orient='records')
    
    return {
        "Usuario con más horas jugadas para el Género": user_max_hours,
        "Horas jugadas por año": hours_per_year
    }


# def best_developer_year( año : int ): Devuelve el top 3 de desarrolladores con juegos MÁS recomendados 
# por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)

#Funcion Best_developer_year
def best_developer_year(año: int):
    # Cargar el dataset
    df = pd.read_parquet('./Datasets/def_best_developer_year.parquet')
    
    # Filtrar el DataFrame por el año dado
    df_filtered = df[df['posted'] == año]
    
    # Agrupar y contar las ocurrencias por desarrollador
    grouped = df_filtered.groupby('publisher').size().reset_index(name='count')
    
    # Ordenar los resultados por cantidad de apariciones
    grouped_sorted = grouped.sort_values(by='count', ascending=False)
    
    # Obtener el top 3 de desarrolladores para el año dado
    top3_developers = grouped_sorted.head(3)
    
    # Formatear el resultado en el formato solicitado
    formatted_result = [{"Puesto 1": top3_developers.iloc[0, 0]}, 
                        {"Puesto 2": top3_developers.iloc[1, 0]},
                        {"Puesto 3": top3_developers.iloc[2, 0]}]
    
    return formatted_result
