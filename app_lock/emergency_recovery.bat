@echo off
title Emergency Recovery - System Optimizer Pro
color 0C

echo ===========================================
echo       EMERGENCY RECOVERY UTILITY
echo ===========================================
echo.
echo [WARNING] This is for EMERGENCY use only!
echo [WARNING] Use if password forgotten or system locked
echo.
echo Options:
echo 1. Reset to default password (mzkyzak)
echo 2. Remove lock system completely
echo 3. Safe Mode unlock (requires restart)
echo 4. Exit
echo.

set /p choice="Select option [1-4]: "

if "%choice%"=="1" (
    echo.
    echo [INFO] Resetting to default password: mzkyzak
    echo.
    
    REM Reset semua file ke password default
    powershell -Command "(Get-Content 'lock_system.py') -replace 'CORRECT_PASSWORD = \".*?\"', 'CORRECT_PASSWORD = \"mzkyzak\"' | Set-Content 'lock_system.py'"
    powershell -Command "(Get-Content 'app_main.py') -replace '\"mzkyzak\"', '\"mzkyzak\"' | Set-Content 'app_main.py'"
    
    echo [SUCCESS] Password reset to: mzkyzak
    echo [INFO] Try unlocking with password: mzkyzak
)

if "%choice%"=="2" (
    echo.
    echo [WARNING] This will completely remove the lock system!
    echo [WARNING] All optimizations will stop!
    echo.
    set /p confirm="Type 'REMOVE' to confirm: "
    
    if /i "%confirm%"=="REMOVE" (
        echo [INFO] Removing lock system...
        
        REM Kill processes
        taskkill /f /im python.exe 2>nul
        taskkill /f /im SystemOptimizer.exe 2>nul
        
        REM Remove registry
        reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "WindowsOptimizer" /f 2>nul
        reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemEnhancer" /f 2>nul
        
        REM Remove startup
        del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\SystemOptimizer.bat" 2>nul
        
        REM Unlock inputs
        powershell -Command "[System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer(([System.Runtime.InteropServices.Marshal]::GetDelegateForFunctionPointer((Get-Process -Id $PID).Modules[0].BaseAddress + 0x1000), [Action[bool]])).Invoke($false)"
        
        echo [SUCCESS] Lock system removed!
        echo [INFO] Restart your computer
    )
)

if "%choice%"=="3" (
    echo.
    echo [INFO] Preparing Safe Mode unlock...
    echo [INFO] Computer will restart in Safe Mode
    echo.
    echo [WARNING] Save all work before continuing!
    echo.
    set /p confirm="Restart in Safe Mode? (yes/no): "
    
    if /i "%confirm%"=="yes" (
        echo [INFO] Configuring Safe Mode boot...
        bcdedit /set {default} safeboot minimal
        echo [INFO] Restarting in 5 seconds...
        timeout /t 5
        shutdown /r /t 0
    )
)

if "%choice%"=="4" (
    echo [INFO] Exiting...
    exit /b 0
)

echo.
echo ===========================================
echo       RECOVERY COMPLETE
echo ===========================================
echo.
echo [IMPORTANT]:
echo 1. Default password: mzkyzak
echo 2. Test unlock immediately
echo 3. Consider changing password
echo 4. Keep this recovery utility safe
echo.
pause
exit