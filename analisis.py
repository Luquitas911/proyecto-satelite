def contar_por_tipo(satelites): 
    
    """devuelve un diccionario {"LEO": n, "MEO": n, "GEO": n, "HEO": n}
    con las cuatro claves siempre presentes (en 0 si no hay satélites de ese tipo).""" 


def mas_bajo(satelites):
    """"devuelven el objeto Satelite de menor y de mayor altitud.mas_bajo(satelites) y mas_alto(satelites): devuelven el objeto Satelite de menor y de mayor altitud."""


def mas_alto(satelites): 
    """"devuelven el objeto Satelite de menor y de mayor altitud.mas_bajo(satelites) y mas_alto(satelites): devuelven el objeto Satelite de menor y de mayor altitud."""


def en_zona(satelites, zona): 
    """devuelve una lista de los satélites dentro de la zona (usando el método esta_en_zona)."""


def ordenar_por(satelites, atributo, descendente=False): 
    """función genérica que devuelve una lista nueva ordenada por cualquier atributo ("altitud_km", "latitud", "nombre", ...). Pista: sorted con key=lambda y getattr."""


def top_n(satelites, n, mas_altos=True): 
    """devuelve los n satélites más altos (o más bajos), reutilizando ordenar_por."""

def resumen_por_grupo(satelites): 
    """usando grupo de catalogo.py, devuelve un diccionario con un resumen de las altitudes de cada grupo:
    {
    "Starlink": {"cantidad": 11125, "minima": 121.0, "media": 470.2, "maxima": 597.2},
    ...}    """

