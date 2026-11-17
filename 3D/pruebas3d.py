import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Funciones3D import (
    leer_satelites, inspeccionar_satelite, calcular_parametros_fisicos,
    normalizar_parametros, velocidad_y_tiempo,
    lineas_tierra, dibujar_ejes, esfera,
    punto_orbita, dibujar_pelota, actualizar,
)

# ----------------------------------------------------------------------
# DATOS: elegimos un satélite de la lista

RUTA_JSON = "datos/satelites.json"
INDICE = 0                       # posición del satélite dentro de la lista
DURACION_VUELTA_S = 10           # cuánto dura una vuelta orbital en la animación

registros = leer_satelites(RUTA_JSON)

if not registros:                # solo para poder probar sin el JSON (ISS de ejemplo)
    registros = [{
        "OBJECT_NAME": "ISS (ZARYA)", "MEAN_MOTION": 15.5, "ECCENTRICITY": 0.0005,
        "INCLINATION": 51.6, "RA_OF_ASC_NODE": 100.0, "ARG_OF_PERICENTER": 80.0,
        "MEAN_ANOMALY": 10.0,
    }]

satelite = inspeccionar_satelite(registros[INDICE])

# ----------------------------------------------------------------------
# FÍSICA: parámetros, radios terrestres, velocidad y tiempo

fisica = calcular_parametros_fisicos(satelite)
if not fisica:
    raise SystemExit("No se pudieron calcular los parámetros físicos de este satélite.")

norm = normalizar_parametros(fisica)
if not norm["orbita_valida"]:
    print("Advertencia: el perigeo queda dentro de la Tierra.")

# Primera llamada para conocer el período; segunda con el factor que hace
# que una vuelta dure DURACION_VUELTA_S segundos en la animación.
cinematica = velocidad_y_tiempo(satelite, fisica)
factor = cinematica["periodo_s"] / DURACION_VUELTA_S
cinematica = velocidad_y_tiempo(satelite, fisica, factor_aceleracion=factor)

# ----------------------------------------------------------------------
#  ÓRBITA: a, b y la inclinación que espera punto_orbita

e = satelite.get("ECCENTRICITY", 0.0)
a = norm["a_norm"]                       # semieje mayor, en radios terrestres
b = a * np.sqrt(1 - e ** 2)              # semieje menor
theta = np.radians(satelite.get("INCLINATION", 0.0))

t = np.linspace(0, 2 * np.pi, 300)
ox, oy, oz = punto_orbita(t, a, b, theta)

# ----------------------------------------------------------------------
# FIGURA: Tierra, malla, ejes y órbita

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection='3d')

x, y, z = esfera(0, 0, 0, 1, n=60)
ax.plot_surface(x, y, z, color='lightsteelblue', alpha=0.3)

for pts, color, ancho in lineas_tierra():      # meridianos, paralelos, ecuador y Greenwich
    ax.plot(*pts, color=color, lw=ancho)

dibujar_ejes(ax)
ax.plot(ox, oy, oz, color='red', linewidth=2)

lim = max(a * 1.1, 1.9)
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)
ax.set_zlim(-lim, lim)
ax.set_box_aspect((1, 1, 1))
ax.set_axis_off()

# Datos del satélite (calculados con velocidad_y_tiempo)
ax.text2D(0.02, 0.97,
          f"{satelite.get('OBJECT_NAME')}\n"
          f"Periodo: {cinematica['periodo_min']:.1f} min\n"
          f"Velocidad en el perigeo: {cinematica['v_perigeo_kms']:.2f} km/s\n"
          f"Velocidad en el apogeo:  {cinematica['v_apogeo_kms']:.2f} km/s\n"
          f"1 vuelta = {DURACION_VUELTA_S} s en pantalla (x{factor:,.0f})\n"
          f"{satelite['aviso_grafico']}",
          transform=ax.transAxes, va='top', family='monospace', fontsize=9)

# ----------------------------------------------------------------------
# ANIMACIÓN: la pelotita recorre la órbita

pelota = [None]
dibujar_pelota(0, pelota, ax, a, b, theta)   # posición inicial, así se ve aunque no corra la animación

intervalo = DURACION_VUELTA_S * 1000 / 120   # actualizar usa 120 cuadros por vuelta
ani = FuncAnimation(fig, actualizar, frames=120, interval=intervalo, blit=False,
                    fargs=(pelota, ax, a, b, theta))

plt.show()
