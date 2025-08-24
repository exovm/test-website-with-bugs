#!/bin/bash
# Deploy TechBlog to Vercel
# Make sure you have Vercel CLI installed: npm install -g vercel

echo "============================================================"
echo " Deploying TechBlog to Vercel"
echo " https://vercel.com deployment"
echo "============================================================"
echo ""

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo -e "${RED}Error: Vercel CLI is not installed${NC}"
    echo "Please install it with: npm install -g vercel"
    echo "Or visit: https://vercel.com/cli"
    exit 1
fi

echo -e "${GREEN}Vercel CLI detected!${NC}"
echo ""

# Login to Vercel if needed
echo -e "${YELLOW}Checking Vercel authentication...${NC}"
if ! vercel whoami &> /dev/null; then
    echo "Please login to Vercel first:"
    vercel login
    if [ $? -ne 0 ]; then
        echo -e "${RED}Login failed or cancelled${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Authentication successful!${NC}"
echo ""

# Deploy to Vercel
echo -e "${YELLOW}Deploying to Vercel...${NC}"
echo "This may take a few minutes..."
echo ""

vercel --prod

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}============================================================${NC}"
    echo -e "${GREEN} Successfully deployed to Vercel!${NC}"
    echo -e "${GREEN} Your TechBlog is now live!${NC}"
    echo -e "${GREEN}============================================================${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Visit your deployment URL shown above"
    echo "2. Test the application functionality"
    echo "3. Use it as target for your webfinder tool"
    echo ""
else
    echo ""
    echo -e "${RED}============================================================${NC}"
    echo -e "${RED} Deployment failed. Common solutions:${NC}"
    echo -e "${RED} 1. Check your internet connection${NC}"
    echo -e "${RED} 2. Verify Vercel account is active${NC}"
    echo -e "${RED} 3. Make sure vercel.json is configured correctly${NC}"
    echo -e "${RED} 4. Try: vercel login (to re-authenticate)${NC}"
    echo -e "${RED}============================================================${NC}"
fi