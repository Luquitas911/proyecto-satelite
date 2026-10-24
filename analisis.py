from satelite import Satelite
from catalogo import grupo

def contar_por_tipo(satelites: list[Satelite]) -> dict[str, int]:
    """
    Devuelve un diccionario {"LEO": n, "MEO": n, "GEO": n, "HEO": n}
    con la cantidad de satélites de cada tipo de órbita.
    Las cuatro claves siempre están presentes (en 0 si no hay satélites de ese tipo).
    """
    conteo = {"LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}
    for satelite in satelites:
        conteo[satelite.tipo_orbita()] += 1
    return conteo


def mas_bajo(satelites: list) -> str:
    """"devuelven el objeto Satelite de menor y de mayor altitud.mas_bajo(satelites) 
    y mas_alto(satelites): devuelven el objeto Satelite de menor y de mayor altitud."""
    menor = satelites[0]
    for satelite in satelites:
        if satelite.altitud_km < menor.altitud_km:
            menor = satelite
    return menor

def mas_alto(satelites: list) -> str:
    """"devuelven el objeto Satelite de menor y de mayor altitud.mas_bajo(satelites) y 
    mas_alto(satelites): devuelven el objeto Satelite de menor y de mayor altitud."""
    mayor = satelites[0]
    for satelite in satelites:
        if satelite.altitud_km > mayor.altitud_km:
            mayor = satelite
    return mayor

def en_zona(satelites: list[Satelite], zona: tuple[float, float, float, float]) -> list[Satelite]:
    """
    Devuelve la lista de satélites que están dentro de la zona.

    La zona es una tupla (lon_min, lat_min, lon_max, lat_max).
    Usa el método esta_en_zona de cada satélite.
    """
    resultado = []
    for satelite in satelites:
        if satelite.esta_en_zona(zona):
            resultado.append(satelite)
    return resultado

def ordenar_por(satelites: list[Satelite], atributo: str, descendente: bool = False) -> list[Satelite]:
    """
    Devuelve una lista nueva con los satélites ordenados por el atributo indicado
    ("altitud_km", "latitud", "longitud", "nombre", ...).

    Si descendente es True, el orden es de mayor a menor. La lista original no se modifica.
    """
    return sorted(satelites, key=lambda s: getattr(s, atributo), reverse=descendente)


def top_n(satelites: list[Satelite], n: int, mas_altos: bool = True) -> list[Satelite]: 
    """devuelve los n satélites más altos (o más bajos), reutilizando ordenar_por."""
    lista = ordenar_por(satelites, "altitud_km", mas_altos)
    return lista[:n]
    

def resumen_por_grupo(satelites: list[Satelite]) -> dict[str, dict[str, float]]: 
    """usando grupo de catalogo.py, devuelve un diccionario con un resumen de las altitudes de cada grupo:
    {
    "Starlink": {"cantidad": 11125, "minima": 121.0, "media": 470.2, "maxima": 597.2},
    ...}    """
    #Agrupar las altitudes por grupo
    altitudes = {}
    for satelite in satelites:
        nombre_grupo = grupo(satelite.nombre)
        if nombre_grupo not in altitudes:
            altitudes[nombre_grupo] = []
        altitudes[nombre_grupo].append(satelite.altitud_km)

    #Calcular el reesumen de cada grupo
    resumen = {}
    for nombre_grupo, lista in altitudes.items():
        resumen[nombre_grupo] = {
            "cantidad": len(lista),
            "minima" : min(lista),
            "media": sum(lista) / len(lista),
            "maxima": max(lista),

        }
    return resumen
