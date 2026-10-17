@echo off
setlocal
chcp 65001 > nul

title Math Classical Books Auto-Pipeline (http://192.168.128.16:1234/)

cd /d "%~dp0"

REM Ensure standard install locations are in PATH
if exist "C:\texlive\2026\bin\windows" set "PATH=C:\texlive\2026\bin\windows;%PATH%"
if exist "C:\texlive\2025\bin\windows" set "PATH=C:\texlive\2025\bin\windows;%PATH%"
if exist "C:\Program Files\Git\cmd" set "PATH=C:\Program Files\Git\cmd;%PATH%"
if exist "C:\Python315" set "PATH=C:\Python315;C:\Python315\Scripts;%PATH%"
if exist "C:\Python314" set "PATH=C:\Python314;C:\Python314\Scripts;%PATH%"
if exist "C:\Python313" set "PATH=C:\Python313;C:\Python313\Scripts;%PATH%"
if exist "%USERPROFILE%\.lmstudio\bin" set "PATH=%USERPROFILE%\.lmstudio\bin;%PATH%"

echo ==================================================================
echo   Math Classical Books Auto-Pipeline Master Runner
echo   Host: %COMPUTERNAME%
echo   Workspace: %CD%
echo   Target LM Studio Server: http://192.168.128.16:1234/
echo ==================================================================

REM Wait 10 seconds after boot for network to stabilize
if "%1"=="--boot" (
    echo [Boot Mode] Waiting 10 seconds for network initialization...
    timeout /t 10 /nobreak > nul
)

:LOOP_START
REM If LM Studio app is installed on this PC, ensure LM Studio GUI/daemon is running first
if exist "%LOCALAPPDATA%\Programs\LM Studio\LM Studio.exe" (
    tasklist /FI "IMAGENAME eq LM Studio.exe" 2>NUL | find /I /N "LM Studio.exe">NUL
    if errorlevel 1 (
        echo [LM Studio] Launching LM Studio application in background...
        start "" /min "%LOCALAPPDATA%\Programs\LM Studio\LM Studio.exe"
        timeout /t 12 /nobreak > nul
    )
) else if exist "C:\Program Files\LM Studio\LM Studio.exe" (
    tasklist /FI "IMAGENAME eq LM Studio.exe" 2>NUL | find /I /N "LM Studio.exe">NUL
    if errorlevel 1 (
        echo [LM Studio] Launching LM Studio application in background...
        start "" /min "C:\Program Files\LM Studio\LM Studio.exe"
        timeout /t 12 /nobreak > nul
    )
)

REM Start LM Studio server bound to 0.0.0.0:1234 so both localhost and LAN (192.168.128.16:1234) work
if exist "%USERPROFILE%\.lmstudio\bin\lms.exe" (
    echo [LM Studio] Starting API server on 0.0.0.0:1234 via lms CLI...
    "%USERPROFILE%\.lmstudio\bin\lms.exe" server start --bind 0.0.0.0 --port 1234 --cors
)

echo.
echo [1/3] Syncing latest repository from GitHub (conflict-free)...
git rebase --abort 2>nul
git merge --abort 2>nul
git fetch origin main
git reset --hard origin/main

echo.
echo [2/3] Launching Master Auto-Pipeline Script...
python scripts\auto_pipeline_master.py

echo.
echo [3/3] Cycle finished. Checking again in 60 seconds for next queued book...
echo ==================================================================
timeout /t 60 /nobreak > nul
goto LOOP_START
