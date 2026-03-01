import psutil
import platform
import os
from datetime import datetime

class SystemSentinel:
    def __init__(self):
        self.system_info = platform.uname()

    def get_vitals(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        print(f"--- System Vitals [{datetime.now().strftime('%H:%M:%S')}] ---")
        print(f"Processor: {self.system_info.processor}")
        print(f"CPU Load: {cpu_usage}% | RAM Usage: {ram_usage}%")
        
        if cpu_usage > 80:
            print("ALERT: High CPU Usage Detected!")

    def scan_large_files(self, directory=".", min_size_mb=100):
        print(f"\n--- Scanning for files > {min_size_mb}MB ---")
        found = False
        for root, dirs, files in os.walk(directory):
            for name in files:
                filepath = os.path.join(root, name)
                try:
                    size = os.path.getsize(filepath) / (1024 * 1024)
                    if size > min_size_mb:
                        print(f"Found: {name} ({size:.2f} MB)")
                        found = True
                except (PermissionError, OSError):
                    continue
        if not found:
            print("No large files found.")

if __name__ == "__main__":
    guard = SystemSentinel()
    guard.get_vitals()
    # Scans the current folder for files bigger than 10MB (for demo purposes)
    guard.scan_large_files(min_size_mb=10)
