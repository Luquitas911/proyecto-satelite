# Pendientes:

- Hacer un programa aparte para las funciones y traerlas al programa


Fase 1: Datos y física

1. Revisar qué trae el JSON
Hay que listar los campos de cada satélite y marcar cuáles están disponibles. Para dibujar una órbita completa se necesitan:

tamaño: semieje mayor a, o perigeo y apogeo
forma: excentricidad e
orientación: inclinación, RAAN y argumento del perigeo

Si faltan los dos últimos, se definen valores por defecto (por ejemplo 0) y se avisa en el gráfico.

2. Normalizar unidades

Radio de la Tierra: 6371 km. La esfera del dibujo mide 1, así que todo se divide por ese valor.
Ojo: perigeo y apogeo suelen venir como altura sobre la superficie. La distancia al centro es altura + 6371 km.
Fórmulas: a = (rp + ra) / 2 y e = (ra − rp) / (ra + rp).
Validar que el perigeo quede fuera de la esfera.

3. Función de posición generalizada (en satelite.py o analisis.py)
Es la función posicion_orbita que te pasé antes: ecuación de Kepler, Tierra en el foco y las tres rotaciones. Conviene que no dibuje nada, que solo calcule posiciones. Así se puede probar sin gráficos.

4. Velocidad y tiempo

Periodo: T = 2π·sqrt(a³/μ), con μ = 398600 km³/s².
Velocidad en cada punto (ecuación vis-viva): v = sqrt(μ·(2/r − 1/a)).
Definir un factor de aceleración (por ejemplo, 1 segundo de animación = 10 minutos reales), porque una órbita real tarda horas.
Con esto la velocidad ya no es constante: el satélite va más rápido en el perigeo.
Fase 2: Dibujo

5. Rotación de la Tierra

Velocidad angular: una vuelta cada 23 h 56 min (86164 s), con el mismo factor de aceleración del paso 4.
Problema importante: una esfera lisa de un solo color rotando no se nota. Hay que dibujarle algo, como meridianos y paralelos, o los continentes.
Rotar líneas es mucho más liviano que redibujar una superficie en cada cuadro.

6. Ejes y referencias del planeta

Eje polar (norte-sur) como línea atravesando la esfera.
Círculo del ecuador.
Meridiano de Greenwich marcado en otro color (sirve para ver la rotación).
Opcional: flechas X, Y, Z con etiquetas.
Aclarar el sistema de referencia: la órbita queda fija en el espacio y la Tierra gira debajo.

7. Animación

Reemplazar la esfera del satélite por un punto, con set_data_3d, para que sea fluida.
Texto en pantalla que se actualice con la velocidad, la altura y el tiempo.
Opcional: estela de las últimas posiciones.
Fase 3: Integración

8. Armar graficos.py
Una función principal tipo graficar_satelite(satelite, factor_tiempo=...) que reciba el diccionario o el objeto, llame a las funciones de los pasos 3 y 4, y dibuje. Las funciones auxiliares (esfera, ejes_planeta, etc.) quedan en el mismo archivo.

9. Salida

Notebook: HTML(ani.to_jshtml()).
Script: plt.show().
Guardar en salidas/ como GIF (necesita pillow) o MP4 (necesita ffmpeg).

10. Validar con casos conocidos

ISS: periodo ~92,9 min, velocidad ~7,66 km/s, inclinación 51,6°.
Geoestacionario: 35 786 km de altura, periodo 23 h 56 min, velocidad ~3,07 km/s, y debería parecer quieto respecto a la Tierra que gira.


