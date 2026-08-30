# test_lock.py - Simple test langsung lock
import os
import sys
import ctypes

print("🔒 TESTING LOCK SYSTEM...")
print("Password: mzkyzak")

# Coba lock keyboard sederhana
try:
    ctypes.windll.user32.BlockInput(True)
    print("✅ Keyboard locked!")
    
    # Buat file test
    with open("test_lock_active.txt", "w") as f:
        f.write("Lock system active\nPassword: mzkyzak")
    
    input("Press Enter to unlock...")
    
    ctypes.windll.user32.BlockInput(False)
    print("✅ Keyboard unlocked!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("⚠️ Need to run as Administrator!")

input("Test complete. Press Enter to exit...")