import csv
import random
import time

from common.box import BasePage, YamlHelper


class PK10Mm(BasePage):
    # pk10
    config_dict_pk10_mm = YamlHelper().get_config_dict('/fusion/yaml/lottery_pk10_mm.yaml')['Pk10_Mm']

    def qian_1(self, row):
        # 导航栏---前一
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前一')
        # 遍历10个号码
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                # 遍历10个号码
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN1GJUN'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('前一---前一:' + str(s1))
                # 遍历全，大，小，单，双
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIANWENZI'], s2)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('前一---前一文字' + str(s2))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三不同号---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---前一
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前一')
                break

    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    def qian_2_fs(self, row):
        # 导航栏
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
        # 前二 - --前二复式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                # 随机抽取号码
                if s0 == 0:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a1)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        print('前二复式：' + str(a0) + str(a1))
                # # 遍历全，大，小，单，双
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], a2)
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], a3)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('前二复式文字：' + str(a2) + str(a3))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三不同号---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
                # 前二 - --前二复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
                break

    def qian_2_fs_error(self, row):
        # 前二
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
        # 前二---前二复式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(50):
            try:
                s0 = random.choice(range(0, 13))
                s1 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                a5 = random.choice(range(0, 10))
                a6 = random.choice(range(0, 10))
                a7 = random.choice(range(0, 10))
                a8 = random.choice(range(0, 10))
                a9 = random.choice(range(0, 10))
                # 十位选择一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a0)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二复式：' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], '5')
                # 个位选择一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a0)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], '5')
                # 选择十位文字
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], '5')
                # 选择个位文字
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], '5')
                # 十位选择两个
                if s0 == 4:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a1)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], '5')
                # 个位选择两个
                if s0 == 5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a3)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], '5')
                # 十位选择三个
                if s0 == 6:
                    if a0 == a1 or a1 == a2 or a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a2)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], '5')
                # 个位选择三个
                if s0 == 7:
                    if a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a3)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a4)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a5)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], '5')
                # 十位选择四个
                if s0 == 8:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a3)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], '5')
                # 个位选择四个
                if s0 == 9:
                    if a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a4)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a5)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a6)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a7)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], '5')
                # 十位选择五个
                if s0 == 10:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a3)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GJUN'], a4)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2GWENZI'], '5')
                # 个位选择五个
                if s0 == 11:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a5)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a6)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a7)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a8)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YJUN'], a9)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2YWENZI'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前二---前二复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前二---前二复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 前二
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
                # 前二---前二复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
                break

    def qian_2_ds(self, row):
        # 导航栏---前一
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
        # 前二---前二单式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
        for i in range(100):
            try:
                s0 = random.choice(range(1, 11))
                s1 = random.choice(range(1, 11))
                s2 = "%02d" % s0
                s3 = "%02d" % s1
                if s0 == s1:
                    pass
                else:
                    ss = str(s2) + ' ' + str(s3)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('前二---前二单式号码：' + str(ss))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前二---前二复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前二---前二复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 前二
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
                # 前二---前二复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
                break

    def qian_2_ds_error(self, row):
        # 导航栏---前一
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
        # 前二---前二单式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
        for i in range(50):
            try:
                s0 = random.choice(range(0, 7))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(-1000, 1))
                s4 = random.choice(range(-1000, 1000))
                s5 = random.choice(range(11, 1000))
                n0 = random.choice(range(1, 11))
                m0 = random.choice(range(1, 11))
                n1 = "%02d" % n0
                m1 = "%02d" % m0
                # 输入一个小于两位数字的号码,前面不补0
                if s0 == 0:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('输入一个小于两位数字的号码：' + str(s1) + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入两个小于两位的号码,前面不补0
                if s0 == 1:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], str(s1) + ' ' + str(s2))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二单式：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入一个小于0的号码，另外一个随机
                if s0 == 2:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], str(s3) + ' ' + str(s4))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二单式：' + str(s) + ' ' + str(s3) + ' ' + str(s4))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入一个大于10的号码，另外一个随机
                if s0 == 3:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], str(s5) + ' ' + str(s4))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二单式：' + str(s) + ' ' + str(s5) + ' ' + str(s4))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 在01-10中输入两个相同的号码
                if s0 == 4:
                    if n1 == m1:
                        self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], str(m1) + ' ' + str(n1))
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前二---前二单式：' + str(s) + ' ' + str(m1) + ' ' + str(n1))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    else:
                        pass
                # 输入3个号码
                if s0 == 5:
                    ss = str(s1) + ' ' + str(s2) + ' ' + str(m1)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二单式：' + str(s) + ' ' + str(m1) + ' ' + str(n1))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入4个号码
                if s0 == 6:
                    ss = str(s1) + ' ' + str(s2) + ' ' + str(m1) + ' ' + str(n1)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前二---前二单式：' + str(s) + ' ' + str(s1) + ' ' + str(s2) + ' ' + str(m1) + ' ' + str(n1))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前二---前二复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前二---前二复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 前二
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
                # 前二---前二复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
                break

    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    def qian_3_fs(self, row):
        # 导航栏---前三
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
        # 前三---前三复式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 7))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                # 从冠军、亚军、季军中各选1个不同的号码组成一注
                # 从冠军选1个、亚军选1个、季军中1个
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a2)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        print('前三---前三复式冠亚军：' + str(a0) + ' ' + str(a1) + ' ' + str(a2))
                # 从冠军选2个、亚军选1个、季军中1个
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a3)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        print('前三---前三复式冠亚军：' + str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3))
                # 从冠军选1个、亚军选2个、季军中1个
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a3)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        print('前三---前三复式冠亚军：' + str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3))
                # 从冠军选1个、亚军选1个、季军中2个
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a3)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        print('前三---前三复式冠亚军：' + str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3))
                # 从冠军选3个、亚军选1个、季军中1个
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        if a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                            ss = str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4)
                            print('前三---前三复式冠亚军：' + str(ss))
                # 从冠军选1个、亚军选3个、季军中1个
                if s0 == 5:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        if a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                            ss = str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4)
                            print('前三---前三复式冠亚军：' + str(ss))
                # 从冠军选1个、亚军选1个、季军中3个
                if s0 == 6:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        if a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a4)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                            ss = str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4)
                            print('前三---前三复式冠亚军：' + str(ss))
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前三---前三复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前二---前二复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---前三
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
                # 前三---前三复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
                break

    def qian_3_fs_error(self, row):
        # 导航栏
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
        # 前三---前三复式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
        self.base_driver.forced_wait(5)
        # 遍历10个号码
        # 从冠军选1个、亚军选1个、季军中1个数字都一样的号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 21))
                s1 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                a5 = random.choice(range(0, 10))
                a6 = random.choice(range(0, 10))
                a7 = random.choice(range(0, 10))
                a8 = random.choice(range(0, 10))
                a9 = random.choice(range(0, 10))
                # 冠军选择一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                # 亚军选择一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a0)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                # 季军选择一个
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a0)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                # 选择冠军文字
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                # 选择亚军文字
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                # 选择季军文字
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三复式：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                # 选择冠军亚军相同，季军随机
                if s0 == 6:
                    if a0 == a1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a2)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前三---前三复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                    else:
                        pass
                # 选择冠军季军相同，亚军随机
                if s0 == 7:
                    if a0 == a2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a2)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前三---前三复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                    else:
                        pass
                # 选择亚军季军相同，冠军随机
                if s0 == 8:
                    if a1 == a2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a2)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前三---前三复式：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                    else:
                        pass
                # 选择冠军两个
                if s0 == 9:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a1)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码十位选择两个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                # 选择亚军两个
                if s0 == 10:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a1)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择两个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                # 选择季军两个
                if s0 == 11:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a1)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择两个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                # 选择冠军三个
                if s0 == 12:
                    if a0 == a1 or a1 == a2 or a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a2)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码十位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                # 选择亚军三个
                if s0 == 13:
                    if a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a3)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a4)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a5)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                # 选择季军三个
                if s0 == 14:
                    if a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a3)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a4)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a5)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                # 选择冠军四个
                if s0 == 15:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a3)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码十位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                # 选择亚军四个
                if s0 == 16:
                    if a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a4)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a5)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a6)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a7)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                # 选择季军四个
                if s0 == 17:
                    if a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a4)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a5)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a6)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a7)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                # 选择冠军五个
                if s0 == 18:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a0)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a1)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a2)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a3)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GJUN'], a4)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码十位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3GWENZI'], '5')
                # 选择亚军五个
                if s0 == 19:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a5)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a6)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a7)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a8)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YJUN'], a9)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3YWENZI'], '5')
                # 选择季军五个
                if s0 == 20:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a5)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a6)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a7)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a8)
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JJUN'], a9)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('极速3d-二码个位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN3JWENZI'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前三---前三复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前三---前三复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---前三
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
                # 前三---前三复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '0')
                break

    def qian_3_ds(self, row):
        # 导航栏---前一
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前二')
        # 前三---前三单式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
        for i in range(100):
            try:
                s0 = random.choice(range(1, 11))
                s1 = random.choice(range(1, 11))
                s2 = random.choice(range(1, 11))
                s3 = "%02d" % s0
                s4 = "%02d" % s1
                s5 = "%02d" % s2
                if s0 == s1:
                    pass
                else:
                    print('s4: ' + str(s3))
                    ss = str(s3) + ' ' + str(s4) + ' ' + str(s5)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN2DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('前三---前三单式：' + str(ss))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前三---前三复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前三---前三复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---前三
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
                # 前三---前三复式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
                break

    def qian_3_ds_error(self, row):
        # 导航栏
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
        # 前三---前三单式
        self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
        for i in range(100):
            try:
                s0 = random.choice(range(0, 9))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 10))
                s4 = random.choice(range(-1000, 1))
                s5 = random.choice(range(-1000, 1000))
                s6 = random.choice(range(11, 1000))
                m0 = random.choice(range(1, 11))
                m1 = random.choice(range(1, 11))
                m2 = random.choice(range(1, 11))
                n0 = "%02d" % m0
                n1 = "%02d" % m1
                n2 = "%02d" % m2
                # 输入一个小于两位数字的号码,前面不补0
                if s0 == 0:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('输入一个小于两位数字的号码：' + str(s1) + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入两个小于两位的号码,前面不补0
                if s0 == 1:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], str(s1) + ' ' + str(s2))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入三个小于两位的号码,前面不补0
                if s0 == 2:
                    ss = str(s1) + ' ' + str(s2) + ' ' + str(s3)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入一个小于0的号码，另外一个随机
                if s0 == 3:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], str(s4) + ' ' + str(s5))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(s4) + ' ' + str(s5) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入一个小于0的号码，另外两个随机
                if s0 == 4:
                    ss = str(s4) + ' ' + str(s5) + ' ' + str(s6)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(s5) + ' ' + str(s5) + ' ' + str(s6) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入一个大于10的号码，另外一个随机
                if s0 == 5:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], str(s6) + ' ' + str(s5))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(s6) + ' ' + str(s5) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 输入一个大于10的号码，另外两个随机
                if s0 == 6:
                    ss = str(s6) + ' ' + str(s5) + ' ' + str(s4)
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], ss)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                # 在01-10中输入三个号码。最少两个相同的号码
                if s0 == 7:
                    if n0 == n1 or n0 == n2 or n1 == n2:
                        x = str(n0) + ' ' + str(n1) + ' ' + str(n2)
                        self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], x)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                        print('前三---前三单式：' + str(x) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                    else:
                        pass
                # 输入4个号码
                if s0 == 8:
                    self.base_driver.type(self.config_dict_pk10_mm['QIAN3DFNTEXT'], str(s1) + ' '
                                          + str(s2) + ' ' + str(m1) + ' ' + str(n1))
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
                    print('前三---前三单式：' + str(s) + ' ' + str(s1) + ' ' + str(s2) + ' ' + str(n0) + ' ' + str(n1))
                    self.base_driver.click(self.config_dict_pk10_mm['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-前三---前三复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('前三---前三复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '前三')
                # 前三---前三单式
                self.base_driver.clicks(self.config_dict_pk10_mm['QIAN2DFN'], '1')
                break
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------

    def dwd_1_5(self, row):
        # 导航栏---定位胆
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '定位胆')
        self.base_driver.forced_wait(1)
        # 定位胆---第1-5名
        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_5'], '0')
        self.base_driver.forced_wait(1)
        '''
        # 冠军---遍历10个号码
        for a in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 冠军---全大小单双
        for a1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], a1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 亚军---遍历10个号码
        for b in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], b)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 亚军---全大小单双
        for b1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 季军---遍历10个号码
        for c in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], c)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 季军---遍全大小单双
        for c1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], c1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第四名---遍历10个号码
        for d in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], d)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第四名---遍历全大小单双
        for d1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], d1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第五名---遍历10个号码
        for e in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], e)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第五名---遍历全大小单双
        for e1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], e1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        '''
        # 随机抽取
        for i in range(200):
            try:
                s0 = random.choice(range(0, 12))
                s1 = random.choice(range(0, 5))
                s2 = random.choice(range(0, 5))
                s3 = random.choice(range(0, 5))
                s4 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 5))
                ss = str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4)
                print('定位胆---第1-5名：' + str(ss))
                # 任意1位置选择一个
                if s0 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置文字选择一个
                if s0 == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择两个
                if s0 == 2:
                    if s1 == 0:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择3个
                if s0 == 3:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择4个
                if s0 == 4:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择5个
                if s0 == 5:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意2位置选择1个
                if s0 == 6:
                    if s1 == s2:
                        pass
                    else:
                        if s1 == 0 or s2 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意2位置文字选择1个
                if s0 == 7:
                    if s1 == s2:
                        pass
                    else:
                        if s1 == 0 or s2 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        if s1 == 1 or s2 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        if s1 == 2 or s2 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        if s1 == 3 or s2 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        if s1 == 4 or s2 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意三个位置选择1个
                if s0 == 8:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意三个位置文字选择1个
                if s0 == 9:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意四个位置选择1个
                if s0 == 10:
                    if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意五个位置随机选择1个
                if s0 == 11:
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a4)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-定位胆---第1-5名.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('定位胆---第1-5名下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---定位胆
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '定位胆')
                self.base_driver.forced_wait(1)
                # 定位胆---第1-5名
                self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_5'], '0')
                self.base_driver.forced_wait(1)
                break

    def dwd_6_10(self, row):
        # 导航栏---定位胆
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '定位胆')
        self.base_driver.forced_wait(1)
        # 定位胆---第6-10名
        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_5'], '1')
        self.base_driver.forced_wait(1)
        # 冠军---遍历10个号码
        '''
        for a in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 冠军---全大小单双
        for a1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], a1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 亚军---遍历10个号码
        for b in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], b)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 亚军---全大小单双
        for b1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 季军---遍历10个号码
        for c in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], c)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 季军---遍全大小单双
        for c1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], c1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第四名---遍历10个号码
        for d in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], d)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第四名---遍历全大小单双
        for d1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], d1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第五名---遍历10个号码
        for e in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], e)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第五名---遍历全大小单双
        for e1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], e1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        '''
        # 随机抽取
        for i in range(200):
            try:
                s0 = random.choice(range(0, 12))
                s1 = random.choice(range(0, 5))
                s2 = random.choice(range(0, 5))
                s3 = random.choice(range(0, 5))
                s4 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 5))
                ss = str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4)
                print('定位胆---第1-5名：' + str(ss))
                # 任意1位置选择一个
                if s0 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置文字选择一个
                if s0 == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择两个
                if s0 == 2:
                    if s1 == 0:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择3个
                if s0 == 3:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择4个
                if s0 == 4:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择5个
                if s0 == 5:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意2位置选择1个
                if s0 == 6:
                    if s1 == s2:
                        pass
                    else:
                        if s1 == 0 or s2 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意2位置文字选择1个
                if s0 == 7:
                    if s1 == s2:
                        pass
                    else:
                        if s1 == 0 or s2 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        if s1 == 1 or s2 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        if s1 == 2 or s2 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        if s1 == 3 or s2 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        if s1 == 4 or s2 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意三个位置选择1个
                if s0 == 8:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意三个位置文字选择1个
                if s0 == 9:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意四个位置选择1个
                if s0 == 10:
                    if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意五个位置随机选择1个
                if s0 == 11:
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a4)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-定位胆---第1-5名.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('定位胆---第1-5名下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---定位胆
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '定位胆')
                self.base_driver.forced_wait(1)
                # 定位胆---第6-10名
                self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_5'], '1')
                self.base_driver.forced_wait(1)
                break

    def dwd_1_10(self, row):
        # 导航栏---定位胆
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '定位胆')
        self.base_driver.forced_wait(1)
        # 定位胆---第1-10名
        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_5'], '2')
        self.base_driver.forced_wait(1)
        # 冠军---遍历10个号码
        '''
        for a in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 冠军---全大小单双
        for a1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], a1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 亚军---遍历10个号码
        for b in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], b)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 亚军---全大小单双
        for b1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 季军---遍历10个号码
        for c in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], c)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 季军---遍全大小单双
        for c1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], c1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第四名---遍历10个号码
        for d in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], d)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第四名---遍历全大小单双
        for d1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], d1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第五名---遍历10个号码
        for e in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], e)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第五名---遍历全大小单双
        for e1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], e1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第六名---遍历10个号码
        for a in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第六名---全大小单双
        for a1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55WZ0'], a1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第七名---遍历10个号码
        for b in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], b)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第七名---全大小单双
        for b1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56WZ0'], b1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第八名---遍历10个号码
        for c in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], c)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第八名---遍全大小单双
        for c1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57WZ0'], c1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第九名---遍历10个号码
        for d in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], d)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第九名---遍历全大小单双
        for d1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58WZ0'], d1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第十名---遍历10个号码
        for e in range(10):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], e)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        # 第十名---遍历全大小单双
        for e1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59WZ0'], e1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        for e1 in range(5):
            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], e1)
            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        '''
        # 随机抽取
        for i in range(200):
            try:
                s0 = random.choice(range(0, 12))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 10))
                s4 = random.choice(range(0, 10))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                a5 = random.choice(range(0, 10))
                a6 = random.choice(range(0, 10))
                a7 = random.choice(range(0, 10))
                a8 = random.choice(range(0, 10))
                a9 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 5))
                s1 = str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' ' + str(a4)
                s2 = str(a5) + ' ' + str(a6) + ' ' + str(a7) + ' ' + str(a8) + ' ' + str(a9)
                print('定位胆---第1-5名：' + str(s1) + ' ' + str(s2))
                # 任意1位置选择一个
                if s0 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 5:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 6:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 7:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置文字选择一个
                if s0 == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 5:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 6:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 7:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 9:
                        self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择两个
                if s0 == 2:
                    if s1 == 0:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 5:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 6:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 7:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 9:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a1)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择3个
                if s0 == 3:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 5:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 6:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 7:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 9:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a2)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择4个
                if s0 == 4:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 5:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 6:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 7:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 9:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a3)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意1位置选择5个
                if s0 == 5:
                    if s1 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 1:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 2:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 5:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 6:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 7:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 8:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    if s1 == 9:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a1)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a2)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a3)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a4)
                            self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意2位置选择1个
                if s0 == 6:
                    if s1 == s2:
                        pass
                    else:
                        if s1 == 0 or s2 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        if s1 == 5 or s2 == 5:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                        if s1 == 6 or s2 == 6:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                        if s1 == 7 or s2 == 7:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                        if s1 == 8 or s2 == 8:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                        if s1 == 9 or s2 == 9:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意2位置文字选择1个
                if s0 == 7:
                    if s1 == s2:
                        pass
                    else:
                        if s1 == 0 or s2 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        if s1 == 1 or s2 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        if s1 == 2 or s2 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        if s1 == 3 or s2 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        if s1 == 4 or s2 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        if s1 == 5 or s2 == 5:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55WZ0'], b0)
                        if s1 == 6 or s2 == 6:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56WZ0'], b0)
                        if s1 == 7 or s2 == 7:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57WZ0'], b0)
                        if s1 == 8 or s2 == 8:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58WZ0'], b0)
                        if s1 == 9 or s2 == 9:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意三个位置选择1个
                if s0 == 8:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        if s1 == 5 or s2 == 5 or s3 == 5:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                        if s1 == 6 or s2 == 6 or s3 == 6:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                        if s1 == 7 or s2 == 7 or s3 == 7:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                        if s1 == 8 or s2 == 8 or s3 == 8:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                        if s1 == 9 or s2 == 9 or s3 == 9:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意三个位置文字选择1个
                if s0 == 9:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50WZ0'], b0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51WZ0'], b0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52WZ0'], b0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53WZ0'], b0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54WZ0'], b0)
                        if s1 == 5 or s2 == 5 or s3 == 5:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55WZ0'], b0)
                        if s1 == 6 or s2 == 6 or s3 == 6:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56WZ0'], b0)
                        if s1 == 7 or s2 == 7 or s3 == 7:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57WZ0'], b0)
                        if s1 == 8 or s2 == 8 or s3 == 8:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58WZ0'], b0)
                        if s1 == 9 or s2 == 9 or s3 == 9:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59WZ0'], b0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意四个位置选择1个
                if s0 == 10:
                    if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a0)
                        if s1 == 5 or s2 == 5 or s3 == 5 or s4 == 5:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], a0)
                        if s1 == 6 or s2 == 6 or s3 == 6 or s4 == 6:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_56111'], a0)
                        if s1 == 7 or s2 == 7 or s3 == 7 or s4 == 7:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_57111'], a0)
                        if s1 == 8 or s2 == 8 or s3 == 8 or s4 == 8:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_58111'], a0)
                        if s1 == 9 or s2 == 9 or s3 == 9 or s4 == 9:
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_59111'], a0)
                        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                # 任意五个位置随机选择1个
                if s0 == 11:
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a0)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a1)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a2)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a3)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a4)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_50111'], a5)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a6)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], a7)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], a8)
                    self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], a9)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-定位胆---第1-5名.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('定位胆---第1-5名下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---定位胆
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '定位胆')
                self.base_driver.forced_wait(1)
                # 定位胆---第1-10名
                self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_5'], '2')
                self.base_driver.forced_wait(1)
                break
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------

    def gjh(self, row):
        # 导航栏---冠军和
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '冠军和')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 15))
                s2 = random.choice(range(0, 2))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIANGYH1'], s1)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('冠军和---和值：' + str(s1))
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_pk10_mm['QIANGYH2'], s2)
                    self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                    print('冠军和---和值：' + str(s2))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-导航栏---冠军和.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('导航栏---冠军和下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 导航栏---冠军和
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '冠军和')
                break

    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    def longhu01(self, row):
        # 导航栏---龙虎
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
        self.base_driver.forced_wait(1)
        # 龙虎---龙虎---冠军
        self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '0')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGLH'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('龙虎---龙虎---冠军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-龙虎---龙虎---冠军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('龙虎---龙虎---冠军下注异常')
                # 导航栏---龙虎
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
                self.base_driver.forced_wait(1)
                # 龙虎---龙虎---冠军
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '0')
                break

    def longhu02(self, row):
        # 导航栏---龙虎
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
        self.base_driver.forced_wait(1)
        # 龙虎---龙虎---亚军
        self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '1')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGLH'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('龙虎---龙虎---亚军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-龙虎---龙虎---冠军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('龙虎---龙虎---冠军下注异常')
                # 导航栏---龙虎
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
                self.base_driver.forced_wait(1)
                # 龙虎---龙虎---冠军
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '1')
                break

    def longhu03(self, row):
        # 导航栏---龙虎
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
        self.base_driver.forced_wait(1)
        # 遍历龙虎---龙虎---季军
        self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '2')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGLH'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('龙虎---龙虎---季军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-龙虎---龙虎---季军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('龙虎---龙虎---季军下注异常')
                # 导航栏---龙虎
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
                self.base_driver.forced_wait(1)
                # 龙虎---龙虎---季军
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '2')
                break

    def longhu04(self, row):
        # 导航栏---龙虎
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
        self.base_driver.forced_wait(1)
        # 遍历龙虎---龙虎---第四名
        self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '3')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGLH'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('龙虎---龙虎---第四名：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-龙虎---龙虎---第四名.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('龙虎---龙虎---第四名下注异常')
                # 导航栏---龙虎
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
                self.base_driver.forced_wait(1)
                # 龙虎---龙虎---第四名
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '3')
                break

    def longhu05(self, row):
        # 导航栏---龙虎
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
        self.base_driver.forced_wait(1)
        # 遍历龙虎---龙虎---第五名
        self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '4')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGLH'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('龙虎---龙虎---第五名：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-龙虎---龙虎---第五名.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('龙虎---龙虎---第五名下注异常')
                # 导航栏---龙虎
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '龙虎')
                self.base_driver.forced_wait(1)
                # 龙虎---龙虎---第五名
                self.base_driver.clicks(self.config_dict_pk10_mm['LONGHUNUM'], '4')
                break
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------

    def wx_g(self, row):
        # 导航栏---五行
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '五行')
        self.base_driver.forced_wait(1)
        # 五行---冠军---金木水火土
        self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ3'], '0')
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ35'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('五行---冠军---金木水火土：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-五行---冠军---金木水火土.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('五行---冠军---金木水火土下注异常')
                # 导航栏---五行
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '五行')
                self.base_driver.forced_wait(1)
                # 五行---冠军---金木水火土
                self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ3'], '0')
                break

    def wx_y(self, row):
        # 导航栏---五行
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '五行')
        self.base_driver.forced_wait(1)
        # 五行---亚军---金木水火土
        self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ3'], '1')
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ35'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('五行---亚军---金木水火土：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-五行---亚军---金木水火土.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('五行---亚军---金木水火土下注异常')
                # 导航栏---五行
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '五行')
                self.base_driver.forced_wait(1)
                # 五行---亚军---金木水火土
                self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ3'], '1')
                break

    def wx_j(self, row):
        # 导航栏---五行
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '五行')
        self.base_driver.forced_wait(1)
        # 五行---季军---金木水火土
        self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ3'], '2')
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ35'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('五行---季军---金木水火土：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-五行---季军---金木水火土.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('五行---季军---金木水火土下注异常')
                # 导航栏---五行
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '五行')
                self.base_driver.forced_wait(1)
                # 五行---季军---金木水火土
                self.base_driver.clicks(self.config_dict_pk10_mm['WXGYJ3'], '0')
                break

    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------

    def dxds_dx_g(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---大小---冠军
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX_GYJ'], '0')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---大小---冠军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---大小---冠军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---大小---冠军注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---大小---冠军
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX_GYJ'], '0')
                break

    def dxds_dx_y(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---大小---亚军
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX_GYJ'], '1')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---大小---亚军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---大小---亚军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---大小---亚军注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---大小---亚军
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX_GYJ'], '1')
                break

    def dxds_dx_j(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---大小---季军
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX_GYJ'], '2')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---大小---季军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---大小---季军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---大小---季军注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---大小---季军
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DX_GYJ'], '2')
                break

    def dxds_ds_g(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---单双---冠军
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS_GYJ'], '0')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---单双---冠军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---大小---季军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---大小---季军注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---单双---冠军
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS_GYJ'], '0')
                break

    def dxds_ds_y(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---单双---亚军
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS_GYJ'], '1')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---单双---亚军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---大小---亚军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---大小---亚军注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---单双---亚军
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS_GYJ'], '1')
                break

    def dxds_ds_j(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---单双---季度军
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS_GYJ'], '2')
        for i in range(2):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---单双---季军：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---大小---季军.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---大小---季军注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---单双---季军
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_DS_GYJ'], '2')
                break

    def dxds_gjh(self, row):
        # 导航栏---大小单双
        self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
        self.base_driver.forced_wait(1)
        # 大小单双---冠军和---冠军和
        self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_GYJH'], '0')
        for i in range(4):
            try:
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_GYJH_DS'], i)
                self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
                print('大小单双---冠军和---冠军和：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-大小单双---冠军和---冠军和.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('大小单双---冠军和---冠军和注异常')
                # 导航栏---大小单双
                self.base_driver.clicks_by_text(self.config_dict_pk10_mm['MENU'], '大小单双')
                self.base_driver.forced_wait(1)
                # 大小单双---冠军和---冠军和
                self.base_driver.clicks(self.config_dict_pk10_mm['DXDS_GYJH'], '0')
                break

    def test(self):
        # 随机抽取一个点击
        el = [self.config_dict_pk10_mm['QIAN1'], self.config_dict_pk10_mm['QIAN2'], self.config_dict_pk10_mm['QIAN3']]
        n = random.choice(el)
        self.base_driver.click(n)
        self.base_driver.forced_wait(2)
        print('随机点击一个')

    def test1(self, row):
        # 循环遍历
        print('------')
        print('------')
        print('------')
        print('------')
        print('------')
        print('------')
        print(row['row'])
        print("进入row['row']")
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        for e in range(10):
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_51111'], a)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_52111'], b)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_53111'], b)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_54111'], d)
                            self.base_driver.clicks(self.config_dict_pk10_mm['DWD1_55111'], e)
                            if e == 10:
                                print("第五名break")
                                break
                        if d == 10:
                            print("第四名break")
                            break
                    if c == 10:
                        print("第四名被break")
                        break
                if b == 10:
                    print("季军被break")
                    break
            if a == 10:
                print("冠军被break")
                break
            else:
                print("循环了一次。")

        else:
            print("所以遍历了一次")

        self.base_driver.forced_wait(1)
        print('随机点击一个')

    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_pk10_mm['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(3)

    def radoms(self, row):

        # 随机5注
        self.base_driver.click(self.config_dict_pk10_mm['RANDOM5'])
        self.base_driver.forced_wait(3)
        # 随机1注2元
        self.base_driver.click(self.config_dict_pk10_mm['RANDOM1'])
        # 随机一注2角
        self.base_driver.click(self.config_dict_pk10_mm['JIAO'])
        self.base_driver.click(self.config_dict_pk10_mm['RANDOM1'])
        # 随机一注2分
        self.base_driver.click(self.config_dict_pk10_mm['FEN'])
        self.base_driver.click(self.config_dict_pk10_mm['RANDOM1'])
        # 随机20
        # self.base_driver.clear(self.config_dict_marksix['XIUGAI'])
        #
        # self.base_driver.forced_wait(20)
        s = random.choice(range(0, 1000))
        self.base_driver.type(self.config_dict_pk10_mm['XIUGAI'], "\b" + str(s))
        self.base_driver.click(self.config_dict_pk10_mm['RANDOM1'])
        # self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机1注')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        self.base_driver.forced_wait(1)
        print('随机5注')

        self.base_driver.click(self.config_dict_pk10_mm['SUREBET'])
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_pk10_mm['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        return surebet

    def get_tips(self):
        tips = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips01(self):
        # 提示请先添加投注内容
        tips = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS01'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips02(self):
        # 提示下注成功
        tips = self.base_driver.get_text(self.config_dict_pk10_mm['TIPS02'])
        print('捕捉到的信息是：' + tips)
        return tips


