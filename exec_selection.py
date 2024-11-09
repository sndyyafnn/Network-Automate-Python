import paramiko
import glob
import time
import logging
from getpass import getpass

# logging.basicConfig(level=logging.DEBUG)

file_pattern = 'D:\Mikrotik-ssh\exec ssh\*.txt'
ip = "192.168.2.1"
user = input("Input user: ")
passw = getpass()
port = 22002

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, password=passw)

    # List semua file .txt di direktori
    all_files = glob.glob(file_pattern)
    if not all_files:
        print("No files found!")
    else:
        print("Available files:")
        for i, file_name in enumerate(all_files):
            print(f"{i + 1}. {file_name}")

        # User input untuk memilih file yang akan dieksekusi
        selected_files = input("Enter the numbers of the files to execute (comma-separated, e.g., 1,3,5): ")

        # Convert input menjadi daftar file yang dipilih
        selected_indices = [int(x.strip()) - 1 for x in selected_files.split(",") if x.strip().isdigit()]
        selected_files_list = [all_files[i] for i in selected_indices if 0 <= i < len(all_files)]

        if not selected_files_list:
            print("No valid files selected!")
        else:
            for file_name in selected_files_list:
                with open(file_name, 'r') as file:
                    commands = file.readlines()

                for command in commands:
                    command = command.strip()

                    session = transport.open_session()
                    session.exec_command(command)

                    stdout = session.makefile('rb', -1).read()
                    print(f"File: {file_name}, Command: {command}, Executed!")
                    print(stdout.decode())

                    session.close()
                    time.sleep(1)

except paramiko.AuthenticationException as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    transport.close()
