import random
import time
from common.box import BasePage, YamlHelper


class TimeMinute(BasePage):
    # 分分时时彩
    config_dict_tmm = YamlHelper().get_config_dict('/fusion/yaml/lottery_time_mm.yaml')['TimeMm']

    def menu(self):
        # 导航栏
        self.base_driver.click_by_text(self.config_dict_tmm['MENU'], '文字')

    def star3_h3zhxfs(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---复式
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '0')
        # # 遍历10个号码
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        '''
        # 百位---十位---个位随机抽取一个数字,抽取300次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                print("输入的号码是" + str(a) + ' ' + str(b) + ' ' + str(b))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '0')
                break
        for i in range(5):
            try:
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a0)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], a1)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], a2)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/choice11_5/' + '%s-三星---后三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '0')
                break
        print('三星---后三直选---复式用例成功')
        print('=====================================================================================')

    def star3_h3zhxfs_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---复式
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '0')
        # 百位---十位---个位随机抽取两位个数字,抽取300次，每个号码抽一位数字
        for i in range(50):
            try:
                ss = random.choice(range(0, 4))
                s0 = random.sample(range(0, 3), 2)
                s1 = s0[0]
                s2 = s0[1]
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))

                if ss == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(d) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], d)
                if ss == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--十位--输入的号码是：' + str(d) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], d)
                if ss == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--个位--输入的号码是：' + str(d) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], d)
                if ss == 3:
                    print(s1, s2, a, b, c)
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三组选--复式：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])

                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '0')
                break

            #
        # 随机文字
        for i in range(25):
            try:
                a = random.choice(range(0, 3))
                b = random.choice(range(0, 5))
                if a == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if a == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '0')
                break
        print('三星---后三直选---复式用例成功')
        print('=====================================================================================')

    def star3_h3zhxds(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '1')
        # 输入任意三个数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                print('三星---后三直选---单式输入的号码是：' + str(s1))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '1')
                break

    def star3_h3zhxds_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '1')
        # 输入小于三位数字任意数字
        for i in range(10):
            try:
                s0 = random.choice(range(0, 100))
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s0)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('三星---后三直选---单式输入的号码是：' + str(s0) + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '1')
                break
        # 输入大于于三位数字并且小于七位任意数字
        for i in range(10):
            try:
                s0 = random.choice(range(1000, 1000000))
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s0)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('三星---后三直选---单式输入的号码是：' + str(s0) + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '1')
                break

    def star3_h3zhxzxhz(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---直选和值
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '2')
        # 随机抽取28个号码
        for i in range(50):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 15))
                s2 = random.choice(range(0, 13))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN1'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN2'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '2')
                break

    def star3_h3zhxzxkd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---直选跨度
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '3')
        # 遍历10个号码
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    print('选择的号码是' + str(s1))
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---直选跨度.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '3')
                break

    def star3_h3zhxhzws(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三直选---直选尾数
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '4')
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                print('三星---后三直选---直选尾数输入的号码是' + str(i))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三直选---直选尾数.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---直选尾数
                self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '4')
                break
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def star3_h3zuxz3(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---组三
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # # 任选2个号码，循环10次
        # for i in range(10):
        #     a1 = random.choice(range(1, 10))
        #     a2 = random.choice(range(1, 10))
        #     if a1 == a2:
        #         pass
        #     else:
        #         self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
        #         self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
        #         self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #         self.base_driver.forced_wait(1)
        # 遍历所有组合
        for i in range(10):
            for j in range(10):
                try:
                    if i == j:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        print('三星---后三直选---组三输入的号码是' + str(i) + ' ' + str(j))
                        # self.base_driver.forced_wait(1)
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---组三.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('三星---后三直选---组三下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 三星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                    # 三星---后三组选---组三
                    self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '0')
                    break

        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)

    def star3_h3zuxz3_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---组三
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '0')
        # 只选一个号码
        # 遍历所有组合
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('三星--后三组选--组三--输入的号码是：' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---组三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---组三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '0')
                break

    def star3_h3zuxz6(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---组六
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # # 任选3个号码，循环10次
        for i in range(300):
            try:
                a1 = random.choice(range(1, 10))
                a2 = random.choice(range(1, 10))
                a3 = random.choice(range(1, 10))
                if a1 == a2 or a1 == a3 or a2 == a3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---组六.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---组六下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '1')
                break
        # # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             if i == j or i == k or j == k:
        #                 pass
        #             else:
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                 self.base_driver.forced_wait(1)
        #
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            self.base_driver.forced_wait(1)

    def star3_h3zuxz6_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---组六
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(30):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三组选--组三--输入的号码是：' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--后三组选--组六--输入的号码是：' + str(s1) + ' ' + str(s2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s2)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---组六.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---组六下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '1')
                break

    def star3_h3zuxhhzhix(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---混合组选
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '2')
        self.base_driver.forced_wait(1)
        # 输入任意三个数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                s2 = s1[0]
                s3 = s1[1]
                s4 = s1[2]
                if s2 == s3 and s2 == s4 and s3 == s4:
                    pass
                else:
                    print('输入的数字是：  ' + ' ' + str(s0))
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '2')
                break

    def star3_h3zuxhhzhix_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---混合组选
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '2')
        self.base_driver.forced_wait(1)
        # 随机组合
        for i in range(50):
            try:
                ss = random.choice(range(0, 3))
                a0 = random.choice(range(0, 100))
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                s2 = s1[0]
                s3 = s1[1]
                s4 = s1[2]
                # 输入小于三位数字任意数字
                if ss == 0:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(a0) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if ss == 1:
                    # 输入三个相同的数字
                    if s2 == s3 and s2 == s4 and s3 == s4:
                        self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--后三组选--混合组选：  ' + ' ' + str(s0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    else:
                        pass
                # 输入大于于三位数字并且小于七位任意数字
                if ss == 2:
                        s5 = random.choice(range(1000, 1000000))
                        self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s5)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--后三复式--百位--输入的号码是：' + str(s5) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '2')
                break

    def star3_h3zuxbd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---后三组选---组选包胆
        self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '3')
        self.base_driver.forced_wait(1)
        # # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(1, 10))
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---后三组选---组选包胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---后三直选---组选包胆下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三组选---组选包胆
                self.base_driver.clicks(self.config_dict_tmm['H3ZUXN'], '3')
                break
        # 遍历所有组合
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def star3_z3zhxfs(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '0')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #             self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 百位---十位---个位随机抽取一个数字
        # 抽取300次，每个号码抽一位数字
        for i in range(300):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                print('选择的号码是： ' + str(a) + ' ' + str(b) + ' ' + str(c))
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '0')
                break

        # 遍历文字
        for i in range(30):
            try:
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a0)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], a1)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], a2)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---复式下注异常')
                self.base_driver.refresh()
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '0')
                break

    def star3_z3zhxfs_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '0')
        self.base_driver.forced_wait(1)
        # 百位---十位---个位随机抽取一个数字
        # 抽取300次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 3))

                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三直选--复式--输入的号码是：' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三直选--复式--输入的号码是：' + ' ' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三直选--复式--输入的号码是：' + ' ' + str(c) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '0')
                break
        # 随机文字
        for i in range(25):
            try:
                a = random.choice(range(0, 3))
                b = random.choice(range(0, 5))
                if a == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if a == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三星---中三直选---复式下注异常')
                self.base_driver.refresh()
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '0')
                break

    def star3_z3zhxds(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '1')
        # 输入小于三位数字任意数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '1')
                break

    def star3_z3zhxds_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '1')
        for i in range(50):
            try:
                # 输入小于三位数字任意数字
                ss = random.choice(range(0, 2))
                s0 = random.choice(range(0, 100))
                s1 = random.choice(range(1000, 1000000))
                if ss == 0:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入大于于三位数字并且小于七位任意数字
                if ss == 1:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '1')
                break

    def star3_z3zhxzxhz(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---直选和值
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '2')
        # 随机抽取号码
        for i in range(30):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 15))
                s2 = random.choice(range(0, 13))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN1'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN2'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '2')
                break

    def star3_z3zhxzxkd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---直选跨度
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '3')
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---直选跨度.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---直选跨度下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---直选跨度
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '3')
                break

    def star3_z3zhxhzws(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三直选---和值尾数
        self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '4')
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---和值尾数.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---和值尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三直选---和值尾数
                self.base_driver.clicks(self.config_dict_tmm['Z3ZHXN'], '4')
                break

    def star3_z3zuxz3(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---组三
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(20):
            try:
                a1 = random.choice(range(1, 10))
                a2 = random.choice(range(1, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---和值尾数.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---和值尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '0')
                break

        # # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         try:
        #             if i == j:
        #                 pass
        #             else:
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #         except Exception as e:
        #             print(e)
        #             now_Time = time.strftime("%Y%m%d.%H.%M.%S")
        #             s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---和值尾数.png' % now_Time
        #             self.base_driver.save_window_snapshot_by_io(s)
        #             # self.logger.infos('三星---中三直选---和值尾数下注异常')
        #             self.base_driver.refresh()
        #             # 三星
        #             self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        #             # 三星---中三组选---组三
        #             self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '0')
        #             break

        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    def star3_z3zuxz3_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---组三
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('三星--中三组选--组三--号码是：' + ' ' + str(i) + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---组三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---组三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '0')
                break

    def star3_z3zuxz6(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---组六
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选3个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(1, 10))
                a2 = random.choice(range(1, 10))
                a3 = random.choice(range(1, 10))
                if a1 == a2 or a1 == a3 or a2 == a3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    # self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---组六.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---组六下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---组六
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '1')
                break
        # # 遍历所有组合
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == j or i == k or j == k:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        self.base_driver.forced_wait(1)
        '''
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)

    def star3_z3zuxz6_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---组六
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                a1 = random.choice(range(1, 10))
                a2 = random.choice(range(1, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三组选--组三--号码是：' + ' ' + str(s1) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                if s0 == 1:
                    if a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--中三组选--组三--号码是：' + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三直选---组六.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三直选---组六下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---组六
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '1')
                break

    def star3_z3zuxzx(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---混合组选
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '2')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                s2 = s1[0]
                s3 = s1[1]
                s4 = s1[2]
                if s2 == s3 and s2 == s4 and s3 == s4:
                    pass
                else:
                    print('输入的数字是：  ' + ' ' + str(s0))
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三组选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '2')
                break

    def star3_z3zuxzx_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---混合组选
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '2')
        self.base_driver.forced_wait(1)

        for i in range(10):
            try:
                ss = random.choice(range(0, 3))
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                s2 = s1[0]
                s3 = s1[1]
                s4 = s1[2]
                s5 = random.choice(range(1000, 1000000))
                a6 = random.choice(range(0, 100))
                # 输入小于三位数字任意数字
                if ss == 0:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], a6)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(a6) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入三个数字相同的号码，豹子号
                if ss == 1:
                    if s2 == s3 and s2 == s4 and s3 == s4:
                        self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--后三组选--混合组选：  ' + ' ' + str(s0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    else:
                        pass
                # 输入大于于三位数字并且小于七位任意数字
                if ss == 2:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s5)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s5) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三组选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '2')
                break

    def star3_z3zuxbd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---中三组选---组选包胆
        self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '3')
        self.base_driver.forced_wait(1)
        # # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(1, 10))
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---中三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---中三组选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---中三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['Z3ZUXN'], '3')
                break
        # 遍历所有组合
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def star3_q3zhxfs(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '0')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        '''
        # 百位---十位---个位随机抽取一个数字
        # 抽取300次，每个号码抽一位数字
        for i in range(300):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                print(a, b, c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '0')
                break
        # 遍历文字
        for i in range(5):
            try:
                s0 = random.choice(range(0, 5))
                s1 = random.choice(range(0, 5))
                s2 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], s0)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], s1)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], s2)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '0')
                break

    def star3_q3zhxfs_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '0')
        self.base_driver.forced_wait(1)
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('三星--中三直选--复式--输入的号码是：' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('三星--中三直选--复式--输入的号码是：' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        for k in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('三星--中三直选--复式--输入的号码是：' + ' ' + str(k) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
        '''
        # 百位---十位---个位随机抽取一个数字
        # 抽取300次，每个号码抽一位数字
        for i in range(50):
            try:
                s0 = random.choice(range(0, 4))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三直选--复式--输入的号码是：' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三直选--复式--输入的号码是：' + ' ' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三直选--复式--输入的号码是：' + ' ' + str(c) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '0')
                break
        # 随机文字
        for i in range(25):
            try:
                a = random.choice(range(0, 3))
                b = random.choice(range(0, 5))
                if a == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if a == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三星---前三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '0')
                break

    def star3_q3zhxds(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '1')
        # 输入三位数字任意数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '1')
                break

    def star3_q3zhxds_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '1')
        # 输入小于三位数字任意数字
        for i in range(10):
            try:
                ss = random.choice(range(0, 2))
                s0 = random.choice(range(0, 100))
                s1 = random.choice(range(1000, 1000000))
                # 输入小于三位数字任意数字
                if ss == 0:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入大于于三位数字并且小于七位任意数字
                if ss == 1:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '1')
                break

    def star3_q3zhxzxhz(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---直选和值
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '2')
        # 遍历10个号码
        for i in range(30):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 15))
                s2 = random.choice(range(0, 13))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN1'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN2'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '2')
                break

    def star3_q3zhxzxkd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---直选跨度
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '3')
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '3')
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    def star3_q3zhxhzws(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三直选---直选尾数
        self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '4')
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三直选---直选尾数.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三直选---直选尾数
                self.base_driver.clicks(self.config_dict_tmm['Q3ZHXN'], '4')

    def star3_q3zuxz3(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---组三
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(1, 10))
                a2 = random.choice(range(1, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    # self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组三---组三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '0')
                break
        '''
        # 遍历所有组合
        for i in range(10):
            for j in range(10):
                if i == j:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    # self.base_driver.forced_wait(1)
        '''

    def star3_q3zuxz3_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---组三
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码，
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('三星--后三复式--百位--输入的号码是：' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组三---组三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '0')
                break

    def star3_q3zuxz6(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---组六
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选3个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(1, 10))
                a2 = random.choice(range(1, 10))
                a3 = random.choice(range(1, 10))
                if a1 == a2 or a1 == a3 or a2 == a3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组选---组三.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '1')
                break
        # # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             if i == j or i == k or j == k:
        #                 pass
        #             else:
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                 self.base_driver.forced_wait(1)

    def star3_q3zuxz6_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---组六
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '1')
        self.base_driver.forced_wait(1)
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--中三组选--组三--号码是：' + ' ' + str(s1) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--中三组选--组三--号码是：' + ' ' + str(s1) + ' ' + str(s2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['N0_9'], s2)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组选---组六.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---组三
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '1')
                break

    def star3_q3zuxzx(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---混合组选
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '2')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s0 = random.choice(range(0, 1000))
                s1 = "%03d" % s0
                s2 = s1[0]
                s3 = s1[1]
                s4 = s1[2]
                if s2 == s3 and s2 == s4 and s3 == s4:
                    pass
                else:
                    print('输入的数字是：  ' + ' ' + str(s0))
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '2')
                break

    def star3_q3zuxzx_error(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---混合组选
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '2')
        self.base_driver.forced_wait(1)
        # 输入小于三位数字任意数字
        for i in range(100):
            try:
                ss = random.choice(range(0, 2))
                a0 = random.choice(range(0, 100))
                # 输入小于三位数字任意数字
                if ss == 0:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('三星--后三复式--百位--输入的号码是：' + str(a0) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入三个相同的数字
                if ss == 0:
                    s0 = random.choice(range(0, 1000))
                    s1 = "%03d" % s0
                    s2 = s1[0]
                    s3 = s1[1]
                    s4 = s1[2]
                    if s2 == s3 and s2 == s4 and s3 == s4:
                        self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('三星--后三组选--混合组选：  ' + ' ' + str(s0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    else:
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组选---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---混合组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---混合组选
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '2')
                break

    def star3_q3zuxbd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
        # 三星---前三组选---组选包胆
        self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '3')
        self.base_driver.forced_wait(1)
        # # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(1, 10))
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-三星---前三组选---混合包胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('三星---前三直选---混合包胆下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '三星')
                # 三星---前三组选---混合包胆
                self.base_driver.clicks(self.config_dict_tmm['Q3ZUXN'], '3')
                break
        # 遍历所有组合
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)

        # --------------------------------------------------------------------------
        # --------------------------------------------------------------------------
        # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def star4_h4zhxfs(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后四直选---复式
        self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '0')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 百位---十位---个位随机抽取一个数字
        # 抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(a, b, c, d)
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '0')
                break
        #
        # # 遍历文字
        # for i in range(0, 5):
        #     for j in range(0, 5):
        #         for k in range(0, 5):
        #             for m in range(0, 5):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMQGWZ'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 随机抽取文件组合
        for i in range(5):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '0')
                break

    def star4_h4zhxfs_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后四直选---复式
        self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '0')
        self.base_driver.forced_wait(1)
        # 百位---十位---个位随机抽取一个数字
        # 抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(s1, s2, s3, a, b, c, d)
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星--后四组选--复式：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])

                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '0')
                break

        # 随机抽取文件组合
        for i in range(5):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print(s1, s2, s3, a, b, c, d)
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                    print('四星---后四直选---复式千位：' + str(a))
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                    print('四星---后四直选---复式百位：' + str(b))
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                    print('四星---后四直选---复式十位：' + str(c))
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                    print('四星---后四直选---复式个位：' + str(d))
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星--后四组选--复式：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])

                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')
                self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后三直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后三直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '0')
                break

    def star4_h4zhxds(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '1')
        # 输入三位数字任意数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 10000))
                s1 = "%04d" % s0
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '1')
                break

    def star4_h4zhxds_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后四直选---单式
        self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '1')

        for i in range(50):
            try:
                ss = random.choice(range(0, 2))
                s0 = random.choice(range(0, 1000))
                s1 = random.choice(range(10000, 1000000))
                if ss == 0:
                    # 输入小于四位数字任意数字
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---后四直选---单式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if ss == 1:
                    # 输入大于于四位数字并且小于七位任意数字
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---后四直选---单式--百位--输入的号码是：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后四直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '1')
                break

    def star4_h4zhxzuhe(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后四直选---组合
        self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
        self.base_driver.forced_wait(2)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 百位---十位---个位随机抽取一个数字
        # 抽取100次，每个号码抽一位数字
        for i in range(30):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print('四星---后四直选---组合:' + str(a) + str(b) + str(c) + str(d))
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
                break
        #
        # # 遍历文字
        # for i in range(0, 5):
        #     for j in range(0, 5):
        #         for k in range(0, 5):
        #             for m in range(0, 5):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMQGWZ'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 随机抽取文件组合
        for i in range(100):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
                break

    def star4_h4zhxzuhe_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后四直选---组合
        self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
        self.base_driver.forced_wait(2)
        # # 遍历10个号码
        # 百位---十位---个位随机抽取一个数字
        # 抽取10次，随机抽取一个号码抽一位数字
        for i in range(50):
            try:
                ss = random.choice(range(0, 3))
                s0 = random.choice(range(0, 4))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))

                a0 = random.sample(range(0, 4), 2)
                a1 = a0[0]
                a2 = a0[1]

                b0 = random.sample(range(0, 4), 3)
                b1 = b0[0]
                b2 = b0[1]
                b3 = b0[2]
                if ss == 0:
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if s0 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---后四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if s0 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                print('----------------------------------------------------------')

                # 随机抽取两位
                if ss == 1:
                    if a1 == 0 or a2 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if a1 == 1 or a2 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if a1 == 2 or a2 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---四三直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    if a1 == 0 or a2 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if a1 == 1 or a2 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if a1 == 2 or a2 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)

                # 随机抽取三位
                if ss == 2:
                    if b1 == 0 or b2 == 0 or b3 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if b1 == 1 or b2 == 1 or b3 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if b1 == 2 or b2 == 2 or b3 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---四三直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    if b1 == 0 or b2 == 0 or b3 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    if b1 == 1 or b2 == 1 or b3 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    if b1 == 2 or b2 == 2 or b3 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
                break
        # 随机文字
        # 随机文字
        # 随机文字
        # 随机文字一个
        for i in range(10):
            try:
                s0 = random.choice(range(0, 4))
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print('四星---后四直选---组合：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---后四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')
                print('----------------------------------------------------------')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
                break

        # 随机文字两位
        for i in range(10):
            try:
                s0 = random.sample(range(0, 4), 2)
                s1 = s0[0]
                s2 = s0[1]
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))

                if s1 == 0 or s2 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                if s1 == 1 or s2 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                if s1 == 2 or s2 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---后四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s1 == 0 or s2 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s1 == 1 or s2 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s1 == 2 or s2 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
                break

        # 随机文字三个
        for i in range(10):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print('四星---后四直选---组合：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d))
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---后四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H4ZHX'], '2')
                break

    def star4_h4zuxz24(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选24
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选4个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a3)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选24
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '0')
                break
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j == k or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                     self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选24.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('四星---前四组选---组选24下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 四星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                    # 四星---前四组选---组选24
                    self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '0')
                    break

    def star4_h4zuxz24_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选24
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '0')
        self.base_driver.forced_wait(1)
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四组选---组选24：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选24
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '0')
                break

        # 随机抽取两位
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                print('四星---前四组选---组选24：  ' + ' ' + str(a) + ' ' + str(b))
                if s0 == 0:
                    if a == b:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b)

                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选24：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            # 随机抽取三位
                if s0 == 1:
                    a = random.choice(range(0, 10))
                    b = random.choice(range(0, 10))
                    c = random.choice(range(0, 10))
                    if a == b or a == c or b == c:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选24：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选24下注异常')
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选24
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '0')
                break

    def star4_h4zuxz12(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选12
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选4个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                if a1 == a2 or a1 == a3 or a2 == a3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选12.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选12下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选12
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '1')
                break
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j == k or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                     self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选12.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('四星---前四组选---组选12下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 四星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                    # 四星---前四组选---组选12
                    self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '1')
                    break

    def star4_h4zuxz12_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选12
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
            print('iiiiiiii:        ' + str(i))
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('四星---前四组选---组选12：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('四星---前四组选---组选12：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
        '''

        # 二重号跟单号有1个相同，其余随机
        for i in range(100):
            try:
                s0 = random.choice(range(0, 4))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))

                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                print(s0, a, b, c, a0, a1, a2, a3, a4)
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选12：' + ' ' + str(a) + '  ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选12：' + ' ' + str(b) + '  ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 2:
                    if a == b or a == c:
                        if b == c:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], c)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' '
                                  + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
                if s0 == 3:
                    if a == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('四星---前四组选---组选12：  ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 2:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                                or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a4)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
            except Exception as e:
                print(e)

                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选12.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选24
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '1')
                break

        # # 遍历文字
        for i in range(12):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 6))
                s2 = random.choice(range(0, 6))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选12：  ' + ' ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选12：  ' + ' ' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选12.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选24
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '1')
                break

    def star4_h4zuxz06(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选6
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '2')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选24
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '2')
                break
        # # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         if i == j:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #             self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    def star4_h4zuxz06_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---后四组选---组选6
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '2')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                a0 = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四组选---组选6：  ' + ' ' + str(a0) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---后四组选---组选6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---后四组选---组选6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---后四组选---组选6
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '2')
                break

    def star4_h4zuxz04(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选4
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '3')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选6
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '3')
                break
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j == k or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                     self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    print(i, j)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选6.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('四星---前四组选---组选6下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 四星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                    # 四星---前四组选---组选6
                    self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '3')
                    break

    def star4_h4zuxz04_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选4
        self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '3')
        self.base_driver.forced_wait(1)
        # # 任选2个相同号码
        for i in range(50):
            try:
                s0 = random.choice(range(0, 3))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选4：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选4：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')

                # 任选2个相同号码
                if s0 == 2:
                    if a1 == a2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('四星---前四组选---组选4：  ' + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选4.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选4下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选6
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '3')
                break
        # 遍历文字
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 5))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选4：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选4：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选4.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四组选---组选4下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四组选---组选6
                self.base_driver.clicks(self.config_dict_tmm['H4ZUXN'], '3')
                break
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def star4_q4zhxfs(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '0')
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.base_driver.execute_js(js)
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 百位---十位---个位随机抽取一个数字
        # 抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(a, b, c, d)
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '0')
                break
        #
        # # 遍历文字
        # for i in range(0, 5):
        #     for j in range(0, 5):
        #         for k in range(0, 5):
        #             for m in range(0, 5):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMQGWZ'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 随机抽取文件组合
        for i in range(10):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print(a, b, c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '0')
                break

    def star4_q4zhxfs_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '0')
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.base_driver.execute_js(js)
        self.base_driver.forced_wait(1)
        # 抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(s1, s2, s3, a, b, c, d)
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---复式：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])

                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '0')
                break

        # 随机抽取文件组合
        for i in range(10):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print(s1, s2, s3, a, b, c, d)
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                    print('四星---前四直选---复式千位：' + str(a))
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                    print('四星---前四直选---复式百位：' + str(b))
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                    print('四星---前四直选---复式十位：' + str(c))
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                    print('四星---前四直选---复式个位：' + str(d))
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---复式：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])

                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                if s1 == 3 or s2 == 3 or s3 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')
                self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '0')
                break

    def star4_q4zhxds(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '1')
        # 输入三位数字任意数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 10000))
                s1 = "%04d" % s0
                self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '1')
                break

    def star4_q4zhxds_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前三直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '1')
        # 输入小于四位数字任意数字
        for i in range(30):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 1000))
                if s0 == 0:
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前三直选---单式：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入大于于四位数字并且小于七位任意数字
                if s0 == 1:
                    s2 = random.choice(range(10000, 1000000))
                    self.base_driver.type(self.config_dict_tmm['H3ZHXDSTEXT'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前三直选---单式：' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前三直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前三直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前三直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '1')
                break

    def star4_q4zhxzuhe(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四直选---组合
        self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMG'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 百位---十位---个位随机抽取一个数字
        # 抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(a, b, c, d)
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break
        #
        # # 遍历文字
        # for i in range(0, 5):
        #     for j in range(0, 5):
        #         for k in range(0, 5):
        #             for m in range(0, 5):
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], k)
        #                 self.base_driver.clicks(self.config_dict_tmm['TTMQGWZ'], m)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 随机抽取文件组合
        for i in range(5):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))

                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break

    def star4_q4zhxzuhe_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四直选---组合
        self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
        # # 遍历10个号码
        # 百位---十位---个位随机抽取一个数字
        # 抽取10次，随机抽取一个号码抽一位数字
        for i in range(10):
            try:
                s0 = random.choice(range(0, 4))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(a, b, c, d)
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                print('----------------------------------------------------------')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break

        # 随机抽取两位
        for j in range(10):
            try:
                s0 = random.sample(range(0, 4), 2)
                s1 = s0[0]
                s2 = s0[1]
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(a, b, c, d)
                if s1 == 0 or s2 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s1 == 0 or s2 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break

        # 随机抽取三位
        for k in range(10):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                print(a, b, c, d)
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMG'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQ'], d)

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break
        # 随机文字
        # 随机文字
        # 随机文字
        # 随机文字一个
        for i in range(10):
            try:
                s0 = random.choice(range(0, 4))
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print(a, b, c, d)
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')
                print('----------------------------------------------------------')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break

        # 随机文字两位
        for i in range(10):
            try:
                s0 = random.sample(range(0, 4), 2)
                s1 = s0[0]
                s2 = s0[1]
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print(a, b, c, d)
                if s1 == 0 or s2 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                if s1 == 1 or s2 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                if s1 == 2 or s2 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s1 == 0 or s2 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s1 == 1 or s2 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s1 == 2 or s2 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break

        # 随机文字三个
        for i in range(10):
            try:
                s0 = random.sample(range(0, 4), 3)
                s1 = s0[0]
                s2 = s0[1]
                s3 = s0[2]
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                print(a, b, c, d)
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a)
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], b)
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], c)
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], d)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组合：  ' + ' ' + str(d) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s1 == 0 or s2 == 0 or s3 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s1 == 1 or s2 == 1 or s3 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s1 == 2 or s2 == 2 or s3 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMGWZ'], '5')
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMQWZ'], '5')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合
                self.base_driver.clicks(self.config_dict_tmm['Q4ZHX'], '2')
                break

    def star4_q4zuxz24(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选24
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选4个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a3)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组合24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组合24
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
                break
                # self.base_driver.forced_wait(1)
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j == k or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                     self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组合24.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('四星---前四直选---组合24下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 四星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                    # 四星---前四直选---组合24
                    self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
                    break

    def star4_q4zuxz24_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选24
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选4个号码，循环10次
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组选24：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)

                print('----------------------------------------------------------')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选24
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
                break
        # 随机抽取两位
        for i in range(10):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                print(a, b)
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b)

                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组选24：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')


            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选24
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
                break

        # 随机抽取三位
        for i in range(10):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                print(a, b, c)
                if a == b or a == c or b == c:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], c)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四直选---组选24：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')


            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选24下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选24
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '0')
                break

    def star4_q4zuxz12(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选12
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选4个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                if a1 == a2 or a1 == a3 or a2 == a3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选24.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选12下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选12
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '1')
                break
                # self.base_driver.forced_wait(1)
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j == k or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                     self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选12.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('四星---前四直选---组选24下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 四星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                    # 四星---前四直选---组选24
                    self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '1')
                    break

    def star4_q4zuxz12_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选12
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 5))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))

                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))

                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                    print('iiiiiiii:        ' + str(i))
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选12：  ' + ' ' + str(b) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                # 二重号跟单号有1个相同，其余随机
                if s0 == 2:
                    if a == b:
                        if b == c:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], c)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
                # 二重号随机个数字跟1单号
                if s0 == 3:
                    if a == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 2:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                                or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('四星---前四组选---组选12：  ' + ' ' + str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选12.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选12下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选12
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '1')
                break

        # # 遍历文字
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 6))
                s2 = random.choice(range(0, 6))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四直选---组选12：  ' + ' ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四直选---组选12：  ' + ' ' + str(s2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选12.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选12下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选12
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '1')
                break

    def star4_q4zuxz06(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选6
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '2')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选6
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '2')
                break
        # # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         if i == j:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #             self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    def star4_q4zuxz06_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选6
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '2')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                a0 = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a0)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('四星---前四组选---组选6：  ' + ' ' + str(a0) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四组选---组选6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选6
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '2')
                break

    def star4_q4zuxz04(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选4
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '3')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选4.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选4下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选6
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '3')
                break
                # self.base_driver.forced_wait(1)
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j == k or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['N0_9'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #                     self.base_driver.forced_wait(1)

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:

                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选64.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('四星---前四直选---组选4下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 四星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                    # 四星---前四直选---组选6
                    self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '3')
                    break
                # self.base_driver.forced_wait(5)

    def star4_q4zuxz04_error(self, row):
        # 四星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
        # 四星---前四组选---组选4
        self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '3')
        self.base_driver.forced_wait(1)
        for i in range(10):
            try:
                s0 = random.choice(range(0, 3))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四直选---组选4：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四直选---组选4：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                # 任选2个相同号码
                if s0 == 2:
                    if a1 == a2:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('四星---前四直选---组选4：  ' + ' ' + str(a1) + ' ' + str(a2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选4.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选4下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选6
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '3')
                break
            # 遍历文字
        for i in range(12):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 6))
                s2 = random.choice(range(0, 6))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选4：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('四星---前四组选---组选4：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-四星---前四直选---组选64.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('四星---前四直选---组选4下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 四星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '四星')
                # 四星---前四直选---组选6
                self.base_driver.clicks(self.config_dict_tmm['Q4ZUXN'], '3')
                break
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def douniu(self, row):
        #  斗牛
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '斗牛')
        # 牛牛
        self.base_driver.clicks(self.config_dict_tmm['DOUNIU'], '0')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(11):
            try:
                a1 = random.choice(range(0, 11))
                self.base_driver.clicks(self.config_dict_tmm['NIUN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-斗牛---牛牛.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('斗牛---牛牛下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                #  斗牛
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '斗牛')
                # 牛牛
                self.base_driver.clicks(self.config_dict_tmm['DOUNIU'], '0')
                break
        # # 遍历所有组合
        # for i in range(11):
        #     self.base_driver.clicks(self.config_dict_tmm['NIUN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def teshn_q3(self, row):
        # 特殊号
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '特殊号')
        # 特殊号---前三
        self.base_driver.clicks(self.config_dict_tmm['TESHU'], '0')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(5):
            try:
                a1 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TESHUN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-特殊号---前三64.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('特殊号---前三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 特殊号
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '特殊号')
                # 特殊号---前三
                self.base_driver.clicks(self.config_dict_tmm['TESHU'], '0')
                break
        # # 遍历所有组合
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_tmm['TESHUN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    def teshn_z3(self, row):
        # 特殊号
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '特殊号')
        # 特殊号---中三
        self.base_driver.clicks(self.config_dict_tmm['TESHU'], '1')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(5):
            try:
                a1 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TESHUN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-特殊号---中三64.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('特殊号---中三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 特殊号
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '特殊号')
                # 特殊号---中三
                self.base_driver.clicks(self.config_dict_tmm['TESHU'], '1')
                break
        # # 遍历所有组合
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_tmm['TESHUN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    def teshn_h3(self, row):
        # 特殊号
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '特殊号')
        # 特殊号---后三
        self.base_driver.clicks(self.config_dict_tmm['TESHU'], '2')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(5):
            try:
                a1 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TESHUN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-特殊号---中三64.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('特殊号---后三下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 特殊号
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '特殊号')
                # 特殊号---后三
                self.base_driver.clicks(self.config_dict_tmm['TESHU'], '2')
                break
        # # 遍历所有组合
        # for i in range(5):
        #     self.base_driver.clicks(self.config_dict_tmm['TESHUN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def dxds_zh(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---总和---总和
        self.base_driver.clicks(self.config_dict_tmm['DXDSNZH'], '0')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 4))
                self.base_driver.clicks(self.config_dict_tmm['DXDSN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---总和---总和.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---总和---总和异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---总和---总和
                self.base_driver.clicks(self.config_dict_tmm['DXDSNZH'], '0')
                break
        # # 遍历所有组合
        # for i in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     self.base_driver.forced_wait(1)

    def dxds_dww(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---定位---万
        self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '0')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 4))
                self.base_driver.clicks(self.config_dict_tmm['DXDSN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---定位---万.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---定位---万异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---定位---万
                self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '0')
                break
        # 遍历所有组合
        # for i in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    def dxds_dwq(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---定位---千
        self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '1')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 4))
                self.base_driver.clicks(self.config_dict_tmm['DXDSN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---定位---千.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---定位---千异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---定位---千
                self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '1')
                break
        # # 遍历所有组合
        # for i in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    def dxds_dwb(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---定位---百
        self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '2')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 4))
                self.base_driver.clicks(self.config_dict_tmm['DXDSN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---定位---百.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---定位---百异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---定位---万
                self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '2')
                break
        # # 遍历所有组合
        # for i in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    def dxds_dws(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---定位---十
        self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '3')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 4))
                self.base_driver.clicks(self.config_dict_tmm['DXDSN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---定位---十.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---定位---十异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---定位---十
                self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '3')
                break
        # # 遍历所有组合
        # for i in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)

    def dxds_dwg(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---定位---个
        self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '4')
        self.base_driver.forced_wait(1)
        # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 4))
                self.base_driver.clicks(self.config_dict_tmm['DXDSN'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---定位---个.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---定位---个异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---定位---个
                self.base_driver.clicks(self.config_dict_tmm['DXDSNDW'], '0')
                break
        # # 遍历所有组合
        # for i in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     self.base_driver.forced_wait(1)

    def dxds_cg(self, row):
        # 大小单双
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
        # 大小单双---定位---串关
        self.base_driver.clicks(self.config_dict_tmm['DXDSNCG'], '0')
        self.base_driver.forced_wait(1)
        # 每组随机N个号码，循环100次---万位
        for i in range(50):
            try:
                s0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 4))
                a2 = random.choice(range(0, 4))
                a3 = random.choice(range(0, 4))
                a4 = random.choice(range(0, 4))
                a5 = random.choice(range(0, 4))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DXDSNCGW'], a1)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DXDSNCGQ'], a2)
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DXDSNCGB'], a3)
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DXDSNCGS'], a4)
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DXDSNCGG'], a5)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-大小单双---定位---串关.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('大小单双---定位---串关异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 大小单双
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '大小单双')
                # 大小单双---定位---万
                self.base_driver.clicks(self.config_dict_tmm['DXDSNCG'], '0')
                break
        # # 遍历所有组合---万位
        # for a in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSNCGW'], a)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 遍历所有组合---千位
        # for b in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSNCGQ'], b)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 遍历所有组合---百位
        # for c in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSNCGB'], c)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 遍历所有组合---十位
        # for d in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSNCGS'], d)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 遍历所有组合---个位
        # for e in range(4):
        #     self.base_driver.clicks(self.config_dict_tmm['DXDSNCGG'], e)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def longhh_wq(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--万千
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '0')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择的是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    # 全选
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--万千.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--万千下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎--万千
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--万千
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '0')
                break

    def longhh_wb(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--万百
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '1')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    # 全选
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--万百.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--万百下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--万百
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '1')
                break

    def longhh_ws(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--万十
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '2')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    # 全选
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--万十.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--万十下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--万十
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '2')
                break

    def longhh_wg(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--万个
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '3')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择的号码是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    # 全选
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--万个.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--万个下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--万十
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '3')
                break

    def longhh_qb(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--千百
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '4')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择的号码是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 全选
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--千百.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--千百下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--千百
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '4')
                break

    def longhh_qs(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--千十
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '5')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择的结果是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 全选
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--千十.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--千十下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--千十
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '5')
                break

    def longhh_qg(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--千个
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '6')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('选择的号码是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 全选
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--千百.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--千百下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--千个
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '6')
                break

    def longhh_bs(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--百十
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '7')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('输入的结果是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 全选
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--百十.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--百十下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--百十
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '7')
                break

    def longhh_bg(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--百个
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '8')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('输入的结果是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 全选
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--百个.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--百个下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--百个
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '8')
                break

    def longhh_sg(self, row):
        # 龙虎
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
        # 龙虎--十个
        self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '9')
        self.base_driver.forced_wait(1)
        # 遍历一个号码
        for i in range(3):
            try:
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 3))
                s2 = random.choice(range(0, 3))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历两个号码
                if s0 == 1:
                    if s1 == s2:
                        pass
                    else:
                        print('输入的结果是：' + str(s1) + str(s2))
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 全选
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['LONGHUN'], '2')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-龙虎--十个.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('龙虎--十个下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 龙虎
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '龙虎')
                # 龙虎--十个
                self.base_driver.clicks(self.config_dict_tmm['LONGHU'], '9')
                break

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def quwei_01(self, row):
        # 趣味
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
        # 趣味---一帆风顺
        self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUNWZN'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-趣味---一帆风顺.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('趣味---一帆风顺下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 趣味
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
                # 趣味---一帆风顺
                self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '0')
                break

    def quwei_02(self, row):
        # 趣味
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
        # 趣味---好事成双
        self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '1')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUNWZN'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-趣味---一帆风顺.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('趣味---好事成双下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 趣味
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
                # 趣味---好事成双
                self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '1')
                break

    def quwei_03(self, row):
        # 趣味
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
        # 趣味---三星报喜
        self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '2')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUNWZN'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-趣味---一帆风顺.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('趣味---三星报喜下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 趣味
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
                # 趣味---三星报喜
                self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '2')
                break

    def quwei_04(self, row):
        # 趣味
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
        # 趣味---四季平安
        self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '3')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['QUWEUNWZN'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-趣味---四季平安.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('趣味---四季平安下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 趣味
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '趣味')
                # 趣味---四季平安
                self.base_driver.clicks(self.config_dict_tmm['QUWEUTS'], '3')
                break

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def renxur2_fs(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---复式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '0')
        self.base_driver.forced_wait(1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 任选2个位置并各选1个号码组成一注
        # 万位---千位---百位---十位---个位
        for i in range(100):
            try:
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                if a0 == a1:
                    pass
                else:
                    if a0 == 0 or a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                    if a0 == 1 or a1 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                    if a0 == 2 or a1 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                    if a0 == 3 or a1 == 3:
                        self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                    if a0 == 4 or a1 == 4:
                        self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '0')
                break
        for i in range(20):
            try:
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 5))
                b1 = random.choice(range(0, 5))
                b2 = random.choice(range(0, 5))
                b3 = random.choice(range(0, 5))
                b4 = random.choice(range(0, 5))
                if a0 == a1:
                    pass
                else:
                    if a0 == 0 or a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], b0)
                    if a0 == 1 or a1 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b1)
                    if a0 == 2 or a1 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], b2)
                    if a0 == 3 or a1 == 3:
                        self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], b3)
                    if a0 == 4 or a1 == 4:
                        self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], b4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '0')
                break

    def renxur2_fs_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---复式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个位置并各选1个号码组成一注
        # 万位---千位---百位---十位---个位
        for i in range(50):
            try:
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                if a0 == 0:
                    if a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 1:
                    if a1 == 0:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 2:
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 3:
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 4:
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '0')
                break
        # 随机文字
        for i in range(20):
            try:
                a0 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 5))
                b1 = random.choice(range(0, 5))
                b2 = random.choice(range(0, 5))
                b3 = random.choice(range(0, 5))
                b4 = random.choice(range(0, 5))
                if a0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                if a0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                if a0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], b2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                if a0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], b3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                if a0 == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], b4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '0')
                break

    def renxur2_ds(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---单式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '1')
        self.base_driver.forced_wait(1)
        # 手动勾选任意2个位置，并输入1个两位数号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数
        for i in range(100):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 100)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                #
                c2 = "%02d" % c1
                if a1 == b1:
                    pass
                else:

                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], c2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---单式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '1')
                break

    def renxur2_ds_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---单式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '1')
        self.base_driver.forced_wait(1)
        # 手动勾选任意2个位置，并输入1个两位数号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数
        for i in range(50):
            try:
                a0 = random.choice(range(0, 8))
                b0 = random.choice(range(0, 5))
                b1 = random.choice(range(0, 5))
                b2 = random.choice(range(0, 5))
                b3 = random.choice(range(0, 5))
                b4 = random.choice(range(0, 5))
                c0 = random.choice(range(0, 10000))
                #
                # c2 = "%02d" % c1
                if a0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if a0 == 1:
                    if b0 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if a0 == 2:
                    if b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if a0 == 3:
                    if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if a0 == 4:
                    if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                            or b2 == b3 or b2 == b4 or b3 == b4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if a0 == 5:
                    if c0 < 10:
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], c0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                if a0 == 6:
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], c0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if a0 == 7:
                    if b0 == b1:
                        pass
                    else:
                        if c0 < 10 or c0 > 100:
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                            self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], c0)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任二---单式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        else:
                            pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---单式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '1')
                break

    def renxur2_zux(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---组选
        self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '2')
        self.base_driver.forced_wait(1)
        # 任选2个位置并各选1个号码组成一注注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                b1 = random.choice(range(0, 5))
                c1 = random.choice(range(0, 10))
                d1 = random.choice(range(0, 10))
                if s0 == 0:
                    if a1 == b1:
                        pass
                    else:
                        if c1 == d1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], d1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历全大小单双清
                if s0 == 1:
                    if a1 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], a0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---组选
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '2')
                break

    def renxur2_zux_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---组选
        self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '2')
        self.base_driver.forced_wait(1)
        # 任选2个位置并各选1个号码组成一注注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                a0 = random.choice(range(0, 11))
                b0 = random.choice(range(0, 5))
                b1 = random.choice(range(0, 5))
                b2 = random.choice(range(0, 5))
                b3 = random.choice(range(0, 5))
                b4 = random.choice(range(0, 5))
                c0 = random.choice(range(0, 10))
                print('任选-任二-组选-' + str(a0) + str(b0) + str(b1) + str(b2) + str(b3) + str(b4))
                if a0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                if a0 == 1:
                    if b0 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                if a0 == 2:
                    if b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                if a0 == 3:
                    if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                if a0 == 4:
                    if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                            or b2 == b3 or b2 == b4 or b3 == b4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b4)
                if a0 == 5:
                    print(c0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---组选：  ' + ' ' + str(c0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                if a0 == 6:
                    # 位置，号码各选一个
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                if a0 == 7:
                    # 位置两个，号码一个
                    if b0 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                if a0 == 8:
                    # 位置三个，号码一个
                    if b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                if a0 == 9:
                    # 位置四个，号码一个
                    if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        print(a0, b0, b1, b2, b3, b4)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                if a0 == 10:
                    # 位置三个，号码一个
                    if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                            or b2 == b3 or b2 == b4 or b3 == b4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b4)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任二---组选：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b4)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], c0)
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任二---组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任二---组选
                self.base_driver.clicks(self.config_dict_tmm['RENXUR2'], '2')
                break

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def renxur3_fs(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---复式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个位置并各选1个号码组成一注
        # 万位---千位---百位---十位---个位---任意三个位置的号码
        for i in range(500):
            try:
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                if a0 == 0:
                    # 任意三个位置一个号码
                    if a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        if a1 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        if a1 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                        if a1 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                        if a1 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                        if a1 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                        if a2 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                        if a2 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        if a2 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                        if a2 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                        if a2 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                        if a3 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                        if a3 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                        if a3 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                        if a3 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                        if a3 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if a0 == 1:
                    # 任意四个位置1个号码
                    if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        if a1 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        if a1 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                        if a1 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                        if a1 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                        if a1 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                        if a2 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                        if a2 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        if a2 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                        if a2 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                        if a2 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                        if a3 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                        if a3 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                        if a3 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                        if a3 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                        if a3 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                        if a4 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                        if a4 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                        if a4 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                        if a4 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                        if a4 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            # self.base_driver.forced_wait(5)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if a0 == 2:
                    # 五个位置都随机一个号码
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                    self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                    self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                    self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                    # self.base_driver.forced_wait(5)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '0')
                break
        # # 遍历文字
        '''
        # for i in range(5):
        #     print(i)
        #     self.base_driver.clicks(self.config_dict_tmm['QUWEUNWZN'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        '''

    def renxur3_fs_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---复式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个位置并各选1个号码组成一注
        # 万位---千位---百位---十位---个位
        for i in range(100):
            try:
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                if a0 == 0:
                    # 每个位置选择一位数字
                    # 万位
                    if a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 1:
                    # 每个位置选择；两位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 2:
                    # 每个位置选择；三位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 3:
                    # 每个位置选择；四位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 4:
                    # 每个位置选择；五位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 5:
                    # 每个两位置选择；一位数字
                    # 万位
                    if a1 == a2:
                        pass
                    else:
                        print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                        print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                        if a1 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        if a1 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                        if a1 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                        if a1 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                        if a1 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                        if a2 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                        if a2 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        if a2 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                        if a2 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                        if a2 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                        # self.base_driver.forced_wait(1)
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '0')
                break

        # # 随机文字
        for i in range(20):
            try:
                a0 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 5))
                b1 = random.choice(range(0, 5))
                b2 = random.choice(range(0, 5))
                b3 = random.choice(range(0, 5))
                b4 = random.choice(range(0, 5))
                print(a0, b0, b1, b2, b3, b4)
                if a0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                if a0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                if a0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], b2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                if a0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], b3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                if a0 == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], b4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '0')
                break

    def renxur3_ds(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---单式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '1')
        self.base_driver.forced_wait(1)
        # 手动勾选任意2个位置，并输入1个两位数号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数
        for i in range(100):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                d0 = range(0, 1000)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                d1 = random.choice(d0)
                #
                d2 = "%03d" % d1
                print(d2)
                print(a1+b1)
                if a1 == b1 or a1 == c1 or b1 == c1:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---单式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '1')
                break

    def renxur3_ds_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---单式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '1')
        self.base_driver.forced_wait(1)
        # 手动勾选任意2个位置，并输入1个两位数号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数
        for i in range(100):
            try:
                s0 = random.choice(range(0, 7))
                b0 = random.choice(range(0, 100))
                b1 = random.choice(range(1000, 100000))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                print('s0:  ' + str(s0))
                print('b0:  ' + str(b0))
                print('b1:  ' + str(b1))
                if s0 == 0:
                    # 任选一个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 1:
                    # 任选一个位置。输入一个小于3位数字号码
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 2:
                    # 任选一个位置。输入一个大于3位数字号码
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 3:
                    # 任选两个位置
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 4:
                    # 任选两个位置，少于三位数字的号码
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 5:
                    # 任选两个位置，大于三位数字的号码
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 6:
                    # 输入小于3位数字
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 7:
                    # 输入大于3位数字
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任三---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任二---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---单式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '1')
                break

    def renxur3_zux3(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---组3
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '2')
        self.base_driver.forced_wait(1)
        # 任选3个位置并各选2个号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                d0 = range(0, 10)
                e0 = range(0, 10)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                d1 = random.choice(d0)
                e1 = random.choice(e0)
                if a1 == b1 or a1 == c1 or b1 == c1:
                    pass
                else:
                    if d1 == e1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], d1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], e1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组3.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---组3下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---组3
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '2')
                break

        # 遍历全大小单双清
        for i in range(1):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                if a1 == b1 or a1 == c1 or b1 == c1:
                    pass
                else:
                    for j in range(5):
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], j)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---组选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---组选
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '2')
                break

    def renxur3_zux3_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---组3
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '2')
        self.base_driver.forced_wait(1)
        # 任选3个位置并各选2个号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 10))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                print('s0:  ' + str(s0))
                print('b0:  ' + str(b0))
                print('b1:  ' + str(b1))
                if s0 == 0:
                    # 任选一个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组选---任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 1:
                    # 任选一个位置。输入1位数字号码
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组选---任选一个位置。输入1位数字号码：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                if s0 == 2:
                    # 任选两个位置
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组选---任选两个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 3:
                    # 任选两个位置，输入一个数字
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组选---任选两个位置，输入一个数字：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                if s0 == 4:
                    # 任选三个位置
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组选---任选三个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                if s0 == 5:
                    # 任选四个位置
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组选---任选四个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                if s0 == 6:
                    # 选择号码一个
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组选---选择号码一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                if s0 == 7:
                    # 选择号码两个
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组选---选择号码两个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                if s0 == 8:
                    # 选择位置1个，文字一个
                    print('a0: ' + str(a0))
                    print('a4: ' + str(a4))
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组选---选择位置1个，文字一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], '5')
                if s0 == 9:
                    # 选择位置2个，文字一个
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组选---选择位置1个，文字一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组3.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---组3下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---组3
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '2')
                break

    def renxur3_zux6(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---组6
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '3')
        self.base_driver.forced_wait(1)
        # 任选3个位置并各选3个号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                d0 = range(0, 10)
                e0 = range(0, 10)
                f0 = range(0, 10)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                d1 = random.choice(d0)
                e1 = random.choice(e0)
                f1 = random.choice(f0)
                if a1 == b1 or a1 == c1 or b1 == c1:
                    pass
                else:
                    if d1 == e1 or d1 == f1 or e1 == f1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], d1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], e1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], f1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---组6
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '3')
                break

        # 遍历全大小单双清
        for i in range(10):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                if a1 == b1 or a1 == c1 or b1 == c1:
                    pass
                else:
                    for j in range(5):
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], j)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        self.base_driver.forced_wait(1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---组6下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---组6
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '3')

    def renxur3_zux6_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任三---组六
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '3')
        self.base_driver.forced_wait(1)
        # 任选3个位置并各选3个号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 15))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                if s0 == 0:
                    # 任选一个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组六任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 1:
                    # 任选一个位置。输入1位数字号码
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任三---组六任选一个位置。输入1位数字号码：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                if s0 == 2:
                    # 任选一个位置。输入2位数字号码
                    if b0 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组六任选一个位置。输入1位数字号码：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                if s0 == 3:
                    # 任选两个位置
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组六任选两个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 4:
                    # 任选两个位置，输入一个数字
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组六任选两个位置，输入一个数字：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                if s0 == 5:
                    # 任选两个位置，输入两个数字
                    if a0 == a1:
                        pass
                    else:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任三---组六任选两个位置，输入一个数字：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                if s0 == 6:
                    # 任选三个位置
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组六任选三个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                if s0 == 7:
                    # 任选四个位置
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任三---组六任选四个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                if s0 == 8:
                    # 选择号码一个
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('选择号码一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                if s0 == 9:
                    # 选择号码两个
                    if b0 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('选择号码两个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                if s0 == 10:
                    # 选择号码三个
                    if b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('选择号码两个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b2)
                if s0 == 11:
                    # 选择位置1个，文字一个
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('选择位置1个，文字一个：  ' + ' ' + str(a0) + ' ' + str(a4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], '5')
                if s0 == 12:
                    # 选择位置2个，文字一个
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], a4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('选择位置1个，文字一个：  ' + ' ' + str(a0) + ' ' + str(a1) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMNWZ'], '5')
                if s0 == 13:
                    # 选择号码三个
                    if b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('选择位置1个，文字一个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2HMN'], b2)
                if s0 == 14:
                    # 五个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('选择位置1个，文字一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组6.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---组6下注异常')
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---组6
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '3')
                break

    def renxur3_zuxhh(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---混合组选
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '4')
        self.base_driver.forced_wait(1)
        # 勾选任意3个位置，并手动输入1个三位数号码（不含豹子号）组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                # 数组1000
                d0 = range(0, 1000)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                # 数组1000随机抽取
                d1 = random.choice(d0)
                # 数组不够三位补够三位
                m = "%03d" % d1
                # 切片取数组第一个数字
                s0 = m[0]
                s1 = m[1]
                s2 = m[2]
                if a1 == b1 or a1 == c1 or b1 == c1:
                    pass
                else:
                    # 如果三个数字相同的直接打印，否则运行用例
                    if s0 == s1 == s2:
                        print('豹子数字为:' + str(m))
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], m)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---混合组选下注异常')
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---混合组选
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '4')
                break

    def renxur3_zuxhh_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任二---组选
        self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '4')
        self.base_driver.forced_wait(1)
        # 勾选任意3个位置，并手动输入1个三位数号码（不含豹子号）组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 20))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                # 数组1000随机抽取
                d0 = random.choice(range(0, 100))
                d1 = random.choice(range(999, 10000))
                d2 = random.choice(range(0, 1000))
                # 数组不够三位补够三位
                m = "%03d" % d2
                # 切片取数组第一个数字
                m0 = m[0]
                m1 = m[1]
                m2 = m[2]
                if s0 == 0:
                    # 任选一个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 1:
                    # 任选一个位置,输入小于三位数字
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 2:
                    # 任选一个位置,三位相同的数字
                    print('mmmm:   ' + str(m))
                    if m[0] == m[1] and m[0] == m[2] and m[1] == m[2]:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], m)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    else:
                        pass
                if s0 == 3:
                    # 任选一个位置,输入大于三位数字
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 4:
                    # 任选二个位置
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 5:
                    # 任选两个位置,输入小于三位数字
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 6:
                    # 任选两个位置,三位相同的数字
                    if a0 == a1:
                        pass
                    else:
                        print('mmmm:   ' + str(m))
                        if m[0] == m[1] and m[0] == m[2] and m[1] == m[2]:
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], m)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        else:
                            pass
                if s0 == 7:
                    # 任选两个位置,输入大于三位数字
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 8:
                    # 任选三个位置
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 9:
                    # 任选三个位置,输入小于三位数字
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                if s0 == 10:
                    # 任选三个位置,三位相同的数字
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        print('mmmm:   ' + str(m))
                        if m[0] == m[1] and m[0] == m[2] and m[1] == m[2]:
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                            self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], m)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        else:
                            pass
                if s0 == 11:
                    # 任选三个位置,输入大于三位数字
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                if s0 == 12:
                    # 任选四个位置
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                if s0 == 13:
                    # 任选四个位置,输入小于三位数字
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                if s0 == 14:
                    # 任选四个位置,三位相同的数字
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        print('mmmm:   ' + str(m))
                        if m[0] == m[1] and m[0] == m[2] and m[1] == m[2]:
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                            self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], m)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选一个位置：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                        else:
                            pass
                if s0 == 15:
                    # 任选四个位置,输入大于三位数字
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选四个位置,输入大于三位数字：  ' + ' ' + str(d1) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a3)
                if s0 == 16:
                    # 五个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五个位置：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                if s0 == 17:
                    # 五个位置，小于三位数字
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五个位置，小于三位数字号码是：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                if s0 == 18:
                    # 五个位置，相同三位数字
                    print(' # 五个位置，相同三位数字')
                    if m0 == m1 and m0 == m2 and m1 == m2:
                        print('m0: ' + str(m))
                        print('m0: ' + str(m0))
                        print('m0: ' + str(m1))
                        print('m0: ' + str(m2))
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], m)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五个位置，相同三位数字是：  ' + ' ' + str(m) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                    else:
                        pass
                if s0 == 19:
                    # 五个位置，大于三位数字
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], d1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选一个位置号码是：  ' + ' ' + str(d1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '0')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '1')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '2')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '3')
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], '4')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---混合组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任三---混合组选下注异常')
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任三---混合组选
                self.base_driver.clicks(self.config_dict_tmm['RENXUR3'], '4')
                break
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def renxur4_fs(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任四---复式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '0')
        self.base_driver.forced_wait(1)
        # 勾选任意3个位置，并手动输入1个三位数号码（不含豹子号）组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(100):
            try:
                s0 = random.choice(range(0, 3))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                if s0 == 0:
                    # 任意四个位置一个号码
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        if a0 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        if a0 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                        if a0 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                        if a0 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                        if a0 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                        if a1 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                        if a1 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        if a1 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                        if a1 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                        if a1 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                        if a2 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                        if a2 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                        if a2 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                        if a2 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                        if a2 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                        if a3 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                        if a3 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                        if a3 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                        if a3 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                        if a3 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                    self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                    self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                    self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    pass
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任三---组选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任四---复式下注异常')
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任四---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '0')
                break

    def renxur4_fs_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任四---复式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '0')
        self.base_driver.forced_wait(1)
        # 勾选任意3个位置，并手动输入1个三位数号码（不含豹子号）组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数100次
        for i in range(200):
            try:
                a0 = random.choice(range(0, 11))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                b5 = random.choice(range(0, 10))
                b6 = random.choice(range(0, 10))
                b7 = random.choice(range(0, 10))
                b8 = random.choice(range(0, 10))
                b9 = random.choice(range(0, 10))
                b10 = random.choice(range(0, 10))
                b11 = random.choice(range(0, 10))
                if a0 == 0:
                    # 每个位置选择一位数字
                    # 万位
                    if a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 1:
                    # 每个位置选择；两位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 2:
                    # 每个位置选择；三位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 3:
                    # 每个位置选择；四位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 4:
                    # 每个位置选择；五位数字
                    # 万位
                    if a1 == 0:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                    if a1 == 1:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 5:
                    # 每个两位置选择；一位数字
                    # 万位
                    if a1 == a2:
                        pass
                    else:
                        print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                        print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                        if a1 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                        if a1 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                        if a1 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                        if a1 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                        if a1 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                        if a2 == 0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                        if a2 == 1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                        if a2 == 2:
                            self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                        if a2 == 3:
                            self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                        if a2 == 4:
                            self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                        # self.base_driver.forced_wait(1)
                if a0 == 6:
                    # 每个两位置选择；两位数字
                    # 万位
                    if a1 == a2:
                        print('a1:  ' + str(a1))
                        print('a1:  ' + str(a2))
                        pass
                    else:
                        if b0 == b1 and b2 == b3:
                            pass
                        else:
                            print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                            print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                            if a1 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            if a1 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            if a1 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            if a1 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            if a1 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            if a2 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            if a2 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            if a2 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            if a2 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            if a2 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 7:
                    # 每个两位置选择；三位数字
                    # 万位
                    if a1 == a2:
                        print('a1:  ' + str(a1))
                        print('a1:  ' + str(a2))
                        pass
                    else:
                        if b0 == b1 or b0 == b2 or b1 == b2 and b3 == b4 or b3 == b5 or b4 == b5:
                            pass
                        else:
                            print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                            print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                            if a1 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            if a1 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            if a1 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            if a1 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            if a1 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            if a2 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                            if a2 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b5)
                            if a2 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b5)
                            if a2 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b5)
                            if a2 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 8:
                    # 每个三位置选择；两位数字
                    # 万位
                    if a1 == a2 or a1 == a3 or a2 == a3:
                        print('a1:  ' + str(a1))
                        print('a1:  ' + str(a2))
                        pass
                    else:
                        if b0 == b1 and b2 == b3:
                            pass
                        else:
                            print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                            print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                            if a1 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                            if a1 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            if a1 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                            if a1 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                            if a1 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                            if a2 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            if a2 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            if a2 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            if a2 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            if a2 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            if a3 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                            if a3 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b5)
                            if a3 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b5)
                            if a3 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b5)
                            if a3 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 9:
                    # 每个三位置选择；三位数字
                    # 万位
                    if a1 == a2 or a1 == a3 or a2 == a3:
                        print('a1:  ' + str(a1))
                        print('a1:  ' + str(a2))
                        pass
                    else:
                        if b0 == b1 or b0 == b2 or b1 == b2 and b3 == b4 or b3 == b5 or b4 == b5:
                            pass
                        else:
                            print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                            print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                            if a1 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                            if a1 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            if a1 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                            if a1 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                            if a1 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                            if a2 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                            if a2 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b5)
                            if a2 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b5)
                            if a2 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b5)
                            if a2 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b5)
                            if a3 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b7)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b8)
                            if a3 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b7)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b8)
                            if a3 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b7)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b8)
                            if a3 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b7)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b8)
                            if a3 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b7)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b8)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                if a0 == 10:
                    # 每个三位置选择；四位数字
                    # 万位
                    if a1 == a2 or a1 == a3 or a2 == a3:
                        print('a1:  ' + str(a1))
                        print('a1:  ' + str(a2))
                        pass
                    else:
                        if b0 == b1 and b2 == b3:
                            pass
                        else:
                            print('a1:  ' + str(a1) + 'b0:  ' + str(b0))
                            print('a2:  ' + str(a2) + 'a0:  ' + str(a0))
                            if a1 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b3)
                            if a1 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            if a1 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDB'], b3)
                            if a1 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDS'], b3)
                            if a1 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b0)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b1)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b2)
                                self.base_driver.clicks(self.config_dict_tmm['DWDG'], b3)
                            if a2 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b7)
                            if a2 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b7)
                            if a2 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b7)
                            if a2 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b7)
                            if a2 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b4)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b5)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b6)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b7)
                            if a3 == 0:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b8)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b9)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b10)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b11)
                            if a3 == 1:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b8)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b9)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b10)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b11)
                            if a3 == 2:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b8)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b9)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b10)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b11)
                            if a3 == 3:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b8)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b9)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b10)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b11)
                            if a3 == 4:
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b8)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b9)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b10)
                                self.base_driver.clicks(self.config_dict_tmm['DWDW'], b11)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('任选---任四---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任四---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任四---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任四---复式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '0')
                break

    def renxur4_ds(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任四---单式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '1')
        self.base_driver.forced_wait(1)
        # 手动勾选任意4个位置，并输入1个四位数号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数
        for i in range(100):
            try:
                a0 = range(0, 5)
                b0 = range(0, 5)
                c0 = range(0, 5)
                d0 = range(0, 5)
                e0 = range(0, 10000)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                d1 = random.choice(d0)
                e1 = random.choice(e0)
                #
                e2 = "%04d" % e1
                print('e2:    ' + str(e2))
                if a1 != b1 and a1 != c1 and a1 != d1 and b1 != c1 and b1 != d1 and c1 != d1:
                    print("aaa:"+str(a1)+str(b1)+str(c1)+str(d1))
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], b1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], c1)
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], d1)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], e2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任四---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任四---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任四---单式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '1')
                break

    def renxur4_ds_error(self, row):
        # 任选
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
        # 任选---任四---单式
        self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '1')
        self.base_driver.forced_wait(1)
        # 手动勾选任意4个位置，并输入1个四位数号码组成一注
        # 万位---千位---百位---十位---个位
        # 运行次数
        for i in range(100):
            try:
                s0 = random.choice(range(0, 7))
                b0 = random.choice(range(0, 1000))
                b1 = random.choice(range(10000, 100000))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                print('s0:  ' + str(s0))
                print('b0:  ' + str(b0))
                print('b1:  ' + str(b1))
                if s0 == 0:
                    # 任选一个位置
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 1:
                    # 任选一个位置。输入一个小于4位数字号码
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 2:
                    # 任选一个位置。输入一个大于4位数字号码
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                if s0 == 3:
                    # 任选两个位置
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 4:
                    # 任选两个位置，少于四位数字的号码
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 5:
                    # 任选两个位置，大于四位数字的号码
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 6:
                    # 任选三个位置，少于四位数字的号码
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 7:
                    # 任选三个位置，大于四位数字的号码
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a2)
                        self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['RENXUR2WZN'], a1)
                if s0 == 8:
                    # 输入小于四位数字
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 9:
                    # 输入大于四位数字
                    self.base_driver.type(self.config_dict_tmm['RENXUR2WZTEXT'], b1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('任选---任四---单式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-任选---任四---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('任选---任四---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 任选
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '任选')
                # 任选---任四---单式
                self.base_driver.clicks(self.config_dict_tmm['RENXUR4'], '1')
                break
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def bdws3_h31(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---后三一码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---后三一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---后三一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---后三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '0')
                break

    def bdws3_z31(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---中三一码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '1')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---中三一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---后三一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---后三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '1')
                break

    def bdws3_q31(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---前三一码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '2')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---前三一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---前三一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---前三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '2')
                break

    def bdws3_h32(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---后三二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '3')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 5))
                if s0 == 0:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---后三二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---后三二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---后三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '3')
                break

    def bdws3_h32_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---后三二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '3')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('不定位---三星不定位---后三二码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---后三二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---后三二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---后三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '3')
                break

    def bdws3_z32(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---中三二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '4')
        self.base_driver.forced_wait(1)
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 5))
                if s0 == 0:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---中三二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位--中三二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---中三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '3')
                break

    def bdws3_z32_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---中三二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '4')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('不定位---三星不定位---中三二码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---中三二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---中三二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---中三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '4')
                break

    def bdws3_q32(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---前三二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '5')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 5))
                if s0 == 0:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---后三二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---后三二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---后三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '5')
                break

    def bdws3_q32_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---前三二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '5')
        self.base_driver.forced_wait(1)
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('不定位---三星不定位---前三二码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---三星不定位---前三二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---三星不定位---前三二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---三星不定位---前三一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS3'], '5')
                break

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------

    def bdws4_q41(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---前四一码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---前四一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---前四一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---前四一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '0')
                break

    def bdws4_h41(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---后四一码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '1')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---后四一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---后四一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---后四一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '1')
                break

    def bdws4_q42(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---前四二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '2')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 5))
                if s0 == 0:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---前四二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---前四二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---前四二码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '2')
                break

    def bdws4_q42_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---前四二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '2')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('不定位---四星不定位---前四二码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---前四二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---前四二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---前四二码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '2')
                break

    def bdws4_h42(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---后四二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '3')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 5))
                if s0 == 0:
                    if s1 == s2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---后四二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---后四二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---后四二码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '3')
                break

    def bdws4_h42_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---后四二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '3')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('不定位---四星不定位---后四二码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---后四二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---后四二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---后四二码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '3')
                break

    def bdws4_q43(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---前四三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '4')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             if i == j or i == k or j == k:
        #                 pass
        #             else:
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], k)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

        # 随机三个号码
        # 随机次数10
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                c1 = random.choice(range(0, 10))
                c2 = random.choice(range(0, 5))
                if s0 == 0:
                    if a1 == b1 or a1 == c1 or b1 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], c1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    # 遍历文字
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], c2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---前四三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---前四三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---前四三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '4')
                break

    def bdws4_q43_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---前四三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '4')
        self.base_driver.forced_wait(1)
        # 随机一注下不了注
        for i in range(30):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('不定位---四星不定位---前四三码：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                # 随机二个号码下了注
                # 随机次数10
                if s0 == 1:
                    if a1 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('不定位---四星不定位---前四三码：  ' + ' ' + str(a1) + ' ' + str(b1) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---前四三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---前四三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---前四三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '4')
                break

    def bdws4_h43(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---四星不定位---后四三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '5')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             if i == j or i == k or j == k:
        #                 pass
        #             else:
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], k)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

        # 随机三个号码
        # 随机次数10
        for i in range(50):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                c1 = random.choice(range(0, 10))
                c2 = random.choice(range(0, 5))
                if s0 == 0:
                    if a1 == b1 or a1 == c1 or b1 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], c1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], c2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---后四三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---后四三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---后四三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '5')
                break

    def bdws4_h43_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---三星不定位---后四三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '5')
        self.base_driver.forced_wait(1)
        # 随机一注下不了注
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('不定位---四星不定位---后四三码：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                # 随机两注下不了注
                if s0 == 1:
                    if a1 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('不定位---四星不定位---后四三码：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---四星不定位---后四三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---四星不定位---后四三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---四星不定位---后四三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS4'], '5')
                break

    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def bdws5_s51(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星一码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '0')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], s2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '0')
                break

    def bdws5_s52(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '1')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         if i == j:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['BDWSN'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

        # 随机二个号码
        # 随机次数10
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 5))
                if s0 == 0:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], b0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星一码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星一码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星一码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '1')
                break

    def bdws5_s52_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星二码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '1')
        self.base_driver.forced_wait(1)
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('不定位---五星不定位---五星二码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星二码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星二码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星二码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '1')
                break

    def bdws5_s53(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '2')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             if i == j or i == k or j == k:
        #                 pass
        #             else:
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['BDWSN'], k)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

        # 随机三个号码
        # 随机次数10
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 5))
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '2')
                break

    def bdws5_s53_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '2')
        self.base_driver.forced_wait(1)
        # 随机一注下不了单
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('不定位---五星不定位---五星三码：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                # 随机两注下不了单
                if s0 == 1:
                    if a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('不定位---五星不定位---五星三码：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '2')
                break

    def bdws5_s54(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星四码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '3')
        self.base_driver.forced_wait(1)
        # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or j == k or i == m or j == m or k == m:
        #                     pass
        #                 else:
        #                     self.base_driver.clicks(self.config_dict_tmm['BDWSN'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['BDWSN'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['BDWSN'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['BDWSN'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

        # 随机三个号码
        # 随机次数10
        for i in range(100):
            try:
                a0 = range(0, 10)
                b0 = range(0, 10)
                c0 = range(0, 10)
                d0 = range(0, 10)
                a1 = random.choice(a0)
                b1 = random.choice(b0)
                c1 = random.choice(c0)
                d1 = random.choice(d0)
                if a1 == b1 or a1 == c1 or b1 == c1 or a1 == d1 or c1 == d1 or b1 == d1:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], b1)
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], c1)
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], d1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星四码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星四码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星四码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '3')
                break
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['BDWSWZ'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    def bdws5_s54_error(self, row):
        # 不定位
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
        # 不定位---五星不定位---五星三码
        self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '3')
        self.base_driver.forced_wait(1)
        # 随机一注下不了单
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('不定位---五星不定位---五星三码：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')

                # 随机两注下不了单
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('不定位---五星不定位---五星三码：  ' + ' ' + str(a0) + ' ' + str(a1) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                # 随机三注下不了单
                if s0 == 2:
                    if a0 == a1 or a0 == a1 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['BDWSN'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('不定位---五星不定位---五星三码：  ' + ' ' + str(a0) + ' ' + str(a1)
                              + ' ' + str(a2) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-不定位---五星不定位---五星三码.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('不定位---五星不定位---五星三码下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 不定位
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '不定位')
                # 不定位---五星不定位---五星三码
                self.base_driver.clicks(self.config_dict_tmm['BDWS5'], '3')
                break
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------
    # -----------------------------------------------------------------

    def dwd(self, row):
        # 定位胆
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '定位胆')
        # 定位胆---定位胆---定位胆
        # self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '0')
        # self.base_driver.forced_wait(5)
        # # 任选1个号码，循环10次
        # 任选1个位置并选1个号码组成一注
        # # 第一位
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 第二位
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDQ'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 第三位
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDB'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 第四位
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDS'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 第五位
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDG'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDB'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDS'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDG'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-定位胆---定位胆---定位胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('定位胆---定位胆---定位胆下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 定位胆---定位胆---定位胆
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '定位胆')
                break
        # 遍历文字
        for i in range(20):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-定位胆---定位胆---定位胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('定位胆---定位胆---定位胆下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 定位胆---定位胆---定位胆
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '定位胆')
                break

    # --------------------------------------------------------
    # --------------------------------------------------------
    # --------------------------------------------------------

    def star2_h2zhxfs(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二直选---复式
        self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '0')
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #         self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #         self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

        # 百位---十位---个位随机抽取一个数字,抽取300次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                print(a, b,)
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '0')
                break
        # 遍历文字
        for i in range(10):
            try:
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a0)
                self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '0')
                break

    def star2_h2zhxfs_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二直选---复式
        self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '0')
        # 遍历10个号码
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('二星---后二直选---复式：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
        '''
        # 十位或个位随机抽取一到六个数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                b5 = random.choice(range(0, 10))
                print(s0, a0, a1, b0, b1, b2, b3, b4, b5)
                if s0 == 0:
                    if a0 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 5:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                                or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 \
                                or b3 == b5 or b4 == b5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b4)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    else:
                        # self.base_driver.forced_wait(3)
                        pass
                else:
                    if a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 5:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                                or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 \
                                or b3 == b5 or b4 == b5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b4)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---后二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')

                    else:
                        # self.base_driver.forced_wait(3)
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---复式
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '0')
                break
                
    def star2_h2zhxds(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二直选---单式
        self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '1')
        # 随机输入两位数字
        # 随机10次
        for i in range(100):
            try:
                # d0 = range(0, 100)
                # d1 = random.choice(d0)
                d2 = "%02d" % random.choice(range(0, 100))
                self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], d2)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '1')
                break

    def star2_h2zhxds_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二直选---单式
        self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '1')
        # 随机输入两位数字
        # 输入1位数字
        for i in range(10):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(101, 100000))
                if s0 == 0:
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---后二直选---单式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 1:
                    # 输入三位相同数字
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], str(a0) + '' + str(a0) + '' + str(a0))
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---后二直选---单式：  ' + str(a0) + '' + str(a0) + '' + str(a0) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 2:
                    # 输入四位相同数字
                    ss = str(a0) + '' + str(a0) + '' + str(a0) + '' + str(a0)
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], ss)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---后二直选---单式：  ' + str(ss) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 3:
                    # 输入五位相同数字
                    ss = str(a0) + '' + str(a0) + '' + str(a0) + '' + str(a0) + '' + str(a0)
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], 'ss')
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---后二直选---单式：  ' + str(ss) + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 4:
                   # 随机100个三到六位的数字
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---后二直选---单式：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---单式
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '1')
                break

    def star2_h2zhxzxhz(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二直选---直选和值
        self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '2')
        # 遍历10个号码
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 15))
                a2 = random.choice(range(0, 4))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN1'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN2'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '2')
                break

    def star2_h2zhxzxkd(self, row):
        # 三星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 三星---后三直选---直选跨度
        self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '3')
        # 遍历10个号码
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN1'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---直选跨度.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---直选跨度下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---直选跨度
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '3')
                break

    def star2_h2zhxhzws(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二直选---直选尾数
        self.base_driver.clicks(self.config_dict_tmm['H3ZHX'], '4')
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二直选---直选尾数.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二直选---直选尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二直选---直选尾数
                self.base_driver.clicks(self.config_dict_tmm['H2ZHX'], '4')
                break

    # ------------------------------------------------------
    # ------------------------------------------------------
    # ------------------------------------------------------

    def star2_h2zuxfs(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二组选---复式
        self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        # for i in range(10):
        #     try:
        #         a1 = random.choice(range(1, 10))
        #         a2 = random.choice(range(1, 10))
        #         if a1 == a2:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #             self.base_driver.forced_wait(1)
        #     except Exception as e:
        #         print(e)
        #         now_Time = time.strftime("%Y%m%d.%H.%M.%S")
        #         s = '/fusion/pictures/time_mm/' + '%s-二星---后二组选---直选和值.png' % now_Time
        #         self.base_driver.save_window_snapshot_by_io(s)
        #         # self.logger.infos('二星---后二组选---直选和值下注异常')
        #         # 二星
        #         self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        #         # 二星---后二组选---复式
        #         self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '0')
        # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         if i == j or i < j:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #             # self.base_driver.forced_wait(1)
        # 随机1-6个选号
        for i in range(100):
            try:
                a0 = random.choice(range(0, 5))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                b5 = random.choice(range(0, 10))
                print(a0, b0, b1, b2, b3, b4, b5)
                if a0 == 0:
                    # 随机2个选号
                    if b0 == b1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if a0 == 1:
                    # 随机3个选号
                    if b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if a0 == 2:
                    # 随机4个选号
                    if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if a0 == 3:
                    # 随机5个选号
                    if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 or b2 == b3 \
                            or b2 == b4 or b3 == b4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if a0 == 4:
                    # 随机6个选号
                    if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 or b1 == b4 \
                            or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 or b3 == b5 or b4 == b5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b4)
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b5)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                else:
                    # self.base_driver.forced_wait(3)
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二组选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二组选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二组选---复式
                self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '0')
                break

        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)

    def star2_h2zuxfs_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二组选---复式
        self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print(' 二星---后二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二组选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二组选---复式
                self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '0')
                break

    def star2_h2zuxds(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        self.base_driver.forced_wait(1)
        # 二星---后二组选---单式
        self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 随机输入两位数字
        # 随机10次
        for i in range(100):
            try:
                d0 = range(0, 100)
                d1 = random.choice(d0)
                d2 = "%02d" % d1
                s0 = d2[0]
                s1 = d2[1]
                if s0 == s1:
                    pass
                else:
                    print(d2)
                    self.base_driver.type(self.config_dict_tmm['H2ZUXTEXT'], d2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二组选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二组选---单式
                self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '1')
                break

    def star2_h2zuxds_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        self.base_driver.forced_wait(1)
        # 二星---后二组选---单式
        self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '1')
        self.base_driver.forced_wait(1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 输入1位数字

        # for i in range(10):
        #     self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        #     print('二星---后二组选---单式：  ' + ' ' + str(i) + ' ' + str(s))
        #     self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])

        # 输入三位到五位的数字
        for i in range(200):
            try:
                d1 = random.choice(range(101, 100000))
                # d2 = "%03d" % d1
                print(d1)
                self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], d1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('二星--后二组选--单式：  ' + ' ' + str(d1) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二组选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二组选---单式
                self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '1')
                break

    def star2_h2zuxbd(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---后二组选---组选包胆
        self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '2')
        self.base_driver.forced_wait(1)
        # # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---后二组选---组选包胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---后二组选---组选包胆下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---后二组选---组选包胆
                self.base_driver.clicks(self.config_dict_tmm['H2ZUXN'], '2')
                break
        # # 遍历所有组合
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     # self.base_driver.forced_wait(1)
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # ---------------------------------------------------------

    def star2_q2zhxfs(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '0')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        # for i in range(10):
        #     for j in range(10):
        #         self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
        #         self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
        #         self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # 百位---十位---个位随机抽取一个数字
        # 抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], a)
                self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '0')
                break

        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---复式.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('二星---前二直选---复式下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 二星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                    # 二星---前二直选---复式
                    self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '0')
                    break

    def star2_q2zhxfs_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '0')
        self.base_driver.forced_wait(1)
        # # 遍历10个号码
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('二星---前二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('二星---前二直选---复式：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
        '''
        # 十位或个位随机抽取一到六个数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                b5 = random.choice(range(0, 10))
                if s0 == 0:
                    if a0 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('二星---前二直选---复式：  ' + ' ' + str(b0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：' + ' ' + str(b0) + ' ' + str(b1) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：' + ' ' + str(b0)
                                  + ' ' + str(b1) + ' ' + str(b2) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            ss = ' ' + str(b0) + ' ' + str(b1) + ' ' + str(b2) + ' ' + str(b3) + ' ' + str(s)
                            print('二星---前二直选---复式：' + str(ss))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            ss = str(b0) + ' ' + str(b1) + ' ' + str(b2) + ' ' + str(b3) + ' ' + str(b4) + ' ' + str(s)
                            print('二星---前二直选---复式：  ' + str(ss))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if a0 == 5:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                                or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 \
                                or b3 == b5 or b4 == b5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b4)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMB'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            ss = str(b0) + ' ' + str(b1) + ' ' + str(b2) + ' ' + str(b3) + ' ' + str(b4) + ' ' + str(b5)
                            print('二星---前二直选---复式：  ' + ' ' + str(ss) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    else:
                        # self.base_driver.forced_wait(3)
                        pass
                else:
                    if a1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('二星---前二直选---复式：  ' + ' ' + str(b0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：' + str(b0) + ' ' + str(b1) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：' + str(b0) + ' ' + str(b1) + ' ' + str(b2) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 3:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 4:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 or b1 == b3 \
                                or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if a1 == 5:
                        if b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                                or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 \
                                or b3 == b5 or b4 == b5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b4)
                            self.base_driver.clicks(self.config_dict_tmm['TTMMS'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('二星---前二直选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        # self.base_driver.forced_wait(3)
                        pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '0')
                break

    def star2_q2zhxds(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '1')
        for i in range(100):
            try:
                d1 = random.choice(range(0, 100))
                d2 = "%02d" % d1
                self.base_driver.type(self.config_dict_tmm['Q2ZHXTEXT'], d2)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '1')
                break

    def star2_q2zhxds_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '1')
        # 输入1位数字
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(101, 100000))
                s3 = "%03d" % s2
                if s0 == 0:
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], s1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二直选---单式：  ' + ' ' + str(s1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入三位到五位的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], s3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二直选---单式：  ' + ' ' + str(s3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '1')
                break

    def star2_q2zhxzxhz(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---直选和值
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '2')
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 15))
                a1 = random.choice(range(0, 4))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN1'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['H3ZHXHEN2'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---直选和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---直选和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---直选和值
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '2')
                break

    def star2_q2zhxzxkd(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---直选跨度
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '3')
        # 遍历10个号码
        for i in range(15):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                # 遍历文字
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---直选跨度.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---直选跨度下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---直选跨度
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '3')
                break

    def star2_q2zhxhzws(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二直选---和值尾数
        self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '4')
        # 遍历10个号码
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二直选---和值尾数.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二直选---和值尾数下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二直选---和值尾数
                self.base_driver.clicks(self.config_dict_tmm['Q2ZHXN'], '4')
                break
    # -----------------------------------------------------
    # -----------------------------------------------------
    # -----------------------------------------------------
    # -----------------------------------------------------

    def star2_q2zuxfs(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二组选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '0')
        self.base_driver.forced_wait(1)
        # 任选2个号码，循环10次
        for i in range(100):
            try:
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                if a1 == a2:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                    self.base_driver.clicks(self.config_dict_tmm['N0_9'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二组选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二组选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '0')
                break
        # # 遍历所有组合
        # for i in range(10):
        #     for j in range(10):
        #         if i == j:
        #             pass
        #         else:
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['N0_9'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #             # self.base_driver.forced_wait(1)
            # 遍历文字
        for i in range(5):
            try:
                self.base_driver.clicks(self.config_dict_tmm['N0_9WENZI'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二组选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二组选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '0')
                break

    def star2_q2zuxfs_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二组选---复式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '0')
        self.base_driver.forced_wait(1)
        for i in range(10):
            try:
                self.base_driver.clicks(self.config_dict_tmm['TTMMB'], i)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二组选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二组选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二组选---复式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '0')
                break

    def star2_q2zuxds(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二组选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '1')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                d0 = range(0, 100)
                d1 = random.choice(d0)
                d2 = "%02d" % d1
                # 取数组第一个数字
                s0 = d2[0]
                s1 = d2[1]
                if s0 == s1:
                    pass
                else:
                    print('输入的数字是： ' + str(d2))
                    self.base_driver.type(self.config_dict_tmm['Q2ZUXTEXT'], d2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二组选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二组选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '1')
                break

    def star2_q2zuxds_error(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二组选---单式
        self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '1')
        self.base_driver.forced_wait(1)
        # 输入1位数字
        for i in range(50):
            try:
                s0 = random.choice(0, 2)
                a0 = random.choice(0, 10)
                d0 = range(101, 100000)
                d1 = random.choice(d0)
                d2 = "%03d" % d1
                if a0 == 0:
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---单式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                # 输入三位到五位的数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_tmm['H2ZHXTEXT'], d2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---单式：  ' + ' ' + str(d2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二组选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二组选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二组选---单式
                self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '1')
                break

    def star2_q2zuxbd(self, row):
        # 二星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
        # 二星---前二组选---组选包胆
        self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '2')
        # self.base_driver.forced_wait(5)
        # # 任选1个号码，循环10次
        for i in range(10):
            try:
                a1 = random.choice(range(1, 10))
                self.base_driver.clicks(self.config_dict_tmm['N0_9'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-二星---前二组选---组选包胆.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('二星---前二组选---组选包胆下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '二星')
                # 二星---前二组选---组选包胆
                self.base_driver.clicks(self.config_dict_tmm['Q2ZUXN'], '1')
                break
        # 遍历所有组合
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['N0_9'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            # self.base_driver.forced_wait(1)

    # --------------------------------------------------------
    # --------------------------------------------------------
    # --------------------------------------------------------
    def star5_s5zhixfs(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星直选---复式
        self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '0')

        # 任选1个号码，循环10次
        # 任选1个位置并选1个号码组成一注
        # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 for n in range(10):
        #                     if i > j or i > k or i > m or i > n or j > k or j > m or j > n or k > m or k > n or m > n:
        #                         # print(i, j, k, m, n)
        #                         pass
        #                     else:
        #                         print(i, j, k, m, n)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDB'], k)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDS'], m)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDG'], n)
        #                         self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                e = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                self.base_driver.clicks(self.config_dict_tmm['DWDB'], c)
                self.base_driver.clicks(self.config_dict_tmm['DWDS'], d)
                self.base_driver.clicks(self.config_dict_tmm['DWDG'], e)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---复式
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '0')
                break
        # 遍历文字
        for i in range(5):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                e = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a)
                self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b)
                self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], c)
                self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], d)
                self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], e)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---复式
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '0')
                break

    def star5_s5zhixfs_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星直选---复式
        self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '0')

        # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s = random.choice(range(0, 5))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                e = random.choice(range(0, 10))
                if s == 0:
                    # 万位
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                if s == 1:
                    # 千万
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                if s == 2:
                    # 百位
                    self.base_driver.clicks(self.config_dict_tmm['DWDB'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                if s == 3:
                    # 十位
                    self.base_driver.clicks(self.config_dict_tmm['DWDS'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                if s == 4:
                    # 个位
                    self.base_driver.clicks(self.config_dict_tmm['DWDG'], e)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---复式
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '0')
                break
        # 遍历文字
        for i in range(20):
            try:
                s = random.choice(range(0, 5))
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                e = random.choice(range(0, 5))
                if s == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                if s == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                if s == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                if s == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                if s == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], e)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---复式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---复式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---复式
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '0')
                break

    def star5_s5zhixds(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星直选---单式
        self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '1')
        # 任选1个号码，循环10次
        # 手动输入1个五位数号码组成一注
        for i in range(100):
            try:
                d0 = range(0, 100000)
                d1 = random.choice(d0)
                d2 = "%05d" % d1
                self.base_driver.type(self.config_dict_tmm['S5ZHIXTEXT'], d2)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---单式
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '1')
                break

    def star5_s5zhixds_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星直选---单式
        self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '1')
        # 任选1个号码，循环10次
        # 手动输入1个四位数号码组成一注
        for i in range(100):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 10000))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                a5 = random.choice(range(0, 10))
                a6 = random.choice(range(0, 10))
                if s0 == 0:
                    # 输入1到4位数字的号码
                    self.base_driver.type(self.config_dict_tmm['S5ZHIXTEXT'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                if s0 == 1:
                    # 输入六位数字
                    b = str(a1) + '' + str(a2) + '' + str(a3) + '' + str(a4) + '' + str(a5) + '' + str(a6)
                    self.base_driver.type(self.config_dict_tmm['S5ZHIXTEXT'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + '123456' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---单式.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---单式下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---单式
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '1')
                break

    def star5_s5zhixzuhe(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星直选---组合
        self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '2')

        # 任选1个号码，循环10次
        # 任选1个位置并选1个号码组成一注
        # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 for n in range(10):
        #                     if i > j or i > k or i > m or i > n or j > k or j > m or j > n or k > m or k > n or m > n:
        #                         # print(i, j, k, m, n)
        #                         pass
        #                     else:
        #                         print(i, j, k, m, n)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDB'], k)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDS'], m)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDG'], n)
        #                         self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                e = random.choice(range(0, 10))
                self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                self.base_driver.clicks(self.config_dict_tmm['DWDB'], c)
                self.base_driver.clicks(self.config_dict_tmm['DWDS'], d)
                self.base_driver.clicks(self.config_dict_tmm['DWDG'], e)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---组合
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '2')
                break
        # 遍历文字
        for i in range(5):
            try:
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                e = random.choice(range(0, 5))
                self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a)
                self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b)
                self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], c)
                self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], d)
                self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], e)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---组合
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '2')
                break

    def star5_s5zhixzuhe_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星直选---复式
        self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '2')
        # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s = random.choice(range(0, 5))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                e = random.choice(range(0, 10))
                if s == 0:
                    # 万位
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                if s == 1:
                    # 千万
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                if s == 2:
                    # 百位
                    self.base_driver.clicks(self.config_dict_tmm['DWDB'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                if s == 3:
                    # 十位
                    self.base_driver.clicks(self.config_dict_tmm['DWDS'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                if s == 4:
                    # 个位
                    self.base_driver.clicks(self.config_dict_tmm['DWDG'], e)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---组合
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '2')
                break
        # 遍历文字
        for i in range(20):
            try:
                s = random.choice(range(0, 5))
                a = random.choice(range(0, 5))
                b = random.choice(range(0, 5))
                c = random.choice(range(0, 5))
                d = random.choice(range(0, 5))
                e = random.choice(range(0, 5))
                if s == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], '5')
                if s == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], '5')
                if s == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDBWZ'], '5')
                if s == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDSWZ'], '5')
                if s == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], e)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('二星---前二组选---复式：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDGWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星直选---组合
                self.base_driver.clicks(self.config_dict_tmm['S5ZHIX'], '2')
                break

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # ------------------------------------------------------------
    # ------------------------------------------------------------

    def star5_s5zuxz120(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选120
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '0')

        # 任选1个号码，循环10次
        # 任选1个位置并选1个号码组成一注
        # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 for n in range(10):
        #                     if i >= j or i >= k or i >= m or i >= n or j >= k or j >= m or j >= n \
        #                             or k >= m or k >= n or m >= n:
        #                         pass
        #                     else:
        #                         print(i, j, k, m, n)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], j)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], k)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], m)
        #                         self.base_driver.clicks(self.config_dict_tmm['DWDW'], n)
        #                         self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                e = random.choice(range(0, 10))
                if a == b or a == c or a == d or a == e or b == c or b == d or b == e \
                        or c == d or c == e or d == e:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], c)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], d)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], e)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组合.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---组合下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选120
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '0')
                break
        # 遍历文字
        for i in range(5):
            self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])

    def star5_s5zuxz120_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选120
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '0')
        # 任选1个号码，循环10次
        # 任选1个位置并选1个号码组成一注
        # # 第一位
        #
        # # 每个号码抽一位数字
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        #     print('五星---五星组选---组选120：  ' + ' ' + str(i) + ' ' + str(s))
        #     self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
        #     self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)

        for i in range(50):

            try:
                s = random.choice(range(0, 4))
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                if s == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                if s == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s == 2:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], c)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选120.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星直选---组选120下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选120
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '0')
                break

    def star5_s5zuxz60(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选60
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '1')

        # 任选1个号码，循环10次
        # 任选1个位置并选1个号码组成一注
        # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             for m in range(10):
        #                 if i == j or i == k or i == m or j >= k or j >= m or k >= m:
        #                     pass
        #                 else:
        #                     print(i, j, k, m)
        #                     self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #                     self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #                     self.base_driver.clicks(self.config_dict_tmm['DWDQ'], k)
        #                     self.base_driver.clicks(self.config_dict_tmm['DWDQ'], m)
        #                     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                d = random.choice(range(0, 10))
                if a == b or a == c or a == d or b == c or b == d or c == d:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], d)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选60.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选60下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选60
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '1')
                break
        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选60.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('五星---五星组选---组选60下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 五星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                    # 五星---五星组选---组选60
                    self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '1')
                    break

    def star5_s5zuxz60_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选60
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '1')
        # 任选1个号码，循环10次
        # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('五星---五星组选---组选120：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('五星---五星组选---组选120：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
        '''
        # 二重号有一个跟单号相同时不能下注
        for i in range(50):
            try:
                s0 = random.choice(range(0, 5))
                m0 = random.choice(range(0, 5))
                m1 = random.choice(range(0, 3))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 5))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                a5 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                b2 = random.choice(range(0, 10))
                b3 = random.choice(range(0, 10))
                b4 = random.choice(range(0, 10))
                b5 = random.choice(range(0, 10))
                c0 = random.choice(range(0, 10))
                c1 = random.choice(range(0, 10))
                c2 = random.choice(range(0, 10))
                c3 = random.choice(range(0, 10))
                print(s0, m0, m1, a0, a1, a2, a3, a4, a5, b0, b1, b2, b3, b4, b5, c0, c1)
                print('------------------')
                print('------------------')
                print('------------------')
                if s0 == 0:
                    if m0 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if m0 == 1:
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if m0 == 2:
                        if a0 == a1 or a0 == a2 or a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if m0 == 3:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if m0 == 4:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                                or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    if m0 == 5:
                        if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 \
                                or a1 == a4 or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 \
                                or a3 == a5 or a3 == a5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a4)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    else:
                        pass
                if s0 == 1:
                    if m1 == 0:
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if m1 == 1:
                        if b0 == b1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if m1 == 2:
                        if b0 == b1 or b0 == b2 or b1 == b2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if m1 == 3:
                        if b0 == b1 or b0 == b2 or a0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if m1 == 4:
                        if b0 == b1 or b0 == b2 or a0 == b3 or a0 == b4 or b1 == b2 or b1 == b3 or b1 == b4 \
                                or b2 == b3 or b2 == b4 or b3 == b4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    if m1 == 5:
                        if b0 == b1 or b0 == b2 or a0 == b3 or a0 == b4 or a0 == b5 or b1 == b2 or b1 == b3 \
                                or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 \
                                or b3 == b5 or b4 == b5:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b3)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b4)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b5)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 2:
                    # 二重号随机一个，单号一个
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], c0)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 3:
                    # 二重号随机一个，单号三个
                    if c1 == c2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], c0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 4:
                    # 二重号随机一个，单号三个，二重号与单号其中一个相同
                    if c0 == c1 or c0 == c2 or c0 == c3:
                        if c1 == c2 or c0 == c3 or c1 == c3 or c2 == c3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], c0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c2)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c3)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选60.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选60下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选60
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '1')
                break

    def star5_s5zuxz30(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选60
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '2')
        # 任选1个号码，循环10次
        # 选2个二重号，1个单号组成一注
        # # 第一位
        '''
        for i in range(10):
            for j in range(10):
                for k in range(10):
                        if i >= j or i == k or j == k:
                            pass
                        else:
                            print(i, j, k)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], j)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], k)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        '''
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                if a == b or a == c or b == c:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], b)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选30.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选30下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选30
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '2')
                break
        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选30.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('五星---五星组选---组选30下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 五星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                    # 五星---五星组选---组选30
                    self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '2')
                    break

    def star5_s5zuxz30_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选30
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '2')

        # 任选1个号码，循环10次
        # 选2个二重号，1个单号组成一注
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('五星---五星组选---组选120：  ' + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('五星---五星组选---组选120：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
        '''
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                if s0 == 0:
                    # 二重号，单号随机一个号码
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 1:
                    if a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 2:
                    if a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 3:
                    if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a3)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 4:
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if a0 == b0 or a0 == b1 and a1 == b0 or a1 == b1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                        else:
                            pass
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选30.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选30下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选30
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '2')
                break
        # 遍历文字
        for i in range(10):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选30.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选30下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选30
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '2')
                break

    def star5_s5zuxz20(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选20
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '3')

        # 任选1个号码，循环10次
        # 选2个二重号，1个单号组成一注
        # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         for k in range(10):
        #             if i == j or i == k or j >= k:
        #                 pass
        #             else:
        #                 print(i, j, k)
        #                 self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #                 self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #                 self.base_driver.clicks(self.config_dict_tmm['DWDQ'], k)
        #                 self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                c = random.choice(range(0, 10))
                if a == b or a == c or b == c:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], c)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选20.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选20下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选20
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '3')
                break
        # 遍历文字
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选20.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('五星---五星组选---组选20下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 五星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                    # 五星---五星组选---组选20
                    self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '3')
                    break

    def star5_s5zuxz20_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选20
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '3')
        '''
        for i in range(10):
            self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('五星---五星组选---组选120：  ' + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        for j in range(10):
            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
            print('五星---五星组选---组选120：  ' + ' ' + str(j) + ' ' + str(s))
            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
        '''
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 10))
                a4 = random.choice(range(0, 10))
                b0 = random.choice(range(0, 10))
                b1 = random.choice(range(0, 10))
                print(s0, a0, a1, a2, a3, a4, b0, b1)
                if s0 == 0:
                    # 三重号，单号随机一个号码
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 1:
                    # 三重号1个，单号两个，其中三重号与其中一个单号相同
                    if a1 == a2:
                        pass
                    else:
                        if a0 == a1 or a0 == a1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                        else:
                            pass
                if s0 == 2:
                    # 三重号选择两个，单号选择一个
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 3:
                    # 三重号选择两个，单号选择二个
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if a0 == b0 and a1 == b1:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                        if a0 == b1 and a1 == b0:
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b0)
                            self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b1)
                            self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                            s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                            print('五星---五星组选---组选120：  ' + ' ' + str(s))
                            self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                            self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                            self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                        else:
                            pass
                if s0 == 4:
                    # 三重号选择三个，单号选择一个
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a3)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 5:
                    # 三重号选择四个，单号选择一个
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a1)
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                        self.base_driver.clicks(self.config_dict_tmm['DWDW'], a3)
                        self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a4)
                        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                        print('五星---五星组选---组选120：  ' + ' ' + str(s))
                        self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                        self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选20.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选320下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选20
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '3')
                break
        # 遍历文字
        for i in range(5):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 5))
                a1 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选20.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选30下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选30
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '3')
                break

    def star5_s5zuxz10(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选10
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '4')

        # 任选1个号码，循环10次
        # 选2个二重号，1个单号组成一注
        # # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         if i == j:
        #             pass
        #         else:
        #             print(i, j)
        #             self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选10.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选10下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选10
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '4')
                break
        # 遍历文字
        for i in range(5):
            try:
                a0 = random.choice(0, 5)
                a1 = random.choice(0, 5)
                self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a0)
                self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], a1)
                self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选10.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选10下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选10
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '4')
                break

    def star5_s5zuxz10_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选20
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '4')

        # # 选1个二重号，1个单号
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        #     print('五星---五星组选---组选120：  ' + ' ' + str(i) + ' ' + str(s))
        #     self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
        #     self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        # for j in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        #     print('五星---五星组选---组选120：  ' + ' ' + str(j) + ' ' + str(s))
        #     self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
        #     self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')

        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选10：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                # 遍历文字
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选20：  ' + ' ' + str(a3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选20：  ' + ' ' + str(a4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选10.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选10下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选10
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '4')
                break

    def star5_s5zuxz5(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选5
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '5')

        # 任选1个号码，循环10次
        # 选2个二重号，1个单号组成一注
        # # # 第一位
        # for i in range(10):
        #     for j in range(10):
        #         if i == j:
        #             pass
        #         else:
        #             print(i, j)
        #             self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #             self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #             self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                a = random.choice(range(0, 10))
                b = random.choice(range(0, 10))
                if a == b:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], b)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选5.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选5下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选5
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '5')
                break
        # 遍历文字
        '''
        for i in range(5):
            for j in range(5):
                try:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], i)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], j)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选10.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(s)
                    # self.logger.infos('五星---五星组选---组选10下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 五星
                    self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                    # 五星---五星组选---组选10
                    self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '5')
                    break
        '''
    def star5_s5zuxz5_error(self, row):
        # 五星
        self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
        # 五星---五星组选---组选20
        self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '5')

        # 任选1个号码，循环10次
        # 选2个二重号，1个单号组成一注
        # 选1个二重号，1个单号
        # for i in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDW'], i)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        #     print('五星---五星组选---组选120：  ' + ' ' + str(i) + ' ' + str(s))
        #     self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
        #     self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
        # for j in range(10):
        #     self.base_driver.clicks(self.config_dict_tmm['DWDQ'], j)
        #     self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        #     s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        #     print('五星---五星组选---组选120：  ' + ' ' + str(j) + ' ' + str(s))
        #     self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
        #     self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')

        # # 随机抽取一个数字,抽取100次，每个号码抽一位数字
        for i in range(100):
            try:
                s0 = random.choice(range(0, 6))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(0, 10))
                a3 = random.choice(range(0, 5))
                a4 = random.choice(range(0, 5))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a0)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选10：  ' + ' ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a1)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_tmm['DWDW'], a2)
                    self.base_driver.clicks(self.config_dict_tmm['DWDQ'], a2)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
                # 遍历文字
                if s0 == 4:
                    self.base_driver.clicks(self.config_dict_tmm['DWDWWZ'], a3)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMBWZ'], '5')
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_tmm['DWDQWZ'], a4)
                    self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
                    print('五星---五星组选---组选120：  ' + ' ' + str(a4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_tmm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_tmm['TTMMSWZ'], '5')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                s = '/fusion/pictures/time_mm/' + '%s-五星---五星直选---组选10.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(s)
                # self.logger.infos('五星---五星组选---组选10下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 五星
                self.base_driver.clicks_by_text(self.config_dict_tmm['MENU'], '五星')
                # 五星---五星组选---组选10
                self.base_driver.clicks(self.config_dict_tmm['S5ZUX'], '5')
                break

      # ---------------------------------------------------------------------
      # ---------------------------------------------------------------------
      # ---------------------------------------------------------------------

    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_tmm['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(3)

    def radoms(self, row):

        # 随机5注
        self.base_driver.click(self.config_dict_tmm['RANDOM5'])
        self.base_driver.forced_wait(3)
        # 随机1注2元
        self.base_driver.click(self.config_dict_tmm['RANDOM1'])
        # 随机一注2角
        self.base_driver.click(self.config_dict_tmm['JIAO'])
        self.base_driver.click(self.config_dict_tmm['RANDOM1'])
        # 随机一注2分
        self.base_driver.click(self.config_dict_tmm['FEN'])
        self.base_driver.click(self.config_dict_tmm['RANDOM1'])
        # 随机20
        # self.base_driver.clear(self.config_dict_marksix['XIUGAI'])
        #
        # self.base_driver.forced_wait(20)
        s = random.choice(range(0, 1000))
        self.base_driver.type(self.config_dict_tmm['XIUGAI'], "\b" + str(s))
        self.base_driver.click(self.config_dict_tmm['RANDOM1'])
        #self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        self.base_driver.forced_wait(1)
        print('随机5注')

        self.base_driver.click(self.config_dict_tmm['SUREBET'])
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_tmm['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        return surebet

    def get_tips(self):
        tips = self.base_driver.get_text(self.config_dict_tmm['TIPS'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips01(self):
        # 提示请先添加投注内容
        tips = self.base_driver.get_text(self.config_dict_tmm['TIPS01'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips02(self):
        # 提示下注成功
        tips = self.base_driver.get_text(self.config_dict_tmm['TIPS02'])
        print('捕捉到的信息是：' + tips)
        return tips

