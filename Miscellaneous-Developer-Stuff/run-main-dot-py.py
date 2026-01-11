import sys
import os
import subprocess

def main():
    # --- 1. Determine paths ---
    if getattr(sys, 'frozen', False):
        # Running as compiled .exe
        application_path = os.path.dirname(sys.executable)
        running_as_exe = True
    else:
        # Running as .py script
        application_path = os.path.dirname(os.path.abspath(__file__))
        running_as_exe = False

    target_script = os.path.join(application_path, "main.py")

    # --- 2. THE SAFETY GUARD (Prevents Infinite Loop) ---
    # We check if the file we are currently running is the same as the target
    current_running_file = sys.executable if running_as_exe else os.path.abspath(__file__)
    
    # Simple name check to prevent simple mistakes
    if os.path.basename(current_running_file).lower() == "main.py":
        print("CRITICAL ERROR: You named this launcher script 'main.py'!")
        print("Please rename this script to 'launcher.py' to avoid an infinite loop.")
        input("Press Enter to exit...")
        sys.exit(1)

    # --- 3. Check if target exists ---
    if not os.path.exists(target_script):
        print(f"Error: Could not find '{target_script}' in {application_path}")
        print("Make sure the external script is named 'main.py' and sits next to the exe.")
        input("Press Enter to exit...")
        sys.exit(1)

    # --- 4. Launch the external script ---
    # We explicitly call the SYSTEM python, not the internal frozen one.
    cmd = ["python", target_script]

    print(f"Launching: {target_script}...")
    
    try:
        # Use subprocess to call the external file
        subprocess.run(cmd, check=True)
    except Exception as e:
        print(f"Failed to launch script: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()