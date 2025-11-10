@echo off
chcp 65001 > nul
echo ================================
echo Daily Paper Assistant
echo ================================
echo.

cd /d "%~dp0"

python run.py

pause
