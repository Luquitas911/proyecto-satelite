class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.altitud_km = altitud_km

#g
    

    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""

        #Tipo 	Altitud
        #LEO (órbita baja) 	menor a 2.000 km
        #MEO (órbita media) 	de 2.000 km a menos de 34.000 km
        #GEO (geoestacionaria) 	de 34.000 km a 37.000 km
        #HEO (alta / otras) 	mayor a 37.000 km
        if self.altitud_km > 2000:
            return "LEO"

        if self.altitud_km > 2000 < 34000:
            return "MEO"

        if self.altitud_km < 37000 < 34000:
            return "GEO"

        else:
            return "HEO"


    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""

    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""

def crear_satelites(registros, momento):
    """Devuelve una lista de objetos Satelite con su posición en `momento`."""

