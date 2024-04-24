import gzip
import os
import re

def buscar_en_archivos_comprimidos(carpeta, patron):
    """
    Busca el patrón en todos los archivos comprimidos (.gz) dentro de la carpeta especificada.
    :param carpeta: Ruta de la carpeta donde se encuentran los archivos comprimidos.
    :param patron: Expresión regular a buscar.
    """
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".gz"):
            ruta_completa = os.path.join(carpeta, archivo)
            with gzip.open(ruta_completa, "rt") as archivo_comprimido:
                for num_linea, linea in enumerate(archivo_comprimido, start=1):
                    if re.search(patron, linea):
                        print(f"Coincidencia encontrada en {ruta_completa}, línea {num_linea}: {linea.strip()}")

def main():
    while True:
        print("\nMenú:")
        print("1. Buscar patrón en archivos comprimidos")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            carpeta_busqueda = input("Ingrese la ruta de la carpeta a buscar: ")
            patron_busqueda = input("Ingrese el patrón a buscar: ")
            buscar_en_archivos_comprimidos(carpeta_busqueda, patron_busqueda)
        elif opcion == "2":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()