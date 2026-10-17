<#
.SYNOPSIS
    One-click Startup & Task Scheduler setup for PG_mathbook Auto-Pipeline.
    Works on both MINISFORUM64GB and sff7020 (http://192.168.128.16:1234/) without requiring Administrator rights.
#>
param(
    [string]$InstallDir = "$HOME\PG_mathbook"
)

$ErrorActionPreference = "Continue"
$RepoUrl = "https://github.com/k518-2026/PG_mathbook.git"

# Determine repository root directory
$CandidateRoot = $PSScriptRoot
if ($CandidateRoot -and ( Split-Path -Leaf $CandidateRoot ) -eq "scripts") {
    $CandidateRoot = Split-Path -Parent $CandidateRoot
}
if ($CandidateRoot -and (Test-Path (Join-Path $CandidateRoot "scripts\auto_pipeline_master.py"))) {
    $WorkDir = $CandidateRoot
} else {
    $WorkDir = $InstallDir
    if (-not (Test-Path (Join-Path $WorkDir ".git"))) {
        Write-Host "[1/4] Cloning PG_mathbook repository to $WorkDir..." -ForegroundColor Cyan
        git clone $RepoUrl $WorkDir
    } else {
        Write-Host "[1/4] Updating PG_mathbook repository in $WorkDir..." -ForegroundColor Cyan
        Push-Location $WorkDir
        git pull --rebase --autostash origin main
        Pop-Location
    }
}

$BatPath = Join-Path $WorkDir "start_auto_pipeline.bat"

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host " PG_mathbook - Autonomous Startup Setup" -ForegroundColor Cyan
Write-Host " Hostname  : $env:COMPUTERNAME" -ForegroundColor Cyan
Write-Host " Workspace : $WorkDir" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

# 1. Install Windows Startup folder script (.cmd) — runs automatically at every PC boot/logon (No Admin required)
try {
    $StartupDir = [Environment]::GetFolderPath('Startup')
    $StartupCmdPath = Join-Path $StartupDir "PG_Mathbook_AutoPipeline.cmd"
    $CmdLines = @(
        "@echo off",
        "cd /d `"$WorkDir`"",
        "start `"PG_mathbook Auto-Pipeline`" /min cmd /c `"`"$BatPath`" --boot`""
    )
    Set-Content -Path $StartupCmdPath -Value ($CmdLines -join "`r`n") -Encoding ASCII -Force
    Write-Host "[OK] Installed Windows Startup script (runs on every PC boot/logon):" -ForegroundColor Green
    Write-Host "     $StartupCmdPath" -ForegroundColor Green
} catch {
    Write-Host "[WARN] Could not write Startup script: $_" -ForegroundColor Yellow
}

# 2. Register Scheduled Task (AtLogOn + Daily 10:00) with fallback to user-level schtasks.exe
try {
    $Action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"`"$BatPath`" --boot`"" -WorkingDirectory $WorkDir
    $TrigLogon = New-ScheduledTaskTrigger -AtLogOn
    $TrigDaily = New-ScheduledTaskTrigger -Daily -At "10:00"
    $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -MultipleInstances IgnoreNew
    Register-ScheduledTask -TaskName "PG_Mathbook_AutoPipeline" -Action $Action -Trigger @($TrigLogon, $TrigDaily) -Settings $Settings -Description "Auto-runs Gutenberg math book translation, LaTeX compilation, and Git push via http://192.168.128.16:1234/" -Force -ErrorAction Stop | Out-Null
    Write-Host "[OK] Registered Scheduled Task 'PG_Mathbook_AutoPipeline' (AtLogOn & Daily 10:00)" -ForegroundColor Green
} catch {
    Write-Host "[INFO] Register-ScheduledTask required elevation, registering via user-level schtasks.exe..." -ForegroundColor Yellow
    $TrCmd = "cmd.exe /c `"`"$BatPath`" --boot`""
    schtasks /Create /TN "PG_Mathbook_AutoPipeline" /TR $TrCmd /SC DAILY /ST 10:00 /F | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] Registered Scheduled Task 'PG_Mathbook_AutoPipeline' via schtasks.exe (Daily 10:00 + Startup folder active)" -ForegroundColor Green
    } else {
        Write-Host "[INFO] Startup folder script is active and will launch automatically on every login." -ForegroundColor Green
    }
}

# 3. Verify environment right now
Write-Host "`n[Verifying Installed Applications & LM Studio Connectivity...]" -ForegroundColor Cyan
Push-Location $WorkDir
python scripts\auto_pipeline_master.py --check-only
Pop-Location
