from datetime import datetime, timezone
import matplotlib.pyplot as plt
import json


# Datos cargados

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

registros = leer_satelites("satelites.json")


def inspeccionar_satelite(satelite):
    """
    Lista todos los campos disponibles de un satélite y verifica si cuenta
    con los parámetros orbitales necesarios para dibujar su órbita.
    """
    datos = {}

    nombre = satelite.get("OBJECT_NAME")
    print(f"Nombre del satelite: {nombre}")

    # 1. Listar todos los campos que trae este diccionario
    for clave, valor in satelite.items():
        if valor is not None:
            datos[clave] = valor

    # 2. Verificar si faltan RAAN o Argumento del perigeo
    faltantes = []

    if "RA_OF_ASC_NODE" not in datos:
        datos["RA_OF_ASC_NODE"] = 0
        faltantes.append("RAAN")

    if "ARG_OF_PERICENTER" not in datos:
        datos["ARG_OF_PERICENTER"] = 0
        faltantes.append("Argumento del perigeo")

    # Guardamos el aviso en el mismo diccionario para usarlo después en el gráfico
    if faltantes:
        datos["aviso_grafico"] = f"Aviso: {', '.join(faltantes)} asumido(s) en 0"
    else:
        datos["aviso_grafico"] = "No hay parametros faltantes"

    return datos

print(inspeccionar_satelite(registros[2]))
