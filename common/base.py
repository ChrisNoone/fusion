# coding: utf-8

import requests
import base64
from common.box import *
from configparser import ConfigParser
from PIL import Image
import tesserocr, pytesser3
import cv2


# 使用“若快”网在线识别，正确率稍高，速度慢
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


# 使用tesseract识别，正确率低
class Captcha(object):
    img_path = './TestData/cache/reccode_img.png'

    def download_img(self, pic_url):
        """
        通过图片链接，下载图片到本地
        :param pic_url:
        """
        r = requests.get(pic_url)
        with open(self.img_path, 'wb') as f:
            f.write(r.content)
        f.close()

    def get_img(self):
        """
        用Image获取图片文件
        :return: 图片文件
        """
        img = Image.open(self.img_path)
        return img

    @staticmethod
    def grayscale_deal_img(image):
        """
        图片转灰度处理
        :param image:图片文件
        :return: 转灰度处理后的图片文件
        """
        img = image.convert('L')
        # img.show()
        return img

    @staticmethod
    def thresholding_method_img(image):
        """
            图片二值化处理
            :param image:转灰度处理后的图片文件
            :return: 二值化处理后的图片文件
        """
        # 阈值，控制二值化程度，自行调整（不能超过256）
        threshold = 160
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        img = image.point(table, '1')
        # img.show()
        return img

    @staticmethod
    def captcha_tesserocr_crack(image):
        """
            图像识别
            :param image: 二值化处理后的图片文件
            :return: 识别结果
        """
        result = tesserocr.image_to_text(image)
        return result


# 使用OpenCV
class OpenCVDealImage(object):
    img_dir = './TestData/cache/'
    '''
    https://www.cnblogs.com/qqandfqr/p/7866650.html
    '''

    def download_img(self, pic_url):
        """
        通过图片链接，下载图片到本地
        :param pic_url:
        """
        r = requests.get(pic_url)
        filename = self.img_dir + 'image.png'
        with open(filename, 'wb') as f:
            f.write(r.content)
        f.close()

    # 读取图片
    def get_img(self, img_name):
        img = cv2.imread(self.img_dir + img_name)
        return img

    # 显示图片
    def show(self, image):
        cv2.imshow('图片', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 保存图片
    def save(self, image, img_name):
        filename = self.img_dir + img_name
        cv2.imwrite(filename, image)

    # 灰度处理
    def grayscale_deal_img(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # self.save(img, 'image_grayscale.png')
        return img

    # 二值化
    def thresholding_method_img(self, image):
        # 固定阈值二值化
        ret, img = cv2.threshold(image, 160, 255, cv2.THRESH_BINARY)
        # self.save(img, 'image_threshold.png')
        return img

    # 去边框
    def clear_border(self, image):
        """
        去除边框
        :param image:
        :return:
        """
        h, w = image.shape[:2]
        for y in range(0, w):
            for x in range(0, h):
                if y < 2 or y > w - 2:
                    image[x, y] = 255
                if x < 2 or x > h - 2:
                    image[x, y] = 255
        # self.save(image, 'image_clearborder.png')
        return image

    # 降噪
    def interference_line(self, image):
        """
        干扰线降噪
        :param image:
        :return:
        """
        h, w = image.shape[:2]
        for y in range(1, w - 1):
            for x in range(1, h - 1):
                count = 0
                if image[x, y - 1].any() > 245:
                    count = count + 1
                if image[x, y + 1].any() > 245:
                    count = count + 1
                if image[x - 1, y].any() > 245:
                    count = count + 1
                if image[x + 1, y].any() > 245:
                    count = count + 1
                if count > 2:
                    image[x, y] = 255
        self.save(image, 'image_interferenceline.png')
        return image

    # 字符切割
    def cut_char(self):
        pass

    # 识别
    def tesserocr_img(self, image):
        result = tesserocr.image_to_text(image)
        return result
