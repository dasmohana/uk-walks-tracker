@ECHO OFF
REM ==============================================================================
REM UK Walks Tracker - Initial Setup Script (Windows)
REM ==============================================================================
REM This script sets up your development environment:
REM 1. Creates a Python virtual environment
REM 2. Installs all required dependencies
REM ==============================================================================

echo.
echo ========================================================================
echo UK Walks Tracker - Initial Setup
echo ========================================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher and try again
    exit /b 1
)

echo Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies from requirements.txt...
python -m pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    exit /b 1
)

echo.
echo ========================================================================
echo SETUP COMPLETE!
echo ========================================================================
echo.
echo Your development environment is ready.
echo.
echo Next steps:
echo   1. Add your GPX files to the gpx\ folder
echo   2. Run: build.bat
echo.
echo To activate the virtual environment manually, run:
echo   venv\Scripts\activate.bat
echo.
