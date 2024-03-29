

#  Web Application Fuzzing Techniques

This guide explores efficient techniques for discovering hidden directories and files within web applications using fuzzing tools like Wfuzz and ffuf. These tools can help identify potentially sensitive information or vulnerabilities that might be overlooked during manual testing.

**1. Directory Enumeration with Dirsearch**

- **Installation and Usage:**

  ```bash
  git clone https://github.com/maurosoria/dirsearch dirsearch
  cd dirsearch
  python dirsearch.py -u http://10.10.10.10 -w db->dic.txt
  ```

  Replace `http://10.10.10.10` with the target URL and `db->dic.txt` with the path to your wordlist containing potential directory names. Dirsearch will attempt to access each directory in the wordlist and report potentially existing directories based on the server's response.

**2. Brute-Force Attacks with Burp Suite Intruder**

- **Steps:**

  1. **Load Wordlist:** Paste your wordlist (e.g., usernames, passwords) into the Intruder payload position.
  2. **Increase Threads:** Within the Intruder settings, adjust the number of threads (concurrent requests) to 100 
  3. **Launch Attack:** Start the Intruder attack.
  4. **Filter Results (Optional):** Use the grep command to match something in the response 


**3. Efficient Enumeration with ffuf**

- **Installation:**

  Refer to the ffuf documentation for installation instructions specific to your platform: [https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf)

- **Command Breakdown:**

  ```bash
  ffuf -w /usr/share/seclists/Discovery/Web-Content/big.txt \
      -recursion -recursion-depth 2 \
      -u http://10.10.10.10/FUZZ \
      -e .php,.txt,.html,.js,.css,.json,.sh,.py \
      -t 10
  ```

  * `-w /usr/share/seclists/Discovery/Web-Content/big.txt`: Path to your wordlist containing potential directories or filenames.
  * `-recursion`: Enables recursive searching, checking subdirectories within discovered directories.
  * `-recursion-depth 2`: Specifies the maximum depth of recursive searching (2 levels in this case).
  * `-u http://10.10.10.10/FUZZ`: Target URL with the placeholder `FUZZ` for where ffuf will insert items from the wordlist.
  * `-e .php,.txt,.html,.js,.css,.json,.sh,.py`: Defines comma-separated file extensions to enumerate. ffuf will append each extension to the wordlist entries.
  * `-t 10`: Sets the number of concurrent threads to 10.
