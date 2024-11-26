import nmap
def scan_network(target_ip):
 # Initialize the scanner
 nm = nmap.PortScanner()
 # Perform a scan on the target IP
 print(f"Scanning {target_ip} for open ports...")
 nm.scan(hosts=target_ip, arguments='-p 1-65535') # Scan all ports (1-65535)
 
 # Get scan results
 for host in nm.all_hosts():
 print(f"\nHost: {host} ({nm[host].hostname()})")
 print(f"State: {nm[host].state()}")
 print("Open Ports:")
 for proto in nm[host].all_protocols():
 lport = nm[host][proto].keys()
 for port in lport:
 print(f"Port: {port} is open ({nm[host][proto][port]['state']})")
 
 return nm.all_hosts()
# Example usage
target_ip = "192.168.1.0/24" # Network range to scan (e.g., entire subnet)
scan_network(target_ip)