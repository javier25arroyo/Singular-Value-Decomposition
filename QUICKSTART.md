# 🚀 Guía de Inicio Rápido

## Instalación en 3 pasos

### Paso 1: Verificar Python
Asegúrate de tener Python 3.10 o superior instalado:
```bash
python --version
```

Si no lo tienes, descárgalo desde [python.org](https://www.python.org/downloads/)

### Paso 2: Instalar dependencias

**Opción A - Windows (Fácil):**
Haz doble clic en `install.bat`

**Opción B - Línea de comandos:**
```bash
pip install -r requirements.txt
```

**Opción C - Con entorno virtual (Recomendado):**
```bash
# Crear entorno virtual
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/Mac)
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Paso 3: Ejecutar la aplicación

**Opción A - Windows (Fácil):**
Haz doble clic en `run.bat`

**Opción B - Línea de comandos:**
```bash
python run.py
```

## 🎯 Uso de la Aplicación

1. **Cargar Imagen**: 
   - Haz clic en "📁 Cargar Imagen"
   - Selecciona cualquier imagen (PNG, JPG, BMP, etc.)

2. **Ajustar Compresión**:
   - Mueve el slider hacia la izquierda para mayor compresión
   - Mueve el slider hacia la derecha para mejor calidad

3. **Ver Resultados**:
   - Lado izquierdo: Imagen original
   - Lado derecho: Imagen comprimida con SVD
   - Abajo: Estadísticas en tiempo real

4. **Guardar**:
   - Haz clic en "💾 Guardar Imagen Comprimida"
   - Elige dónde guardar tu imagen

## 📊 Entendiendo los Resultados

### Número de Valores Singulares (k)
- **Valor bajo (ej. k=10)**: Mucha compresión, imagen más borrosa
- **Valor alto (ej. k=100)**: Poca compresión, imagen más nítida

### Ratio de Compresión
- Indica cuántas veces más pequeña es la representación
- **Mayor ratio** = Más compresión = Menor tamaño de archivo

### Energía Retenida
- Porcentaje de información preservada
- **90%+**: Excelente calidad, pérdida mínima
- **70-90%**: Buena calidad, compresión notable
- **<70%**: Baja calidad, alta compresión

## 💡 Consejos

### Para obtener mejores resultados:
- Usa imágenes de tamaño mediano (300x300 a 1000x1000 píxeles)
- Imágenes con patrones simples comprimen mejor
- Fotografías requieren más valores singulares para mantener calidad

### Valores recomendados de k:
- **Iconos/logos**: k = 10-30
- **Dibujos simples**: k = 20-50
- **Fotografías**: k = 50-150
- **Imágenes detalladas**: k = 100-200

## 🔧 Solución de Problemas

### Error: "No module named 'PIL'"
```bash
pip install Pillow
```

### Error: "No module named 'numpy'"
```bash
pip install numpy matplotlib scipy
```

### Error: "tkinter no encontrado"
**Windows**: Reinstala Python desde python.org con la opción "tcl/tk" marcada
**Linux**: `sudo apt-get install python3-tk`
**Mac**: Tkinter debería venir incluido

### La aplicación no inicia
1. Verifica que Python esté en el PATH
2. Ejecuta `install.bat` nuevamente
3. Intenta ejecutar directamente: `python src\proyecto_svd\gui.py`

## 📚 Más Información

- Consulta el [README.md](README.md) completo para detalles técnicos
- Explora el notebook [ejemplo_svd.ipynb](notebooks/ejemplo_svd.ipynb)
- Revisa el código en `src/proyecto_svd/`

## 🆘 Ayuda Adicional

Si encuentras problemas:
1. Verifica que todas las dependencias estén instaladas
2. Asegúrate de estar en el directorio correcto del proyecto
3. Revisa que la versión de Python sea 3.10 o superior

---

¡Disfruta comprimiendo imágenes con SVD! 🎉
