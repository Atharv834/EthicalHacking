
# Windows Enumeration and Privilege Escalation

## Basic Enumeration Commands

### Updates Information
```sh
wmic qfe list --last | find "InstalledOn"   # Last time updates installed and by whom
wmic qfe get Caption,Description           # Get updates description
```

### Disk Information
```sh
wmic logicaldisk get Caption,Description,ProviderName   # List existing disks in the computer
```

## User Enumeration

### Current User Information
```sh
whoami                            # Display current user
whoami /priv                      # Display current user's privileges
whoami /groups                    # Display groups the current user is a part of
net user                          # List all users on the system
net user <username>               # Info about a particular user
net localgroup                    # List local groups
```

## Network Enumeration

### Network Configuration
```sh
ipconfig                          # Basic network configuration
ipconfig /all                     # Detailed network configuration
arp -a                            # Display ARP table
netstat -ano                      # List network connections
route print                       # Display routing table
```

## Password Hunting
```sh
findstr /si password *.txt *.ini *.config   # Search for passwords in specified file types
```
Reference: [Total OSCP Guide - Privilege Escalation (Windows)](https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html)

## Firewall and Antivirus Checking

### Firewall Status
```sh
netsh firewall show state                    # Show firewall status
netsh firewall show config                   # Show firewall configuration
```

### Windows Defender Status
```sh
sc query windefend                           # Check status of Windows Defender
sc queryex type=service                      # List all running services
```

Reference: [Windows Local Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)

---
