<h1 align="center">Network Host Discovery and Connection Monitoring Tool</h1>

<p align="center">
A Python-based tool that scans the local network for active hosts and analyzes
established network connections to detect potentially suspicious activity.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project is a <b>network monitoring and analysis tool written in Python</b>.
It automatically detects the current local network, scans for active devices,
and inspects active network connections on the system.
</p>

<p>
The tool helps users understand:
</p>

<ul>
<li>Which devices are active on their local network</li>
<li>What external servers their system is communicating with</li>
<li>Whether connections are using unusual ports</li>
<li>Which processes are responsible for network connections</li>
</ul>

<hr>

<h2>⚙️ Features</h2>

<ul>
<li>Automatic detection of the local IPv4 address</li>
<li>Automatic detection of the local subnet</li>
<li>Local network host discovery using ping scanning</li>
<li>Established connection monitoring using <code>netstat</code></li>
<li>Reverse DNS lookup to resolve domain names from IP addresses</li>
<li>Detection of unusual or uncommon network ports</li>
<li>Identification of external/public IP connections</li>
<li>Displays processes associated with network connections (when available)</li>
</ul>

<hr>

<h2>🖥 How the Tool Works</h2>

<h3>1. Network Host Discovery</h3>

<p>
The tool scans the detected subnet (for example <code>192.168.1.0/24</code>)
and checks which devices respond to ping requests.
</p>

<pre>
Scanning network: 192.168.1.0/24

Active Host: 192.168.1.1
Active Host: 192.168.1.5
Active Host: 192.168.1.12
</pre>

<h3>2. Connection Monitoring</h3>

<p>
The program reads the system’s connection table using <code>netstat</code>
and analyzes established connections.
</p>

<p>It extracts information such as:</p>

<ul>
<li>Local IP address and port</li>
<li>Remote IP address</li>
<li>Remote port</li>
<li>Connection state</li>
<li>Associated process</li>
</ul>

<pre>
Local: 192.168.1.5:50432
Remote: 140.82.114.26:443
Domain: github.com
Process: chrome.exe
Status: Normal
</pre>

<h3>3. Suspicious Connection Detection</h3>

<p>
The tool highlights connections that may require further inspection.
</p>

<pre>
[!] Suspicious Connection Detected
Remote IP: 185.23.12.55
Port: 4444
Domain: Unknown
</pre>

<hr>

<h2>📦 Requirements</h2>

<p>Python 3.x</p>

<p>Standard Python libraries used:</p>

<ul>
<li><code>socket</code></li>
<li><code>subprocess</code></li>
<li><code>ipaddress</code></li>
<li><code>platform</code></li>
<li><code>re</code></li>
</ul>

<p>No external packages are required.</p>

<hr>

<h2>🚀 How to Run</h2>

<h3>1. Clone the repository</h3>

<pre>
git clone https://github.com/yourusername/network-monitor-tool.git
</pre>

<h3>2. Navigate to the project folder</h3>

<pre>
cd network-monitor-tool
</pre>

<h3>3. Run the program</h3>

<pre>
python network_monitor.py
</pre>

<p>
For full functionality (process detection), run the program with administrator
or root privileges.
</p>

<h3>Linux</h3>

<pre>
sudo python3 network_monitor.py
</pre>

<h3>Windows</h3>

<p>Run the terminal as <b>Administrator</b> and execute:</p>

<pre>
python network_monitor.py
</pre>

<hr>

<h2>📋 Program Menu</h2>

<pre>
===== Network Monitor Tool =====

1. Scan Active Hosts
2. Check Established Connections
3. Full Scan
4. Exit
</pre>

<hr>

<h2>🎯 Example Use Cases</h2>

<ul>
<li>Learning network monitoring techniques</li>
<li>Identifying devices connected to a local network</li>
<li>Analyzing outgoing network connections</li>
<li>Detecting unusual connection behavior</li>
<li>Educational cybersecurity projects</li>
</ul>

<hr>

<h2>⚠ Limitations</h2>

<ul>
<li>Some devices block ICMP ping and may not appear in host scans.</li>
<li>Suspicious detection is based on simple heuristics.</li>
<li>This tool is not a replacement for full intrusion detection systems.</li>
</ul>

<hr>

<h2>📚 Educational Purpose</h2>

<p>
This project is designed for learning purposes and demonstrates concepts such as:
</p>

<ul>
<li>Network host discovery</li>
<li>Network connection analysis</li>
<li>Python networking libraries</li>
<li>Basic cybersecurity monitoring techniques</li>
</ul>

<hr>

<h2>🔮 Possible Future Improvements</h2>

<ul>
<li>Multithreaded host scanning</li>
<li>IP geolocation lookup</li>
<li>Integration with IP reputation databases</li>
<li>Real-time connection monitoring</li>
<li>Colored terminal alerts</li>
</ul>

<hr>

<h2>📜 License</h2>

<p>
This project is open-source and intended for educational and research purposes.
</p>

<h2>Author & Contribution</h2>

<div style="background-color:#f6f8fa;padding:15px;border-radius:8px;font-family:Arial;">

<h3>Main Author</h3>
<p>
<strong>Rahat Sahriar Rafi</strong><br>
Designed and developed the core structure of the project including:
<ul>
<li>Local IPv4 detection</li>
<li>Network range identification</li>
<li>Active host scanning on the LAN</li>
<li>Initial network monitoring functionality</li>
</ul>
</p>

<h3>Contributor</h3>
<p>
<strong>Md. Munkasir Haque</strong><br>
Extended and improved the project by adding advanced monitoring features:
<ul>
<li>Established connection analysis using <code>netstat</code></li>
<li>Suspicious IP detection</li>
<li>Domain name resolution from IP addresses</li>
<li>Unusual port detection</li>
<li>Connection process identification</li>
</ul>
</p>

</div>