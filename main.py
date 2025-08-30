from ui.display import get_user_input, show_report
from api.client import get_department_data

def main():
    print("--- Bienvenido al consultor de datos COVID-19 de Colombia ---")
    
    continuar = 'S'
    while continuar.upper() == 'S':
        department, limit = get_user_input()
        print(f"\nBuscando {limit} registros para el departamento: {department}...")
        
        try:
            data = get_department_data(department, limit)
            if data.empty:
                print(f"No se encontraron datos para '{department}'. Intenta con otro departamento.")
            else:
                show_report(data)
        except Exception as e:
            print(f"\nOcurrió un error inesperado al consultar los datos: {e}")
            print("Por favor, intenta de nuevo.")

        while True:
            continuar = input("\n¿Desea realizar otra consulta? (S/N): ")
            if continuar.upper() in ['S', 'N']:
                break
            else:
                print("Respuesta no válida. Por favor, introduce S o N.")

    print("\n--- Gracias por usar el programa. ¡Hasta luego! ---")

if __name__ == "__main__":
    main()