"""
Script de ejecución principal para la aplicación SVD Image Compression.
Ejecuta este archivo para iniciar la interfaz gráfica.
"""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from proyecto_svd import main

if __name__ == "__main__":
    print("=== Iniciando SVD Image Compression ===")
    print("Cargando interfaz gráfica...")
    main()
