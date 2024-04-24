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
            with gzip.open(ruta_completa, "rt", encoding="latin1") as archivo_comprimido:
                for num_linea, linea in enumerate(archivo_comprimido, start=1):
                    if re.search(patron, linea):
                        print(f"Coincidencia encontrada en {ruta_completa}, línea {num_linea}: {linea.strip()}")

# Ejemplo de uso
carpeta_busqueda = "/mnt/local/datos/Contras/Collection 1"
patron_busqueda = r"nopoquina@hotmail\.com"
buscar_en_archivos_comprimidos(carpeta_busqueda, patron_busqueda)
