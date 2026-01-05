@echo off
echo ========================================
echo Social Content Creator - Frontend
echo ========================================
echo.

cd /d "%~dp0frontend"

if not exist "node_modules" (
    echo Instalando dependencias...
    npm install
)

echo.
echo Iniciando frontend...
echo URL: http://localhost:5173
echo.

npm run dev
