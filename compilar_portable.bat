@echo off
echo ========================================
echo   Compilando AsistenciaQR PORTABLE
echo ========================================
echo.

REM Limpiar builds anteriores
if exist "dist\AsistenciaQR" rmdir /s /q "dist\AsistenciaQR"
if exist "build" rmdir /s /q "build"

REM Compilar con PyInstaller (sin empaquetar static)
echo [1/3] Compilando con PyInstaller...
python -m PyInstaller --onedir --noconsole --icon=icono.ico ^
    --add-data "templates;templates" ^
    --hidden-import=flask ^
    --hidden-import=werkzeug ^
    --hidden-import=jinja2 ^
    --hidden-import=waitress ^
    --hidden-import=qrcode ^
    --hidden-import=PIL ^
    --hidden-import=openpyxl ^
    --hidden-import=pandas ^
    --hidden-import=numpy ^
    --exclude-module=tkinter ^
    --exclude-module=matplotlib ^
    --name=AsistenciaQR ^
    app.py

if errorlevel 1 (
    echo [ERROR] Fallo la compilacion
    pause
    exit /b 1
)

echo.
echo [2/3] Copiando carpeta static...
xcopy /E /I /Y "static" "dist\AsistenciaQR\static"

echo.
echo [3/3] Copiando base de datos...
if exist "base_datos.db" (
    copy /Y "base_datos.db" "dist\AsistenciaQR\"
) else if exist "_datos.db" (
    copy /Y "_datos.db" "dist\AsistenciaQR\base_datos.db"
) else (
    echo [AVISO] No se encontro base de datos, se creara al ejecutar
)

echo.
echo ========================================
echo   COMPILACION COMPLETADA
echo ========================================
echo.
echo La aplicacion esta en: dist\AsistenciaQR\
echo.
echo ESTRUCTURA FINAL:
echo   AsistenciaQR.exe      (ejecutable principal)
echo   _internal\            (dependencias Python)
echo   static\               (recursos, fotos, QR, config)
echo   base_datos.db         (base de datos)
echo.
pause
