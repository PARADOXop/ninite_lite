import os
import subprocess
import sys

def install_exe_files(directory):
    # Ensure the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # List .exe files in the directory
    exe_files = [f for f in os.listdir(directory) if f.endswith('.exe')]
    
    if not exe_files:
        print("No .exe files found in the directory.")
        return
    
    # Install each .exe file
    for exe_file in exe_files:
        exe_path = os.path.join(directory, exe_file)
        print(f"Starting installation of {exe_file}...")
        
        try:
            process = subprocess.Popen(exe_path)
            process.wait()  # Wait for the installer to complete
        except Exception as e:
            print(f"An error occurred while installing {exe_file}: {e}")

if __name__ == "__main__":
    # Debugging information
    print("Command-line arguments:", sys.argv)
    print("Current working directory:", os.getcwd())
    
    # Ensure a directory is provided
    if len(sys.argv) != 2:
        print("Usage: python install_exe.py <directory_with_exe_files>")
    else:
        # Change to the specified directory
        directory = sys.argv[1]
        install_exe_files(directory)
