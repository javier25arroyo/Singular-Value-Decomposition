@echo off
echo ========================================
echo   SVD Image Compression
echo ========================================
echo.
echo Iniciando aplicacion...
echo.

python run.py

if errorlevel 1 (
    echo.
    echo ERROR: No se pudo ejecutar la aplicacion
    echo.
    echo Posibles soluciones:
    echo 1. Asegurate de haber instalado las dependencias: install.bat
    echo 2. Verifica que Python este instalado correctamente
    echo.
    pause
)
