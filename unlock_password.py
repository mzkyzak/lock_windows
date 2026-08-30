# unlock_password.py - PASSWORD PROTECTED UNLOCK
import tkinter as tk
import ctypes
import os
import sys
import time

# CORRECT PASSWORD
CORRECT_PASSWORD = "mzkyzak"

def create_unlock_interface():
    """Create password unlock interface"""
    root = tk.Tk()
    root.title("🔓 SYSTEM UNLOCK UTILITY")
    root.geometry("500x400")
    root.configure(bg='#0a0a0a')
    root.resizable(False, False)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Main frame
    main_frame = tk.Frame(root, bg='#0a0a0a')
    main_frame.pack(expand=True, fill='both', padx=30, pady=30)
    
    # Header
    header = tk.Label(main_frame,
                     text="🔐 SYSTEM UNLOCK",
                     font=('Consolas', 28, 'bold'),
                     fg='#00ff00',
                     bg='#0a0a0a')
    header.pack(pady=(0, 20))
    
    # Subtitle
    subtitle = tk.Label(main_frame,
                       text="Administrator Access Required",
                       font=('Lucida Console', 14),
                       fg='#ffffff',
                       bg='#0a0a0a')
    subtitle.pack(pady=(0, 30))
    
    # Password frame
    pass_frame = tk.Frame(main_frame, bg='#001a00', relief='ridge', bd=2)
    pass_frame.pack(fill='x', padx=20, pady=20)
    
    # Password label
    pass_label = tk.Label(pass_frame,
                         text="Enter Administrator Password:",
                         font=('Courier New', 14),
                         fg='#ffffff',
                         bg='#001a00')
    pass_label.pack(pady=(20, 10))
    
    # Password entry
    pass_entry = tk.Entry(pass_frame,
                         font=('Terminal', 16),
                         show="•",
                         width=25,
                         bg='#000000',
                         fg='#00ff00',
                         insertbackground='#00ff00',
                         relief='sunken',
                         bd=2)
    pass_entry.pack(pady=(0, 15))
    pass_entry.focus_set()
    
    # Status label
    status_label = tk.Label(pass_frame,
                           text="",
                           font=('Courier New', 12),
                           fg='#ffff00',
                           bg='#001a00')
    status_label.pack(pady=(0, 15))
    
    # Attempt counter
    attempts = 0
    max_attempts = 3
    
    def check_unlock_password():
        """Check password and unlock system"""
        nonlocal attempts
        
        entered = pass_entry.get()
        
        if entered == CORRECT_PASSWORD:
            # Correct password
            status_label.config(text="✅ PASSWORD ACCEPTED", fg='#00ff00')
            pass_entry.config(state='disabled')
            
            # Show unlocking progress
            progress_frame = tk.Frame(main_frame, bg='#0a0a0a')
            progress_frame.pack(fill='x', pady=20)
            
            tk.Label(progress_frame,
                    text="🔓 UNLOCKING SYSTEM...",
                    font=('Consolas', 16),
                    fg='#00ff00',
                    bg='#0a0a0a').pack()
            
            # Progress bar simulation
            progress = tk.Label(progress_frame,
                               text="[                    ]",
                               font=('Courier New', 14),
                               fg='#ffffff',
                               bg='#0a0a0a')
            progress.pack(pady=10)
            
            # Animate progress
            def animate_progress():
                steps = ["[▮                   ]",
                        "[▮▮                  ]",
                        "[▮▮▮                 ]",
                        "[▮▮▮▮                ]",
                        "[▮▮▮▮▮               ]",
                        "[▮▮▮▮▮▮              ]",
                        "[▮▮▮▮▮▮▮             ]",
                        "[▮▮▮▮▮▮▮▮            ]",
                        "[▮▮▮▮▮▮▮▮▮           ]",
                        "[▮▮▮▮▮▮▮▮▮▮          ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮         ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮        ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮       ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮      ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮     ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮    ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮   ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮  ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ ]",
                        "[▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮]"]
                
                for step in steps:
                    progress.config(text=step)
                    root.update()
                    time.sleep(0.1)
                
                # Actually unlock system
                perform_unlock()
            
            root.after(100, animate_progress)
            
        else:
            # Wrong password
            attempts += 1
            remaining = max_attempts - attempts
            
            if attempts >= max_attempts:
                status_label.config(text="❌ MAX ATTEMPTS REACHED", fg='#ff0000')
                pass_entry.config(state='disabled')
                
                # Permanent lock measures
                tk.Label(pass_frame,
                        text="⚠️ SYSTEM PERMANENTLY LOCKED",
                        font=('Consolas', 12, 'bold'),
                        fg='#ff0000',
                        bg='#001a00').pack(pady=10)
            else:
                status_label.config(text=f"❌ ACCESS DENIED - {remaining} ATTEMPT(S) LEFT", fg='#ff6666')
                pass_entry.delete(0, tk.END)
                
                # Shake effect
                for _ in range(3):
                    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x+5}+{y+5}")
                    root.update()
                    time.sleep(0.05)
                    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x-5}+{y-5}")
                    root.update()
                    time.sleep(0.05)
                    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x}+{y}")
                    root.update()
    
    def perform_unlock():
        """Actually unlock the system"""
        print("[UNLOCK] Restoring system...")
        
        # Unlock inputs
        ctypes.windll.user32.BlockInput(False)
        ctypes.windll.user32.ShowCursor(True)
        
        # Remove registry locks
        commands = [
            'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /f 2>nul',
            'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableCMD /f 2>nul',
            'reg delete HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v NoWinKeys /f 2>nul',
            'reg delete HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v "SysGuard" /f 2>nul',
            'reg delete "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Shell /f 2>nul',
            'schtasks /delete /tn "SystemGuard" /f 2>nul'
        ]
        
        for cmd in commands:
            os.system(cmd)
        
        # Show success message
        success_frame = tk.Frame(main_frame, bg='#0a0a0a')
        success_frame.pack(fill='x', pady=30)
        
        tk.Label(success_frame,
                text="✅ SYSTEM UNLOCKED SUCCESSFULLY",
                font=('Consolas', 18, 'bold'),
                fg='#00ff00',
                bg='#0a0a0a').pack()
        
        tk.Label(success_frame,
                text="System security has been restored",
                font=('Lucida Console', 12),
                fg='#ffffff',
                bg='#0a0a0a').pack(pady=10)
        
        # Countdown to close
        countdown = 5
        close_label = tk.Label(success_frame,
                              text=f"Closing in {countdown} seconds...",
                              font=('Courier New', 11),
                              fg='#cccccc',
                              bg='#0a0a0a')
        close_label.pack()
        
        def update_countdown():
            nonlocal countdown
            if countdown > 0:
                close_label.config(text=f"Closing in {countdown} seconds...")
                countdown -= 1
                root.after(1000, update_countdown)
            else:
                root.destroy()
        
        update_countdown()
    
    # Unlock button
    unlock_btn = tk.Button(pass_frame,
                          text=" UNLOCK SYSTEM ",
                          font=('Consolas', 12, 'bold'),
                          fg='#000000',
                          bg='#00ff00',
                          activeforeground='#000000',
                          activebackground='#33ff33',
                          relief='raised',
                          bd=2,
                          command=check_unlock_password)
    unlock_btn.pack(pady=(0, 20))
    
    # Bind Enter key
    def on_enter(event):
        check_unlock_password()
    
    pass_entry.bind('<Return>', on_enter)
    
    # Hint (optional)
    hint = tk.Label(main_frame,
                   text="Hint: Password is 'mzkyzak'",
                   font=('Terminal', 9),
                   fg='#666666',
                   bg='#0a0a0a')
    hint.pack(pady=(20, 0))
    
    # Footer
    footer = tk.Label(main_frame,
                     text="© 2026 Security Recovery Utility",
                     font=('Courier New', 9),
                     fg='#666666',
                     bg='#0a0a0a')
    footer.pack(pady=(20, 0))
    
    root.mainloop()

if __name__ == "__main__":
    print("🔓 SYSTEM UNLOCK UTILITY")
    print("========================")
    create_unlock_interface()