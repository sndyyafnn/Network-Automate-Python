def generate_queue_tree_commands():
    commands = []
    command = f'/queue tree add burst-limit=100M burst-time=10s comment="RMB" disabled=no max-limit=45M name=RMB parent=global priority=5 queue=default'
    commands.append(command)
    for i in range(2, 52):  
        rule_name = f"IP-100.{i}"
        command = f"/queue tree add burst-limit=15M disabled=no burst-time=5s limit-at=1M max-limit=10M name={rule_name} packet-mark={rule_name} parent=RMB priority=2 queue=default"
        commands.append(command)
    return commands

def write_commands_to_file(commands, filename):
    with open(filename, 'w') as file:
        for command in commands:
            file.write(command + '\n')  # Menulis setiap perintah ke file

def main():
    # Menghasilkan perintah
    queue_commands = generate_queue_tree_commands()

    # Menyimpan perintah ke dalam file
    output_file = "D:\Mikrotik-ssh\exec ssh\queue_zRMB.txt"  # Nama file output
    write_commands_to_file(queue_commands, output_file)

    print(f"Commands have been written to {output_file}")

if __name__ == "__main__":
    main()
