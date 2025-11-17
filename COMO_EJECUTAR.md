# 🚀 Cómo Ejecutar el Proyecto SVD

## ⚡ Método Rápido (Windows) - RECOMENDADO

### Paso 1: Instalar Dependencias
1. Abre la carpeta `Proyecto-SVD`
2. **Haz doble clic en `install.bat`**
3. Espera a que termine la instalación (1-2 minutos)
4. Presiona cualquier tecla cuando termine

### Paso 2: Ejecutar la Aplicación
1. **Haz doble clic en `run.bat`**
2. ¡La aplicación se abrirá automáticamente!

```
┌─────────────────────────────────┐
│  📁 Proyecto-SVD               │
├─────────────────────────────────┤
│  📄 install.bat    ← Haz doble clic PRIMERO
│  📄 run.bat        ← Haz doble clic DESPUÉS
│  📄 run.py
│  📄 README.md
│  ...
└─────────────────────────────────┘
```

---

## 💻 Método Manual (Línea de Comandos)

### Opción A: PowerShell o CMD

```powershell
# 1. Abre PowerShell o CMD en la carpeta del proyecto
cd d:\GitHub\Algebra-lineal\Proyecto-SVD

# 2. Instala las dependencias (solo la primera vez)
pip install -r requirements.txt

# 3. Ejecuta la aplicación
python run.py
```

### Opción B: Terminal de VS Code

```bash
# Si estás en VS Code, abre la terminal (Ctrl + `)
# Y ejecuta:

pip install -r requirements.txt
python run.py
```

---

## 🐍 Método con Entorno Virtual (Recomendado para Desarrolladores)

### Windows PowerShell:

```powershell
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
python run.py
```

### Windows CMD:

```cmd
# 1. Crear entorno virtual
python -m venv .venv

# 2. Activar entorno virtual
.venv\Scripts\activate.bat

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
python run.py
```

### Linux/Mac:

```bash
# 1. Crear entorno virtual
python3 -m venv .venv

# 2. Activar entorno virtual
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar aplicación
python run.py
```

---

## 🎯 Alternativa: Ejecutar Directamente la GUI

```bash
# Desde la carpeta del proyecto:
python src\proyecto_svd\gui.py
```

---

## ✅ Verificar que Todo Funciona

### Ejecutar los Demos (sin GUI)

```bash
# Demo simple para verificar que SVD funciona
python src\proyecto_svd\demo_simple.py
```

Esto ejecutará 3 demos:
1. SVD con matriz simple
2. SVD con imagen sintética
3. Creación de imagen de ejemplo

### Ejecutar Tests

```bash
# Instalar pytest si no lo tienes
pip install pytest

# Ejecutar tests
pytest tests/
```

---

## 🔧 Solución de Problemas

### ❌ Error: "python no se reconoce como comando"

**Solución:**
1. Instala Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca "Add Python to PATH"
3. Reinicia tu terminal/CMD

### ❌ Error: "No module named 'PIL'" o "No module named 'numpy'"

**Solución:**
```bash
pip install -r requirements.txt
```

### ❌ Error: "tkinter no encontrado"

**Solución Windows:**
1. Reinstala Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, selecciona "Customize installation"
3. Asegúrate de que "tcl/tk and IDLE" esté marcado

**Solución Linux:**
```bash
sudo apt-get install python3-tk
```

**Solución Mac:**
Tkinter viene incluido con Python de python.org

### ❌ Error: "Permission denied" al ejecutar .bat

**Solución:**
1. Clic derecho en el archivo .bat
2. Selecciona "Ejecutar como administrador"

### ❌ La ventana se abre pero está en blanco

**Solución:**
1. Cierra la aplicación
2. Actualiza las dependencias: `pip install --upgrade pillow numpy matplotlib`
3. Intenta de nuevo

---

## 📖 Uso Básico de la Aplicación

Una vez que la aplicación se abra:

### 1️⃣ Cargar una Imagen
- Clic en **"📁 Cargar Imagen"**
- Selecciona cualquier imagen (PNG, JPG, etc.)
- Puedes usar tus propias fotos o descargar imágenes de prueba

### 2️⃣ Ajustar la Compresión
- Mueve el **slider** de valores singulares (k)
- Hacia la izquierda = Más compresión (menor calidad)
- Hacia la derecha = Menos compresión (mayor calidad)

### 3️⃣ Ver Resultados
- **Izquierda**: Imagen original
- **Derecha**: Imagen comprimida con SVD
- **Abajo**: Estadísticas (ratio, energía retenida)

### 4️⃣ Guardar
- Clic en **"💾 Guardar Imagen Comprimida"**
- Elige ubicación y nombre
- Guarda en PNG, JPG u otro formato

### 5️⃣ Aprender Más
- Clic en **"ℹ️ Información SVD"**
- Lee sobre la teoría matemática
- Entiende cómo funciona la compresión

---

## 🎨 Ejemplo Visual del Flujo

```
INICIO
  ↓
