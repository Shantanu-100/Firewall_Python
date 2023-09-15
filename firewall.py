import subprocess

def enable_firewall():
    subprocess.run(['iptables', '-P', 'INPUT', 'DROP'])
    subprocess.run(['iptables', '-P', 'FORWARD', 'DROP'])
    subprocess.run(['iptables', '-P', 'OUTPUT', 'DROP'])
    print("Firewall enabled.")

def allow_port(port):
    subprocess.run(['iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
    subprocess.run(['iptables', '-A', 'OUTPUT', '-p', 'tcp', '--sport', str(port), '-j', 'ACCEPT'])
    print(f"Port {port} allowed.")

# Example usage
enable_firewall()
allow_port(80)  # Allow incoming and outgoing traffic on port 80 (HTTP)
allow_port(443)  # Allow incoming and outgoing traffic on port 443 (HTTPS)
