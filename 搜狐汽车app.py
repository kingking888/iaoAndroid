# !/usr/bin/python
# -*- coding: utf-8 -*-


import hashlib
import json
import time

import requests
import base64
from urllib import parse
from lxml import etree
import warnings

warnings.filterwarnings("ignore")

url = "https://app.auto.sohu.com/api/car/evals/389573"
# url = "https://app.auto.sohu.com/api/car/evals/388614?_ts=1603004716509&_v=72100&sign=967071e16db07a787d006df076f9c2e1"

headers = {
    'X-APP-NAME': 'autonews',
    'X-DEVICE-ID': 'ca7e8c9f5ab069f9',
    'X-OS': 'android',
    'X-OS-VERSION': '8.1.0',
    'X-UA': 'Mozilla/5.0 (Linux; Android 8.1.0; Pixel Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36',
    'X-CHANNEL': 'huawei',
    'X-MANUFACTURER': 'Google',
    'X-MODEL-RAW': 'Pixel',
    'X-VERSION-CODE': '72100',
    'X-VERSION-NAME': '7.2.1',
    'X-SCREEN-WIDTH': '1080',
    'X-SCREEN-HEIGHT': '1794',
    'x-umid': 'ai40a118696aaa2519c95d2e1a470306ce',
    'User-Agent': 'sohuauto_7.2.1_android_8.1.0_huawei_ca7e8c9f5ab069f9_google',
    'Host': 'app.auto.sohu.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Accept': None,
}


_ts = int(time.time() * 1000)
params = {
    '_ts': str(_ts),
    '_v': '72100',
    # 'sign': '1338f3e6bef648ef09d33ca80bc5544d',
}
data_sorted = sorted(params.items(), key=lambda d: d[0])
new_s = ''.join(['{}'.format(v) for k, v in data_sorted])
data = new_s + "70THe92NEwSOul80SHouLD15Be23FReE"
sign = hashlib.md5(data.encode("utf-8")).hexdigest()
print(sign)
params['sign'] = sign

response = requests.get(url, headers=headers, params=params, verify=False)
print(response.text)
# print(json.dumps(json.loads(response.text), indent=4, ensure_ascii=False))