[Doble clic en install.bat] → Instala dependencias
  ↓
[Doble clic en run.bat] → Abre la aplicación
  ↓
┌─────────────────────────────────────────┐
│  🖼️ SVD Image Compression              │
│  [📁 Cargar] [💾 Guardar] [ℹ️ Info]   │
├────────────────┬────────────────────────┤
│   ORIGINAL     │   COMPRIMIDA           │
│   [Imagen]     │   [Imagen]             │
├────────────────┴────────────────────────┤
│  k: [━━━●━━━━━] 50                      │
│  Ratio: 4.5x | Energía: 95%            │
└─────────────────────────────────────────┘
  ↓
[Ajustar slider] → Ver cambios en tiempo real
  ↓
[Guardar] → Exportar imagen comprimida
  ↓
FIN
```

---

## 📝 Comandos Útiles

```bash
# Ver versión de Python
python --version

# Ver paquetes instalados
pip list

# Actualizar pip
python -m pip install --upgrade pip

# Instalar un paquete individual
pip install numpy
pip install pillow
pip install matplotlib

# Desinstalar todo y empezar de nuevo
pip uninstall -r requirements.txt -y
pip install -r requirements.txt

# Ver ayuda de Python
python --help
```

---

## 🆘 ¿Necesitas Más Ayuda?

1. **Documentación completa**: Lee `README.md`
2. **Guía rápida**: Lee `QUICKSTART.md`
3. **Ejemplos de código**: Revisa `docs/EJEMPLOS.md`
4. **Teoría**: Consulta `docs/TEORIA_SVD.md`
5. **Código fuente**: Explora `src/proyecto_svd/`

---

## ✨ Tips Adicionales

### Para Estudiantes
- Experimenta con diferentes imágenes
- Prueba valores extremos de k (muy bajo y muy alto)
- Observa cómo cambian las estadísticas
- Lee la ventana de información (botón ℹ️)

### Para Desarrolladores
- Revisa el código en `src/proyecto_svd/svd_image.py`
- Ejecuta los tests: `pytest tests/`
- Explora el notebook: `jupyter lab notebooks/ejemplo_svd.ipynb`
- Personaliza la GUI en `src/proyecto_svd/gui.py`

### Para Docentes
- Usa el demo simple: `python src\proyecto_svd\demo_simple.py`
- Muestra el notebook en clase
- Explica la teoría con `docs/TEORIA_SVD.md`
- Deja que los estudiantes experimenten con la GUI

---

## 🎓 Recursos de Aprendizaje

Después de ejecutar el proyecto:

1. **Notebook Interactivo**:
   ```bash
   jupyter lab notebooks/ejemplo_svd.ipynb
   ```

2. **Demo Simple**:
   ```bash
   python src\proyecto_svd\demo_simple.py
   ```

3. **Tests**:
   ```bash
   pytest tests/ -v
   ```

---

¡Disfruta explorando SVD! 🎉
