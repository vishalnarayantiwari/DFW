import re
from collections import defaultdict

# Function to parse p0f log file
def parse_p0f_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    clients = set()
    servers = set()
    unique_communication = set()
    client_ports = set()
    server_ports = set()
    timestamps = []

    for line in lines:
        # Example log line: "1 192.168.1.2 192.168.1.1 80 443 2023-10-01 12:00:00"
        match = re.match(r'(\d+) (\S+) (\S+) (\d+) (\d+) (.+)', line)
        if match:
            client_ip = match.group(2)
            server_ip = match.group(3)
            client_port = match.group(4)
            server_port = match.group(5)
            timestamp = match.group(6)

            clients.add(client_ip)
            servers.add(server_ip)
            client_ports.add(client_port)
            server_ports.add(server_port)
            unique_communication.add((client_ip, server_ip))
            timestamps.append(timestamp)

    return {
        'unique_clients': len(clients),
        'unique_servers': len(servers),
        'unique_communication': len(unique_communication),
        'unique_client_ports': len(client_ports),
        'unique_server_ports': len(server_ports),
        'most_recent_packet': max(timestamps) if timestamps else None,
        'oldest_packet': min(timestamps) if timestamps else None,
    }

# Path to the p0f log file
log_file_path = 'p0f.log'
results = parse_p0f_log(log_file_path)

# Print results
print("Number of unique clients:", results['unique_clients'])
print("Number of unique servers:", results['unique_servers'])
print("Number of unique server-client communications:", results['unique_communication'])
print("Number of unique client ports:", results['unique_client_ports'])
print("Number of unique server ports:", results['unique_server_ports'])
print("Most recent packet timestamp:", results['most_recent_packet'])
print("Oldest packet timestamp:", results['oldest_packet'])
