@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo ==================================================================
echo  PG_mathbook - Autonomous Worker Setup (Windows)
echo ==================================================================
echo.
echo [1/2] Pulling latest code from GitHub...
git pull --rebase --autostash origin main

echo.
echo [2/2] Running PowerShell Startup & Task Scheduler Setup...
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\register_startup_task.ps1"
echo.
pause
