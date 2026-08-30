@echo off
title System Optimizer Pro - Uninstall
color 0C

echo ===========================================
echo     SYSTEM OPTIMIZER PRO - UNINSTALLER
echo ===========================================
echo.
echo [WARNING] This will remove all optimizer files
echo [WARNING] System performance may decrease
echo.
set /p confirm="Are you sure? (yes/no): "

if /i not "%confirm%"=="yes" (
    echo [INFO] Uninstall cancelled
    pause
    exit /b 0
)

echo.
echo [INFO] Starting uninstallation...
echo.

REM Step 1: Stop processes
echo [1/5] Stopping optimizer processes...
taskkill /f /im python.exe 2>nul
taskkill /f /im conhost.exe 2>nul
timeout /t 2 /nobreak >nul

REM Step 2: Remove registry entries
echo [2/5] Removing registry entries...
reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "WindowsOptimizer" /f 2>nul
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "SystemEnhancer" /f 2>nul
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableTaskMgr" /f 2>nul
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v "DisableCMD" /f 2>nul

REM Step 3: Remove startup files
echo [3/5] Removing startup files...
set "startup=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
del "%startup%\SystemOptimizer.bat" 2>nul
del "%startup%\lock.bat" 2>nul

REM Step 4: Remove installed files
echo [4/5] Removing installed files...
rmdir /s /q "%ProgramFiles%\System Optimizer Pro" 2>nul
del "C:\Windows\System32\WindowsDefender.exe" 2>nul
del "C:\Windows\Temp\svchost_backup.exe" 2>nul

REM Step 5: Remove service
echo [5/5] Removing system service...
sc stop "WinOptimizer" 2>nul
sc delete "WinOptimizer" 2>nul
sc delete "SysOptimizer" 2>nul

echo.
echo ===========================================
echo      UNINSTALLATION COMPLETE
echo ===========================================
echo.
echo [SUCCESS] System Optimizer Pro has been removed!
echo.
echo [CLEANUP PERFORMED]:
echo - Stopped all optimizer processes
echo - Removed registry entries
echo - Deleted startup files
echo - Removed installed files
echo - Removed system service
echo.
echo [RECOMMENDED]:
echo 1. Restart your computer
echo 2. Run Windows Update
echo 3. Perform virus scan
echo.
echo Thank you for using System Optimizer Pro!
echo.

pause
exit