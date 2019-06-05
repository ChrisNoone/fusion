# -*- coding: UTF-8 -*-
import random
import time

from common.box import BasePage, YamlHelper


class Choice11_5_Mm(BasePage):
    # 分分11选5
    config_dict_lowsp3 = YamlHelper().get_config_dict('/fusion/yaml/lottery_choice11_5_mm.yaml')['Choice11_5_Mm']

    def ch11_5_q3zhixfs(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        self.base_driver.forced_wait(2)
        # 三码-前三直选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '0')
        self.base_driver.forced_wait(2)
        # 遍历从百、十、个位各选1个号码组成一注
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == j or i == k or j == k:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], i)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], j)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], k)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百位-十位-个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                # 每个位置随机抽取一个
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        print('三码-前三直选-复式：第一位 ' + str(a0) + '第二位： ' + str(a1) + '第三位: ' + str(a2))
                # 随机一个位置两个号码。两个位置一个
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        print('三码-前三直选-复式：第一位 ' + str(a0) + '第二位： ' + str(a1)
                              + '第三位: ' + str(a2) + ' ' + str(a3))
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        print('三码-前三直选-复式：第一位 ' + str(a0) + '第二位： ' + str(a1) + ' ' + str(a2)
                              + '第三位: ' + str(a3))
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        print('三码-前三直选-复式：第一位 ' + str(a0) + str(a1) + '第二位： ' + ' ' + str(a2)
                              + '第三位: ' + str(a3))
                else:
                    pass
            except Exception as e:
                print('三码-前三直选-复式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-前三直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '0')
                break
        # # 遍历文字
        # for i in range(20):
        #     a0 = random.choice(range(0, 5))
        #     a1 = random.choice(range(0, 5))
        #     a2 = random.choice(range(0, 5))
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], a0)
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], a1)
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], a2)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

        # 百位-十位-个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(10):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], b)
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], c)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print('三码-前三直选-复式：文字第一位 ' + str(a) + '第二位： ' + str(b) + '第三位: ' + str(c))
            except Exception as e:
                print('三码-前三直选-复式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                self.base_driver.save_window_snapshot_by_io('/fusion/pictures/choice11_5/'
                                                            + '%s-三码-前三直选-复式-文字.png' % now_Time)
                # self.logger.infos('三码-直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '0')
                break

    def ch11_5_q3zhixfs_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-前三直选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '0')
        # 遍历从百、十、个位各选1个号码组成一注
        '''
        for i in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
            print('从二同号1个号码：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], i)
        for j in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], j)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
            print('从二同号1个号码：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], j)
        for k in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], k)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
            print('从二同号1个号码：  ' + ' ' + str(k) + ' ' + str(s))
            self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], k)
        '''
        # 随机抽样
        for i in range(1000):
            try:
                s0 = random.choice(range(0, 18))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                # 每个位置随机抽取
                # 第一位选一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第一位选一个：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                # 第二位选一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第二位选一个：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                # 第三位选一个
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第三位选一个：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                # 第一位，第二位各选一个
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第一位，第二位各选一个：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                # 第二位，第三位各选一个
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第二位，第三位各选一个：  ' + str(a0) + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                # 第一位，第三位各选一个
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第一位，第三位各选一个：  ' + str(a0) + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                # 三个数字，第一二相同，第三随机
                if s0 == 6:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式三个数字，第一二相同，第三随机：  ' + str(a0) + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                # 三个数字，第一三相同，第二随机
                if s0 == 7:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式三个数字，第一三相同，第二随机：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                # 三个数字，第二三相同，第一随机
                if s0 == 8:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                # 第一位取三位
                if s0 == 9:
                    if a0 == a1 or a0 == a2 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], '5')
                # 第二位取三位
                if s0 == 10:
                    if a0 == a1 or a0 == a2 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], '5')
                # 第三位取三位
                if s0 == 11:
                    if a0 == a1 or a0 == a2 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], '5')
                # 第一位取四位
                if s0 == 12:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], '5')
                # 第二位取四位
                if s0 == 13:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], '5')
                # 第三位取四位
                if s0 == 14:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], '5')
                # 第一位取五位
                if s0 == 15:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], '5')
                # 第二位取五位
                if s0 == 16:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], '5')
                # 第三位取五位
                if s0 == 17:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三直选-复式三个数字，第二三相同，第一随机：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], '5')
            except Exception as e:
                print('三码-前三直选-复式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '0')
                break
        # 遍历文字
        for i in range(20):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                a5 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第一位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第二位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], '5')
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第三位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], '5')
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第一位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], '5')
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], a2)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], a3)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第二位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX2WZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], '5')
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], a4)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], a5)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三直选-复式第三位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX1WZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX3WZ'], '5')
            except Exception as e:
                print('三码-前三直选-复式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '0')
                break
    def ch11_5_q3zhixds(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-前三直选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '1')
        self.base_driver.forced_wait(1)
        # 0-11中，手动输入3个互不相同的号码组成一注
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                if d1 == d2 or d1 == d3 or d2 == d3:
                    # print('三码-前三直选-单式输入号码最少两个相同的组合:-' + str(d1) + ' ' + str(d2) + ' ' + str(d3))
                    pass
                else:
                    print("三码-前三直选-单式输入的号码是：" + str(d1) + ' ' + str(d2) + ' ' + str(d3))
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2 + ' ' + d3)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print('三码-前三直选-单式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三直选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-直选-单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三直选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '1')
                break

    def ch11_5_q3zhixds_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-直选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '1')
        self.base_driver.forced_wait(1)
        # 0-11中，手动输入3个互不相同的号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                s1 = random.choice(range(0, 100))
                a1 = random.choice(range(1, 12))
                a2 = random.choice(range(1, 12))
                a3 = random.choice(range(1, 12))
                a4 = random.choice(range(12, 100))
                a5 = random.choice(range(12, 100))
                a6 = random.choice(range(12, 100))
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                # 在1-11中
                # 输入1个两位数字以下的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-直选-单式号码：  ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-直选-单式号码：  ' + str(d1) + ' ' + str(d2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意相等的三个号码
                if s0 == 2:
                    if d1 == d2 or d1 == d3 or d2 == d3:
                        # print("输入的号码(最少两个相同)是：" + str(d1) + ' ' + str(d2) + ' ' + str(d3))
                        self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2 + ' ' + d3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-直选-单式号码：  ' + str(d1) + ' ' + str(d2) + ' ' + str(d3) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
                # 输入任意大于12的一个号码
                if s0 == 3:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-直选-单式号码：  ' + ' ' + str(d4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的两个号码
                if s0 == 4:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print("三码-直选-单式号码：" + str(d4) + ' ' + str(d5) + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的三个号码
                if s0 == 5:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5 + ' ' + d6)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print("三码-直选-单式号码：" + str(d4) + ' ' + str(d5) + ' ' + str(d6) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print('三码-前三直选-单式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三直选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-直选-单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三直选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZHIX'], '1')
                break

    def ch11_5_q3zuxfs(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-前三组选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '0')
        # 随机从0-9中任选3个号码组成一注
        for i in range(100):
            try:
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                c = random.choice(range(0, 11))
                if a == b or a == c or b == c:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], b)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], c)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('三码-前三组选-复式:' + str(a) + str(b) + str(c))
            except Exception as e:
                print('三码-前三组选-复式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三组选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-直选-单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三组选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '0')
                break

        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print('三码-前三组选-复式' + str(e))
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三组选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-前三组选-单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三组选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '0')
                # 随机从0-9中任选3个号码组成一注
                break

    def ch11_5_q3zuxfs_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-前三组选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '0')
        # 随机从0-9中任选3个号码组成一注
        for i in range(30):
            try:
                s = random.choice(range(0, 2))
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                # 选择一个号码
                if s == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三组选-复式--选择一个号码：  ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                # 选择两个号码
                if s == 1:
                    if a == b:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], b)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三组选-复式--选择一个号码：  ' + str(a) + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], b)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三组选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-前三组选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三组选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '0')
                break

    def ch11_5_q3zuxds(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-前三组选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                if d1 == d2 or d1 == d3 or d2 == d3:
                    # print('输入号码最少两个相同的组合:-' + str(d1) + ' ' + str(d2) + ' ' + str(d3))
                    pass
                else:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZUXSTEXT'], d1 + ' ' + d2 + ' ' + d3)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print("三码-前三组选-单式输入的号码是：" + str(d1) + ' ' + str(d2) + ' ' + str(d3))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三组选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-前三组选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三组选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '1')
                break

    def ch11_5_q3zuxds_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码-前三组选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                s1 = random.choice(range(0, 100))
                a1 = random.choice(range(1, 12))
                a2 = random.choice(range(1, 12))
                a3 = random.choice(range(1, 12))
                a4 = random.choice(range(12, 100))
                a5 = random.choice(range(12, 100))
                a6 = random.choice(range(12, 100))
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                # 在1-11中
                # 输入1个两位数字以下的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三组选-单式号码： ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三组选-单式号码：  ' + str(d1) + ' ' + str(d2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意相等的三个号码
                if s0 == 2:
                    if d1 == d2 or d1 == d3 or d2 == d3:
                        ss = str(d1) + ' ' + str(d2) + ' ' + str(d3)
                        self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2 + ' ' + d3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('三码-前三组选-单式输入的号码(最少两个相同)是："：  ' + ss + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
                # 输入任意大于12的一个号码
                if s0 == 3:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三组选-单式：  ' + str(d4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的两个号码
                if s0 == 4:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三组选-单式：  ' + str(d4) + ' ' + str(d5) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的三个号码
                if s0 == 5:
                    ss = str(d4) + ' ' + str(d5) + ' ' + str(d6)
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5 + ' ' + d6)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码-前三组选-单式：  ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三码-前三组选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码-前三组选-单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码-前三组选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX'], '1')
                # 手动输入1个三位数号码组成一注
                break
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------

    def ch11_5_q2zhixfs(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二直选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
        # 从第一位、第二位各选1个不同号码组成一注
        # for i in range(11):
        #     for j in range(11):
        #         if i == j:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], i)
        #             self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], j)
        #             self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

        # 从第一位、第二位随机抽取一个互不相同的数字,抽取100次
        for i in range(100):
            try:
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('二码-前二直选-复式： ' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
                break
        # # 遍历文字
        # for i in range(5):
        #     for j in range(5):
        #         self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1WZ'], i)
        #         self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2WZ'], j)
        #         self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

        # 随机文字
        for i in range(10):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1WZ'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2WZ'], b)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
                break

    def ch11_5_q2zhixfs_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二直选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
        # 从第一位、第二位随机抽取一个互不相同的数字,抽取100次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 9))
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                c = random.choice(range(0, 11))
                d = random.choice(range(0, 11))
                # 第一位数字取一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-前二直选-复式第一位数字取一个：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                # 第二位数字取一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-前二直选-复式第二位数字取一个：  ' + ' ' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                # 第一、二位相同的数字
                if s0 == 2:
                    if a == b:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                    else:
                        pass
                # 第一位取两位
                if s0 == 3:
                    if a == b:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], b)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], b)
                # 第二位取两位
                if s0 == 4:
                    if a == b:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                # 第一位取三位
                if s0 == 5:
                    if a == b or a == c or b == c:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], c)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], c)
                # 第二位取三位
                if s0 == 6:
                    if a == b or a == c or b == c:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], c)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], c)
                # 第一位取四位
                if s0 == 7:
                    if a == b or a == c or a == d or b == c or b == d or c == d:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], c)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], d)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], c)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1'], d)
                # 第二位取四位
                if s0 == 8:
                    if a == b or a == c or a == d or b == c or b == d or c == d:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], c)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], d)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-前二直选-复式第一、二位相同的数字：  ' + ' ' + str(b) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], b)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], c)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2'], d)
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
                break

        # 遍历文字
        for m in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1WZ'], m)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('遍历第一位文字：  ' + ' ' + str(m) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1WZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
                break

        for n in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX2WZ'], n)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('遍历第二位文字：  ' + ' ' + str(n) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX1WZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二直选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '0')
                break

    def ch11_5_q2zhixds(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二直选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                if d1 == d2:
                    # print('输入号码最少两个相同的组合:---' + str(d1) + ' ' + str(d2))
                    pass
                else:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ2ZHIXSTEXT'], d1 + ' ' + d2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print("二码-前二直选-单式输入的号码是：" + str(d1) + ' ' + str(d2))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前we直选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '1')
                break

    def ch11_5_q2zhixds_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二直选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                s1 = random.choice(range(0, 10000))
                s2 = random.choice(range(0, 10000))
                a1 = random.choice(range(1, 12))
                a2 = random.choice(range(1, 12))
                a4 = random.choice(range(12, 100))
                a5 = random.choice(range(12, 100))
                a6 = random.choice(range(12, 100))
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % s2
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                # 在1-11中
                # 输入1个的号码--五位以下
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-前二直选-单式第一位文字：  ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个号码。最少1个号码大于11
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d3 + ' ' + d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-前二直选-单式输入两个号码,最少1个号码大于11：  ' + str(d3) + ' ' + str(d4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意相等的三个号码
                if s0 == 2:
                    if d1 == d2:
                        self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print("二码-前二直选-单式输入的号码(最少两个相同)是：" + str(d1) + ' ' + str(d2) + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
                # 输入任意大于12的一个号码
                if s0 == 3:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-前二直选-单式：  ' + str(d4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的两个号码
                if s0 == 4:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print("二码-前二直选-单式输入的号码是：" + str(d4) + ' ' + str(d5) + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的三个号码
                if s0 == 5:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5 + ' ' + d6)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print("二码-前二直选-单式输入的号码：" + str(d4) + ' ' + str(d5) + ' ' + str(d6) + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二直选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二直选-单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二直选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZHIX'], '1')
                break

    def ch11_5_q2zuxfs(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二组选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '0')
        # 随机从1-11中任选2个号码组成一注
        for i in range(100):
            try:
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                if a == b:
                    pass
                else:
                    print('二码-前二组选-复式' + str(a) + str(b))
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX1'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX1'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二组选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二组选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二组选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '0')
                # 随机从1-11中任选2个号码组成一注
                break

        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX1WZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二组选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-前二组选-复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二组选-复式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '0')
                # 随机从1-11中任选2个号码组成一注
                break

    def ch11_5_q2zuxfs_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二组选-复式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '0')
        # 随机从1-11中选1个号码
        for i in range(11):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX1'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('二码-前二组选-复式从1-11中任选1个号码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX1'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二组选-复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-组选-组6
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '0')
                break

    def ch11_5_q2zuxds(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-前二组选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '1')
        # 1-11手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                if d1 == d2:
                    # print('输入号码最少两个相同的组合:---' + str(d1) + ' ' + str(d2))
                    pass
                else:
                    print("二码-前二组选-单式输入的号码是：" + str(d1) + ' ' + str(d2))
                    self.base_driver.type(self.config_dict_lowsp3['CHQ2ZUXSTEXT'], d1 + ' ' + d2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二码-前二组选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-直选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '1')
                break

    def ch11_5_q2zuxds_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码-直选-单式
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '1')
        for i in range(1000):
            try:
                s0 = random.choice(range(0, 6))
                s1 = random.choice(range(0, 10000))
                s2 = random.choice(range(0, 10000))
                a1 = random.choice(range(1, 12))
                a2 = random.choice(range(1, 12))
                a4 = random.choice(range(12, 100))
                a5 = random.choice(range(12, 100))
                a6 = random.choice(range(12, 100))
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % s2
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                # 在1-11中
                # 输入1个的号码--五位以下
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-直选-单式：  ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个号码。最少1个号码大于11
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d3 + ' ' + d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-直选-单式输入两个号码,最少1个号码大于11：  ' + ' ' + str(d4) + ' ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意相等的两个号码
                if s0 == 2:
                    if d1 == d2:
                        self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d1 + ' ' + d2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('二码-直选-单式输入的号码(最少两个相同)是：' + str(d1) + ' ' + str(d2) + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
                # 输入任意大于12的一个号码
                if s0 == 3:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-直选-单式：  ' + str(d4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的两个号码
                if s0 == 4:
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('二码-直选-单式：  ' + str(d4) + ' ' + str(d5) + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入任意大于12的三个号码
                if s0 == 5:
                    print("输入的号码是：" + str(d4) + ' ' + str(d5) + ' ' + str(d6))
                    self.base_driver.type(self.config_dict_lowsp3['CHQ3ZHIXSTEXT'], d4 + ' ' + d5 + ' ' + d6)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('第一位文字：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-二二码-前二组选-单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码-前二组选-单式
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ2ZUX'], '1')
                break
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------

    def ch11_5_bddan(self, row):
        # 不定胆
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '不定胆')
        # 不定胆-前三位
        # self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
        # 随机从0-11中任选1个号码组成一注
        for i in range(100):
            try:
                a = random.choice(range(0, 11))
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-不定胆-前三位.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 不定胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '不定胆')
                # 不定胆-前三位
                # self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break
        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-不定胆-前三位.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 不定胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '不定胆')
                # 不定胆-前三位
                # self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')

    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------
    def ch11_5_dwd(self, row):
        # 定位胆
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '定位胆')
        # 定位胆
        '''
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
        # 任选1个位置并选1个号码组成一注
        # 第一位
        for i in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHDWD1'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # 第二位
        for i in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHDWD2'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # 第三位
        for i in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHDWD3'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # 第四位
        for i in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHDWD4'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # 第五位
        for i in range(11):
            self.base_driver.clicks(self.config_dict_lowsp3['CHDWD5'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                x = random.choice(range(0, 5))
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                c = random.choice(range(0, 11))
                d = random.choice(range(0, 11))
                e = random.choice(range(0, 11))
                if x == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD1'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if x == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD2'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if x == 2:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD3'], c)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if x == 3:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD4'], d)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD5'], e)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-定位胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 定位胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '定位胆')
                break
        '''      
        # 遍历文字
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHDWD1WZ'], i)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHDWD2WZ'], i)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHDWD3WZ'], i)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHDWD4WZ'], i)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHDWD5WZ'], i)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        for i in range(20):
            try:
                x = random.choice(range(0, 5))
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                e = random.choice(range(0, 5))
                if x == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD1WZ'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if x == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD2WZ'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if x == 2:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD3WZ'], c)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if x == 3:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD4WZ'], d)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHDWD5WZ'], e)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-定位胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码-组选-组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 定位胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '定位胆')
                break

    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------

    def ch11_5_rxfs_1z1(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-一中一
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '0')
        # 随机从0-11中任选1个号码组成一注
        for i in range(10):
            try:
                a = random.choice(range(0, 11))
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-一中一.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-一中一下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-一中一
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '0')
                break
        # for i in range(11):
        #     self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], i)
        #     self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def ch11_5_rxfs_2z2(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-二中二
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '1')
        # 随机从0-11中任选2个号码组成一注
        for i in range(11):
            try:
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-二中二.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-二中二下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-二中二
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '1')
                break

        # 遍历数字组合
        for i in range(11):
            for j in range(11):
                try:
                    if i >= j:
                        pass
                    else:
                        print('组合是: ' + str(i) + str(j))
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], i)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], j)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-二中二.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(ss)
                    # self.logger.infos('任选-任选复式-二中二下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(3)
                    # 任选
                    self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                    # 任选-任选复式-二中二
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '1')
                    break
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def ch11_5_rxfs_2z2_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-二中二
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '1')
        # 随机从0-11中任选1个号码组成一注
        for i in range(11):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-二中二.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-二中二下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-二中二
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '1')

    def ch11_5_rxfs_3z3(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-三中三
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '2')
        # 随机从0-11中任选3个号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                # 随机三个号码
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机四个号码
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机五个号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机六个号码
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-三中三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-三中三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '2')
                break
        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-三中三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-三中三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '2')
                break

    def ch11_5_rxfs_3z3_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-三中三
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '2')
        # 随机从0-11中任选3个号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 2))
                a = random.choice(range(0, 11))
                b = random.choice(range(0, 11))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                else:
                    if a == b:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], b)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-三中三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-三中三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '2')
                break

    def ch11_5_rxfs_4z4(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-四中四
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '3')
        # 随机从0-11中任选四个号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                a6 = random.choice(range(0, 11))
                a7 = random.choice(range(0, 11))
                # 随机四个号码
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机五个号码
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机六个号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机七个号码
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                            or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机八个号码
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                            or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                            or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                            or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a7)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-四中四.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-四中四
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '3')
        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-四中四.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-四中四
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '3')

    def ch11_5_rxfs_4z4_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-四中四
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '3')
        # 随机从0-11中任选3个号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                # 选择一个号码
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 选择两个号码
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 选择三个号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-四中四.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-四中四
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '3')

    def ch11_5_rxfs_5z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-五中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '4')
        # 随机从0-11中任选5个号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                a6 = random.choice(range(0, 11))
                a7 = random.choice(range(0, 11))

                # 随机五个号码
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机六个号码
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机七个号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                            or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机八个号码
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                            or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                            or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                            or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a7)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-五中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '4')
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def ch11_5_rxfs_5z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-五中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '4')
        # 随机从0-11中任选5个号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                # 随机一个数字
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机二个数字
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选2个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机三个数字
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选3个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机四个数字
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-五中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '4')
                break

    def ch11_5_rxfs_6z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-六中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '5')
        # 随机从0-11中任选6个号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 3))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                a6 = random.choice(range(0, 11))
                a7 = random.choice(range(0, 11))
                # 随机六个号码
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机七个号码
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                            or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机八个号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                            or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                            or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                            or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a7)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-六中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-六中五注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '4')
                break
        # 遍历文字
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '0')
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '2')
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '3')
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def ch11_5_rxfs_6z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-六中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '5')
        # 随机从0-11中任选5个号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 7))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                # 随机一个数字
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机二个数字
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选2个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机三个数字
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选3个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机四个数字
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机五个数字
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 文字大不能下注
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '1')
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 文字双不能下注
                if s0 == 6:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '4')
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-六中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-六中五注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '5')
                break

    def ch11_5_rxfs_7z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-七中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '6')
        # 随机从0-11中任选七个号码组成一注
        for i in range(500):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                a6 = random.choice(range(0, 11))
                a7 = random.choice(range(0, 11))
                # print(s0,a0,a1,a2,a3,a4,a5,a6,a7)
                # 随机七个号码
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                            or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6:
                        pass
                    else:
                        print(s0, a0, a1, a2, a3, a4, a5, a6, a7)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                # 随机八个号码
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                            or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                            or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                            or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a7)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-七中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-六中五注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '6')
                break
        # # 遍历文字
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '0')
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def ch11_5_rxfs_7z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-七中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '6')
        # 随机从0-11中任选六个号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 7))
                s1 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                # 随机一个数字
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机二个数字
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选2个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机三个数字
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选3个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机四个数字
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机五个数字
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机六个数字
                if s0 == 5:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 文字不能下注
                if s0 == 6:
                    # 文字大不能下注
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '1')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                    # 文字小不能下注
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '2')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                    # 文字单不能下注
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '3')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                    # 文字双不能下注
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '4')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-七中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-六中五注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '6')
                break

    def ch11_5_rxfs_8z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-八中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '7')
        # 随机从0-11中任选七个号码组成一注
        for i in range(300):
            try:
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                a6 = random.choice(range(0, 11))
                a7 = random.choice(range(0, 11))
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 \
                        or a3 == a6 or a3 == a7 or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 \
                        or a6 == a7:
                    # print('失败的是:' + str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' '
                    #       + str(a4) + ' ' + str(a5)+ ' ' + str(a6))
                    pass
                else:
                    print('号码是:' + str(a0) + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(a3) + ' '
                          + str(a4) + ' ' + str(a5) + ' ' + str(a6))
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a7)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-八中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-八中五注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '7')
                break
        # 遍历文字
        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '0')
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def ch11_5_rxfs_8z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选复式-八中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '7')
        # 随机从0-11中任选七个号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 7))
                s1 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 11))
                a2 = random.choice(range(0, 11))
                a3 = random.choice(range(0, 11))
                a4 = random.choice(range(0, 11))
                a5 = random.choice(range(0, 11))
                a6 = random.choice(range(0, 11))
                # 随机一个数字
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机二个数字
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选2个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机三个数字
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选3个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机四个数字
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机五个数字
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机六个数字
                if s0 == 5:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 随机七个数字
                if s0 == 6:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                            or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1'], a6)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                # 文字不能下注
                if s0 == 7:
                    # 文字大不能下注
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '1')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                    # 文字小不能下注
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '2')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                    # 文字单不能下注
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '3')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                    # 文字双不能下注
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_lowsp3['CHQ3ZUX1WZ'], '4')
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['CHRXFXWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选复式-八中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选复式-八中五注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选复式-五中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXFS'], '7')
                break
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------
    # ---------------------------------------

    def ch11_5_rxds_1z1(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-一中一
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '0')
        # 随机输入1个1-11中的号码
        for i in range(20):
            try:
                a1 = random.choice(range(1, 12))
                d1 = "%02d" % a1
                print("输入的号码是：" + str(d1))
                self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], d1)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-一中一.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-一中一注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-一中一
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '0')
                break

    def ch11_5_rxds_1z1_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-一中一
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '0')
        # 随机输入1个1-11中的号码
        for i in range(50):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                # 输入一位数字
                if s0 == 0:
                    print("输入的号码是：" + str(a1))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                else:
                    print("输入的号码是：" + str(a2))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-一中一.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-一中一注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-一中一
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '0')
                break

    def ch11_5_rxds_2z2(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-二中二
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '1')
        # 随机输入2个1-11中的号码
        for i in range(30):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                if d1 == d2:
                    print('输入号码最少两个相同的组合:---' + str(d1) + ' ' + str(d2))
                    pass
                else:
                    print("输入的号码是：" + str(d1))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], d1 + ' ' + d2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-二中二.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-一中一注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-二中二
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '1')
                break

    def ch11_5_rxds_2z2_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-二中二
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '1')
        # 随机输入2个1-11中的号码
        for i in range(50):
            try:
                s0 = random.choice(range(0, 4))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(1, 12))
                a5 = random.choice(range(1, 12))
                d1 = "%02d" % a4
                d2 = "%02d" % a5
                # 输入一位数字
                if s0 == 0:
                    print("输入的号码是：" + str(a1))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    print("输入的号码是：" + str(a2))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    print("输入的号码是：" + str(a2))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], str(a2) + ' ' + str(a3))
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 在0-11中输入两个相同的数字
                if s0 == 3:
                    if d1 == d2:
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], d1 + ' ' + d2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-二中二.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-一中一注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-二中二
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '1')
                break

    def ch11_5_rxds_3z3(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-三中三
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '2')
        # 随机输入3个1-11中的号码
        for i in range(20):
            try:
                a1 = random.choice(range(1, 12))
                a2 = random.choice(range(1, 12))
                a3 = random.choice(range(1, 12))
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                if d1 == d2 or d1 == d3 or d2 == d3:
                    #print('输入号码最少两个相同的组合:---' + str(d1) + '|' + str(d2) + '|' + str(d3))
                    pass
                else:
                    print("输入的号码是：" + str(d1))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], d1 + ' ' + d2 + ' ' + d3)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-三中三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-三中三注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '2')
                break

    def ch11_5_rxds_3z3_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-三中三
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '2')
        # 随机输入3个1-11中的号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(0, 100000))
                b4 = random.choice(range(1, 12))
                b5 = random.choice(range(1, 12))
                b6 = random.choice(range(1, 12))
                d1 = "%02d" % b4
                d2 = "%02d" % b5
                d3 = "%02d" % b6
                # 输入一位数字
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选1个号码组成一注：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    ss = str(a2) + ' ' + str(a3)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入三数字，其中一个大于11，其他随机
                if s0 == 3:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 在0-11中输入最少两个相同的数字,
                if s0 == 4:
                    if d1 == d2 or d1 == d3 or d2 == d3:
                        ss = str(d1) + ' ' + str(d2) + ' ' + str(d3)
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-三中三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-三中三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '2')
                break

    def ch11_5_rxds_4z4(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-四中四
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '3')
        # 随机输入4个1-11中的号码
        for i in range(50):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                a4 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                if d1 == d2 or d1 == d3 or d1 == d4 or d2 == d3 or d2 == d4 or d3 == d4:
                   # print('输入号码最少两个相同的组合:---' + str(d1) + '|' + str(d2) + '|' + str(d3) + '|' + str(d4))
                    pass
                else:
                    print("输入的号码是：" + str(d1))
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], d1 + ' ' + d2 + ' ' + d3 + ' ' + d4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-四中四.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '3')
                break

    def ch11_5_rxds_4z4_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-四中四
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '3')
        # 随机输入4个1-11中的号码
        for i in range(520):
            try:
                s0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(0, 100000))
                a5 = random.choice(range(0, 100000))
                b1 = random.choice(range(1, 12))
                b2 = random.choice(range(1, 12))
                b3 = random.choice(range(1, 12))
                b4 = random.choice(range(1, 12))
                d1 = "%02d" % b1
                d2 = "%02d" % b2
                d3 = "%02d" % b3
                d4 = "%02d" % b4
                # 输入一位数字
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    ss = str(a2) + ' ' + str(a3)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入三数字，其中一个大于11，其他随机
                if s0 == 3:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入四数字，其中一个大于11，其他随机
                if s0 == 4:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 在0-11中输入最少两个相同的数字,
                if s0 == 5:
                    if d1 == d2 or d1 == d3 or d1 == d4 or d2 == d3 or d2 == d4 or d3 == d4:
                        ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-四中四.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-四中四下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-四中四
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '3')
                break

    def ch11_5_rxds_5z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-五中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '4')
        # 随机输入5个1-11中的号码
        for i in range(50):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                a4 = random.choice(x)
                a5 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d2 == d3 or d2 == d4 or d2 == d5 or d3 == d4 \
                        or d3 == d5 or d4 == d5:

                    pass
                else:
                    ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('输入号码最少两个相同的组合:-' + str(ss))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-五中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-五中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '4')
                break

    def ch11_5_rxds_5z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-五中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '4')
        # 随机输入5个1-11中的号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 7))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(0, 100000))
                a5 = random.choice(range(0, 100000))
                a6 = random.choice(range(0, 100000))
                b1 = random.choice(range(1, 12))
                b2 = random.choice(range(1, 12))
                b3 = random.choice(range(1, 12))
                b4 = random.choice(range(1, 12))
                b5 = random.choice(range(1, 12))
                d1 = "%02d" % b1
                d2 = "%02d" % b2
                d3 = "%02d" % b3
                d4 = "%02d" % b4
                d5 = "%02d" % b5
                # 输入一位数字
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    ss = str(a2) + ' ' + str(a3)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入三数字，其中一个大于11，其他随机
                if s0 == 3:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入四数字，其中一个大于11，其他随机
                if s0 == 4:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入五数字，其中一个大于11，其他随机
                if s0 == 5:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 在0-11中输入最少两个相同的数字,
                if s0 == 6:
                    if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d2 == d3 or d2 == d4 or d2 == d5 \
                            or d3 == d4 or d3 == d5 or d4 == d5:
                        ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-五中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-五中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-三中三
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '4')
                break

    def ch11_5_rxds_6z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-六中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '5')
        # 随机输入6个1-11中的号码
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                a4 = random.choice(x)
                a5 = random.choice(x)
                a6 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 or d2 == d3 or d2 == d4 or d2 == d5 \
                        or d2 == d6 or d3 == d4 or d3 == d5 or d3 == d6 or d4 == d5 or d4 == d6 or d5 == d6:
                    pass
                else:
                    ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5 + ' ' + d6
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-六中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-六中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-六中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '5')
                break

    def ch11_5_rxds_6z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-六中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '5')
        # 随机输入6个1-11中的号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 8))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(0, 100000))
                a5 = random.choice(range(0, 100000))
                a6 = random.choice(range(0, 100000))
                a7 = random.choice(range(0, 100000))
                b1 = random.choice(range(1, 12))
                b2 = random.choice(range(1, 12))
                b3 = random.choice(range(1, 12))
                b4 = random.choice(range(1, 12))
                b5 = random.choice(range(1, 12))
                b6 = random.choice(range(1, 12))
                d1 = "%02d" % b1
                d2 = "%02d" % b2
                d3 = "%02d" % b3
                d4 = "%02d" % b4
                d5 = "%02d" % b5
                d6 = "%02d" % b6
                # 输入一位数字
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注： ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注： ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    ss = str(a2) + ' ' + str(a3)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入三数字，其中一个大于11，其他随机
                if s0 == 3:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入四数字，其中一个大于11，其他随机
                if s0 == 4:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入五数字，其中一个大于11，其他随机
                if s0 == 5:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入六数字，其中一个大于11，其他随机
                if s0 == 6:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6) + ' ' + str(a7)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                #  六个数字中，在0-11中输入最少两个相同的数字,
                if s0 == 7:
                    if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 or d2 == d3 or d2 == d4 or d2 == d5 \
                            or d2 == d6 or d3 == d4 or d3 == d5 or d4 == d5 or d4 == d6 or d5 == d6:
                        ss = str(d1) + ' ' + str(d2) + ' ' + str(d3) + ' ' + str(d4) + ' ' + str(d5) + ' ' + str(d6)
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-六中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-六中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-六中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '5')
                break

    def ch11_5_rxds_7z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-七中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '6')
        # 随机输入7个1-11中的号码
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                a4 = random.choice(x)
                a5 = random.choice(x)
                a6 = random.choice(x)
                a7 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                d7 = "%02d" % a7
                if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 or d1 == d7 or d2 == d3 or d2 == d4 \
                        or d2 == d5 or d2 == d6 or d2 == d7 or d3 == d4 or d3 == d5 or d3 == d6 or d3 == d7 \
                        or d4 == d5 or d4 == d6 or d4 == d7 or d5 == d6 or d5 == d7 or d6 == d7:

                    pass
                else:
                    ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5 + ' ' + d6 + ' ' + d7
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('最少两个相同的组合:' + str(ss))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-七中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-七中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-七中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '6')
                break

    def ch11_5_rxds_7z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-七中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '6')
        # 随机输入7个1-11中的号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 9))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(0, 100000))
                a5 = random.choice(range(0, 100000))
                a6 = random.choice(range(0, 100000))
                a7 = random.choice(range(0, 100000))
                a8 = random.choice(range(0, 100000))
                b1 = random.choice(range(1, 12))
                b2 = random.choice(range(1, 12))
                b3 = random.choice(range(1, 12))
                b4 = random.choice(range(1, 12))
                b5 = random.choice(range(1, 12))
                b6 = random.choice(range(1, 12))
                b7 = random.choice(range(1, 12))
                d1 = "%02d" % b1
                d2 = "%02d" % b2
                d3 = "%02d" % b3
                d4 = "%02d" % b4
                d5 = "%02d" % b5
                d6 = "%02d" % b6
                d7 = "%02d" % b7
                # 输入一位数字
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    ss = str(a2) + ' ' + str(a3)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入三数字，其中一个大于11，其他随机
                if s0 == 3:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入四数字，其中一个大于11，其他随机
                if s0 == 4:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入五数字，其中一个大于11，其他随机
                if s0 == 5:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入六数字，其中一个大于11，其他随机
                if s0 == 6:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6) + ' ' + str(a7)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入七数字，其中一个大于11，其他随机
                if s0 == 7:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6) + ' ' + str(a7) + ' ' + str(a8)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                #  七个数字中，在0-11中输入最少两个相同的数字,
                if s0 == 8:
                    if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 or d1 == d7 or d2 == d3 or d2 == d4 \
                            or d2 == d5 or d2 == d6 or d2 == d7 or d3 == d4 or d3 == d5 or d3 == d6 or d3 == d7 \
                            or d4 == d5 or d4 == d6 or d4 == d7 or d5 == d7 or d6 == d7:
                        ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5 + ' ' + d6 + ' ' + d7
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], )
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-七中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-七中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-七中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '6')
                break

    def ch11_5_rxds_8z5(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-八中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '7')
        # 随机输入7个1-11中的号码
        for i in range(100):
            try:
                x = range(1, 12)
                a1 = random.choice(x)
                a2 = random.choice(x)
                a3 = random.choice(x)
                a4 = random.choice(x)
                a5 = random.choice(x)
                a6 = random.choice(x)
                a7 = random.choice(x)
                a8 = random.choice(x)
                d1 = "%02d" % a1
                d2 = "%02d" % a2
                d3 = "%02d" % a3
                d4 = "%02d" % a4
                d5 = "%02d" % a5
                d6 = "%02d" % a6
                d7 = "%02d" % a7
                d8 = "%02d" % a8
                if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 or d1 == d7 or d1 == d8 or d2 == d3 \
                        or d2 == d4 or d2 == d5 or d2 == d6 or d2 == d7 or d2 == d8 or d3 == d4 or d3 == d5 \
                        or d3 == d6 or d3 == d7 or d3 == d8 or d4 == d5 or d4 == d6 or d4 == d7 or d4 == d8 \
                        or d5 == d6 or d5 == d7 or d5 == d8 or d6 == d7 or d6 == d8 or d7 == d8:
                    pass
                else:
                    print("输入的号码是：" + str(d1) + '|' + str(d2) + '|' + str(d3) + '|' + str(d4) + '|' + str(d5)
                          + '|' + str(d6) + '|' + str(d7) + '|' + str(d8))
                    dn = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5 + ' ' + d6 + ' ' + d7 + ' ' + d8
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], dn)
                    self.base_driver.forced_wait(4)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-八中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-八中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-八中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '7')
                break

    def ch11_5_rxds_8z5_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
        # 任选-任选单式-七中五
        self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '7')
        # 随机输入7个1-11中的号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(12, 100000))
                a3 = random.choice(range(0, 100000))
                a4 = random.choice(range(0, 100000))
                a5 = random.choice(range(0, 100000))
                a6 = random.choice(range(0, 100000))
                a7 = random.choice(range(0, 100000))
                a8 = random.choice(range(0, 100000))
                b1 = random.choice(range(1, 12))
                b2 = random.choice(range(1, 12))
                b3 = random.choice(range(1, 12))
                b4 = random.choice(range(1, 12))
                b5 = random.choice(range(1, 12))
                b6 = random.choice(range(1, 12))
                b7 = random.choice(range(1, 12))
                b8 = random.choice(range(1, 12))
                d1 = "%02d" % b1
                d2 = "%02d" % b2
                d3 = "%02d" % b3
                d4 = "%02d" % b4
                d5 = "%02d" % b5
                d6 = "%02d" % b6
                d7 = "%02d" % b7
                d8 = "%02d" % b8
                # 输入一位数字
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入1个大于11的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，其中一个大于11，其他随机
                if s0 == 2:
                    ss = str(a2) + ' ' + str(a3)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入三数字，其中一个大于11，其他随机
                if s0 == 3:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入四数字，其中一个大于11，其他随机
                if s0 == 4:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入五数字，其中一个大于11，其他随机
                if s0 == 5:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入六数字，其中一个大于11，其他随机
                if s0 == 6:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' + str(a6) + ' ' + str(a7)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入七数字，其中一个大于11，其他随机
                if s0 == 7:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' \
                         + str(a6) + ' ' + str(a7) + ' ' + str(a8)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入八数字，其中一个大于11，其他随机
                if s0 == 8:
                    ss = str(a2) + ' ' + str(a3) + ' ' + str(a4) + ' ' + str(a5) + ' ' \
                         + str(a6) + ' ' + str(a7) + ' ' + str(a8)
                    self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                #  八个数字中，在0-11中输入最少两个相同的数字,
                if s0 == 9:
                    if d1 == d2 or d1 == d3 or d1 == d4 or d1 == d5 or d1 == d6 or d1 == d7 or d1 == d8 or d2 == d3 \
                            or d2 == d4 or d2 == d5 or d2 == d6 or d2 == d7 or d2 == d8 or d3 == d4 or d3 == d5 \
                            or d3 == d6 or d3 == d7 or d3 == d8 or d4 == d5 or d4 == d6 or d4 == d7 \
                            or d4 == d8 or d5 == d7 or d5 == d8 or d6 == d7 or d6 == d8 or d7 == d8:
                        ss = d1 + ' ' + d2 + ' ' + d3 + ' ' + d4 + ' ' + d5 + ' ' \
                             + d6 + ' ' + d7 + ' ' + d8
                        self.base_driver.type(self.config_dict_lowsp3['CHRXDANSTEXT'], ss)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('随机从0-11中任选4个号码组成一注：  ' + ' ' + str(ss) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-任选-任选单式-八中五.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('任选-任选单式-八中五下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(3)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '任选')
                # 任选-任选单式-八中五
                self.base_driver.clicks(self.config_dict_lowsp3['CHRXDANS'], '7')

    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(3)

    def radoms(self, row):

        # 随机5注
        self.base_driver.click(self.config_dict_lowsp3['RANDOM5'])
        self.base_driver.forced_wait(3)
        # 随机1注2元
        self.base_driver.click(self.config_dict_lowsp3['RANDOM1'])
        # 随机一注2角
        self.base_driver.click(self.config_dict_lowsp3['JIAO'])
        self.base_driver.click(self.config_dict_lowsp3['RANDOM1'])
        # 随机一注2分
        self.base_driver.click(self.config_dict_lowsp3['FEN'])
        self.base_driver.click(self.config_dict_lowsp3['RANDOM1'])
        # 随机20
        s = random.choice(range(0, 1000))
        self.base_driver.type(self.config_dict_lowsp3['XIUGAI'], "\b" + str(s))
        self.base_driver.click(self.config_dict_lowsp3['RANDOM1'])
        #self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])

        print('随机5注')

        self.base_driver.click(self.config_dict_lowsp3['SUREBET'])
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_lowsp3['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        return surebet

    def get_tips(self):
        tips = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips01(self):
        # 提示请先添加投注内容
        tips = self.base_driver.get_text(self.config_dict_lowsp3['TIPS01'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips02(self):
        # 提示下注成功
        tips1 = self.base_driver.get_text(self.config_dict_lowsp3['TIPS02'])
        print('捕捉到的信息是：' + tips1)
        return tips1
