# Proyecto Satélite - Análisis Orbital

Trabajo práctico de procesamiento y análisis de datos de satélites activos con Python y Jupyter Notebook. Permite:

- Clasificar satélites por tipo de órbita.
- Analizar altitudes extremas.
- Agrupar satélites por constelaciones comerciales.
- Evaluar la evolución de los lanzamientos desde 2015.
- Calcular qué objetos pasan sobre una zona geográfica específica (Bariloche).

## Estructura del repositorio

```
proyecto-satelite/
├── datos/
│   └── satelites.json        # Datos de entrada de los satélites
├── analisis.py               # Funciones de filtrado, ordenamiento y estadísticas
├── catalogo.py               # Lectura del JSON y clasificación comercial/temporal
├── funciones_base.py         # Cálculos de posición y órbita con Skyfield
├── satelite.py               # Clase Satelite y sus métodos
├── informe.ipynb             # Notebook principal con la ejecución y el informe
├── .gitignore
└── README.md
```

## Requisitos y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/Luquitas911/proyecto-satelite.git
cd proyecto-satelite
```

2. Instalar las dependencias:

```bash
pip install skyfield
```

3. Abrir `informe.ipynb` en VS Code o Jupyter Notebook y ejecutar todas las celdas en orden, de principio a fin.

## Integrantes y aportes

### Ezequiel Santana

- Desarrollo completo del módulo `catalogo.py` (`leer_satelites`, `anio_lanzamiento`, `grupo`, `contar_por_grupo` y `lanzamientos_por_anio`).
- Secciones 4 (Tipos de órbita), 5 (Extremos) y 8 (Conclusiones) de `informe.ipynb`.

### Esteban

- Implementación inicial de `funciones_base.py`.
- Clase `Satelite` y sus métodos (`tipo_orbita`, `esta_en_zona`) en `satelite.py`.
- Funciones `mas_bajo` y `mas_alto` en `analisis.py`.
- Secciones 6 (Comparación de grupos) y 7 (Satélites sobre Bariloche) de `informe.ipynb`.

### Lucas

- Configuración inicial del repositorio, carga de los datos JSON y definición del `.gitignore`.
- Estructura inicial y desarrollo del módulo `analisis.py`.
- Implementación de type hints, corrección de bugs y resolución de conflictos en el historial de Git.
- Armado base e integración general de `informe.ipynb`.
