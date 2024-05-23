import pandas as pd

# def developer( desarrollador : str ): 
# Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.

# Cargar el Dataset
df_desarrolladores = pd.read_parquet('./Datasets/def_developer.parquet')

def developer(desarrollador: str):
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


#