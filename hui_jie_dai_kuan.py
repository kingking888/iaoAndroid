#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021.1.26
# @Author  : 二大爷
# @Platform: 惠借贷款 登录

import json
import random
import requests
import time
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
import base64
import warnings

warnings.filterwarnings("ignore")


def Md5withRSA(data):
    privateKey = '''MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAKPTzFdkU5BqQev6ohBcSP5TDXx0w7DXnErbARr8XF4ltEn6NcStQtg5UqiQ/DrrH6bexnooVkBSy4fAAzY1G7Q5YVWs9pm13fJe38xXi4PlKbYciqvQq0K5sUr9IOovK6hQyb32E+Fz7NpGKZdb16nIzHYF0fdX9sCuN3VkCXbrAgMBAAECgYAmQu70ch/6GHbw8AYtoAAENc1uha62fISqDuABN3MzIccrh95K4tQ7v5eIeuQNtqAbzue32/fY6f1S5Qta+6hOXPOb7GKavnr1hAnJ5XFQmtpVpmzaNmUH0bkFAEcIzVfFBiHweAOHf7wtyGplDChdhgu9Mu+G7XyBrbAay0CRYQJBAOMyCIZObPOGG9KFY3GD+ctw55k/cqfEV+E4LNo9+o2keee2OWcDFavqTVyD3qDeN3S+mNn0dvbjeqxLfZtR/IMCQQC4mQ7/z8MJOwlxozM5AD8RNautgCHKSDBpM4cVZ7fcqOTJXYjf8zM5UExoypfwcFYn4LfDDSNNP5OTtF1I8d95AkAoFAZu8tzDZM/5pjAxsS9alRM19HxcXgWGpGs9IJvXasFaf8nGg0PKbO2yuUyHoku0G39JS5fE28IjLLn+sUrTAkEAhqHrFJu8zaCnNKAonawWU0DnozTOcC/STwfrv6rTqDXuFwcG6v7/Hw/3in4n7o6f55m3rKSKWK7DvXhQiQEPUQJBAMLqGejiiH9E18hDvDROp/KtaceqT7GFc0izJZ8Z9iUFWmAJVo3gy0CIvyvbjOPCTfm3QC8bI1/l7+zuFtKj9yQ='''

    private_keyBytes = base64.b64decode(privateKey)
    priKey = RSA.importKey(private_keyBytes)
    # priKey = RSA.importKey(privateKey)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = MD5.new(data.encode('utf-8'))
    signature = base64.b64encode(signer.sign(hash_obj)).decode('utf8')
    return signature


