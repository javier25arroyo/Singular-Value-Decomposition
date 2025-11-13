# Proyecto SVD (Álgebra Lineal)

Proyecto en Python para trabajar con la Descomposición en Valores Singulares (SVD) aplicada a problemas de álgebra lineal.

## Objetivo
Configurar la base del repositorio y documentar cómo instalar, ejecutar y estructurar el proyecto.

## Requisitos
- Python 3.10 o superior

## Instalación
1) Crear entorno virtual (opcional pero recomendado):
   - Windows PowerShell: `python -m venv .venv && .\.venv\Scripts\Activate.ps1`
2) Instalar dependencias: `pip install -r requirements.txt`

## Uso
- Añade tus scripts en `src/` o un paquete `proyecto_svd/` y ejecuta con `python tu_script.py`.
- Para notebooks, usa `notebooks/` y ejecuta con Jupyter o VS Code.

## Estructura sugerida
```
Proyecto-SVD/
├─ data/                # Datos de entrada/salida (no sensibles)
├─ notebooks/           # Exploración y prototipos
├─ src/                 # Código fuente del proyecto
│  └─ proyecto_svd/
│     ├─ __init__.py
│     └─ main.py
├─ tests/               # Pruebas unitarias
├─ requirements.txt
├─ README.md
└─ .gitignore
```

## Desarrollo
- Estándar de código: PEP8 (recomendado usar linters como flake8/ruff y black).
- Convenciones de commits: tipo convencional (feat, fix, docs, chore, etc.).

## Licencia
Por definir.
