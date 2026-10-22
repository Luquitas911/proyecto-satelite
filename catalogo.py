import json

#TODO no faltarian mas grupos? 
GRUPOS = {
        "STARLINK": "Starlink",
        "ONEWEB": "OneWeb",
        "KUIPER": "Kuiper",
        "QIANFAN": "Qianfan",
        "IRIDIUM": "Iridium",
        "GLOBALSTAR": "Globalstar",
        "NAVSTAR": "GPS",
        "BEIDOU": "BeiDou"
    }

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


#TODO Se hace generalizado o hay que poner un parametro extra? 
# Porque aca lo resolvi poniendo un [1], pero entonces solo agarra el primer item de todo el diccionario

def anio_lanzamiento(registro: list) -> int:

    """
    ... devuelve el año de lanzamiento como int, a partir de los
    ... primeros cuatro caracteres de "OBJECT_ID"
    """

    anio = int(registro[1]["OBJECT_ID"][:4])
    return anio


#TODO la funcion funciona, pero faltan prefijos
def grupo(nombre: str) -> str:

    """
    ... Devuelve el grupo al que pertenece un satélite según cómo empieza su nombre, 
    ... de acuerdo con la tabla de abajo. Si no coincide con ningún prefijo, devuelve "Otros". 
    """

    for nombre_registro, nombre_comercial in GRUPOS.items():
        if nombre.startswith(nombre_registro): 
            return nombre_comercial     
            
    return "Otros"


#TODO funciona bien esta funcion
def contar_por_grupo(registros: list) -> dict:

    """
    ... devuelve un diccionario {grupo: cantidad}, con la cantidad de satélites de cada grupo.
    """

    conteo = {}

    for satelite in registros:

        nombre_sat = satelite.get("OBJECT_NAME", "")
        grupo_st = grupo(nombre_sat)
        conteo[grupo_st] = conteo.get(grupo_st, 0) + 1
        
    return conteo



#TODO falta definir bien que es registro
def lanzamientos_por_anio(registros: list) -> dict:
    """
    ... Devuelve un diccionario {año: cantidad de satélites lanzados ese año}
    ... a partir de la lista de registros.
    """

    conteo = {}
    
    for satelite in registros:
        anio = anio_lanzamiento(satelite)
        conteo[anio] = conteo.get(anio, 0) + 1
        
    return conteo


