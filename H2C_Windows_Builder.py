import subprocess
import sys
import os

"""
H2C WINDOWS BUILDER
This script automatically installs requirements and compiles the H2C Cockpit 
into a standalone Windows Executable (.exe).
"""

def run_command(cmd):
    print(f">> Executing: {cmd}")
    process = subprocess.Popen(cmd, shell=True)
    process.wait()

if __name__ == "__main__":
    print("=== H2C COCKPIT WINDOWS BUILDER ===")
    
    # 1. Install required tools
    print("\n1. Installing requirements...")
    run_command("pip install streamlit pyinstaller pandas numpy matplotlib st-pyinstaller")

    # 2. Build the EXE
    print("\n2. Compiling into standalone EXE...")
    # Using st-pyinstaller for easier Streamlit bundling
    run_command("st-pyinstaller H2C_Universal_Cockpit.py --name=H2C_Universal_Cockpit --onefile")

    print("\n" + "="*40)
    print("SUCCESS! Your executable is ready in the 'dist/' folder.")
    print("File: H2C_Universal_Cockpit.exe")
    print("="*40)
    input("\nPress Enter to exit...")
