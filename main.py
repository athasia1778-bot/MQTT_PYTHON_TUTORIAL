import subprocess
import os
import sys
import time

# launcher main file: opens separate windows for publisher and receiver

def launch_window(script_name):
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    if os.name == "nt":
        # Create a small .bat wrapper that runs the script with the current Python
        python_exe = sys.executable
        bat_path = os.path.join(os.path.dirname(__file__), f"run_{os.path.splitext(script_name)[0]}.bat")
        with open(bat_path, "w", encoding="utf-8") as f:
            f.write(f"@echo off\n\"")
            f.write(f"{python_exe}\" \"%~dp0\\{script_name}\"\n")
            f.write("echo.\npause\n")
        # Use start via os.startfile to open the batch in a new window (avoids PowerShell parsing problems)
        try:
            os.startfile(bat_path)
        except Exception:
            # Fallback to subprocess if startfile is not available
            subprocess.Popen(["cmd", "/c", "start", "", bat_path], cwd=os.path.dirname(__file__))
    else:
        subprocess.Popen(["xterm", "-hold", "-e", "python3", script_path])


def main():
    print("[MAIN] Launching publisher and receiver windows...")
    launch_window("receiver.py")
    launch_window("publisher.py")
    print("[MAIN] Windows opened. This launcher will stay alive until you press Ctrl+C.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[MAIN] Launcher exiting")



if __name__ == "__main__":
    main()