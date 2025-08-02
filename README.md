# 📚 Gestor de Colecciones

Una aplicación de consola en Python para gestionar tu colección personal de películas, libros y música de manera organizada y eficiente.

## 🚀 Características

- **Gestión completa de medios**: Administra películas, libros y música en un solo lugar
- **Búsqueda avanzada**: Busca por título, autor/director/artista, género o identificador único
- **Categorización**: Organiza tus elementos por género
- **Edición flexible**: Modifica cualquier campo de tus elementos existentes
- **Sistema de IDs únicos**: Cada elemento tiene un identificador único para evitar duplicados
- **Persistencia de datos**: Guarda y carga colecciones en formato JSON
- **Interfaz intuitiva**: Menús claros y navegación sencilla

## 🛠️ Instalación

### Prerrequisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

### Dependencias

Instala las dependencias necesarias:

```bash
pip install tabulate
```

### Configuración

1. Clona o descarga el proyecto
2. Asegúrate de que la estructura de carpetas sea la siguiente:

```
proyecto/
├── main_menu.py                    # Archivo principal
├── Anadir/
│   └── anadir_elemento.py         # Módulo para añadir elementos
├── modif/
│   ├── buscar.py                  # Módulo de búsqueda
│   ├── editar.py                  # Módulo de edición
│   ├── eliminar.py                # Módulo de eliminación
│   └── colecciones.py             # Gestión de colecciones
├── tablas_contenido/
│   ├── contenido.py               # Visualización de contenido
│   └── categorias.py              # Navegación por categorías
├── utils/
│   ├── corefiles.py               # Manejo de archivos JSON
│   ├── id.py                      # Generación de IDs únicos
│   ├── screencontrollers.py       # Control de pantalla
│   └── validatedata.py            # Validación de datos
└── data/
    └── coleccion.json             # Archivo de datos (se crea automáticamente)
```

## 🎮 Uso

### Iniciar la aplicación

```bash
python main_menu.py
```

### Menú Principal

La aplicación presenta un menú principal con las siguientes opciones:

1. **Añadir un nuevo elemento**: Agrega películas, libros o música
2. **Ver elementos existentes**: Visualiza tu colección por categorías
3. **Buscar un elemento**: Encuentra elementos específicos
4. **Editar elementos**: Modifica información de elementos existentes
5. **Eliminar un elemento**: Remueve elementos de tu colección
6. **Ver elementos por categoría**: Explora por géneros
7. **Guardar y cargar colección**: Gestiona múltiples colecciones
8. **Salir**: Cierra la aplicación

### Añadir Elementos

#### Película
- Título
- Director
- Género
- Valoración

#### Libro
- Título
- Autor
- Género
- Valoración

#### Música
- Título
- Artista
- Género
- Valoración

### Funciones de Búsqueda

- **Por título**: Búsqueda exacta del nombre
- **Por autor/director/artista**: Busca por el creador del contenido
- **Por género**: Filtra por categoría
- **Por ID único**: Localiza usando el identificador del sistema

### Gestión de Colecciones

- **Guardar colección actual**: Preserva tu trabajo actual
- **Nombrar y guardar**: Crea colecciones con nombres personalizados
- **Cargar colección**: Abre colecciones previamente guardadas
- **Ver colecciones disponibles**: Lista todas las colecciones guardadas

## 📁 Estructura de Datos

Los datos se almacenan en formato JSON con la siguiente estructura:

```json
{
    "peliculas": [
        {
            "titulo": "Nombre de la película",
            "director": "Nombre del director",
            "genero": "Género",
            "valoracion": "Puntuación",
            "id": "pelicula0001"
        }
    ],
    "libros": [
        {
            "titulo": "Nombre del libro",
            "autor": "Nombre del autor",
            "genero": "Género",
            "valoracion": "Puntuación",
            "id": "libro0001"
        }
    ],
    "musica": [
        {
            "titulo": "Nombre de la canción",
            "artista": "Nombre del artista",
            "genero": "Género",
            "valoracion": "Puntuación",
            "id": "musica0001"
        }
    ]
}
```

## 🔧 Módulos del Sistema

### Utils
- **corefiles.py**: Manejo de archivos JSON y persistencia de datos
- **id.py**: Generación automática de identificadores únicos
- **screencontrollers.py**: Control de la interfaz de consola
- **validatedata.py**: Validación de entrada de datos

### Funcionalidades Principales
- **anadir_elemento.py**: Lógica para agregar nuevos elementos
- **buscar.py**: Sistema de búsqueda con múltiples criterios
- **editar.py**: Modificación de elementos existentes
- **eliminar.py**: Eliminación segura de elementos
- **colecciones.py**: Gestión de múltiples colecciones

### Visualización
- **contenido.py**: Muestra elementos en formato de tabla
- **categorias.py**: Navegación y filtrado por géneros

## 🐛 Problemas Conocidos

- El archivo `utils/id.py` tiene funciones duplicadas con el mismo nombre, lo que puede causar comportamiento inesperado
- La búsqueda por identificador en `buscar.py` busca por "identificador" en lugar de "id"
- Algunos elementos en el JSON de ejemplo no tienen ID asignado

## 🤝 Contribuir

1. Haz fork del proyecto
2. Crea una rama para tu función (`git checkout -b feature/nueva-funcion`)
3. Realiza commit de tus cambios (`git commit -am 'Agrega nueva función'`)
4. Push a la rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## 📝 Notas de Desarrollo

- El sistema utiliza identificadores únicos automáticos para cada tipo de elemento
- Los datos se validan antes de ser guardados
- La interfaz se limpia automáticamente para mejor experiencia de usuario
- Compatible con Windows, macOS y Linux

## 🆘 Soporte

Si encuentras algún problema o tienes sugerencias, por favor:

1. Revisa la sección de problemas conocidos
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de que la estructura de carpetas sea correcta
4. Comprueba los permisos de escritura en la carpeta `data/`

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**¡Disfruta organizando tu colección de medios!** 🎬📚🎵