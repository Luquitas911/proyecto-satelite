def contar_por_tipo(satelites):
    conteo = {"LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}
    for satelite in satelites:
        conteo[satelite.tipo_orbita()] += 1
    return conteo


def mas_bajo(satelites: list) -> str:
    """"devuelven el objeto Satelite de menor y de mayor altitud.mas_bajo(satelites) y mas_alto(satelites): devuelven el objeto Satelite de menor y de mayor altitud."""
    menor = satelites[0]
    for satelite in satelites:
        if satelite.altitud_km < menor.altitud_km:
            menor = satelite
    return menor

def mas_alto(satelites: list) -> str:
    """"devuelven el objeto Satelite de menor y de mayor altitud.mas_bajo(satelites) y mas_alto(satelites): devuelven el objeto Satelite de menor y de mayor altitud."""
    mayor = satelites[0]
    for satelite in satelites:
        if satelite.altitud_km > mayor.altitud_km:
            mayor = satelite
    return mayor

def en_zona(satelites, zona):
    """devuelve una lista de los satélites dentro de la zona (usando el método esta_en_zona)."""
    resultado = []
    for satelite in satelites:
        if satelite.esta_en_zona(zona):
            resultado.append(satelite)
    return resultado

def ordenar_por(satelites, atributo, descendente=False): 
    """función genérica que devuelve una lista nueva ordenada por cualquier atributo ("altitud_km", "latitud", "nombre", ...). Pista: sorted con key=lambda y getattr."""
    resultado = []
    for satelite in satelites:
            if satelite.esta_en_zona(zona):
                resultado.append(satelite)
    return resultado.sort()

def top_n(satelites, n, mas_altos=True): 
    """devuelve los n satélites más altos (o más bajos), reutilizando ordenar_por."""

def resumen_por_grupo(satelites): 
    """usando grupo de catalogo.py, devuelve un diccionario con un resumen de las altitudes de cada grupo:
    {
    "Starlink": {"cantidad": 11125, "minima": 121.0, "media": 470.2, "maxima": 597.2},
    ...}    """

