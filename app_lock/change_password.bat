@echo off
title Change Password - System Optimizer Pro
color 0A

echo ===========================================
echo       CHANGE PASSWORD UTILITY
echo ===========================================
echo.

echo [INFO] Current password: mzkyzak
echo [INFO] 3 attempts allowed before permanent lock
echo.

set /p old_pass="Enter current password to continue: "

if not "%old_pass%"=="mzkyzak" (
    echo [ERROR] Wrong password!
    echo [INFO] Exiting for security...
    pause
    exit /b 1
)

echo [OK] Password verified!
echo.

set /p new_pass="Enter new password: "
set /p confirm_pass="Confirm new password: "

if not "%new_pass%"=="%confirm_pass%" (
    echo [ERROR] Passwords don't match!
    pause
    exit /b 1
)

if "%new_pass%"=="" (
    echo [ERROR] Password cannot be empty!
    pause
    exit /b 1
)

echo.
echo [INFO] Changing password in all files...
echo.

REM Update password in Python files
powershell -Command "(Get-Content 'lock_system.py') -replace 'CORRECT_PASSWORD = \"mzkyzak\"', 'CORRECT_PASSWORD = \"%new_pass%\"' | Set-Content 'lock_system.py'"
powershell -Command "(Get-Content 'app_main.py') -replace '\"mzkyzak\"', '\"%new_pass%\"' | Set-Content 'app_main.py'"

REM Update in other files
if exist "..\brutal_lock.py" (
    powershell -Command "(Get-Content '..\brutal_lock.py') -replace '\"mzkyzak\"', '\"%new_pass%\"' | Set-Content '..\brutal_lock.py'"
)

echo [SUCCESS] Password changed to: %new_pass%
echo.
echo [IMPORTANT]:
echo - New password: %new_pass%
echo - Old password: mzkyzak (no longer works)
echo - Write down your new password!
echo - No password recovery available
echo.

echo [INFO] Rebuilding .exe files with new password...
echo.

REM Rebuild .exe dengan password baru
if exist "build_exe.bat" (
    call build_exe.bat
    echo [OK] .EXE files rebuilt with new password
)

echo.
echo ===========================================
echo       PASSWORD CHANGE COMPLETE
echo ===========================================
echo.
echo [SUCCESS] All systems updated with new password!
echo.
echo [FILES UPDATED]:
echo - lock_system.py
echo - app_main.py
echo - brutal_lock.py (if exists)
echo - All .exe files (rebuilt)
echo.
echo [REMEMBER]:
echo 1. New password: %new_pass%
echo 2. Keep it secret!
echo 3. No recovery if forgotten!
echo 4. Test unlock immediately
echo.
pause
exit