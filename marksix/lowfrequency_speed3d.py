import random
import time

from common.box import BasePage, YamlHelper


class LowfSpeed3D(BasePage):
   # 低频彩---极速3D
    config_dict_lowsp3 = YamlHelper().get_config_dict('/fusion/yaml/lottery_lowfre_speed3d.yaml')['Speed3D']

    def sp3_3_zhxfs(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---直选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
        # 遍历数字从百、十、个位各选1个号码组成一注
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], j)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], k)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百位---十位---个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], b)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], c)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print('三码---直选---复式百十个：' + str(a) + ' ' + str(b) + ' ' + str(c))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break
        # 遍历文字
        for i in range(10):
            try:
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], a0)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], a1)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], a2)
                print('三码---直选---复式文字百十个：' + str(a0) + ' ' + str(a1) + ' ' + str(a2))
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break

    def sp3_3_zhxfs_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---直选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
        # 遍历数字从百、十、个位各选1个号码组成一注
        # 遍历10个号码
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
            print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
        for j in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], j)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
            print('极速3d-直选复式十位号码是：' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], j)
        for k in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], k)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
            print('极速3d-直选复式个位号码是：' + str(k) + ' ' + str(s))
            self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], k
        '''
        # 百位---十位---个位随机抽取两位个数字,抽取300次，每个号码抽一位数字
        for i in range(100):
            try:
                s = random.choice(range(0, 7))
                m0 = random.sample(range(0, 3), 2)
                s1 = m0[0]
                s2 = m0[1]
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
                a10 = random.choice(range(0, 10))
                a11 = random.choice(range(0, 10))
                # 每个位置随机一个号码
                if s == 0:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                # 每个位置随机两个号码
                if s == 1:
                    if s1 == 0 or s2 == 0:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                    if s1 == 1 or s2 == 1:
                        if a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a2)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a3)
                    if s1 == 2 or s2 == 2:
                        if a4 == a5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a4)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a5)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                # 每个位置随机三个号码
                if s == 2:
                    if s1 == 0 or s2 == 0:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                    if s1 == 1 or s2 == 1:
                        if a3 == a4 or a3 == a5 or a4 == a5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a3)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a4)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                    if s1 == 2 or s2 == 2:
                        if a6 == a7 or a6 == a8 or a7 == a8:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a6)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a7)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a8)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                # 每个位置随机四个号码
                if s == 3:
                    if s1 == 0 or s2 == 0:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a3)
                    if s1 == 1 or s2 == 1:
                        if a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a5 == a7:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a4)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a6)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                    if s1 == 2 or s2 == 2:
                        if a8 == a9 or a8 == a10 or a8 == a11 or a9 == a10 or a9 == a11 or a10 == a11:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a8)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a9)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a10)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a11)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                # 任意两个位置1个号码
                if s == 4:
                    if s1 == s2:
                        pass
                    if s1 == 0 and s2 == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a1)
                    if s1 == 0 and s2 == 2:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a1)
                    if s1 == 1 and s2 == 2:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                # 任意两个位置两个号码 + 一号码
                if s == 5:
                    if s1 == s2:
                        pass
                    if s1 == 0 and s2 == 1:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a2)
                    if s1 == 0 and s2 == 2:
                        if a3 == a4 or a3 == a5 or a4 == a5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a4)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a5)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a6)
                    if s1 == 1 and s2 == 2:
                        if a6 == a7 or a6 == a8 or a7 == a8:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a8)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a9)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式一号码：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                # 任意两个位置一个号码 + 两号码
                if s == 6:
                    if s1 == s2:
                        pass
                    if s1 == 0 and s2 == 1:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a1)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a2)
                    if s1 == 0 and s2 == 2:
                        if a3 == a4 or a3 == a5 or a4 == a5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a4)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a5)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a6)
                    if s1 == 1 and s2 == 2:
                        if a6 == a7 or a6 == a8 or a7 == a8:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a8)
                            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], a9)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三码---直选---复式 + 两号码  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break

        # 随机文字
        for i in range(25):
            try:
                a = random.choice(range(0, 3))
                b = random.choice(range(0, 5))
                if a == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                if a == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break

    def sp3_3_zhxds(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---直选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                d1 = random.choice(range(0, 1000))
                d2 = "%03d" % d1
                self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], d2)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print('三码---直选---单式号码：' + str(d2))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '1')
                break

    def sp3_3_zhxds_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---直选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                s1 = random.choice(range(0, 100))
                s2 = random.choice(range(999, 10000))
                # d0 = random.choice(range(0, 1000))
                # d1 = "%03d" % d0
                # 输入小于三位数字的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入大于三位数字号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '1')
                break

    def sp3_3_zhxzxhezhi(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---直选---直选和值
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '2')
        # 遍历从0-27中任选1个号码组成一注
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 15))
                a1 = random.choice(range(0, 13))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ0'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('三码---直选---直选和值：' + str(a0))
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ1'], a1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('三码---直选---直选和值：' + str(a1))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---直选---直选和值异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---直选---直选和值
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '2')
                break

        # 随机从0-27中任选1个号码组成一注
        for i in range(100):
            a = random.choice(range(0, 27))
            if a <= 14:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ0'], a)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            else:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ1'], a-14)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def sp3_3_zuxzu3(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---组选---组3
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '0')
        self.base_driver.forced_wait(1)
        # 遍历从0-9中任选2个号码组成两注
        '''
        for i in range(10):
            for j in range(10):
                if i <= j:
                    print(i, j)
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], j)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''

        # 随机从0-9中任选2个号码组成两注
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('三码---组选---组3：' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---组3.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---组3异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---组3
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '0')
                self.base_driver.forced_wait(1)
                break

        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])

    def sp3_3_zuxzu3_error(self, row):
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---组选---组3
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '0')
        self.base_driver.forced_wait(1)
        # 遍历从0-9中任选2个号码组成两注
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---组3.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---组3异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---组3
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '0')
                self.base_driver.forced_wait(1)
                break

    def sp3_3_zuxzu6(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---组选---组6
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '1')
        # 遍历从0-9中任选3个号码组成一注
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i >= j or i >= k or j >= k:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], j)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], k)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机从0-9中任选3个号码组成一注
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                if a == b or a == c or b == c:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], b)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], c)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('三码---组选---组6：' + str(a) + ' ' + str(b) + ' ' + str(c))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---组6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---组6异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---组6
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '1')
                self.base_driver.forced_wait(1)
                break

        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---组6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---组6异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---组6
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '1')
                self.base_driver.forced_wait(1)
                break

    def sp3_3_zuxzu6_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---组选---组6
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '1')
        # 遍历从0-9中任选3个号码组成一注
        for i in range(30):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-直选复式百位号码是：' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-直选复式百位号码是：' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---组6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---组6异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---组6
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '1')
                self.base_driver.forced_wait(1)
                break

    def sp3_3_zuxhhzx(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---组选---混合组选
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '2')
        # 手动输入1个三位数号码组成一注，号码不能重复
        for i in range(100):
            try:
                # 数组1000
                # 数组1000随机抽取
                d1 = random.choice(range(0, 1000))
                # 数组不够三位补够三位
                m = "%03d" % d1
                # 切片取数组第一个数字
                s0 = m[0]
                s1 = m[1]
                s2 = m[2]
                # 如果三个数字相同的直接打印，否则运行用例
                if s0 == s1 == s2:
                    # print('豹子数字为:' + str(m))
                    pass
                else:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZUXTEXT'], m)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('三码---组选---混合组选：' + str(m))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---混合组选异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---混合组选
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '2')
                break

    def sp3_3_zuxhhzx_error(self, row):
        # 三码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
        # 三码---组选---混合组选
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '2')
        # 手动输入1个三位数号码组成一注，号码不能重复
        # 手动输入1个三位数号码组成一注
        for i in range(30):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 100))
                s2 = random.choice(range(999, 10000))
                d0 = random.choice(range(0, 1000))
                d1 = "%03d" % d0
                a0 = d1[0]
                a1 = d1[1]
                a2 = d1[2]
                # 输入小于三位数字的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入大于三位数字号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入一个三个数字相同三位数的号码
                if s0 == 2:
                    if a0 == a1 == a2:
                        self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], d0)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-直选复式百位号码是：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---混合组选异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '三码')
                # 三码---组选---混合组选
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZUX'], '2')
                break

    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------

    def sp3_2_h2zhixfs(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码直选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '0')
        # 从十、个位各选1个号码组成一注
        '''
        for i in range(10):
            for j in range(10):
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], j)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百十位---个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], b)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print(' 二码---后二码直选---复式：' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---混合组选异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '0')
                break
        '''
        # 遍历文字
        for i in range(5):
            for j in range(5):
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], j)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机抽取文字
        for i in range(10):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], b)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print(' 二码---后二码直选---复式：' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-三码---组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三码---组选---混合组选异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '0')
                break

    def sp3_2_h2zhixfs_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码直选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '0')
        # 从十、个位各选1个号码组成一
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
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                # 个位选择一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a0)
                # 选择十位文字
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码十位文字选择一个：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 选择个位文字
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择两个
                if s0 == 5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择两个：' + str(a0) + str(a1) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择两个
                if s0 == 6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择两个：' + str(a2) + str(a3) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择三个
                if s0 == 7:
                    if a0 == a1 or a1 == a2 or a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择三个
                if s0 == 8:
                    if a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择四个
                if s0 == 9:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择四个
                if s0 == 10:
                    if a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择五个
                if s0 == 11:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择五个
                if s0 == 12:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a8)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a9)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '0')
                break

    def sp3_2_h2zhixds(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码直选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                d1 = random.choice(range(0, 100))
                d2 = "%02d" % d1
                self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], d2)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print(' 二码---后二码直选---单式：' + str(d2))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码直选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '1')
                break

    def sp3_2_h2zhixds_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码直选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(99, 1000))
                # 输入小于两位数字的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入大于三位数字的号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码直选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '1')
                break

    def sp3_2_h2zhixzhixhzhi(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码直选---直选和值
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '2')
        # 遍历从0-27中任选1个号码组成一注
        '''
        for i in range(15):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ0'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        for j in range(4):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ1'], j)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机从0-27中任选1个号码组成一注
        for i in range(100):
            try:
                a = random.choice(range(0, 18))
                if a <= 14:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ0'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print(' 二码---后二码直选---直选和值：' + str(a))
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ1'], a-14)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print(' 二码---后二码直选---直选和值：' + str(a-14))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码直选---直选和值异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码直选---直选和值
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZHIX'], '2')
                break

    # ----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------

    def sp3_2_h2zuxfs(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码组选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '0')
        # 遍历从0-9中任选2个号码组成两注
        '''
        for i in range(10):
            for j in range(10):
                if i >= j:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], j)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机从0-9中任选2个号码组成两注
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print(' 二码---后二码组选---复式：' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码直选---直选和值异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码组选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '0')
                break
        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print(' 二码---后二码组选---复式：' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码直选---直选和值异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码组选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '0')
                break

    def sp3_2_h2zuxfs_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码组选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '0')
        # 遍历从0-9中任选1个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('极速3d-二码个位选择一个：' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码组选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码组选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '0')
                break

    def sp3_2_h2zuxds(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码组选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '1')
        # 手动输入1个三位数号码组成一注，号码不能重复
        for i in range(100):
            try:
                # 数组1000
                # 数组1000随机抽取
                d1 = random.choice(range(0, 100))
                # 数组不够三位补够三位
                m = "%02d" % d1
                # 切片取数组第一个数字
                s0 = m[0]
                s1 = m[1]
                # 如果三个数字相同的直接打印，否则运行用例
                if s0 == s1:
                    # print('二码---后二码组选---单式豹子数字为:' + str(m))
                    pass
                else:
                    self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], m)
                    print('二码---后二码组选---单式输入数字为:' + str(m))
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码组选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码组选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '1')
                break

        # --------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------
        # --------------------------------------------------------------------------------

    def sp3_2_h2zuxds_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---后二码组选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '1')
        # 手动输入1个三位数号码组成一注，号码不能重复
        for i in range(200):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(99, 1000))
                d1 = random.choice(range(0, 100))
                # 数组不够两位补够两位
                d2 = "%02d" % d1
                # 切片取数组第一个数字
                m0 = d2[0]
                m1 = d2[1]
                # 输入小于两位数字的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入大于三位数字的号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], s2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，十个位置相同号码
                if s0 == 2:
                    if m0 == m1:
                        self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], d2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择一个：' + str(s2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---后二码组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---后二码组选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---后二码组选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3H2ZUX'], '1')
                break

    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------
    def sp3_2_q2zhixfs(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码直选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '0')
        # 从十、个位各选1个号码组成一注
        '''
        for i in range(10):
            for j in range(10):
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], j)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百十位---个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], b)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print('二码---前二码直选---复式:' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '0')
                break
        '''
        # 遍历文字
        for i in range(5):
            for j in range(5):
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], j)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机抽取文字
        for i in range(10):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], b)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '0')
                break

    def sp3_2_q2zhixfs_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码直选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '0')
        # 从十、个位各选1个号码组成一注
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
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                # 个位选择一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a0)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a0)
                # 选择十位文字
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码十位文字选择一个：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 选择个位文字
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择两个
                if s0 == 5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择两个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择两个
                if s0 == 6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择两个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择三个
                if s0 == 7:
                    if a0 == a1 or a1 == a2 or a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择三个
                if s0 == 8:
                    if a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择三个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择四个
                if s0 == 9:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a3)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择四个
                if s0 == 10:
                    if a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a4)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择四个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                # 十位选择五个
                if s0 == 11:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a0)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a1)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a2)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a3)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a4)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码十位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
                # 个位选择五个
                if s0 == 12:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a5)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a6)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a7)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a8)
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], a9)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择五个：' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码直选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码直选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '0')
                break

    def sp3_2_q2zhixds(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码直选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        for i in range(100):
            try:
                d1 = random.choice(range(0, 100))
                d2 = "%02d" % d1
                self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], d2)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                print('二码---前二码直选---单式:' + str(d2))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码直选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码直选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '1')
                break

    def sp3_2_q2zhixds_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码直选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '1')
        # 手动输入1个三位数号码组成一注
        # 手动输入1个三位数号码组成一注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(99, 1000))
                # 输入小于两位数字的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入大于三位数字的号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['SP3ZHIXDSTEXT'], s2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码直选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码直选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '1')
                break

    def sp3_2_q2zhixzhixhzhi(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码直选---直选和值
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '2')
        # 遍历从0-27中任选1个号码组成一注
        '''
        for i in range(15):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ0'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        for j in range(4):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ1'], j)
        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机从0-27中任选1个号码组成一注
        for i in range(100):
            try:
                a = random.choice(range(0, 18))
                if a <= 14:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ0'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('二码---前二码直选---直选和值:' + str(a))
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXHZ1'], a-14)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('二码---前二码直选---直选和值:' + str(a-14))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码直选---直选和值异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码直选---直选和值
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZHIX'], '2')
                break

   # --------------------------------------------------------------------------------
   # --------------------------------------------------------------------------------
   # --------------------------------------------------------------------------------
   # --------------------------------------------------------------------------------
    def sp3_2_q2zuxfs(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码组选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '0')
        # 遍历从0-9中任选2个号码组成两注
        '''
        for i in range(10):
            for j in range(10):
                if i >= j:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], j)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 随机从0-9中任选2个号码组成两注
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('二码---前二码组选---复式:' + str(a) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码组选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码组选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '0')
                break
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)

    def sp3_2_q2zuxfs_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码组选---复式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '0')
        # 遍历从0-9中任选2个号码组成两注
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                print('极速3d-二码个位选择一个：' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码组选---复式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码组选---复式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '0')
                break

    def sp3_2_q2zuxds(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码组选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '1')
        # 手动输入1个三位数号码组成一注，号码不能重复
        for i in range(100):
            try:
                # 数组1000
                # 数组1000随机抽取
                d1 = random.choice(range(0, 100))
                # 数组不够两位补够三位
                m = "%02d" % d1
                # 切片取数组第一个数字
                s0 = m[0]
                s1 = m[1]
                # 如果三个数字相同的直接打印，否则运行用例
                if s0 == s1:
                    # print('豹子数字为:' + str(m))
                    pass
                else:
                    self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], m)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    print('二码---前二码组选---复式:' + str(m))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码组选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码组选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '1')
                break

    def sp3_2_q2zuxds_error(self, row):
        # 二码
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
        # 二码---前二码组选---单式
        self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '1')
        # 手动输入1个三位数号码组成一注，号码不能重复
        for i in range(100):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(99, 1000))
                d1 = random.choice(range(0, 100))
                # 数组不够两位补够两位
                d2 = "%02d" % d1
                # 切片取数组第一个数字
                m0 = d2[0]
                m1 = d2[1]
                # 输入小于两位数字的号码
                if s0 == 0:
                    self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], s1)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入大于三位数字的号码
                if s0 == 1:
                    self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], s2)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                    print('极速3d-二码个位选择一个：' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                # 输入两个数字，十个位置相同号码
                if s0 == 2:
                    if m0 == m1:
                        self.base_driver.type(self.config_dict_lowsp3['SP3H2ZUXTEXT'], d2)
                        self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_lowsp3['TIPS'])
                        print('极速3d-二码个位选择一个：' + str(d2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_lowsp3['TIPSBUTTON'])
                    else:
                        pass
                else:
                    pass

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码组选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二码
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '二码')
                # 二码---前二码组选---单式
                self.base_driver.clicks(self.config_dict_lowsp3['SP3Q2ZUX'], '1')
                break

   # --------------------------------------------------------------------------------
   # --------------------------------------------------------------------------------
   # --------------------------------------------------------------------------------
   # --------------------------------------------------------------------------------
    def sp3_dwd(self, row):
        # 定位胆
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '定位胆')
        # 定位胆
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
        # 从百、十、个位各选1个号码组成一注
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        for j in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], j)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        for k in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], k)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百位---十位---个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 3))
                if d == 0:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                if d == 1:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXS'], b)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXG'], c)
                    self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码组选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 定位胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '定位胆')
                # 定位胆
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break
        # 遍历文字
        '''
        for i in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        for j in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], j)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        for k in range(5):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], k)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百位---十位---个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(10):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], a)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXSWZ'], b)
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXGWZ'], c)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-二码---前二码组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二码---前二码组选---单式异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 定位胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '定位胆')
                # 定位胆
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break

    def sp3_bddan(self, row):
        # 不定胆
        self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '不定胆')
        # 不定胆---一码不定胆
        self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
        # 从百、十、个位各选1个号码组成一注
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], i)
            self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
        '''
        # 百位---十位---个位随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXB'], a)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-不定胆---一码不定胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('不定胆---一码不定胆异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '不定胆')
                # 不定胆---一码不定胆
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break
        # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIXBWZ'], i)
                self.base_driver.click(self.config_dict_lowsp3['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/speed_3d/' + '%s-不定胆---一码不定胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不定胆---一码不定胆异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定胆
                self.base_driver.clicks_by_text(self.config_dict_lowsp3['MENU'], '不定胆')
                # 不定胆---一码不定胆
                self.base_driver.clicks(self.config_dict_lowsp3['SP3ZHIX'], '0')
                break

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
        # self.base_driver.clear(self.config_dict_marksix['XIUGAI'])
        #
        s = random.choice(range(0, 1000))
        self.base_driver.type(self.config_dict_lowsp3['XIUGAI'], "\b" + str(s))
        self.base_driver.click(self.config_dict_lowsp3['RANDOM1'])
        #self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机1注')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        self.base_driver.forced_wait(1)
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
        tips = self.base_driver.get_text(self.config_dict_lowsp3['TIPS02'])
        print('捕捉到的信息是：' + tips)
        return tips
