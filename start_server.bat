@echo off
REM TechBlog Server Starter
REM Community blog platform

echo ============================================================
echo  TechBlog - Community Platform
echo  Starting development server...
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing Flask...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo Starting TechBlog server...
echo.
echo Server will be available at: http://localhost:5000
echo.
echo User accounts:
echo   sarah_dev / summer2023 (admin)
echo   mike_codes / password1
echo   alex_js / 123456
echo   jenny_react / qwerty
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause