# -*- coding: utf-8 -*-
import hashlib
import hmac
import base64
from urllib.parse import unquote, urlencode


class EncryptionHmac(object):
    def __init__(self):
        pass

    @staticmethod
    def get_md5_hex(value):
        m2 = hashlib.md5()
        m2.update(value.encode('utf-8'))
        return m2.hexdigest()

    @staticmethod
    def get_encrypt_hmac_sha1(secret, data):
        # print(hmac.new(bytes(secret, 'utf-8'), bytes(data, 'utf-8'), hashlib.sha1).digest())
        return str(base64.b64encode(hmac.new(bytes(secret, 'utf-8'),
                                             bytes(data, 'utf-8'), hashlib.sha1).digest()),
                   'utf-8')

    # 入参json， 按key排序，再转成query形式的参数。 eg.  apple=100&appKey=xxxx
    # unquote忽略转义，需要保留转义请取掉unquote
    def generate_sign(self, app_secret, data, encrypt_method='hmac-sha1'):
        # s = unquote(urlencode([(k, data[k]) for k in sorted(data.keys())]))
        if encrypt_method == "hmac-sha1":
            # sign = self.get_encrypt_hmac_sha1(app_secret, s)
            sign = self.get_encrypt_hmac_sha1(app_secret, data)
        else:
            # s += app_secret
            data += app_secret
            sign = self.get_md5_hex(data)
        print("SIGN is : {}".format(sign))
        return sign


if __name__ == '__main__':
    # app_key = "3f82df082747de1ea85f95c4c9f53c97"
    # app_secret = "e2afd6d564854cb79e320ef1226bdb4a"
    # param = {'nonceStr': '8B9yTWlx', 'appKey': app_key, 'apple': 100}
    app_secret = "asfsaADDJF55b262d99cff7cac7459e8&"
    data = "PUT&https%3A%2F%2Fmapi.mafengwo.cn%2Frest%2Fapp%2Fuser%2Flogin%2F&after_style%3Ddefault%26app_code%3Dcom.mfw.roadbook%26app_ver%3D8.1.6%26app_version_code%3D535%26brand%3Dgoogle%26channel_id%3DGROWTH-WAP-LC-3%26device_id%3DAC%253A37%253A43%253A4C%253A11%253A3B%26device_type%3Dandroid%26hardware_model%3DPixel%26mfwsdk_ver%3D20140507%26o_lat%3D31.103866%26o_lng%3D121.265273%26oauth_consumer_key%3D5%26oauth_nonce%3D04832440-45b7-411e-bcbd-afab8610c26e%26oauth_signature_method%3DHMAC-SHA1%26oauth_timestamp%3D1601658453%26oauth_version%3D1.0%26open_udid%3DAC%253A37%253A43%253A4C%253A11%253A3B%26put_style%3Ddefault%26screen_height%3D1794%26screen_scale%3D2.625%26screen_width%3D1080%26sys_ver%3D8.1.0%26time_offset%3D480%26x_auth_mode%3Dclient_auth%26x_auth_password%3D123456%26x_auth_username%3D13788995555"
    sign = EncryptionHmac().generate_sign(app_secret, data)
    print("sign : ", sign)
