import json

def leer_satelites(ruta: str) -> list:

    """
    ... lee el archivo JSON (con codificación utf-8) y devuelve la lista de registros. 
    ... Si el archivo no existe, imprime un aviso y devuelve una lista vacía.
    """

    try:
        with open (ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
            return datos
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{ruta}' no existe.")
        return []

def anio_lanzamiento(registro: list) -> int:

    """
    ... devuelve el año de lanzamiento como int, a partir de los
    ... primeros cuatro caracteres de "OBJECT_ID"
    """

    anio = int(registro[OBJECT_ID][:4])
    return anio
