import paramiko
import glob
import time
import logging
from getpass import getpass

# logging.basicConfig(level=logging.DEBUG)

file_pattern = 'D:\Mikrotik-ssh\exec ssh\*.txt'
ip = "192.168.110.99"
user = input("Input user: ")
passw = getpass()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    transport = paramiko.Transport((ip))
    transport.connect(username=user, password=passw)

    for file_name in glob.glob(file_pattern):
        with open(file_name, 'r') as file:
            commands = file.readlines()
            print(file_name)
            time.sleep(5)

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