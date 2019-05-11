# coding: utf-8

import requests
import base64
from common.box import *
from configparser import ConfigParser



class RuoKuai(object):
    def download_img(self, pic_url):
        """
        通过图片链接，下载图片到本地
        :param pic_url:
        """
        r = requests.get(pic_url)
        with open('./TestData/cache/reccode_img.png', 'wb') as f:
            f.write(r.content)
        f.close()

    def encode_img(self):
        """
        对本地图片进行base64编码
        :return:
        """
        with open('./TestData/cache/reccode_img.png', 'rb', ) as f:
            base64_data = base64.b64encode(f.read())
            stream = base64_data.decode()
        f.close()
        return stream

    def ruokuai(self, pic_url):
        """
        使用若快网识别验证码
        :param pic_url:
        :return:
        """
        self.download_img(pic_url)
        s = self.encode_img()
        conf = ConfigParser()
        conf.read('fusion.conf')
        param = {
            'username': conf.get('ruokuai', 'username'),
            'password': conf.get('ruokuai', 'password'),
            'typeid': int(conf.get('ruokuai', 'typeid')),
            'timeout': int(conf.get('ruokuai', 'timeout')),
            'softid': int(conf.get('ruokuai', 'softid')),
            'softkey': conf.get('ruokuai', 'softkey'),
            'image': s
        }

        rk_url = 'https://api.ruokuai.com/create.json'
        headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }
        try:
            r = requests.post(rk_url, data=param, headers=headers)
            return r.json()['Result']
        except:
            TestLogger.error('验证码识别超时')
