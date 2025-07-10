# Kali Linux Wi-Fi Scanner

A professional GUI tool to scan and analyze nearby Wi-Fi networks in Kali Linux.

## Features
- List all available Wi-Fi networks
- Display SSID, BSSID, signal strength, channel, and security type
- Color-coded signal strength indicators
- Auto-refresh functionality
- Works with Kali Linux's NetworkManager (nmcli)

## Installation

### 1. Clone or download this repository
```bash
git clone https://github.com/yourusername/kali-wifi-scanner.git
cd kali-wifi-scanner
```
2. Set up virtual environment
Kali Linux requires Python packages to be installed in a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv
```
# Activate the environment
```
source venv/bin/activate
```
# Install dependencies
```
pip install -r requirements.txt
```
Usage
# Activate the virtual environment (if not already active)
```
source venv/bin/activate
```
# Run the scanner
```
python wifi_scanner.py
```
