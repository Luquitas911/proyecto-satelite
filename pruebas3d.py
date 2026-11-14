import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def esfera(cx, cy, cz, r, n=30):
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)
    x = cx + r * np.outer(np.cos(u), np.sin(v))
    y = cy + r * np.outer(np.sin(u), np.sin(v))
    z = cz + r * np.outer(np.ones_like(u), np.cos(v))
    return x, y, z

# Órbita
a, b = 2.0, 1.3
theta = np.radians(30)

def punto_orbita(t):
    ex = a * np.cos(t)
    ey = b * np.sin(t)
    ez = 0 * t
    ey_rot = ey * np.cos(theta) - ez * np.sin(theta)
    ez_rot = ey * np.sin(theta) + ez * np.cos(theta)
    return ex, ey_rot, ez_rot

t = np.linspace(0, 2 * np.pi, 300)
ox, oy, oz = punto_orbita(t)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Elementos fijos
x, y, z = esfera(0, 0, 0, 1, n=60)
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
ax.plot(ox, oy, oz, color='red', linewidth=2)

ax.set_box_aspect((1, 1, 1))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
ax.set_axis_off()

# Pelotita: se dibuja YA desde el principio
pelota = [None]

def dibujar_pelota(t0):
    if pelota[0] is not None:
        pelota[0].remove()
    px, py, pz = punto_orbita(t0)
    x2, y2, z2 = esfera(px, py, pz, 0.2)
    pelota[0] = ax.plot_surface(x2, y2, z2, color='orange')

dibujar_pelota(0)   # posición inicial, así se ve aunque no corra la animación

def actualizar(frame):
    dibujar_pelota(2 * np.pi * frame / 120)

ani = FuncAnimation(fig, actualizar, frames=120, interval=30, blit=False)

plt.show()