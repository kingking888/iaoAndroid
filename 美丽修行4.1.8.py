# !/usr/bin/env python
# -*- coding:utf-8 -*-


import hashlib
import requests
import warnings

warnings.filterwarnings("ignore")


def get_sorted_key(data):
    data_sorted = sorted(data.items(), key=lambda d: d[0])
    new_s = ''.join(['&{}={}'.format(k, v) for k, v in data_sorted])
    return new_s


def get_md5_encrypt(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()


def get_signature(data):
    encryption_1_before = get_sorted_key(data)
    # print("encryption_1_before : ", encryption_1_before)

    encryption_1 = get_md5_encrypt(encryption_1_before)
    # print("encryption_1 : ", encryption_1)

    encryption_2_before = encryption_1 + "uAXDBeQs3Cl3"
    encryption_2 = get_md5_encrypt(encryption_2_before)
    print("signature : ", encryption_2)
    return encryption_2


def mlxx_login():
    url = "https://api.bevol.com/app/login3"

    headers = {
        'Accept': 'application/json;versions=1',
        'Cache-Control': 'public, max-age=60',
        'Cookie': '',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '257',
        'Host': 'api.bevol.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0',
    }

    data = {
        'uid': '',
        'uuid': '863386747311479',
        'imei': '3fb4c894d38e56ecdc442fe927ea98f6',
        'model': 'VOG-AL00',
        'sys_v': '7.1.2',
        'v': '4.1.8',
        'o': 'Android',
        'channel': 'taobao',
        'opentime': '1604411738',
        'req_timestamp': '1604411757835',
        'tel': '86',
        'account': '13788995576',
        'password': '123456',
        # 'signature': 'a12bd331d306781994d6ab2eb78580cd',
    }

    signature = get_signature(data)

    data["signature"] = signature

    response = requests.post(url, headers=headers, data=data, verify=False)
    print(response.text)

if __name__ == '__main__':
    mlxx_login()

"""
1、data

uid	
uuid	863386747311479
imei	3fb4c894d38e56ecdc442fe927ea98f6
model	VOG-AL00
sys_v	7.1.2
v	4.1.8
o	Android
channel	taobao
opentime	1604402733
req_timestamp	1604403501090
tel	86
account	13788995576
password	123456
signature	eb79ab78c65e9e21239cedc568e80e79

2、headers

POST /app/login3 HTTP/1.1
Accept: application/json;versions=1
Cache-Control: public, max-age=60
Cookie: 
Content-Type: application/x-www-form-urlencoded
Content-Length: 257
Host: api.bevol.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.10.0

3、url 

https://api.bevol.com/app/login3

"""
