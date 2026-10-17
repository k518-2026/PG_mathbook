@echo off
setlocal
chcp 65001 > nul

title Math Classical Books Auto-Pipeline (http://192.168.128.16:1234/)

REM Wait 15 seconds after boot for network & LM Studio service to stabilize
if "%1"=="--boot" (
    echo Waiting 15 seconds for network and LM Studio initialization...
    timeout /t 15 /nobreak > nul
)

cd /d "%~dp0"

REM Ensure standard install locations are in PATH
if exist "C:\texlive\2026\bin\windows" set "PATH=C:\texlive\2026\bin\windows;%PATH%"
if exist "C:\texlive\2025\bin\windows" set "PATH=C:\texlive\2025\bin\windows;%PATH%"
if exist "C:\Program Files\Git\cmd" set "PATH=C:\Program Files\Git\cmd;%PATH%"
if exist "C:\Python314" set "PATH=C:\Python314;C:\Python314\Scripts;%PATH%"
if exist "%USERPROFILE%\.lmstudio\bin" set "PATH=%USERPROFILE%\.lmstudio\bin;%PATH%"

echo ==================================================================
echo   Math Classical Books Auto-Pipeline Master Runner
echo   Host: %COMPUTERNAME%
echo   Workspace: %CD%
echo   Target LM Studio Server: http://192.168.128.16:1234/
echo ==================================================================

echo.
echo [1/4] Checking installed applications (Python, Git, LuaLaTeX)...
python --version
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    exit /b 1
)

git --version
if errorlevel 1 (
    echo [ERROR] Git is not installed or not in PATH!
    exit /b 1
)

lualatex --version | findstr /i "LuaTeX"
if errorlevel 1 (
    echo [WARNING] LuaLaTeX might not be in PATH.
)

REM If LM Studio CLI is installed on this PC, ensure the local server is started
if exist "%USERPROFILE%\.lmstudio\bin\lms.exe" (
    echo.
    echo [2/4] Starting local LM Studio API server via lms CLI...
    "%USERPROFILE%\.lmstudio\bin\lms.exe" server start
)

echo.
echo [3/4] Syncing latest repository from GitHub...
git pull --rebase --autostash origin main

echo.
echo [4/4] Launching Master Auto-Pipeline Script...
python scripts\auto_pipeline_master.py

echo.
echo ==================================================================
echo   Process finished. See auto_pipeline.log for details.
echo ==================================================================
timeout /t 10
