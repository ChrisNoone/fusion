import csv
import random
import time

from common.box import BasePage, YamlHelper


class Fast3Mm(BasePage):
    # 分分快3
    config_dict_f3mm = YamlHelper().get_config_dict('/fusion/yaml/lottery_fast3_mm.yaml')['FAST3_MM']

    def num_s2_ds(self, row):
        # 二同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
        self.base_driver.forced_wait(1)
        # 二同号单选---标准选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
        self.base_driver.forced_wait(1)
        # 从二同号和不同号中各选1个号码组成一注。
        for i in range(100):
            try:
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                if a0 == a1:
                    pass
                else:
                    print('二同号单选:  ' + str(a0) + str(a1))
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DS_SNN'], a0)
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DS_NN'], a1)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二同号单选---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二同号单选---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
                self.base_driver.forced_wait(1)
                # 二同号单选---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
                break

    def num_s2_ds_error(self, row):
        # 二同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
        self.base_driver.forced_wait(1)
        # 二同号单选---标准选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
        self.base_driver.forced_wait(1)
        # 从二同号和不同号中各选1个号码组成一注。
        for i in range(20):
            try:
                s0 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DS_SNN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('从二同号1个号码：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DS_SNN'], a0)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DS_NN'], a1)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('从不同号1个号码：  ' + ' ' + str(a1) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DS_NN'], a1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二同号单选---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二同号单选---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
                self.base_driver.forced_wait(1)
                # 二同号单选---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
                break

    def num_s2_sd(self, row):
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
        self.base_driver.forced_wait(1)
        # 二同号单选---手动选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s0 = random.choice(range(1, 6))
                s1 = random.choice(range(1, 6))
                s2 = random.choice(range(1, 6))
                if s1 == s2:
                    pass
                else:
                    if s0 == 0:
                        ss = str(s1) + str(s1) + str(s2)
                        self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], ss)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号手动单选:  ' + ss )
                    if s0 == 1:
                        ss = str(s1) + str(s2) + str(s1)
                        self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], ss)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号手动单选:  ' + ss)
                    if s0 == 2:
                        ss = str(s2) + str(s1) + str(s1)
                        self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], ss)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号手动单选:  ' + ss)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二同号单选---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二同号单选---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
                self.base_driver.forced_wait(1)
                # 二同号单选---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
                break

    def num_s2_sd_error(self, row):
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
        self.base_driver.forced_wait(1)
        # 二同号单选---手动选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s0 = random.choice(range(0, 4))
                s1 = random.choice(range(0, 10))
                s2 = random.choice(range(0, 10))
                s3 = random.choice(range(0, 10))
                s4 = random.choice(range(999, 10000))
                s5 = random.choice(range(-999, 0))
                if s0 == 0:
                    # 输入互不相同的三个数字
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], str(s1) + str(s2) + str(s3))
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('二同号手动选号：  ' + str(s1) + str(s2) + str(s3) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                if s0 == 1:
                    # 输入3个相同的号码
                    self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], str(s1) + str(s1) + str(s1))
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('二同号手动选号：  ' + str(s1) + str(s2) + str(s3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                if s0 == 2:
                    # 输入超过3位数字的号码
                    self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], s4)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('二同号手动选号：  ' + str(s1) + str(s2) + str(s3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                if s0 == 3:
                    self.base_driver.type(self.config_dict_f3mm['NUM_S2_DH_TEXT'], s5)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('二同号手动选号：  ' + str(s1) + str(s2) + str(s3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二同号单选---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二同号单选---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
                self.base_driver.forced_wait(1)
                # 二同号单选---手动选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
                break

    def num_s2_fx(self, row):
        # 二同号复选
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
        self.base_driver.forced_wait(1)
        # 二同号复选---二同号复选
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FXN'], '0')
        self.base_driver.forced_wait(1)
        # 从6组对子中任选1组对子号码组成一注。
        for i in range(50):
            try:
                s0 = random.choice(range(0, 6))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 6))
                a3 = random.choice(range(0, 6))
                a4 = random.choice(range(0, 6))
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    print('二同号复选---二同号复选:  ' + str(a0))
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号复选---二同号复选:  ' + str(a0) + str(a1))
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号复选---二同号复选:  ' + str(a0) + str(a1) + str(a2))
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a3)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号复选---二同号复选:  ' + str(a0) + str(a1) + str(a2) + str(a3))
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], a4)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        print('二同号复选---二同号复选:  ' + str(a0) + str(a1) + str(a2) + str(a3) + str(a4))
                if s0 == 5:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], '0')
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], '1')
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], '2')
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], '3')
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], '4')
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FX_SNNN'], '5')
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    print('二同号复选---二同号复选--全选:')
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二同号复选---二同号复选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二同号复选---二同号复选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二同号复选
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二同号')
                self.base_driver.forced_wait(1)
                # 二同号复选---二同号复选
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_FXN'], '0')
                self.base_driver.forced_wait(1)
                break

    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    def num_n2(self, row):
        # 二不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
        self.base_driver.forced_wait(1)
        # 二不同号---标准选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 6))
                a3 = random.choice(range(0, 6))
                a4 = random.choice(range(0, 6))
                if s0 == 0:
                    if a0 == a1:
                        pass
                    else:
                        print('a0:  ' + str(a0))
                        print('a1:  ' + str(a1))
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        print('a0:  ' + str(a0))
                        print('a1:  ' + str(a1))
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        print('a0:  ' + str(a0))
                        print('a1:  ' + str(a1))
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a3)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], a4)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        print('a0:  ' + str(a0))
                        print('a1:  ' + str(a1))
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], '0')
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], '1')
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], '2')
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], '3')
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], '4')
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], '5')
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二不同号---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不同号---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
                self.base_driver.forced_wait(1)
                # 二不同号---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
                self.base_driver.forced_wait(1)
                break

    def num_n2_error(self, row):
        # 二不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
        self.base_driver.forced_wait(1)
        # 二不同号---标准选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
        self.base_driver.forced_wait(1)
        for i in range(6):
            try:
                self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], i)
                self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                print('从二同号1个号码：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_BZ'], i)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二不同号---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不同号---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
                self.base_driver.forced_wait(1)
                # 二不同号---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '0')
                self.base_driver.forced_wait(1)
                break

    def num_n2_sd(self, row):
        # 二不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
        self.base_driver.forced_wait(1)
        # 二不同号---手动选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s1 = random.choice(range(1, 6))
                s2 = random.choice(range(1, 6))
                if s1 == s2:
                    pass
                else:
                    ss = str(s1) + '' + str(s2)
                    self.base_driver.type(self.config_dict_f3mm['NUM_N2_SD_TEXT'], ss)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    print('二不同号---手动选号:  ' + str(ss))
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二不同号---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
                self.base_driver.forced_wait(1)
                # 二不同号---手动选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
                break

    def num_n2_sd_error(self, row):
        # 二不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
        self.base_driver.forced_wait(1)
        # 二不同号---手动选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
        self.base_driver.forced_wait(1)
        for i in range(1000):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 10))
                a1 = random.choice(range(0, 10))
                a2 = random.choice(range(99, 1000))
                a3 = random.choice(range(-999, 0))
                if s0 == 0:
                    # 输入每个数字大于6的数字
                    if a0 > 6 and a1 > 6:
                        self.base_driver.type(self.config_dict_f3mm['NUM_N2_SD_TEXT'], str(a0) + '' + str(a1))
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('从二同号手动选号：  ' + ' ' + str(a0) + '' + str(a1) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    else:
                        pass
                if s0 == 1:
                    # 输入相同的两个号码
                    self.base_driver.type(self.config_dict_f3mm['NUM_N2_SD_TEXT'], str(a0) + '' + str(a0))
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('从二同号手动选号：  ' + ' ' + str(a0) + '' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                if s0 == 2:
                    # 输入小于0的数字
                    self.base_driver.type(self.config_dict_f3mm['NUM_N2_SD_TEXT'], str(a2))
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('从二同号手动选号：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                if s0 == 3:
                    # 输入大于两位数字的号码
                    self.base_driver.type(self.config_dict_f3mm['NUM_N2_SD_TEXT'], str(a2))
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('从二同号手动选号：  ' + ' ' + str(a2) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                if s0 == 4:
                    # 输入0 + 任意数字的组合的数字
                    self.base_driver.type(self.config_dict_f3mm['NUM_N2_SD_TEXT'], str(a2) + str(a3))
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('从二同号手动选号：  ' + str(a2) + str(a3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二不同号---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
                self.base_driver.forced_wait(1)
                # 二不同号---手动选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
                self.base_driver.forced_wait(1)
                break

    def num_n2_dt(self, row):
        # 二不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
        self.base_driver.forced_wait(1)
        # 二不同号---胆拖选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '2')
        self.base_driver.forced_wait(1)
        for i in range(100):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 6))
                a3 = random.choice(range(0, 6))
                a4 = random.choice(range(0, 6))
                a5 = random.choice(range(0, 6))
                # 胆选1个 拖选1个
                if s0 == 0:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 胆选1个 拖选2个
                if s0 == 1:
                    if a0 == a1 or a0 == a2:
                        pass
                    else:
                        if a1 == a2:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                            self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 胆选1个 拖选3个
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3:
                        pass
                    else:
                        if a1 == a2 or a1 == a3 or a2 == a3:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                            self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 胆选1个 拖选4个
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4:
                        pass
                    else:
                        if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                            self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a4)
                            self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 胆选1个 拖选5个
                if s0 == 4:
                    if a0 != a1 and a0 != a2 and a0 != a3 and a0 != a4 and a0 != a5:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a4)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a5)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    else:
                        pass
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二不同号---胆拖选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
                self.base_driver.forced_wait(1)
                # 二不同号---手动选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '1')
                self.base_driver.forced_wait(1)
                break

    def num_n2_dt_error(self, row):
        # 二不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
        self.base_driver.forced_wait(1)
        # 二不同号---胆拖选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '2')
        self.base_driver.forced_wait(1)
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        for i in range(100):
            try:
                s0 = random.choice(range(0, 8))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 6))
                a3 = random.choice(range(0, 6))
                a4 = random.choice(range(0, 6))
                a5 = random.choice(range(0, 6))
                # 胆选1个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                # 拖选1个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                # 胆拖选相同
                if s0 == 2:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a1)
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                #  拖选2个
                if s0 == 3:
                    if a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                # 拖选3个
                if s0 == 4:
                    if a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                # 拖选4个
                if s0 == 5:
                    if a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a4)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a4)
                # 拖选5个
                if s0 == 6:
                    if a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 \
                            or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a4)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a5)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a4)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a5)
                # 拖选6个
                if s0 == 7:
                    for a in range(6):
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('二不同号---胆拖选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    for a in range(6):
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_TN'], a)
                else:
                    pass

            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-二不同号---胆拖选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('二不同号---胆拖选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 二不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '二不同号')
                self.base_driver.forced_wait(1)
                # 二不同号---胆拖选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S2_DSN'], '2')
                self.base_driver.forced_wait(1)
                break

    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------

    def num3_n3_bz(self, row):
        # 三不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
        # 三不同号---标准选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '0')
        for i in range(50):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 6))
                a3 = random.choice(range(0, 6))
                a4 = random.choice(range(0, 6))
                # # 选择三个不同的号码
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择四不同的号码
                if s0 == 1:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a3)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择五不同的号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a4)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 全选
                if s0 == 3:
                    for a in range(6):
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三不同号---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三不同号---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
                # 三不同号---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '0')
                self.base_driver.forced_wait(1)
                break

    def num3_n3_bz_error(self, row):
        # 三不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
        # 三不同号---标准选号
        self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '0')
        for i in range(100):
            try:
                s0 = random.choice(range(0, 3))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                # 选择一个不同的号码
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('三不同号---标准选号：  ' + str(a0) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                # # 选择二不同的号码
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('三不同号---标准选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_N2_DT_DN'], a1)
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三不同号---标准选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三不同号---标准选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
                # 三不同号---标准选号
                self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '0')
                self.base_driver.forced_wait(1)
                break

    def num3_n3_sd(self, row):
        # 三不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
        # 三不同号---手动选号---输入框
        self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '1')
        for i in range(50):
            try:
                s0 = random.choice(range(1, 6))
                s1 = random.choice(range(1, 6))
                s2 = random.choice(range(1, 6))
                if s0 == s1 or s0 == s2 or s1 == s2:
                    pass
                else:
                    ss = str(s0) + str(s1) + str(s2)
                    self.base_driver.type(self.config_dict_f3mm['NUM_N3_SD_TEXT'], ss)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三不同号---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
                # 三不同号---手动选号---输入框
                self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '1')
                break

    def num3_n3_sd_error(self, row):
        # 三不同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
        # 三不同号---手动选号---输入框
        self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '1')
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        for i in range(100):
            try:
                s0 = random.choice(range(1, 6))
                a0 = random.choice(range(1, 6))
                a1 = random.choice(range(1, 6))
                a2 = random.choice(range(1, 6))
                a3 = random.choice(range(-100, 100))
                a4 = random.choice(range(999, 10000))
                # 输入只是两个相同号码的三位数字
                if s0 == 0:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        ss = str(a0) + '' + str(a1) + '' + str(a2)
                        self.base_driver.type(self.config_dict_f3mm['NUM_N3_SD_TEXT'], ss)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                        print('三不同号---手动选号：  ' + str(a0) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                    else:
                        pass
                # 输入小于3位数字
                if s0 == 1:
                    self.base_driver.type(self.config_dict_f3mm['NUM_N3_SD_TEXT'], a3)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('三不同号---手动选号：  ' + str(a3) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                # 输入大于3位数字
                if s0 == 2:
                    self.base_driver.type(self.config_dict_f3mm['NUM_N3_SD_TEXT'], a4)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
                    print('三不同号---手动选号：  ' + str(a4) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_f3mm['TIPSBUTTON'])
                else:
                    pass
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三不同号---手动选号.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三不同号---手动选号下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三不同号')
                # 三不同号---手动选号---输入框
                self.base_driver.clicks(self.config_dict_f3mm['NUM_N3_BZN'], '1')
                break

    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------

    def num_s3_ds(self, row):
        # 三同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三同号')
        # 三同号---三同号单选---三同号单选
        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_D'], '0')
        for i in range(30):
            try:
                s0 = random.choice(range(0, 5))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 6))
                a3 = random.choice(range(0, 6))
                a4 = random.choice(range(0, 6))
                # 选择一个号码
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择两个不同的号码
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择三个不同的号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择四不同的号码
                if s0 == 3:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a3)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择五不同的号码
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a4)
                # 全选
                if s0 == 5:
                    for a in range(6):
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_DNNN'], a)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-三同号---三同号单选.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('三同号---三同号单选下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 三不同号
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三同号')
                # 三同号---三同号单选---三同号单选
                self.base_driver.clicks(self.config_dict_f3mm['NUM_S3_D'], '0')
                break

    def num_s3_ts(self, row):
        # 三同号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三同号')
        # 三同号--三同号通选
        self.base_driver.click(self.config_dict_f3mm['NUM_S3_T'])
        try:
            self.base_driver.click(self.config_dict_f3mm['NUM_S3_T111'])
            self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
        except Exception as e:
            print(e)
            now_Time = time.strftime("%Y%m%d.%H.%M.%S")
            ss = '/fusion/pictures/fast3_mm/' + '%s-三同号---三同号通选.png' % now_Time
            self.base_driver.save_window_snapshot_by_io(ss)
            # self.logger.infos('三同号---三同号通选下注异常')
            self.base_driver.refresh()
            self.base_driver.forced_wait(4)
            # 三同号
            self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三同号')
            # 三同号--三同号通选
            self.base_driver.click(self.config_dict_f3mm['NUM_S3_T'])

    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------------
    def num_s3_l(self, row):
        # 三连号
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三连号')
        # 三连号---三连号通选
        self.base_driver.click(self.config_dict_f3mm['NUM_L3_TX'])
        # 号码
        try:
            self.base_driver.click(self.config_dict_f3mm['NUM_L3_TX111'])
            self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
        except Exception as e:
            print(e)
            now_Time = time.strftime("%Y%m%d.%H.%M.%S")
            ss = '/fusion/pictures/fast3_mm/' + '%s-三连号---三连号通选.png' % now_Time
            self.base_driver.save_window_snapshot_by_io(ss)
            # self.logger.infos('三连号---三连号通选下注异常')
            self.base_driver.refresh()
            self.base_driver.forced_wait(4)
            # 三连号
            self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '三连号')
            # 三连号---三连号通选
            self.base_driver.click(self.config_dict_f3mm['NUM_L3_TX'])

    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------
    def num_hh_dxds(self, row):
        # 和值
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '和值')
        # 和值---大小单双
        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSN'], '0')
        for i in range(20):
            try:
                s0 = random.choice(range(0, 4))
                a0 = random.choice(range(0, 4))
                a1 = random.choice(range(0, 4))
                a2 = random.choice(range(0, 4))
                # 选择一个号码
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择两个不同的号码
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择三个不同的号码
                if s0 == 2:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 选择四不同的号码
                if s0 == 3:
                    for a in range(4):
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSNN'], a)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
            except Exception as e:
                    print(e)
                    now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                    ss = '/fusion/pictures/fast3_mm/' + '%s-和值---大小单双.png' % now_Time
                    self.base_driver.save_window_snapshot_by_io(ss)
                    # self.logger.infos('和值---大小单双下注异常')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(4)
                    # 和值
                    self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '和值')
                    # 和值---大小单双
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSN'], '0')

    def num_hh_hezhi(self, row):
        # 和值
        self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '和值')
        # 和值---和值---和值
        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSN'], '1')
        # 遍历号码
        '''
        for i in range(14):
            self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], i)
            self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
        self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
        '''
        # 随机号码
        for i in range(100):
            try:
                s0 = random.choice(range(0, 12))
                a0 = random.choice(range(0, 15))
                a1 = random.choice(range(0, 15))
                a2 = random.choice(range(0, 15))
                a3 = random.choice(range(0, 15))
                a4 = random.choice(range(0, 15))
                a5 = random.choice(range(0, 15))
                # 随机一位
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 1:
                    self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 随机两位
                if s0 == 2:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 3:
                    self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                    self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
                    self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 随机三位
                if s0 == 4:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 随机四位
                if s0 == 6:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a3)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 7:
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 随机五位
                if s0 == 8:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 \
                            or a1 == a4 or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a4)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 9:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a3)
                        self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                # 随机六位
                if s0 == 10:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a4)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a5)
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
                if s0 == 11:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 \
                            or a2 == a3 or a2 == a4 or a3 == a4:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a0)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a1)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a2)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a3)
                        self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_NN'], a4)
                        self.base_driver.click(self.config_dict_f3mm['NUM_HH_18'])
                        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
            except Exception as e:
                print(e)
                now_Time = time.strftime("%Y%m%d.%H.%M.%S")
                ss = '/fusion/pictures/fast3_mm/' + '%s-和值---和值.png' % now_Time
                self.base_driver.save_window_snapshot_by_io(ss)
                # self.logger.infos('和值---和值下注异常')
                self.base_driver.refresh()
                self.base_driver.forced_wait(4)
                # 和值
                self.base_driver.clicks_by_text(self.config_dict_f3mm['MENU'], '和值')
                # 和值---和值---和值
                self.base_driver.clicks(self.config_dict_f3mm['NUM_HH_DXDSN'], '1')
                break

    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_f3mm['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(3)

    def radoms(self, row):

        # 随机5注
        self.base_driver.click(self.config_dict_f3mm['RANDOM5'])
        self.base_driver.forced_wait(3)
        # 随机1注2元
        self.base_driver.click(self.config_dict_f3mm['RANDOM1'])
        # 随机一注2角
        self.base_driver.click(self.config_dict_f3mm['JIAO'])
        self.base_driver.click(self.config_dict_f3mm['RANDOM1'])
        # 随机一注2分
        self.base_driver.click(self.config_dict_f3mm['FEN'])
        self.base_driver.click(self.config_dict_f3mm['RANDOM1'])
        # 随机20
        # self.base_driver.clear(self.config_dict_marksix['XIUGAI'])
        #
        # self.base_driver.forced_wait(20)
        s = random.choice(range(0, 1000))
        self.base_driver.type(self.config_dict_f3mm['XIUGAI'], "\b" + str(s))
        self.base_driver.click(self.config_dict_f3mm['RANDOM1'])
        # self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机1注')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        #self.base_driver.forced_wait(5)

        self.base_driver.click(self.config_dict_f3mm['SUREBET'])
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机5注')

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_f3mm['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        return surebet

    def get_tips(self):
        tips = self.base_driver.get_text(self.config_dict_f3mm['TIPS'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips01(self):
        # 提示请先添加投注内容
        tips = self.base_driver.get_text(self.config_dict_f3mm['TIPS01'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips02(self):
        # 提示下注成功
        tips = self.base_driver.get_text(self.config_dict_f3mm['TIPS02'])
        print('捕捉到的信息是：' + tips)
        return tips


