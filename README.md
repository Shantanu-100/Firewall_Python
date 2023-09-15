# Simple Firewall Configuration Script

This Python script provides a basic firewall configuration using the `iptables` tool on Linux. It allows you to enable a firewall and selectively allow incoming and outgoing traffic on specific ports.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Shantanu-100/Firewall_Python
   ```

2. Navigate to the project directory:

   ```bash
   cd Firewaaall_Python
   ```

3. Run the script with Python 3:

   ```bash
   python3 firewall.py
   ```

   The script will enable the firewall with default DROP policies for INPUT, FORWARD, and OUTPUT chains.

4. To allow specific ports for incoming and outgoing traffic, call the `allow_port` function with the desired port numbers:

   ```python
   allow_port(80)  # Allow incoming and outgoing traffic on port 80 (HTTP)
   allow_port(443)  # Allow incoming and outgoing traffic on port 443 (HTTPS)
   ```

   You can customize the list of allowed ports based on your requirements.

## Features

- **Firewall Enablement:** The script sets the default policies for the INPUT, FORWARD, and OUTPUT chains to DROP, effectively blocking all incoming and outgoing traffic.

- **Port Allowance:** You can selectively allow traffic on specific ports by calling the `allow_port` function with the desired port numbers. The script uses `iptables` rules to permit traffic on those ports.

## Important Notes

- This script is a basic example and may not cover all firewall use cases. More complex firewall configurations may be necessary for specific network requirements.

- Ensure you have the necessary permissions to run `iptables` commands. You may need to run the script with administrative privileges (e.g., using `sudo`) depending on your system configuration.

- Be cautious when configuring firewalls, as misconfigurations can lead to network disruptions. Verify your rules thoroughly before applying them.

## Acknowledgments

- This script uses the `subprocess` module to execute `iptables` commands.

Please feel free to contribute, report issues, or suggest improvements to this project.
