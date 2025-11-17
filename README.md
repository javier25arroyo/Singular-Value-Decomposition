# Proyecto SVD - Compresión de Imágenes

Aplicación interactiva en Python para compresión de imágenes usando Descomposición en Valores Singulares (SVD).

## 🎯 Características

- **Interfaz Gráfica Intuitiva**: UI amigable construida con Tkinter
- **Compresión con SVD**: Aplica la descomposición en valores singulares a imágenes
- **Control en Tiempo Real**: Ajusta el nivel de compresión con un slider interactivo
- **Estadísticas Detalladas**: Visualiza el ratio de compresión y energía retenida
- **Soporte Multi-formato**: Compatible con PNG, JPG, BMP, GIF, TIFF
- **Guardar Resultados**: Exporta las imágenes comprimidas

## 🔧 Requisitos

- Python 3.10 o superior
- pip

## 📦 Instalación

1. **Clonar o descargar el repositorio**

2. **Crear entorno virtual (recomendado)**:
   ```powershell
   # Windows PowerShell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Instalar dependencias**:
   ```powershell
   pip install -r requirements.txt
   ```

## 🚀 Uso

### Iniciar la aplicación:

```powershell
python run.py
```

O también puedes ejecutar directamente:

```powershell
python src\proyecto_svd\gui.py
```

### Pasos para usar la aplicación:

1. **Cargar Imagen**: Haz clic en "📁 Cargar Imagen" y selecciona una imagen
2. **Ajustar Compresión**: Mueve el slider para cambiar el número de valores singulares (k)
3. **Ver Resultados**: Observa la imagen comprimida y las estadísticas en tiempo real
4. **Guardar**: Haz clic en "💾 Guardar Imagen Comprimida" para exportar el resultado

### Información sobre los parámetros:

- **k (Valores Singulares)**: Número de componentes principales a mantener
  - Valor bajo: Mayor compresión, menor calidad
  - Valor alto: Menor compresión, mayor calidad
  
- **Ratio de Compresión**: Cuántas veces más pequeña es la representación comprimida

- **Energía Retenida**: Porcentaje de información preservada de la imagen original

## 🧮 Fundamentos Matemáticos

La Descomposición en Valores Singulares (SVD) factoriza una matriz A en:

```
A = U × Σ × V^T
```

Donde:
- **U**: Matriz ortogonal de vectores singulares izquierdos
- **Σ**: Matriz diagonal con valores singulares (ordenados)
- **V^T**: Matriz ortogonal transpuesta de vectores singulares derechos

Para comprimir una imagen:
1. Cada canal de color se trata como una matriz
2. Se calcula la SVD de cada matriz
3. Se retienen solo los k valores singulares más grandes
4. Se reconstruye: A_k = U[:, :k] × Σ[:k, :k] × V^T[:k, :]

## 📁 Estructura del Proyecto

```
Proyecto-SVD/
├─ data/                    # Imágenes de entrada/salida
├─ src/
│  └─ proyecto_svd/
│     ├─ __init__.py        # Inicialización del paquete
│     ├─ svd_image.py       # Lógica de procesamiento SVD
│     ├─ gui.py             # Interfaz gráfica
│     └─ main.py            # Punto de entrada
├─ tests/                   # Pruebas unitarias
├─ notebooks/               # Jupyter notebooks (exploración)
├─ requirements.txt         # Dependencias
├─ run.py                   # Script de ejecución principal
└─ README.md
```

## 📚 Módulos Principales

### `svd_image.py`
Contiene la clase `SVDImageProcessor` que maneja:
- Carga de imágenes
- Cálculo de SVD por canal de color
- Reconstrucción con k componentes
- Cálculo de métricas (compresión, energía)

### `gui.py`
Implementa la interfaz gráfica `SVDImageApp` con:
- Visualización lado a lado (original vs comprimida)
- Control interactivo con slider
- Información en tiempo real
- Carga y guardado de imágenes

## 🎓 Aplicaciones

- **Educación**: Aprender sobre álgebra lineal y SVD
- **Compresión**: Reducir tamaño de imágenes con pérdida controlada
- **Análisis**: Entender qué información es más importante en una imagen
- **Procesamiento**: Preprocesar imágenes para machine learning

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Haz fork del repositorio
2. Crea una rama para tu feature
3. Commit con mensajes descriptivos
4. Abre un Pull Request

## 📄 Licencia

Por definir.

## 👨‍💻 Desarrollo

### Estándares de código:
- PEP 8 para estilo de Python
- Docstrings para funciones y clases
- Type hints donde sea apropiado

### Testing:
```powershell
python -m pytest tests/
```

## 📖 Referencias

- [Singular Value Decomposition - Wikipedia](https://en.wikipedia.org/wiki/Singular_value_decomposition)
- [NumPy SVD Documentation](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html)
- Aplicaciones de SVD en procesamiento de imágenes

---

Desarrollado con ❤️ para el curso de Álgebra Lineal
