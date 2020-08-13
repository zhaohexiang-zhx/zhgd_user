
import time
import requests

def sleep(n_secs):
    time.sleep(n_secs)

#11位
def get_timestamp():
    return str(int(time.time() * 10))  

#5位
def get_timestamp1():
    return str(time.time()).replace(".", "")[5:10]

def get_cookie(username="zhaohexiang", password="123456"):
    url = "http://10.23.190.107/zhgd_mms/user/login"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }
    body = {
        "_sign": 'bd49d5b78c71d2268c181e9c70ba9233',
        "_timestamp": '1596009876000',
        "loginName": username,
        "password": password,
        "terminal":'pc',
        "token": '',
        "v": ''
    }
    res = requests.post(url, headers=headers, data=body)
    try:
        sign = res.json()["login_info"]["sign"]
    except:
        sign = ""
    cookie = "{}={}".format(username, sign)
    return cookie

if __name__ == '__main__':
    cookie = get_cookie()
    print(cookie)
