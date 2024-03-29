##USING fuzzing ,wfuzz,ffuf tools
 1) Dirserach gitrepso - in   db-> dic.txt  and many more check here https://github.com/maurosoria/dirsearch for sensitive directories sucha s /admin and many more

2) Use burpusite indtruder functions qand increase the threads to 100 and paste the woeldits to do so and starr the attack youll get and if you want ot match somewthing then add it in grep command 

Using Wfuzz 
wfuzz -c -z file,/usr/share/wordlists/wfuzz/general/common.txt --hc 404 http://10.10.10.10/FUZZ

-c: This option tells wfuzz to print the output in a nice format.
--hc 404: This option tells wfuzz to hide responses with the status code 404. This can be useful to filter out known non-existent pages.

Using ffuf -
"ffuf -w /usr/share/seclists/Discovery/Web-Content/big.txt  -recursion -recursion-depth 2   -u http://10.10.10.10/FUZZ -e .php,.txt,.html,.js,.css,.json,.sh,.py -t 100"

-e .php,.txt,.html,.js,.css,.json,.sh,.py: This option specifies the extensions to search for. ffuf will append each extension to the end of the items in the wordlist and make a request to the server.
t 10: This option sets the number of threads to 10
