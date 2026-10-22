import json

def leer_satelites(ruta: str) -> list:

    """
    ... lee el archivo JSON (con codificación utf-8) y devuelve la lista de registros. 
    ... Si el archivo no existe, imprime un aviso y devuelve una lista vacía.
    """

    try:
        with open (ruta, "r", encoding="utf-8") as f:
            registro = json.load(f)
            return registro
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{ruta}' no existe.")
        return []

