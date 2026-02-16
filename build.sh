#!/bin/bash
# ==============================================================================
# UK Walks Tracker - One-Command Build Script (Unix/Linux/Mac)
# ==============================================================================
# This script automates the entire build process:
# 1. Updates walks.yaml with new GPX files
# 2. Generates the interactive map
# 3. Creates missing journal files
# 4. Builds the Sphinx documentation
# ==============================================================================

set -e  # Exit on error

echo ""
echo "========================================================================"
echo "UK Walks Tracker - Build Process"
echo "========================================================================"
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "ERROR: Python is not installed or not in PATH"
    echo "Please install Python and try again"
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "WARNING: Virtual environment not found"
    echo "Run setup.sh first to create the environment and install dependencies"
    echo ""
    read -p "Continue anyway? (y/n): " CONTINUE
    if [ "$CONTINUE" != "y" ] && [ "$CONTINUE" != "Y" ]; then
        exit 1
    fi
fi

# Activate virtual environment if it exists
if [ -f "venv/bin/activate" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo ""
fi

echo "========================================================================"
echo "Step 1: Updating walks.yaml and generating map..."
echo "========================================================================"
$PYTHON_CMD scripts/update_uk_walks.py

echo ""
echo "========================================================================"
echo "Step 2: Building Sphinx documentation..."
echo "========================================================================"
cd docs
make html
cd ..

echo ""
echo "========================================================================"
echo "BUILD COMPLETE!"
echo "========================================================================"
echo ""
echo "Your documentation is ready at:"
echo "  docs/_build/html/index.html"
echo ""
echo "To view it, run:"
echo "  open docs/_build/html/index.html    # macOS"
echo "  xdg-open docs/_build/html/index.html  # Linux"
echo ""
