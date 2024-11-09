import paramiko
import logging
from getpass import getpass

# Aktifkan logging untuk debugging
logging.basicConfig(level=logging.DEBUG)

ip_address = "192.168.110.99"
user = input("Input user: ")
password = getpass()
# port = 22002  # Port harus berupa integer, bukan string

# Membuat objek SSHClient
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Membuat objek Transport
    transport = paramiko.Transport((ip_address))
    transport.connect(username=user, password=password)

    # Membuka sesi dan menjalankan perintah
    session = transport.open_session()
    session.exec_command("ip address print")

    # Membaca output
    stdout = session.makefile('rb', -1).read()
    print(stdout.decode())
    
except paramiko.AuthenticationException as e:
    print(f"Authentication failed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Pastikan untuk menutup transport
    transport.close()
