# This module will handle displaying the data to the user.
import pandas as pd

def show_report(df):
    """
    Receives a DataFrame and displays a filtered version of it.
    """
    try:
        # Lista de columnas requeridas segun el PDF
        required_columns = [
            'ciudad_municipio_nom',
            'departamento_nom',
            'edad',
            'fuente_tipo_contagio',
            'estado',
            'ubicacion'
        ]
        
        reporte_filtrado = df[required_columns]
        
        print("\n--- Reporte de Casos ---")
        print(reporte_filtrado.to_string())
        print("------------------------\n")

    except KeyError as e:
        print(f"\nError: Una columna requerida no se encontró: {e}")
        print("Por favor, verifica los nombres de las columnas.")
        print("Columnas disponibles en los datos recibidos:", df.columns.tolist())


def get_user_input():
    """
    Prompts the user for department and limit, and returns them.
    """
    department = input("Introduce el nombre del departamento: ")
    
    while True:
        try:
            limit_str = input("Introduce el número de registros a consultar: ")
            limit = int(limit_str)
            if limit <= 0:
                print("El número de registros debe ser positivo.")
            else:
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

    return department, limit
