

### Subdomains Active Status

First, use the `amass` tool with the following command to find subdomains:

```bash
amass enum -d target.com -passive -o filename.txt
```

This command will enumerate subdomains of the target domain (`target.com`) in passive mode and save the results in a file named `filename.txt`.



Next, pass the list of subdomains obtained above into the `massdns` tool using the following command to check their activity:

```bash
massdns -r /home/lord/Tools/massdns/lists/resolvers.txt -t A -o S /home/lord/Tools/amass/filename.txt -w Finalactive.txt
```

This command utilizes `massdns` to check the activity of the subdomains enumerated by `amass`. It reads the list of subdomains from `filename.txt`, checks their activity using the resolvers specified in `/home/lord/Tools/massdns/lists/resolvers.txt`, and saves the active subdomains to a file named `Finalactive.txt` In directly it checks whether the domains are valid or not.

Afterward, you'll need to sort the list of active subdomains into a single file. Execute the following command to achieve this:

```bash
sed 's/A.*//' Finalactive.txt | sed 's/CN.*//' | sed 's/\..$//' > live_subdomains.txt
```

This command sorts the list of active subdomains (`Finalactive.txt`) into a single file named `live_subdomains.txt` using `sed`.

---

### Disclaimer 🚨

⚠️ **Disclaimer:** The above content is not owned by me. It has been sourced from the internet for educational purposes only. I do not claim ownership or responsibility for the content provided. Please use it responsibly and in accordance with applicable laws and ethical guidelines.



