# coding: utf-8

import requests
import base64
from common.box import *
from configparser import ConfigParser
from PIL import Image
import tesserocr
import cv2
import queue


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

    # 线降噪
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

    # 点降噪
    def interference_point(self, img):
        """
        9邻域框,以当前点为中心的田字框,黑点个数
        清除孤立的点
        :param img:
        :return:
        """
        height, width = img.shape[:2]

        for y in range(0, width):
            for x in range(0, height):
                if y == 0:  # 第一列
                    if x == 0:  # 左上顶点,4邻域
                        # 中心点旁边3个点
                        sum = int(img[x, y + 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum >= 2 * 255:
                            img[x, y] = 255
                    elif x == height - 1:  # 左下顶点
                        sum = int(img[x, y + 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1])
                        if sum >= 2 * 255:
                            img[x, y] = 255
                    else:  # 最左非顶点,6邻域
                        sum = int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1]) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum >= 4 * 255:
                            img[x, y] = 255
                elif y == width - 1:  # 最后一列
                    if x == 0:  # 右上顶点
                        sum = int(img[x + 1, y]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x, y - 1])
                        if sum >= 2 * 255:
                            img[x, y] = 255
                    elif x == height - 1:  # 右下顶点
                        sum = int(img[x, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y - 1])
                        if sum >= 2 * 255:
                            img[x, y] = 255
                    else:  # 最右非顶点,6邻域
                        sum = int(img[x - 1, y]) \
                              + int(img[x + 1, y]) \
                              + int(img[x, y - 1]) \
                              + int(img[x - 1, y - 1]) \
                              + int(img[x + 1, y - 1])
                        if sum >= 4 * 255:
                            img[x, y] = 255
                else:  # 不在最左右两列
                    if x == 0:  # 上非顶点
                        sum = int(img[x, y - 1]) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum >= 4 * 255:
                            img[x, y] = 255
                    elif x == height - 1:  # 下边非顶点
                        sum = int(img[x, y - 1]) \
                              + int(img[x, y + 1]) \
                              + int(img[x - 1, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1])
                        if sum >= 4 * 255:
                            img[x, y] = 255
                    else:  # 具备9领域条件的
                        sum = int(img[x - 1, y - 1]) \
                              + int(img[x - 1, y]) \
                              + int(img[x - 1, y + 1]) \
                              + int(img[x, y - 1]) \
                              + int(img[x, y + 1]) \
                              + int(img[x + 1, y - 1]) \
                              + int(img[x + 1, y]) \
                              + int(img[x + 1, y + 1])
                        if sum >= 7 * 255:
                            img[x, y] = 255
        self.save(img, 'image_interferencepoint.png')
        return img

    # 字符切割
    def detect4Xy(self, im, x_fd, y_fd):
        """
        遍历图片与初始点有连接的所有点，返回最大/最小的，横/总坐标
        用队列和集合记录遍历过的像素坐标代替单纯递归以解决cfs访问过深问题
        """
        xaxis = []
        yaxis = []
        visited = set()
        q = queue.Queue()
        q.put((x_fd, y_fd))
        visited.add((x_fd, y_fd))
        offsets = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 四邻域

        while not q.empty():
            x, y = q.get()

            for xoffset, yoffset in offsets:
                x_neighbor, y_neighbor = x + xoffset, y + yoffset

                if (x_neighbor, y_neighbor) in (visited):
                    continue  # 已经访问过了

                visited.add((x_neighbor, y_neighbor))

                try:
                    if im[x_neighbor, y_neighbor] == 0:
                        xaxis.append(x_neighbor)
                        yaxis.append(y_neighbor)
                        q.put((x_neighbor, y_neighbor))

                except IndexError:
                    pass
        if (len(xaxis) == 0 | len(yaxis) == 0):
            xmax = x_fd + 1
            xmin = x_fd
            ymax = y_fd + 1
            ymin = y_fd

        else:
            xmax = max(xaxis)
            xmin = min(xaxis)
            ymax = max(yaxis)
            ymin = min(yaxis)

        return xmax, xmin, ymax, ymin

    def detectFirstPix(self, im, ymax):
        """
        搜索区块起点
        :param im:
        :param ymax:
        :return: 返回起点的纵坐标x, 横坐标y
        """
        h, w = im.shape[:2]
        for y_fd in range(ymax + 1, w):
            for x_fd in range(h):
                if im[x_fd, y_fd] == 0:
                    return x_fd, y_fd

    def buildCoordinate(self, im):
        """
        寻找切割字符位置
        :param im:
        :return: zoneL - 将要被切割的区块的宽度集合，zoneHB - 将要被切割的区块的纵坐标[起始x, 终点x]集合，zoneWB - 将要被切割的区块的横坐标[起始y, 终点y]集合
        """
        zoneL = []  # 各区块长度L列表
        zoneWB = []  # 各区块的X轴[起始，终点]列表
        zoneHB = []  # 各区块的Y轴[起始，终点]列表

        ymax = 0  # 上一区块结束黑点横坐标,这里是初始化
        for i in range(10):
            try:
                x_fd, y_fd = self.detectFirstPix(im, ymax)
                xmax, xmin, ymax, ymin = self.detect4Xy(im, x_fd, y_fd)
                L = ymax - ymin
                # H = ymax - ymin
                zoneL.append(L)
                zoneHB.append([xmin, xmax])
                zoneWB.append([ymin, ymax])

            except TypeError:
                return zoneL, zoneHB, zoneWB

        return zoneL, zoneHB, zoneWB

    def cutting_img(self, image, img_name='cache', xoffset=1, yoffset=1):
        """
        切割字符
        :param image: 待切割图片对象
        :param img_name: 切割后的文件名
        :param xoffset: 切割偏移量，纵向
        :param yoffset: 切割偏移量，横向
        :return:
        """
        # 建立待切割坐标数据集
        im_position = self.buildCoordinate(image)

        # 处理有连接字符，如果一个字符的长度过长就认为是粘连字符，并从中间进行切割
        maxL = max(im_position[0])
        minL = min(im_position[0])
        if (maxL > minL + minL * 0.7):
            maxL_index = im_position[0].index(maxL)
            # minL_index = im_position[0].index(minL)
            # 设置字符的宽度
            im_position[0][maxL_index] = maxL // 2
            im_position[0].insert(maxL_index + 1, maxL // 2)
            # 设置字符X轴[起始，终点]位置
            im_position[1][maxL_index][1] = im_position[1][maxL_index][0] + maxL // 2
            im_position[1].insert(maxL_index + 1,
                                  [im_position[1][maxL_index][1] + 1, im_position[1][maxL_index][1] + 1 + maxL // 2])
            # 设置字符的Y轴[起始，终点]位置
            im_position[2].insert(maxL_index + 1, im_position[2][maxL_index])

        filename = self.img_dir + img_name.split('.')[0]
        # 识别出的字符个数
        im_number = len(im_position[1])
        # 切割字符
        for i in range(im_number):
            im_start_X = im_position[1][i][0] - xoffset
            im_end_X = im_position[1][i][1] + xoffset
            im_start_Y = im_position[2][i][0] - yoffset
            im_end_Y = im_position[2][i][1] + yoffset
            cropped = image[im_start_X:im_end_X, im_start_Y:im_end_Y]
            cv2.imwrite(filename + str(i) + '.png', cropped)

    # 识别
    def tesserocr_img(self, image):
        result = tesserocr.image_to_text(image)
        return result
