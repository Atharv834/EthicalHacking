
### Js Sensitive Files

```bash
batcat domains.txt | waybackurls | grep '.js' | httpx -mc 200 >> js.txt
```

Use Nuclei tool to find the JS files:

```bash
nuclei -l js.txt -t /nuclei-templates/http/exposures -o potential_secrets.txt
```

Then try .json to find out the info or try out brute forcing below sensitive directory paths.

🚨Here is a list of WP-exposed (wp-config sensitive) files!🚨

- /wp-config.php-backup 
- /wp-config.php.orig
- /.wp-config.php.swp
- /wp-config-sample.php 
- /wp-config.inc 
- /wp-config.old 
- /wp-config.txt
- /wp-config.php.txt
- /wp-config.php.bak
- /wp-config.php.old
- /wp-config.php.dist
- /wp-config.php.inc
- /wp-config.php.swp
- /wp-config.php.html
- /wp-config-backup.txt
- /wp-config.php.save
- /wp-config.php~
- /wp-config.php.original
- /_wpeprivate/config.json



### Disclaimer 🚨

⚠️ **Disclaimer:** The above content is not owned by me. It has been sourced from the internet for educational purposes only. I do not claim ownership or responsibility for the content provided. Please use it responsibly and in accordance with applicable laws and ethical guidelines.
