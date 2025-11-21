# 📘 Guía de Instalación en Windows (Solo Windows)

Esta guía explica EXCLUSIVAMENTE cómo instalar y ejecutar el proyecto en computadoras con Windows.

## ✅ Requisitos Previos
- Windows 10/11
- Python 3.10 o superior (descargar desde https://www.python.org)
- Acceso a Internet para instalar dependencias
- (Opcional) Visual Studio Code para desarrollo

## 1️⃣ Verificar Instalación de Python
Abrir PowerShell (Win + X → Windows PowerShell) y ejecutar:
```powershell
python --version
```
Si aparece error, instala Python y marca la opción "Add Python to PATH" durante la instalación.

## 2️⃣ Métodos de Instalación
### Opción A (Usuario Final) – Automática
1. Abre la carpeta del proyecto.
2. Doble clic en `install.bat` (instala pip y dependencias).
3. Al finalizar, doble clic en `run.bat` para abrir la aplicación.

### Opción B (Manual Rápida) – Línea de Comandos
```powershell
# En la carpeta del proyecto
pip install -r requirements.txt
python run.py
```

### Opción C (Desarrollo) – Entorno Virtual (PowerShell)
```powershell
# 1. Crear entorno
python -m venv .venv

# 2. Activar entorno (PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. Actualizar pip (opcional)
python -m pip install --upgrade pip

# 4. Instalar dependencias
tpip install -r requirements.txt

# 5. Ejecutar aplicación
python run.py
```
Si usas CMD en lugar de PowerShell:
```cmd
.venv\Scripts\activate.bat
```

## 3️⃣ Ejecutar Directamente la Interfaz Gráfica
```powershell
python src\proyecto_svd\gui.py
```

## 4️⃣ Comprobación Rápida
```powershell
# Probar que funciona la compresión
python src\proyecto_svd\demo_simple.py
```

## 5️⃣ Estructura Mínima Esperada
```
Proyecto-SVD/
├─ install.bat
├─ run.bat
├─ run.py
├─ requirements.txt
├─ src/
│  └─ proyecto_svd/
│     ├─ gui.py
│     └─ svd_image.py
```

## 6️⃣ Problemas Comunes y Soluciones
| Problema | Causa | Solución |
|----------|-------|----------|
| "python no se reconoce" | Python no en PATH | Reinstalar marcando "Add Python to PATH" |
| "No module named PIL" | Falta Pillow | `pip install Pillow` |
| "No module named numpy" | Falta NumPy | `pip install numpy` |
| Ventana en blanco | Dependencias corruptas | `pip install --upgrade pillow numpy matplotlib` |
| Error al ejecutar .bat | Permisos | Clic derecho → "Ejecutar como administrador" |
| Tkinter ausente | Instalación incompleta | Reinstalar Python con "tcl/tk" marcado |

## 7️⃣ Comandos Útiles
```powershell
python --version          # Ver versión
pip list                  # Ver paquetes instalados
python -m pip install --upgrade pip
pip install numpy pillow matplotlib scipy
pytest tests/             # Ejecutar pruebas (si instalas pytest)
```

## 8️⃣ Limpieza (Reinstalar Dependencias)
```powershell
# (Opcional) Crear nuevo entorno limpio
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 9️⃣ Flujo Visual
```
INICIO
  ↓
[Doble clic install.bat] → Instala dependencias
  ↓
[Doble clic run.bat] → Abre aplicación
  ↓
[Interactuar con slider k]
  ↓
[Guardar imagen comprimida]
  ↓
FIN
```

## 🔍 Verificación de Calidad
- Prueba con una imagen pequeña (PNG/JPG)
- Ajusta k a valores bajos (10–30) y luego altos (100–150) para comparar
- Observa Ratio y Energía Retenida

## 🛠 Modo Desarrollo Adicional
```powershell
# Abrir VS Code en la carpeta
code .

# Ejecutar tests (instalar antes)
pip install pytest
pytest tests/ -v
```

## ❓ Ayuda
Si algo falla:
1. Confirma versión de Python.
2. Ejecuta nuevamente `install.bat`.
3. Activa entorno correcto (si usas .venv).
4. Revisa mensajes de error y aplica tabla de soluciones.

---
¡Listo! Tu entorno Windows está preparado para usar la compresión de imágenes con SVD. 🎉
