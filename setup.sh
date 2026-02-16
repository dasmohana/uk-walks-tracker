#!/bin/bash
# ==============================================================================
# UK Walks Tracker - Initial Setup Script (Unix/Linux/Mac)
# ==============================================================================
# This script sets up your development environment:
# 1. Creates a Python virtual environment
# 2. Installs all required dependencies
# ==============================================================================

set -e  # Exit on error

echo ""
echo "========================================================================"
echo "UK Walks Tracker - Initial Setup"
echo "========================================================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "ERROR: Python is not installed or not in PATH"
    echo "Please install Python 3.8 or higher and try again"
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Installing dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "========================================================================"
echo "SETUP COMPLETE!"
echo "========================================================================"
echo ""
echo "Your development environment is ready."
echo ""
echo "Next steps:"
echo "  1. Add your GPX files to the gpx/ folder"
echo "  2. Run: ./build.sh"
echo ""
echo "To activate the virtual environment manually, run:"
echo "  source venv/bin/activate"
echo ""
