@echo off
title STARPath - Accessible STAR Programme Assistant
echo ==============================================================================
echo  STARPath - Accessible STAR Programme Assistant (CO2007 Agile Team Project)
echo  Starting local FastAPI server at http://127.0.0.1:8000
echo ==============================================================================

cd /d "%~dp0"

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python was not found on PATH.
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

:: Launch default web browser after 1 second
start "" http://127.0.0.1:8000

:: Start FastAPI application with Uvicorn
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload

pause
