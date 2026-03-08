<h1 align="center">Network Security Monitoring Toolkit</h1>

<p align="center">
A Python-based network security toolkit designed for monitoring, analyzing,
and detecting suspicious activity within a local network environment.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project is an advanced <b>network monitoring and security analysis tool</b>
built using Python. The toolkit is capable of scanning the local network,
detecting active hosts, monitoring live network connections, capturing packets,
and identifying potential security threats such as suspicious connections
or ARP spoofing attacks.
</p>

<p>
It combines multiple network security techniques into a single toolkit that can
assist users in understanding and analyzing network behavior in real time.
</p>

<hr>

<h2>⚙️ Core Features</h2>

<ul>
<li>Automatic detection of the local IPv4 address</li>
<li>Automatic detection of the local network range</li>
<li>Multithreaded LAN host discovery</li>
<li>MAC address detection for active devices</li>
<li>Vendor identification (Apple, Cisco, Samsung, etc.)</li>
<li>Real-time monitoring of established network connections</li>
<li>Suspicious port detection</li>
<li>Reverse DNS lookup (resolve domain names from IP)</li>
<li>IP geolocation lookup (country and ISP detection)</li>
<li>Live network connection monitoring</li>
<li>Real-time packet sniffing</li>
<li>ARP Spoofing / Man-in-the-Middle attack detection</li>
<li>Colored terminal output for better visibility</li>
</ul>

<hr>

<h2>🖥 How the Toolkit Works</h2>

<h3>1. Network Host Discovery</h3>

<p>
The tool scans the local subnet and identifies active devices by sending
ICMP ping requests.
</p>

<pre>
Scanning network: 192.168.0.0/24

Active Host: 192.168.0.1
Active Host: 192.168.0.105
Active Host: 192.168.0.120
</pre>

<p>
For each active host, the tool attempts to retrieve:
</p>

<ul>
<li>IP address</li>
<li>MAC address</li>
<li>Device vendor information</li>
</ul>

<hr>

<h3>2. Connection Monitoring</h3>

<p>
The program reads the system’s connection table using <code>netstat</code>
and analyzes active connections to identify potentially suspicious
external communication.
</p>

<pre>
[OK] 140.82.114.26 (github.com)

[!] Suspicious Port Detected
IP: 185.23.12.55
Port: 4444
Location: Russia | ISP: Example ISP
</pre>

<hr>

<h3>3. Live Network Monitoring</h3>

<p>
The toolkit can continuously monitor network connections in real time,
refreshing results periodically and highlighting unusual activity.
</p>

<pre>
Monitoring connections...

[OK] google.com
[OK] github.com
[!] Suspicious connection detected
</pre>

<hr>

<h3>4. Packet Sniffer</h3>

<p>
A built-in packet sniffer captures live network packets and displays
basic packet information such as source IP, destination IP, and protocol.
</p>

<pre>
[PACKET DETECTED]

Source IP: 192.168.0.105
Destination IP: 8.8.8.8
Protocol: UDP
</pre>

<hr>

<h3>5. ARP Spoofing Detection</h3>

<p>
The toolkit monitors ARP packets on the network and detects potential
Man-in-the-Middle (MITM) attacks by identifying changes in the gateway
MAC address.
</p>

<pre>
⚠ WARNING: Possible ARP Spoofing Detected

Gateway IP: 192.168.0.1
Real MAC: 00:1A:2B:AA:BB:CC
Fake MAC: 88:71:E5:22:19:9A
</pre>

<hr>

<h2>📦 Requirements</h2>

<p>Python 3.x</p>

<p>Required Python libraries:</p>

<ul>
<li><code>socket</code></li>
<li><code>subprocess</code></li>
<li><code>ipaddress</code></li>
<li><code>platform</code></li>
<li><code>re</code></li>
<li><code>requests</code></li>
<li><code>scapy</code></li>
<li><code>colorama</code></li>
<li><code>mac-vendor-lookup</code></li>
</ul>

<hr>

<h2>📥 Installation</h2>

<h3>Clone the repository</h3>

<pre>
git clone https://github.com/yourusername/network-security-toolkit.git
</pre>

<h3>Navigate to the project folder</h3>

<pre>
cd network-security-toolkit
</pre>

<h3>Create a virtual environment</h3>

<pre>
python3 -m venv venv
source venv/bin/activate
</pre>

<h3>Install dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🚀 Running the Tool</h2>

<p>
Some features such as packet sniffing require root privileges.
</p>

<pre>
sudo ./venv/bin/python network_toolkit.py
</pre>

<hr>

<h2>📋 Program Menu</h2>

<pre>
===== Network Security Toolkit =====

1. Scan Active Hosts
2. Check Connections
3. Full Scan
4. Live Monitoring
5. Packet Sniffer
6. ARP Spoof Detection
7. Exit
</pre>

<hr>

<h2>🎯 Example Use Cases</h2>

<ul>
<li>Learning network security monitoring techniques</li>
<li>Identifying devices connected to a local network</li>
<li>Analyzing suspicious outbound connections</li>
<li>Detecting potential Man-in-the-Middle attacks</li>
<li>Educational cybersecurity research and practice</li>
</ul>

<hr>

<h2>⚠ Disclaimer</h2>

<p>
This project is intended strictly for <b>educational and research purposes</b>.
Users should only run the tool on networks they own or have permission to analyze.
</p>

<hr>

<h2>👨‍💻 Authors & Contributions</h2>

<div style="background-color:#f6f8fa;padding:15px;border-radius:8px;font-family:Arial;">

<h3>Main Author</h3>
<p>

<h3>Contributor</h3>
<p>
<strong>Md. Munkasir Haque</strong><br>
Developed the initial version of the project including:
</p>

<ul>
<li>Local IPv4 detection</li>
<li>Network range identification</li>
<li>LAN host discovery</li>
<li>Basic connection monitoring using <code>netstat</code></li>
<li>Suspicious connection detection logic</li>
<li>Domain resolution from IP addresses</li>
</ul>
<strong>Rahat Sahriar Rafi</strong><br>
Developed and expanded the project into a full network security toolkit by adding:
</p>

<ul>
<li>Multithreaded network scanning</li>
<li>MAC address and vendor detection</li>
<li>Live connection monitoring</li>
<li>Packet sniffing functionality</li>
<li>IP geolocation lookup</li>
<li>ARP spoofing / MITM attack detection</li>
<li>Enhanced CLI interface and monitoring features</li>
</ul>

</div>

<hr>

<h2>📜 License</h2>

<p>
This project is open-source and available for educational use.
</p>