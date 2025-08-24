#!/bin/bash
# Upload TechBlog to GitHub
# Make sure you have git installed and are logged into GitHub

echo "============================================================"
echo " Uploading TechBlog to GitHub"
echo " Repository: https://github.com/exovm/test-website-with-bugs"
echo "============================================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}Error: Git is not installed${NC}"
    echo "Please install Git from https://git-scm.com/"
    exit 1
fi

# Initialize git repository if not already done
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}Initializing Git repository...${NC}"
    git init
    echo ""
fi

# Add remote repository
echo -e "${YELLOW}Adding GitHub remote...${NC}"
git remote remove origin 2>/dev/null
git remote add origin https://github.com/exovm/test-website-with-bugs.git
echo ""

# Add all files
echo -e "${YELLOW}Adding files to git...${NC}"
git add .
echo ""

# Create commit
echo -e "${YELLOW}Creating commit...${NC}"
git commit -m "Initial commit: TechBlog community platform

- Flask-based blog platform for developers
- User authentication and profiles  
- Post creation and search functionality
- File upload capabilities
- Admin dashboard
- Network tools for developers
- RESTful API endpoints
- Modern responsive design"
echo ""

# Push to GitHub
echo -e "${YELLOW}Pushing to GitHub...${NC}"
git branch -M main
git push -u origin main
echo ""

if [ $? -eq 0 ]; then
    echo -e "${GREEN}============================================================${NC}"
    echo -e "${GREEN} Successfully uploaded to GitHub!${NC}"
    echo -e "${GREEN} Repository: https://github.com/exovm/test-website-with-bugs${NC}"
    echo -e "${GREEN}============================================================${NC}"
else
    echo -e "${RED}============================================================${NC}"
    echo -e "${RED} Upload failed. Please check:${NC}"
    echo -e "${RED} 1. You're logged into GitHub${NC}"
    echo -e "${RED} 2. You have access to the repository${NC}"
    echo -e "${RED} 3. Repository exists and is accessible${NC}"
    echo -e "${RED}============================================================${NC}"
fi