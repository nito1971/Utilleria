import os

# Ruta a recorrer.
ruta = "rutaARecorer"

# Función para recorrer el directorio y sus subdirectorios recursivamente.
def recorrer_directorio():
    """
    Recorre un directorio y sus subdirectorios y muestra la ruta de cada archivo.
    """
    try: # Comprobamos si la ruta es válida.
        for directorio, subdirectorio, archivos in os.walk(ruta):
            for archivo in archivos:
                ruta_archivo = os.path.join(directorio, archivo)
                print(ruta_archivo)
    except Exception as e:
        print(f"Error al recorrer el directorio: {e}")

# Ejecutamos la función.
if __name__ == "__main__":
    recorrer_directorio(ruta)