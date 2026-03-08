import socket
import subprocess
import ipaddress
import platform
import re
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
from mac_vendor_lookup import MacLookup
from scapy.all import sniff, ARP, IP

init(autoreset=True)

SUSPICIOUS_PORTS = [4444, 5555, 6667, 1337, 31337]

# -----------------------------
# Local IP Detection
# -----------------------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# -----------------------------
# Network Range
# -----------------------------
def get_network(ip):
    return ipaddress.IPv4Network(ip + "/24", strict=False)


# -----------------------------
# Ping Host
# -----------------------------
def ping_host(ip):

    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", "500", str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(cmd, stdout=subprocess.DEVNULL)

    if result.returncode == 0:

        mac = get_mac(ip)
        vendor = get_vendor(mac)

        print(Fore.GREEN + f"Active Host: {ip}")
        print(Fore.CYAN + f"MAC: {mac}")
        print(Fore.YELLOW + f"Vendor: {vendor}\n")


# -----------------------------
# Multithreaded Scan
# -----------------------------
def scan_network(network):

    print(Fore.YELLOW + f"\nScanning network {network}\n")

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(ping_host, network)


# -----------------------------
# MAC Detection
# -----------------------------
def get_mac(ip):

    try:
        result = subprocess.check_output(f"arp -n {ip}", shell=True).decode()

        mac_match = re.search(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", result)

        if mac_match:
            return mac_match.group(0)

    except:
        pass

    return "Unknown"


# -----------------------------
# Vendor Detection
# -----------------------------
def get_vendor(mac):

    try:
        return MacLookup().lookup(mac)
    except:
        return "Unknown Vendor"


# -----------------------------
# Domain Resolution
# -----------------------------
def resolve_domain(ip):

    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"


# -----------------------------
# IP Geolocation
# -----------------------------
def get_ip_location(ip):

    try:
        url = f"http://ip-api.com/json/{ip}"
        data = requests.get(url).json()

        country = data.get("country", "Unknown")
        isp = data.get("isp", "Unknown")

        return f"{country} | ISP: {isp}"

    except:
        return "Unknown"


# -----------------------------
# Connection Monitoring
# -----------------------------
def check_connections():

    print(Fore.YELLOW + "\nChecking connections...\n")

    if platform.system().lower() == "windows":
        command = "netstat -ano"
    else:
        command = "netstat -tunap"

    output = subprocess.check_output(command, shell=True).decode()

    for line in output.splitlines():

        if "ESTABLISHED" in line:

            ip_match = re.findall(r"\d+\.\d+\.\d+\.\d+", line)

            if ip_match:

                remote_ip = ip_match[-1]
                domain = resolve_domain(remote_ip)
                location = get_ip_location(remote_ip)

                port_match = re.findall(r":(\d+)", line)

                if port_match:
                    port = int(port_match[-1])
                else:
                    port = 0

                if port in SUSPICIOUS_PORTS:

                    print(Fore.RED + f"[!] Suspicious Port {port}")
                    print(f"IP: {remote_ip}")
                    print(f"Domain: {domain}")
                    print(f"Location: {location}\n")

                else:

                    print(Fore.GREEN + f"[OK] {remote_ip} ({domain})")


# -----------------------------
# Live Monitoring
# -----------------------------
def live_monitor():

    print(Fore.YELLOW + "\nLive monitoring started\n")

    try:

        while True:

            check_connections()

            print(Fore.CYAN + "\nRefreshing in 5 seconds...\n")

            time.sleep(10)

    except KeyboardInterrupt:

        print(Fore.RED + "\nMonitoring stopped.")


# -----------------------------
# Packet Sniffer
# -----------------------------
def packet_callback(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst

        print(Fore.MAGENTA + "\n[PACKET]")
        print("Source:", src)
        print("Destination:", dst)


def packet_sniffer():

    print("\nStarting packet monitoring...")
    print("Press CTRL+C to stop\n")

    sniff(prn=packet_callback, store=False)


# -----------------------------
# Gateway Detection
# -----------------------------
def get_gateway():

    try:
        route = subprocess.check_output("ip route", shell=True).decode()

        match = re.search(r"default via (\d+\.\d+\.\d+\.\d+)", route)

        if match:
            return match.group(1)

    except:
        pass

    return None


# -----------------------------
# Gateway MAC
# -----------------------------
def get_gateway_mac(ip):

    try:
        result = subprocess.check_output(f"arp -n {ip}", shell=True).decode()

        mac_match = re.search(r"([0-9a-fA-F]{2}:){5}[0-9a-f-F]{2}", result)

        if mac_match:
            return mac_match.group(0)

    except:
        pass

    return None


# -----------------------------
# ARP Spoof Detection
# -----------------------------
def detect_arp_spoof():

    gateway = get_gateway()

    if not gateway:
        print("Gateway not detected")
        return

    real_mac = get_gateway_mac(gateway)

    print("\nMonitoring ARP packets...\n")

    def process(packet):

        if packet.haslayer(ARP):

            ip = packet[ARP].psrc
            mac = packet[ARP].hwsrc

            if ip == gateway and mac != real_mac:

                print(Fore.RED + "\n⚠ ARP SPOOF DETECTED!")
                print("Gateway:", gateway)
                print("Real MAC:", real_mac)
                print("Fake MAC:", mac)

    sniff(store=False, prn=process)


# -----------------------------
# MAIN MENU
# -----------------------------
def main():

    local_ip = get_local_ip()
    network = get_network(local_ip)

    while True:

        print("\n===== Network Security Toolkit =====")
        print("Your IPv4:", local_ip)
        print("Network:", network)

        print("\n1. Scan Active Hosts")
        print("2. Check Connections")
        print("3. Full Scan")
        print("4. Live Monitoring")
        print("5. Packet Sniffer")
        print("6. ARP Spoof Detection")
        print("7. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            scan_network(network)

        elif choice == "2":
            check_connections()

        elif choice == "3":
            scan_network(network)
            check_connections()

        elif choice == "4":
            live_monitor()

        elif choice == "5":
            packet_sniffer()

        elif choice == "6":
            detect_arp_spoof()

        elif choice == "7":
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()