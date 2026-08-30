# unlock_brutal.py - SAFE MODE UNLOCK
import os
import ctypes
import subprocess
import sys

def restore_system():
    print("=" * 60)
    print("🔓 SYSTEM RESTORATION UTILITY")
    print("=" * 60)
    
    # 1. Unlock inputs
    print("[1/8] Unlocking keyboard & mouse...")
    ctypes.windll.user32.BlockInput(False)
    ctypes.windll.user32.ShowCursor(True)
    
    # 2. Kill malicious processes
    print("[2/8] Terminating lock processes...")
    os.system('taskkill /f /im python.exe 2>nul')
    os.system('taskkill /f /im syslock.exe 2>nul')
    os.system('taskkill /f /im cmd.exe 2>nul')
    
    # 3. Remove registry entries
    print("[3/8] Cleaning registry...")
    reg_entries = [
        'HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v "SysGuard"',
        'HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon /v Shell',
        'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr',
        'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD',
        'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v NoWinKeys'
    ]
    
    for entry in reg_entries:
        os.system(f'reg delete {entry} /f 2>nul')
    
    # 4. Restore default values
    print("[4/8] Restoring system defaults...")
    os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Shell /t REG_SZ /d "explorer.exe" /f')
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD /t REG_DWORD /d 0 /f')
    
    # 5. Delete malicious files
    print("[5/8] Removing lock files...")
    files_to_delete = [
        'C:\\Windows\\System32\\syslock.exe',
        'C:\\Windows\\System32\\brutal.py',
        'C:\\Windows\\Temp\\wmi.ps1'
    ]
    
    for file in files_to_delete:
        try:
            os.remove(file)
        except:
            pass
    
    # 6. Remove task scheduler
    print("[6/8] Removing scheduled tasks...")
    tasks = ['SystemGuard', 'SystemSecure1', 'SystemSecure2', 'SystemSecure3']
    for task in tasks:
        os.system(f'schtasks /delete /tn "{task}" /f 2>nul')
    
    # 7. Clean startup folder
    print("[7/8] Cleaning startup entries...")
    startup = os.path.expandvars('%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    for item in ['brutal.bat', 'lock.bat', 'system.bat']:
        try:
            os.remove(os.path.join(startup, item))
        except:
            pass
    
    # 8. Restart explorer
    print("[8/8] Restarting explorer...")
    os.system('taskkill /f /im explorer.exe 2>nul')
    time.sleep(2)
    os.system('start explorer.exe')
    
    print("=" * 60)
    print("✅ SYSTEM RESTORATION COMPLETE")
    print("=" * 60)
    print("\n📋 SUMMARY:")
    print("• Keyboard/Mouse: UNLOCKED")
    print("• Registry: CLEANED")
    print("• Malicious files: REMOVED")
    print("• Task Scheduler: CLEANED")
    print("• Explorer: RESTARTED")
    print("\n⚠️ RECOMMENDATION: Run antivirus scan immediately!")
    print("=" * 60)

if __name__ == "__main__":
    import time
    restore_system()
    input("\nPress Enter to exit...")