class RsaCode:
    rsa_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAKPTzFdkU5BqQev6ohBcSP5TDXx0w7DXnErbARr8XF4ltEn6NcStQtg5UqiQ/DrrH6bexnooVkBSy4fAAzY1G7Q5YVWs9pm13fJe38xXi4PlKbYciqvQq0K5sUr9IOovK6hQyb32E+Fz7NpGKZdb16nIzHYF0fdX9sCuN3VkCXbrAgMBAAECgYAmQu70ch/6GHbw8AYtoAAENc1uha62fISqDuABN3MzIccrh95K4tQ7v5eIeuQNtqAbzue32/fY6f1S5Qta+6hOXPOb7GKavnr1hAnJ5XFQmtpVpmzaNmUH0bkFAEcIzVfFBiHweAOHf7wtyGplDChdhgu9Mu+G7XyBrbAay0CRYQJBAOMyCIZObPOGG9KFY3GD+ctw55k/cqfEV+E4LNo9+o2keee2OWcDFavqTVyD3qDeN3S+mNn0dvbjeqxLfZtR/IMCQQC4mQ7/z8MJOwlxozM5AD8RNautgCHKSDBpM4cVZ7fcqOTJXYjf8zM5UExoypfwcFYn4LfDDSNNP5OTtF1I8d95AkAoFAZu8tzDZM/5pjAxsS9alRM19HxcXgWGpGs9IJvXasFaf8nGg0PKbO2yuUyHoku0G39JS5fE28IjLLn+sUrTAkEAhqHrFJu8zaCnNKAonawWU0DnozTOcC/STwfrv6rTqDXuFwcG6v7/Hw/3in4n7o6f55m3rKSKWK7DvXhQiQEPUQJBAMLqGejiiH9E18hDvDROp/KtaceqT7GFc0izJZ8Z9iUFWmAJVo3gy0CIvyvbjOPCTfm3QC8bI1/l7+zuFtKj9yQ=
    -----END RSA PRIVATE KEY-----"""

    rsa_public_key = """-----BEGIN PUBLIC KEY-----
    MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCj08xXZFOQakHr+qIQXEj+Uw18dMOw15xK2wEa/FxeJbRJ+jXErULYOVKokPw66x+m3sZ6KFZAUsuHwAM2NRu0OWFVrPaZtd3yXt/MV4uD5Sm2HIqr0KtCubFK/SDqLyuoUMm99hPhc+zaRimXW9epyMx2BdH3V/bArjd1ZAl26wIDAQAB
    -----END PUBLIC KEY-----
    """

    def encrypt(self, msg):
        msg = msg.encode('utf-8')
        rsakey = RSA.importKey(self.rsa_public_key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(msg))
        return cipher_text

    def decrypt(self, cipher_text):
        rsakey = RSA.importKey(self.rsa_private_key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        random_generator = Random.new().read
        text = cipher.decrypt(base64.b64decode(cipher_text), random_generator)
        return text.decode('utf8')

    def long_encrypt(self, msg):
        msg = msg.encode('utf-8')
        length = len(msg)
        default_length = 117
        # 公钥加密
        pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(self.rsa_public_key))
        # 长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(msg))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(msg[offset:offset + default_length]))
            else:
                res.append(pubobj.encrypt(msg[offset:]))
            offset += default_length
        byte_data = b''.join(res)
        return base64.b64encode(byte_data)

    def long_decrypt(self, msg):
        msg = base64.b64decode(msg)
        print(msg)
        length = len(msg)
        default_length = 128
        # 私钥解密
        priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(self.rsa_private_key))
        # 长度不用分段
        if length < default_length:
            return b''.join(priobj.decrypt(msg, b'xyz'))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(priobj.decrypt(msg[offset:offset + default_length], b'xyz'))
            else:
                res.append(priobj.decrypt(msg[offset:], b'xyz'))
            offset += default_length

        return b''.join(res).decode('utf8')


phone = "131" + str(random.randint(10000000, 99999999))
timestamp = int(time.time() * 1000)
passwrod = "".join(random.sample("0123efghijklEFGHIJKL456mnopqrstuvwsyzMNOPQRSTUVWXYZ789abcdABCD", 8))
message = {
    "phone": phone,
    "password": passwrod,
    "timestamp": timestamp,
    "appName": "惠借贷款"
}
sign = Md5withRSA(json.dumps(message, separators=(',', ':'), ensure_ascii=False))

url = "https://jsyloan.jishiyu2019.com/user/passwordLogin.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; G011C Build/N2G48H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Mobile Safari/537.36',
    'imei': '',
    'Content-Length': '0',
    'Host': 'jsyloan.jishiyu2019.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}
mainDoctorParams = {
    "appId": 217,
    "v": 3,
    "channel": "XM",
    "token": "",
    "data": "{\"phone\":\"" + phone + "\",\"password\":\"" + passwrod + "\",\"timestamp\":" + f"{timestamp}" + ",\"appName\":\"惠借贷款\"}",
    "sign": sign
}
params = {
    'req': json.dumps(mainDoctorParams, separators=(',', ':'), ensure_ascii=False),
}
response = requests.post(url, headers=headers, params=params, verify=False)
print(response.text)
