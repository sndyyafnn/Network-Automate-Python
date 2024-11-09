def generate_upload_connection_commands():
    commands = []
    for i in range(2, 52): 
        rule_name = f"Upload-Conn-100.{i}"
        ip = f"192.168.100.{i}"
        command = f'/ip firewall mangle add comment="{rule_name}" chain=prerouting action=mark-connection new-connection-mark={rule_name} passthrough=yes src-address={ip} in-interface=LAN'
        commands.append(command)
    return commands

def write_commands_to_file(commands, filename):
    with open(filename, 'w') as file:
        for command in commands:
            file.write(command + '\n')  

def main():
    # Generate commands for marking upload connections
    upload_commands = generate_upload_connection_commands()

    # Save commands to a file
    output_file = "upload_conn_mangle.txt"
    write_commands_to_file(upload_commands, output_file)

    print(f"Upload connection marking commands have been written to {output_file}")

if __name__ == "__main__":
    main()
