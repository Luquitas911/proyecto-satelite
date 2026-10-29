Proyecto Satélite - Análisis Orbital

Trabajo práctico de procesamiento y análisis de datos de satélites activos utilizando Python y Jupyter Notebook. El proyecto permite clasificar satélites por tipo de órbita, analizar altitudes extremas, agrupar por constelaciones comerciales, evaluar la evolución de lanzamientos desde 2015 y calcular la presencia de objetos sobre zonas geográficas específicas (Bariloche).

Estructura del repositorio

proyecto-satelite/
├── datos/
│   └── satelites.json        # Archivo de entrada con datos de satélites
├── analisis.py               # Funciones de filtrado, ordenamiento y estadísticas
├── catalogo.py               # Lectura de JSON y clasificación comercial/temporal
├── funciones_base.py         # Cálculos de posición y órbita con Skyfield
├── satelite.py               # Clase Satelite y sus métodos
├── informe.ipynb             # Notebook principal con la ejecución e informe
├── .gitignore
└── README.md


Requisitos y ejecución

Clonar el repositorio:

git clone https://github.com/Luquitas911/proyecto-satelite.git
cd proyecto-satelite


Instalar dependencias necesarias:

pip install skyfield


Abrir y ejecutar informe.ipynb en VS Code o Jupyter Notebook corriendo las celdas en orden de principio a fin.

Integrantes y aportes

Ezequiel Santana:

Desarrollo íntegro del módulo catalogo.py (incluyendo las funciones leer_satelites, anio_lanzamiento, grupo, contar_por_grupo y lanzamientos_por_anio).

Desarrollo de las secciones 4 (Tipos de órbita), 5 (Extremos) y 8 (Conclusiones) en el notebook informe.ipynb.

Esteban:

Implementación inicial de funciones_base.py.

Definición de la clase Satelite y sus métodos (tipo_orbita, esta_en_zona) en satelite.py.

Desarrollo de las funciones mas_bajo y mas_alto en analisis.py.

Desarrollo de las secciones 6 (Comparación de grupos) y 7 (Satélites sobre Bariloche) en informe.ipynb.

Lucas:

Configuración inicial del repositorio, carga de datos JSON y definición del .gitignore.

Estructura inicial y desarrollo del módulo analisis.py.

Implementación de type hints, corrección de bugs y resolución de conflictos del historial de Git.

Armado base e integración general del notebook informe.ipynb.