#!/bin/bash
# TechBlog Server Starter
# Community blog platform

echo "============================================================"
echo " TechBlog - Community Platform"
echo " Starting development server..."
echo "============================================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}Error: Python is not installed${NC}"
        echo "Please install Python from https://python.org"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

# Check if Flask is installed
if ! $PYTHON_CMD -c "import flask" &> /dev/null; then
    echo -e "${YELLOW}Installing Flask...${NC}"
    if command -v pip3 &> /dev/null; then
        pip3 install -r requirements.txt
    else
        pip install -r requirements.txt
    fi
    
    if [ $? -ne 0 ]; then
        echo -e "${RED}Error: Failed to install dependencies${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Starting TechBlog server...${NC}"
echo ""
echo -e "${GREEN}Server will be available at: http://localhost:5000${NC}"
echo ""
echo "User accounts:"
echo "  sarah_dev / summer2023 (admin)"
echo "  mike_codes / password1"
echo "  alex_js / 123456"
echo "  jenny_react / qwerty"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

$PYTHON_CMD app.py