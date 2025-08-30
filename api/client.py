# Este archivo contendrá la lógica para conectarse a la API de datos.gov.co
import pandas as pd
from sodapy import Socrata

def get_department_data(nombre_departamento, limite_registros):
    """
    Consulta la API de datos.gov.co para obtener casos de COVID-19
    por departamento y un límite de registros.
    """
    # Cliente no autenticado para datasets públicos
    client = Socrata("www.datos.gov.co", None)

    # Realizar la consulta con los parámetros recibidos por la función.
    # Nota: Se usa 'departamento_nom' según la documentación de la API.
    results = client.get(
        "gt2j-8ykr",
        limit=limite_registros,
        departamento_nom=nombre_departamento
    )

    # Convertir los resultados a un DataFrame de pandas y retornarlo.
    results_df = pd.DataFrame.from_records(results)
    return results_df
