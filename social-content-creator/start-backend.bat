@echo off
echo ========================================
echo Social Content Creator - Backend
echo ========================================
echo.

cd /d "%~dp0backend"

if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Instalando dependencias...
pip install -r requirements.txt --quiet

echo.
echo Iniciando servidor...
echo API: http://localhost:8000
echo Docs: http://localhost:8000/docs
echo.

python main.py
