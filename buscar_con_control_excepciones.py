import gzip
import os
import re

carpeta_busqueda = "/mnt/local/datos/Contras/Collection 1"

def abrir_otros(ruta_completa, patron):
    try:
        with open(os.path.join(ruta_completa), "r", encoding="latin1") as archivo_normal:
            for num_linea, linea in enumerate(archivo_normal, start=1):
                if re.search(re.escape(patron), linea):  # Escape patron input
                    print(f"Coincidencia encontrada en {ruta_completa}, línea {num_linea}: {linea.strip()}")
    except exit as e:
        print(f"Error al procesar archivo normal: {e}")
        pass
 

# Buscar en archivos comprimidos
def abrir_gz(ruta_completa, patron):
    try:
        with gzip.open(ruta_completa, "rt", encoding="latin1") as archivo_comprimido:
            for num_linea, linea in enumerate(archivo_comprimido, start=1):
                if re.search(re.escape(patron), linea):  # Escape patron input
                    print(f"Coincidencia encontrada en {ruta_completa}, línea {num_linea}: {linea.strip()}")
    except gzip.BadGzipFile as e:
        print(f"Error al procesar archivo comprimido: {e}")
        pass


def semilla(carpeta, patron):
    """
    Busca el patrón en todos los archivos comprimidos (.gz) dentro de la carpeta especificada.
    :param carpeta: Ruta de la carpeta donde se encuentran los archivos comprimidos.
    :param patron: Expresión regular a buscar.
    """
    try:
        for archivo in os.listdir(carpeta):
            ruta_completa = os.path.join(carpeta, archivo)
            if archivo.endswith(".gz"):               
                abrir_gz(ruta_completa, patron)
            else:
                abrir_otros(ruta_completa, patron)
                with open(os.path.join(carpeta, archivo), "r", encoding="latin1") as archivo_normal:
                    for num_linea, linea in enumerate(archivo_normal, start=1):
                        if re.search(re.escape(patron), linea):  # Escape patron input
                            print(f"Coincidencia encontrada en {ruta_completa}, línea {num_linea}: {linea.strip()}")
    except FileNotFoundError:
        print(f"No se encontró la carpeta '{carpeta}'.")
        pass
    except gzip.BadGzipFile as e:
        print(f"Error al procesar archivo comprimido: {e}")
        pass

def main():
    while True:
        print("\nMenú:")
        print("1. Buscar patrón en archivos comprimidos")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            carpeta_busqueda = input("Ingrese la ruta de la carpeta a buscar: ")
            patron_busqueda = input("Ingrese el patrón a buscar: ")            
            semilla(carpeta_busqueda, patron_busqueda)
        elif opcion == "2":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()