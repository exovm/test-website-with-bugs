@echo off
REM Deploy TechBlog to Vercel
REM Make sure you have Vercel CLI installed: npm install -g vercel

echo ============================================================
echo  Deploying TechBlog to Vercel
echo  https://vercel.com deployment
echo ============================================================
echo.

REM Check if Vercel CLI is installed
vercel --version >nul 2>&1
if errorlevel 1 (
    echo Error: Vercel CLI is not installed
    echo Please install it with: npm install -g vercel
    echo Or visit: https://vercel.com/cli
    pause
    exit /b 1
)

echo Vercel CLI detected!
echo.

REM Login to Vercel if needed
echo Checking Vercel authentication...
vercel whoami >nul 2>&1
if errorlevel 1 (
    echo Please login to Vercel first:
    vercel login
    if errorlevel 1 (
        echo Login failed or cancelled
        pause
        exit /b 1
    )
)

echo Authentication successful!
echo.

REM Deploy to Vercel
echo Deploying to Vercel...
echo This may take a few minutes...
echo.

vercel --prod

if errorlevel 0 (
    echo.
    echo ============================================================
    echo  Successfully deployed to Vercel!
    echo  Your TechBlog is now live!
    echo ============================================================
    echo.
    echo Next steps:
    echo 1. Visit your deployment URL shown above
    echo 2. Test the application functionality
    echo 3. Use it as target for your webfinder tool
    echo.
) else (
    echo.
    echo ============================================================
    echo  Deployment failed. Common solutions:
    echo  1. Check your internet connection
    echo  2. Verify Vercel account is active
    echo  3. Make sure vercel.json is configured correctly
    echo  4. Try: vercel login (to re-authenticate)
    echo ============================================================
)

pause