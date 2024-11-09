def generate_queue_tree_commands():
    commands = []
    for i in range(2, 52): 
        rule_name = f"IP-100.{i}"
        ip = f"192.168.100.{i}"
        command = f'/ip firewall mangle add comment="{rule_name}" chain=forward action=mark-packet new-packet-mark={rule_name} passthrough=yes dst-address={ip} src-address-list=!Content_unlimit'
        commands.append(command)
    return commands

def write_commands_to_file(commands, filename):
    with open(filename, 'w') as file:
        for command in commands:
            file.write(command + '\n')  

def main():
    # Menghasilkan perintah
    queue_commands = generate_queue_tree_commands()

    # Menyimpan perintah ke dalam file
    output_file = "3_mangle_RMB.txt"  # Nama file output
    write_commands_to_file(queue_commands, output_file)

    print(f"Commands have been written to {output_file}")

if __name__ == "__main__":
    main()
