# encoding: utf-8

import time
import requests

def sleep(n_secs):
    time.sleep(n_secs)

# 11位
def get_timestamp():
    return str(int(time.time() * 10))  

# 5位
def get_timestamp1():
    return str(time.time()).replace(".", "")[5:10]

# 登录一级用户并获取token
def get_token(username="zhaohexiang1", password="72732414d750775c1eb0b5b915b3561b"):
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
    r = requests.post(url, headers=headers, data=body)
    try:
        # 获取token的方法：["一级"]["二级"]["..."]
        return_token = r.json()["results"]["data"]["token"]
    except:
        print("没取到token \n %s" % r.text)
        return_token = ''
    return return_token

if __name__ == "__main__":
    return_token = get_token()
    print(return_token)

# 登录二级用户并获取token
def get_token1(username="ceshi_admin", password="72732414d750775c1eb0b5b915b3561b"):
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
    r = requests.post(url, headers=headers, data=body)
    try:
        # 获取token的方法：["一级"]["二级"]["..."]
        return_token = r.json()["results"]["data"]["token"]
    except:
        print("没取到token \n %s" % r.text)
        return_token = ''
    return return_token

if __name__ == "__main__":
    return_token = get_token1()
    print(return_token)



#     res = requests.post(url, headers=headers, data=body)
#     try:
#         sign = res.json()["login_info"]["sign"]
#     except:
#         sign = ""
#     cookie = "{}={}".format(username, sign)
#     return cookie

# if __name__ == '__main__':
#     cookie = get_cookie()
#     print(cookie)
