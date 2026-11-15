from datetime import datetime, timezone
import matplotlib.pyplot as plt
import json
import math


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




def calcular_parametros_fisicos(satelite):

    """
    ... Recibe el diccionario de un satélite y devuelve un nuevo diccionario
    ... con el semieje mayor (a), perigeo, apogeo y alturas en kilómetros.
    """

    MU_TIERRA = 398600.4418  # Constante gravitacional de la Tierra (km^3/s^2)
    RADIO_TIERRA = 6378.137  # Radio ecuatorial de la Tierra (km)

    resultados = {}

    mean_motion = satelite.get("MEAN_MOTION")
    excentricidad = satelite.get("ECCENTRICITY", 0)

    if mean_motion is None or mean_motion <= 0:
        print("Error: MEAN_MOTION inválido o faltante.")
        return resultados

    # Convertir movimiento medio (rev/día) a velocidad angular (rad/s)
    n_rad_s = (mean_motion * 2 * math.pi) / 86400.0

    # Tercera Ley de Kepler: a = (mu / n^2)^(1/3)
    semieje_mayor = (MU_TIERRA / (n_rad_s ** 2)) ** (1 / 3)

    # Radios desde el centro de la Tierra (en km)
    radio_perigeo = semieje_mayor * (1 - excentricidad)
    radio_apogeo = semieje_mayor * (1 + excentricidad)


    resultados["semieje_mayor_km"] = semieje_mayor
    resultados["radio_perigeo_km"] = radio_perigeo
    resultados["radio_apogeo_km"] = radio_apogeo
    resultados["altura_perigeo_km"] = radio_perigeo - RADIO_TIERRA
    resultados["altura_apogeo_km"] = radio_apogeo - RADIO_TIERRA

    return resultados


def normalizar_parametros(fisica):
    """
    ... Reutiliza el diccionario de salida generado por `calcular_parametros_fisicos`
    ... (que contiene 'semieje_mayor_km', 'radio_perigeo_km' y 'radio_apogeo_km')
    ... para escalar las distancias a Radios Terrestres (RT = 6371.0 km).
    """
    RADIO_TIERRA = 6378.137
    normalizados = {}

    if not fisica or "semieje_mayor_km" not in fisica:
        print("Se requiere el diccionario válido generado por 'calcular_parametros_fisicos'.")
        return normalizados

    # Reutilizar las distancias en km y dividirlas por el radio de la Tierra
    a_norm = fisica["semieje_mayor_km"] / RADIO_TIERRA
    rp_norm = fisica["radio_perigeo_km"] / RADIO_TIERRA
    ra_norm = fisica["radio_apogeo_km"] / RADIO_TIERRA

    # Validar que el perigeo quede fuera de la esfera terrestre (radio > 1)
    orbita_valida = rp_norm > 1.0

    normalizados["a_norm"] = a_norm
    normalizados["rp_norm"] = rp_norm
    normalizados["ra_norm"] = ra_norm
    normalizados["orbita_valida"] = orbita_valida

    return normalizados


print(normalizar_parametros(calcular_parametros_fisicos(registros[1])))
