from scapy.all import rdpcap
from collections import defaultdict

# Load the PCAP file
pcap_file = "example.pcap"  # Replace with your file name
packets = rdpcap(pcap_file)

# Initialize containers for analysis
clients = set()  # To store unique client IPs
servers = set()  # To store unique server IPs
server_client_pairs = set()  # To store unique server-client communication pairs
client_ports = set()  # To store unique client ports
server_ports = set()  # To store unique server ports
protocols = set()  # To store unique protocol names

# Analyze each packet
for packet in packets:
    if packet.haslayer("IP"):  # Check for IP layer
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        clients.add(src_ip)
        servers.add(dst_ip)
        server_client_pairs.add((src_ip, dst_ip))  # Unique server-client pair
        
        # Check for transport layers like TCP/UDP
        if packet.haslayer("TCP") or packet.haslayer("UDP"):
            src_port = packet.sport
            dst_port = packet.dport
            client_ports.add(src_port)
            server_ports.add(dst_port)
        
        # Add protocol names
        protocols.add(packet["IP"].proto)

# Display Results
print("1. Number of Unique Clients:", len(clients))
print("2. Number of Unique Servers:", len(servers))
print("3. Unique Server-Client Pairs:", len(server_client_pairs))
print("4. Number of Unique Client Ports:", len(client_ports))
print("5. Number of Unique Server Ports:", len(server_ports))
print("6. Protocol Names:", {proto for proto in protocols})
# python3 q12.py
