class Satelite:

    def __init__(self, nombre, latitud, longitud, altitud_km): #constructor
        """Toma los datos que entraron por los parámetros y los "pega" dentro del objeto usando self.."""
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altitud_km = altitud_km

    def tipo_orbita(self):
            """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""

            #Tipo 	Altitud
            #LEO (órbita baja) 	menor a 2.000 km
            #MEO (órbita media) 	de 2.000 km a menos de 34.000 km
            #GEO (geoestacionaria) 	de 34.000 km a 37.000 km
            #HEO (alta / otras) 	mayor a 37.000 km

            if self.altitud_km < 2000:
                return "LEO"

            if self.altitud_km < 34000:
                return "MEO"

            if self.altitud_km <= 37000 :
                return "GEO"

            else:
                return "HEO"


    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""

        lon_min, lat_min, lon_max, lat_max = zona
        return (lon_min <= self.longitud <= lon_max and lat_min <= self.latitud <= lat_max)

    def __str__(self) -> str:

        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""
        return f"{self.nombre} | {self.tipo_orbita()} | {self.altitud_km} km"


def crear_satelites(registros: list, momento) -> list:
    """Devuelve una lista de objetos Satelite con su posición en `momento`."""
    satelites = []
    for registro in registros:
        objeto = crear_objeto_skyfield(registro)
        latitud, longitud, altitud_km = obtener_posicion(objeto, momento)
        if altitud_km >= 100:
            satelites.append(Satelite(registro["OBJECT_NAME"], latitud, longitud, altitud_km))
    return satelites

