
### Shodan.io / Hunter.io

Github repository for Automation: [Hunter.how](https://github.com/Hunter)
Clone the Subdomain finder from SHODOMAIN git repository and get started.

###  ```crt.sh```

1) To see the certificate SSL validity and to verify it is trusted and issued by CT, try to enumerate the "dev" subdomain, as it's the most vulnerable domain.

2) For gov.in websites, to report vulnerabilities, you should report to [Nciipc.gov.in](https://nciipc.gov.in). Go to the footer and report to the vulnerability disclosure email given there.

#### Automation Process

To automate the process, use the bash script given in the git repository. Search for crt.sh git repository, clone it, and enter the target to get started.

### Facebook Certificate Search

Certificate search: [Facebook Certificate Search](https://developers.facebook.com/tools/ct/)

### Google Certificate Search

Certificate search: [Google Certificate Search](https://transparencyreport.google.com/https/certificates)

You can find the certificates of the websites here.

### Sublist3r

Github repository: [Sublist3r](https://github.com/aboul3la/Sublist3r)

```bash
python3 sublist3r.py -d https://xyx.com > subdomains.txt
```

```bash
python3 sublist3r.py -d https://xyx.com | tee subdomains.txt
```

```bash
python sublist3r.py -d yahoo.com -b -v -e google,virustotal -t 20
```

- `-d`: for domain
- `-b`: brute force the directories
- `-v`: verbosity
- `-e`: uses external domains for discovery of domains such as Virustotal and Google
- `-t`: number of threads

### Nmmapper.com

For viewing the WAF, subdomains, IP, and more online port checker: [Nmmapper.com](https://www.nmmapper.com/)
``` 

