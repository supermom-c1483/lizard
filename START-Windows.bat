@echo off
title Lizard Pal 🦎
cd /d "%~dp0"

echo.
echo  Starting Lizard Pal...
echo.

:: Check for Python
python --version >nul 2>&1
if errorlevel 1 (
  python3 --version >nul 2>&1
  if errorlevel 1 (
    echo  Python is not installed.
    echo  Please install it from: https://www.python.org/downloads/
    echo  Make sure to check "Add Python to PATH" during install!
    pause
    exit /b 1
  )
  set PYTHON=python3
) else (
  set PYTHON=python
)

:: Check for .env file
if not exist ".env" (
  echo  Missing .env file!
  echo.
  echo  1. Find the file called '.env.example' in this folder
  echo  2. Make a copy of it and rename the copy to '.env'
  echo  3. Open .env with Notepad and replace 'your-api-key-here' with your API key
  echo  4. Save and double-click this file again
  echo.
  pause
  exit /b 1
)

:: Open browser after a short delay
start "" timeout /t 2 >nul
start "" "http://localhost:3000"

%PYTHON% server.py
pause
