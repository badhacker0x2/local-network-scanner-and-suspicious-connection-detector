import socket
import subprocess
import ipaddress
import platform
import re

# -------------------------------
# Get Local IPv4 Address
# -------------------------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# -------------------------------
# Detect Network Range
# -------------------------------
def get_network(ip):
    return ipaddress.IPv4Network(ip + "/24", strict=False)


# -------------------------------
# Ping Host
# -------------------------------
def ping_host(ip):
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "1", "-w", "500", str(ip)]
    else:
        cmd = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(cmd, stdout=subprocess.DEVNULL)
    return result.returncode == 0


# -------------------------------
# Scan Active Hosts
# -------------------------------
def scan_network(network):
    active_hosts = []

    print(f"\nScanning network: {network}\n")

    for ip in network:
        if ping_host(ip):
            print("Active Host:", ip)
            active_hosts.append(str(ip))

    print("\nTotal Active Hosts:", len(active_hosts))


# -------------------------------
# Check Suspicious IP
# -------------------------------
def is_suspicious(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)

        # public IP connection
        if not ip_obj.is_private:
            return True

    except:
        pass

    return False


# -------------------------------
# Check Established Connections
# -------------------------------
def check_connections():

    print("\nChecking established connections...\n")

    try:
        output = subprocess.check_output("netstat -an", shell=True).decode()
        lines = output.splitlines()

        for line in lines:
            if "ESTABLISHED" in line:

                ip_match = re.findall(r"\d+\.\d+\.\d+\.\d+", line)

                if ip_match:
                    remote_ip = ip_match[-1]

                    if is_suspicious(remote_ip):
                        print("[!] Suspicious Connection:", line)
                    else:
                        print("[OK]", line)

    except Exception as e:
        print("Error:", e)


# -------------------------------
# MAIN MENU WITH WHILE LOOP
# -------------------------------
def main():

    local_ip = get_local_ip()
    network = get_network(local_ip)

    while True:

        print("\n===== Network Monitor Tool =====")
        print("Your IPv4:", local_ip)
        print("Detected Network:", network)

        print("\n1. Scan Active Hosts")
        print("2. Check Established Connections")
        print("3. Full Scan")
        print("4. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            scan_network(network)

        elif choice == "2":
            check_connections()

        elif choice == "3":
            scan_network(network)
            check_connections()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()