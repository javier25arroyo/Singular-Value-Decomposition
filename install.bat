@echo off
echo ========================================
echo   Instalador SVD Image Compression
echo ========================================
echo.

echo [1/3] Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en PATH
    echo Por favor instala Python 3.10 o superior desde https://www.python.org
    pause
    exit /b 1
)
echo.

echo [2/3] Actualizando pip...
python -m pip install --upgrade pip
echo.

echo [3/3] Instalando dependencias...
pip install -r requirements.txt
echo.

echo ========================================
echo   Instalacion completada exitosamente!
echo ========================================
echo.
echo Para ejecutar la aplicacion, usa:
echo    run.bat
echo.
echo O directamente:
echo    python run.py
echo.
pause
