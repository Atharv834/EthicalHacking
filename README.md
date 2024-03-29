# Bug Bounty Command Repository

Welcome to the Bug Bounty Command Repository! This repository contains a collection of useful commands and notes for bug bounty hunters. Whether you're a beginner or an experienced hunter, you'll find valuable resources here to aid in your bug bounty endeavors.

## Table of Contents

1. [Introduction](#introduction)
2. [Commands](#commands)
    - [XSS](#xss)
    - [Fuzzing](#fuzzing)
    - [Website Recon](#website-recon)
    - [Subdomain Check](#subdomain-check)
    - [Privilege Escalation](#privilege-escalation)
    - [RCE (Remote Code Execution)](#rce)
3. [Notes](#notes)
4. [Contributing](#contributing)

## Introduction

Bug bounty hunting involves identifying and reporting security vulnerabilities in software products for monetary rewards. This repository aims to provide bug bounty hunters with a handy collection of commands and notes to streamline their hunting process.

## Commands

### XSS

```bash
# Command for testing XSS vulnerabilities
xss_scan --url [http://target.com/page.php?parameter=value](https://github.com/Atharv834/Hacking/blob/main/Bug%20bounty%20/1linerxss.md)
```

### Fuzzing

```bash
# Fuzzing with OWASP ZAP
zap-cli --fuzzer fuzz_xss.py --output fuzz_report.html
```

### Website Recon

```bash
# Subdomain enumeration with Sublist3r
python3 sublist3r.py -d target.com > subdomains.txt
```

### Subdomain Check

```bash
# Check subdomain validity with amass
amass enum -d target.com -o subdomains.txt
```

### Privilege Escalation

```bash
# Check for SUID binaries
find / -type f -perm -4000 -exec ls -la {} 2>/dev/null \;
```

### RCE

```bash
# Test for RCE using a vulnerable parameter
curl -X POST http://target.com/vulnerable_endpoint --data "param=$(uname -a)"
```

## Notes

- Always ensure you have permission before testing any targets.
- Use automation tools like Burp Suite, OWASP ZAP, and Nmap to expedite the hunting process.
- Document your findings thoroughly and report them responsibly to the appropriate channels.

## Contributing

Contributions to this repository are welcome! If you have any useful bug bounty commands or notes to add, please feel free to submit a pull request.

Happy hunting! 🐞🔍
