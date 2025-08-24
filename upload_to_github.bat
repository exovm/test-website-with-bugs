@echo off
REM Upload TechBlog to GitHub
REM Make sure you have git installed and are logged into GitHub

echo ============================================================
echo  Uploading TechBlog to GitHub
echo  Repository: https://github.com/exovm/test-website-with-bugs
echo ============================================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Error: Git is not installed
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

REM Initialize git repository if not already done
if not exist ".git" (
    echo Initializing Git repository...
    git init
    echo.
)

REM Add remote repository
echo Adding GitHub remote...
git remote remove origin >nul 2>&1
git remote add origin https://github.com/exovm/test-website-with-bugs.git
echo.

REM Add all files
echo Adding files to git...
git add .
echo.

REM Create commit
echo Creating commit...
git commit -m "Initial commit: TechBlog community platform

- Flask-based blog platform for developers
- User authentication and profiles  
- Post creation and search functionality
- File upload capabilities
- Admin dashboard
- Network tools for developers
- RESTful API endpoints
- Modern responsive design"
echo.

REM Push to GitHub
echo Pushing to GitHub...
git branch -M main
git push -u origin main
echo.

if errorlevel 0 (
    echo ============================================================
    echo  Successfully uploaded to GitHub!
    echo  Repository: https://github.com/exovm/test-website-with-bugs
    echo ============================================================
) else (
    echo ============================================================
    echo  Upload failed. Please check:
    echo  1. You're logged into GitHub
    echo  2. You have access to the repository
    echo  3. Repository exists and is accessible
    echo ============================================================
)

pause