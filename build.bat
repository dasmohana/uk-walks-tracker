@ECHO OFF
REM ==============================================================================
REM UK Walks Tracker - One-Command Build Script (Windows)
REM ==============================================================================
REM This script automates the entire build process:
REM 1. Updates walks.yaml with new GPX files
REM 2. Generates the interactive map
REM 3. Creates missing journal files
REM 4. Builds the Sphinx documentation
REM ==============================================================================

SETLOCAL EnableDelayedExpansion

echo.
echo ========================================================================
echo UK Walks Tracker - Build Process
echo ========================================================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and try again
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv\" (
    echo WARNING: Virtual environment not found
    echo Run setup.bat first to create the environment and install dependencies
    echo.
    set /p CONTINUE="Continue anyway? (y/n): "
    if /i not "!CONTINUE!"=="y" exit /b 1
)

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
    echo.
)

echo ========================================================================
echo Step 1: Updating walks.yaml and generating map...
echo ========================================================================
python scripts\update_uk_walks.py
if errorlevel 1 (
    echo.
    echo ERROR: Failed to update walks and generate map
    exit /b 1
)

echo.
echo ========================================================================
echo Step 2: Building Sphinx documentation...
echo ========================================================================
cd docs
call make.bat html
if errorlevel 1 (
    cd ..
    echo.
    echo ERROR: Failed to build Sphinx documentation
    exit /b 1
)
cd ..

echo.
echo ========================================================================
echo BUILD COMPLETE!
echo ========================================================================
echo.
echo Your documentation is ready at:
echo   docs\_build\html\index.html
echo.
echo To view it, run:
echo   start docs\_build\html\index.html
echo.

ENDLOCAL
