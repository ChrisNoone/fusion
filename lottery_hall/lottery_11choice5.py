import os
import random
import time


from common.box import BasePage, YamlHelper


class Lottery11Choice5(BasePage):

    config_dict_tmmcq = YamlHelper().get_config_dict('/fusion/lottery_hall/yaml/lottery_choice11x5.yaml')['LOTTERY_HALL']

    def double_count(self):
        # 彩票大厅
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '今日开奖')
        self.base_driver.forced_wait(1)
        # 双面统计
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['IDLENUM01'], '双面统计')
        self.base_driver.forced_wait(10)
        a00 = []
        a01 = []
        a02 = []
        a03 = []
        a04 = []
        a05 = []
        a06 = []
        a07 = []
        a08 = []
        a09 = []
        a10 = []
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        a15 = []
        a16 = []
        for i in range(100):
            try:
                # 时间
                date1 = self.base_driver.get_texts(self.config_dict_tmmcq['TIME_NUM'], i)
                # print(date1[:8])
                if date1[:10] == time.strftime('%Y-%m-%d'):
                    # 开奖号码
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM00'], i)
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM01'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM02'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM03'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM04'], i)
                    # 总和--大小和
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_NUM00'], i)
                    # 总和--单双
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_NUM01'], i)
                    # 龙虎
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_NUM02'], i)
                    # 前三
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_NUM03'], i)
                    # 中三
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_NUM04'], i)
                    # 后三
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_NUM05'], i)

                    a00.append(s00)
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)
                    a07.append(s07)
                    a08.append(s08)
                    a09.append(s09)
                    a10.append(s10)
            except Exception as e:
                print(e)
                print('今日开奖双面统计运行' + str(i) + '行')
                break

        b00 = a00.count('01') + a01.count('01') + a02.count('01') + a03.count('01') + a04.count('01')
        b01 = a00.count('02') + a01.count('02') + a02.count('02') + a03.count('02') + a04.count('02')
        b02 = a00.count('03') + a01.count('03') + a02.count('03') + a03.count('03') + a04.count('03')
        b03 = a00.count('04') + a01.count('04') + a02.count('04') + a03.count('04') + a04.count('04')
        b04 = a00.count('05') + a01.count('05') + a02.count('05') + a03.count('05') + a04.count('05')
        b05 = a00.count('06') + a01.count('06') + a02.count('06') + a03.count('06') + a04.count('06')
        b06 = a00.count('07') + a01.count('07') + a02.count('07') + a03.count('07') + a04.count('07')
        b07 = a00.count('08') + a01.count('08') + a02.count('08') + a03.count('08') + a04.count('08')
        b08 = a00.count('09') + a01.count('09') + a02.count('09') + a03.count('09') + a04.count('09')
        b09 = a00.count('10') + a01.count('10') + a02.count('10') + a03.count('10') + a04.count('10')
        b10 = a00.count('11') + a01.count('11') + a02.count('11') + a03.count('11') + a04.count('11')

        c00 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 1)
        print(c00)
        c01 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 2)
        c02 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 3)
        c03 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 4)
        c04 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 5)
        c05 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 6)
        c06 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 7)
        c07 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 8)
        c08 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 9)
        c09 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 10)
        c10 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 11)

        print('--------------------------------------------------------------------------------------')
        if str(c00) == str(b00):
            print(' 号码01出现次数统计正确 ' + str(b00))
        else:
            print(' 号码01出现次数统计错误 ' + str(b00))
        if str(c01) == str(b01):
            print(' 号码02出现次数统计正确 ' + str(b01))
        else:
            print(' 号码02出现次数统计错误 ' + str(b01))
        if str(c02) == str(b02):
            print(' 号码03出现次数统计正确 ' + str(b02))
        else:
            print(' 号码03出现次数统计错误 ' + str(b02))
        if str(c03) == str(b03):
            print(' 号码04出现次数统计正确 ' + str(b03))
        else:
            print(' 号码04出现次数统计错误 ' + str(b03))
        if str(c04) == str(b04):
            print(' 号码05出现次数统计正确 ' + str(b04))
        else:
            print(' 号码05出现次数统计错误 ' + str(b04))
        if str(c05) == str(b05):
            print(' 号码06出现次数统计正确 ' + str(b05))
        else:
            print(' 号码06出现次数统计错误 ' + str(b05))
        if str(c06) == str(b06):
            print(' 号码07出现次数统计正确 ' + str(b06))
        else:
            print(' 号码07出现次数统计错误 ' + str(b06))
        if str(c07) == str(b07):
            print(' 号码08出现次数统计正确 ' + str(b07))
        else:
            print(' 号码08出现次数统计错误 ' + str(b07))
        if str(c08) == str(b08):
            print(' 号码09出现次数统计正确 ' + str(b08))
        else:
            print(' 号码09出现次数统计错误 ' + str(b08))
        if str(c09) == str(b09):
            print(' 号码10出现次数统计正确 ' + str(b09))
        else:
            print(' 号码10出现次数统计错误 ' + str(b09))
        if str(c10) == str(b10):
            print(' 号码10出现次数统计正确 ' + str(b10))
        else:
            print(' 号码10出现次数统计错误 ' + str(b10))

        m00 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 1)
        m01 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 2)
        m02 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 3)
        m03 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 4)
        m04 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 5)
        m05 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 6)
        m06 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 7)
        m07 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 8)
        m08 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 9)
        m09 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 10)
        m10 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 11)
        m11 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 12)
        m12 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 13)
        m13 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 14)
        m14 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 15)
        m15 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 16)
        m16 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 17)
        m17 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 18)
        m18 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 19)
        m19 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 20)
        m20 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 21)
        m21 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 22)
        m22 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 23)
        m23 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 24)

        # 总和单双
        print('--------------------------------------------------------------------------------------')
        d00 = a06.count('单')
        d01 = a06.count('双')
        d02 = a05.count('大')
        d03 = a05.count('小')
        # d03_1 = a05.count('和')

        if str(m00) == str(d00):
            print('总和单统计正确' + str(d00))
        else:
            print('总和单统计错误' + str(d00))
        if str(m01) == str(d01):
            print('总和双统计正确' + str(d01))
        else:
            print('总和双统计错误' + str(d01))
        if str(m02) == str(d02):
            print('总和大统计正确' + str(d02))
        else:
            print('总和大统计错误' + str(d02))
        if str(m03) == str(d03):
            print('总和小统计正确' + str(d03))
        else:
            print('总和小统计错误' + str(d03))
        # if str(m02) == str(d02):
        #     print('总和和统计正确' + str(d03_1))
        # else:
        #     print('总和和统计错误' + str(d03_1))

        print('--------------------------------------------------------------------------------------')
        d04 = a00.count('01') + a00.count('03') + a00.count('05') + a00.count('07') + a00.count('09') + a00.count('11')
        d05 = a00.count('02') + a00.count('04') + a00.count('06') + a00.count('08') + a00.count('10')
        d06 = a00.count('06') + a00.count('07') + a00.count('08') + a00.count('09') + a00.count('10') + a00.count('11')
        d07 = a00.count('01') + a00.count('02') + a00.count('03') + a00.count('04') + a00.count('05')
        if str(m04) == str(d04):
            print('第一球单统计正确' + str(d04))
        else:
            print('第一球单统计错误' + str(d04))
        if str(m05) == str(d05):
            print('第一球双统计正确' + str(d05))
        else:
            print('第一球双统计错误' + str(d05))
        if str(m06) == str(d06):
            print('第一球大统计正确' + str(d06))
        else:
            print('第一球大统计错误' + str(d06))
        if str(m07) == str(d07):
            print('第一球小统计正确' + str(d07))
        else:
            print('第一球小统计错误' + str(d07))

        d08 = a01.count('01') + a01.count('03') + a01.count('05') + a01.count('07') + a01.count('09') + a01.count('11')
        d09 = a01.count('02') + a01.count('04') + a01.count('06') + a01.count('08') + a01.count('10')
        d10 = a01.count('06') + a01.count('07') + a01.count('08') + a01.count('09') + a01.count('10') + a01.count('11')
        d11 = a01.count('01') + a01.count('02') + a01.count('03') + a01.count('04') + a01.count('05')
        if str(m08) == str(d08):
            print('第二球单统计正确' + str(d08))
        else:
            print('第二球单统计错误' + str(d08))
        if str(m09) == str(d09):
            print('第二球双统计正确' + str(d09))
        else:
            print('第二球双统计错误' + str(d09))
        if str(m10) == str(d10):
            print('第二球大统计正确' + str(d10))
        else:
            print('第二球大统计错误' + str(d10))
        if str(m11) == str(d11):
            print('第二球小统计正确' + str(d11))
        else:
            print('第二球小统计错误' + str(d11))

        d12 = a02.count('01') + a02.count('03') + a02.count('05') + a02.count('07') + a02.count('09') + a02.count('11')
        d13 = a02.count('02') + a02.count('04') + a02.count('06') + a02.count('08') + a02.count('10')
        d14 = a02.count('06') + a02.count('07') + a02.count('08') + a02.count('09') + a02.count('10') + a02.count('11')
        d15 = a02.count('01') + a02.count('02') + a02.count('03') + a02.count('04') + a02.count('05')
        if str(m12) == str(d12):
            print('第三球单统计正确' + str(d12))
        else:
            print('第三球单统计错误' + str(d12))
        if str(m13) == str(d13):
            print('第三球双统计正确' + str(d13))
        else:
            print('第三球双统计错误' + str(d13))
        if str(m14) == str(d14):
            print('第三球大统计正确' + str(d14))
        else:
            print('第三球大统计错误' + str(d14))
        if str(m15) == str(d15):
            print('第三球小统计正确' + str(d15))
        else:
            print('第三球小统计错误' + str(d15))

        d16 = a03.count('01') + a03.count('03') + a03.count('05') + a03.count('07') + a03.count('09') + a03.count('11')
        d17 = a03.count('02') + a03.count('04') + a03.count('06') + a03.count('08') + a03.count('10')
        d18 = a03.count('06') + a03.count('07') + a03.count('08') + a03.count('09') + a03.count('10') + a03.count('11')
        d19 = a03.count('01') + a03.count('02') + a03.count('03') + a03.count('04') + a03.count('05')
        if str(m16) == str(d16):
            print('第四球单统计正确' + str(d16))
        else:
            print('第四球单统计错误' + str(d16))
        if str(m17) == str(d17):
            print('第四球双统计正确' + str(d17))
        else:
            print('第四球双统计错误' + str(d17))
        if str(m18) == str(d18):
            print('第四球大统计正确' + str(d18))
        else:
            print('第四球大统计错误' + str(d18))
        if str(m19) == str(d19):
            print('第四球小统计正确' + str(d19))
        else:
            print('第四球小统计错误' + str(d19))

        d20 = a04.count('01') + a04.count('03') + a04.count('05') + a04.count('07') + a04.count('09') + a04.count('11')
        d21 = a04.count('02') + a04.count('04') + a04.count('06') + a04.count('08') + a04.count('10')
        d22 = a04.count('06') + a04.count('07') + a04.count('08') + a04.count('09') + a04.count('10') + a04.count('11')
        d23 = a04.count('01') + a04.count('02') + a04.count('03') + a04.count('04') + a04.count('05')
        if str(m20) == str(d20):
            print('第五球单统计正确' + str(d20))
        else:
            print('第五球单统计错误' + str(d20))
        if str(m21) == str(d21):
            print('第五球双统计正确' + str(d21))
        else:
            print('第五球双统计错误' + str(d21))
        if str(m22) == str(d22):
            print('第五球大统计正确' + str(d22))
        else:
            print('第五球大统计错误' + str(d22))
        if str(m23) == str(d23):
            print('第五球小统计正确' + str(d23))
        else:
            print('第五球小统计错误' + str(d23))

    def lotteryhall_today_rules(self):
        # 彩票大厅
        # 今日开奖---规则校对
        self.base_driver.forced_wait(5)
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '今日开奖')
        for i in range(100):
            try:
                # 时间
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TIME_NUM'], i)
                qishu = self.base_driver.get_texts(self.config_dict_tmmcq['PERIODS_NUM'], i)
                # print(datetime)
                # print(qishu)
                if datetime[:10] == time.strftime('%Y-%m-%d'):
                    # 总和
                    s0 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_SUM'], i)
                    # 总和大小
                    s1 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_DX_NUM'], i)
                    # 总和单双
                    s2 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_DS_NUM'], i)

                    # 开奖号码1-5
                    s3 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM01'], i)
                    s4 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM02'], i)
                    s5 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM03'], i)
                    s6 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM04'], i)
                    s7 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM05'], i)
                    # 1-5龙虎
                    s8 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_LH_NUM'], i)
                    # print(s0)
                    # print(str(s3) + str(s4) + str(s5))
                    m0 = [int(s3), int(s4), int(s5), int(s6), int(s7)]
                    # print(sum(m0))
                    if str(s0) == str(sum(m0)):
                        pass
                        if sum(m0) > 22:
                            if s1 == '大':
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和大---正确')
                            else:
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和大---错误')
                            if sum(m0) % 2 == 0:
                                if s2 == '双':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双---错误')
                            if sum(m0) % 2 == 1:
                                if s2 == '单':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单---错误')
                            if s3 > s7:
                                if s8 == '龙':
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和龙---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和龙---错误')
                            if s3 == s7:
                                if s8 == '和':
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和和---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和和---错误')
                            if s3 < s7:
                                if s8 == '虎':
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和虎---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和虎---错误')
                        if sum(m0) < 23:
                            if s1 == '小':
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和小---正确')
                            else:
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和小---错误')
                            if sum(m0) % 2 == 0:
                                if s2 == '双':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双---错误')
                            if sum(m0) % 2 == 1:
                                if s2 == '单':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单---错误')
                            if s3 > s7:
                                if s8 == '龙':
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和龙---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和龙---错误')
                            if s3 == s7:
                                if s8 == '和':
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和和---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和和---错误')
                            if s3 < s7:
                                if s8 == '虎':
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和虎---正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(s8) + '  总和虎---错误')

                    else:
                        print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和---错误')
            #
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

    def lotteryhall_trend_basic(self):
        # 走势图
        # 基本走势
        self.base_driver.forced_wait(1)
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')

        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '基本走势')
        self.base_driver.forced_wait(5)

        a00 = []
        a01 = []
        a02 = []
        a03 = []
        a04 = []

        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d'):
                    # 开奖号码
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_LOTTERY_NUM_01'], i)
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_LOTTERY_NUM_02'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_LOTTERY_NUM_03'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_LOTTERY_NUM_04'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_LOTTERY_NUM_05'], i)

                    a00.append(s00)
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a00)
        print(a01)
        print(a02)
        print(a03)
        print(a04)
        # 数据统计
        # 出现次数 第一球0~9
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 1)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 2)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 3)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 4)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 5)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 6)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 7)
        ball_1_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 8)
        ball_1_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 9)
        ball_1_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 10)
        ball_1_10 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 11)
        ss = [ball_1_0, ball_1_1, ball_1_2, ball_1_2, ball_1_3, ball_1_4,
              ball_1_5, ball_1_6, ball_1_7, ball_1_8, ball_1_9, ball_1_10]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_0))
        print('a00.count:  ' + str(a00.count('01')))
        if str(ball_1_0) == str(a00.count('01')):
            print('第一球统计01---正确---' + str(a00.count('01')))
        else:
            print('第一球统计01---错误---' + str(a00.count('01')))
        if str(ball_1_1) == str(a00.count('02')):
            print('第一球统计02---正确---' + str(a00.count('02')))
        else:
            print('第一球统计02---错误---' + str(a00.count('2')))
        if str(ball_1_2) == str(a00.count('03')):
            print('第一球统计03---正确---' + str(a00.count('03')))
        else:
            print('第一球统计03---错误---' + str(a00.count('03')))
        if str(ball_1_3) == str(a00.count('04')):
            print('第一球统计04---正确---' + str(a00.count('04')))
        else:
            print('第一球统计05---错误---' + str(a00.count('04')))
        if str(ball_1_4) == str(a00.count('05')):
            print('第一球统计05---正确---' + str(a00.count('05')))
        else:
            print('第一球统计05---错误---' + str(a00.count('05')))
        if str(ball_1_5) == str(a00.count('06')):
            print('第一球统计06---正确---' + str(a00.count('06')))
        else:
            print('第一球统计06---错误---' + str(a00.count('06')))
        if str(ball_1_6) == str(a00.count('07')):
            print('第一球统计07---正确---' + str(a00.count('07')))
        else:
            print('第一球统计07---错误---' + str(a00.count('07')))
        if str(ball_1_7) == str(a00.count('08')):
            print('第一球统计08---正确---' + str(a00.count('08')))
        else:
            print('第一球统计08---错误---' + str(a00.count('08')))
        if str(ball_1_8) == str(a00.count('09')):
            print('第一球统计09---正确---' + str(a00.count('09')))
        else:
            print('第一球统计09---错误---' + str(a00.count('09')))
        if str(ball_1_9) == str(a00.count('10')):
            print('第一球统计10---正确---' + str(a00.count('10')))
        else:
            print('第一球统计10---错误---' + str(a00.count('10')))
        if str(ball_1_10) == str(a00.count('11')):
            print('第一球统计11---正确---' + str(a00.count('11')))
        else:
            print('第一球统计11---错误---' + str(a00.count('11')))

        # 第二球0~9
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 12)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 13)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 14)
        ball_2_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 15)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 16)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 17)
        ball_2_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 18)
        ball_2_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 19)
        ball_2_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 20)
        ball_2_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 21)
        ball_2_10 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 22)
        if str(ball_2_0) == str(a01.count('01')):
            print('第二球统计01---正确---' + str(a01.count('01')))
        else:
            print('第二球统计01---错误---' + str(a01.count('01')))
        if str(ball_2_1) == str(a01.count('02')):
            print('第二球统计02---正确---' + str(a01.count('02')))
        else:
            print('第一球统计02---错误---' + str(a01.count('02')))
        if str(ball_2_2) == str(a01.count('03')):
            print('第二球统计03---正确---' + str(a01.count('03')))
        else:
            print('第二球统计03---错误---' + str(a01.count('03')))
        if str(ball_2_3) == str(a01.count('04')):
            print('第二球统计04---正确---' + str(a01.count('04')))
        else:
            print('第二球统计04---错误---' + str(a01.count('04')))
        if str(ball_2_4) == str(a01.count('05')):
            print('第一球统计05---正确---' + str(a01.count('05')))
        else:
            print('第二球统计05---错误---' + str(a01.count('05')))
        if str(ball_2_5) == str(a01.count('06')):
            print('第二球统计06---正确---' + str(a01.count('06')))
        else:
            print('第二球统计06---错误---' + str(a01.count('06')))
        if str(ball_2_6) == str(a01.count('07')):
            print('第二球统计07---正确---' + str(a01.count('07')))
        else:
            print('第二球统计07---错误---' + str(a01.count('07')))
        if str(ball_2_7) == str(a01.count('08')):
            print('第二球统计08---正确---' + str(a01.count('8')))
        else:
            print('第二球统计08---错误---' + str(a01.count('8')))
        if str(ball_2_8) == str(a01.count('09')):
            print('第二球统计09---正确---' + str(a01.count('09')))
        else:
            print('第二球统计09---错误---' + str(a01.count('09')))
        if str(ball_2_9) == str(a01.count('10')):
            print('第二球统计10---正确---' + str(a01.count('10')))
        else:
            print('第二球统计10---错误---' + str(a01.count('10')))
        if str(ball_2_10) == str(a01.count('11')):
            print('第二球统计11---正确---' + str(a01.count('11')))
        else:
            print('第二球统计11---错误---' + str(a01.count('11')))
        # 出现次数 第三球0~9
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 23)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 24)
        ball_3_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 25)
        ball_3_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 26)
        ball_3_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 27)
        ball_3_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 28)
        ball_3_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 29)
        ball_3_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 30)
        ball_3_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 31)
        ball_3_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 32)
        ball_3_10 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 33)
        if str(ball_3_0) == str(a02.count('01')):
            print('第三球统计01---正确---' + str(a02.count('01')))
        else:
            print('第三球统计01---错误---' + str(a02.count('01')))
        if str(ball_3_1) == str(a02.count('02')):
            print('第三球统计02---正确---' + str(a02.count('02')))
        else:
            print('第三球统计02---错误---' + str(a02.count('02')))
        if str(ball_3_2) == str(a02.count('03')):
            print('第三球统计03---正确---' + str(a02.count('03')))
        else:
            print('第一球统计03---错误---' + str(a02.count('03')))
        if str(ball_3_3) == str(a02.count('04')):
            print('第三球统计04---正确---' + str(a02.count('04')))
        else:
            print('第三球统计04---错误---' + str(a02.count('04')))
        if str(ball_3_4) == str(a02.count('05')):
            print('第三球统计05---正确---' + str(a02.count('05')))
        else:
            print('第三球统计05---错误---' + str(a02.count('05')))
        if str(ball_3_5) == str(a02.count('06')):
            print('第三球统计06---正确---' + str(a02.count('06')))
        else:
            print('第三球统计06---错误---' + str(a02.count('06')))
        if str(ball_3_6) == str(a02.count('07')):
            print('第三球统计07---正确---' + str(a02.count('07')))
        else:
            print('第三球统计07---错误---' + str(a02.count('07')))
        if str(ball_3_7) == str(a02.count('08')):
            print('第三球统计08---正确---' + str(a02.count('08')))
        else:
            print('第三球统计08---错误---' + str(a02.count('08')))
        if str(ball_3_8) == str(a02.count('09')):
            print('第三球统计09---正确---' + str(a02.count('09')))
        else:
            print('第三球统计09---错误---' + str(a02.count('09')))
        if str(ball_3_9) == str(a02.count('10')):
            print('第三球统计10---正确---' + str(a02.count('10')))
        else:
            print('第三球统计10---错误---' + str(a02.count('10')))
        if str(ball_3_10) == str(a02.count('11')):
            print('第三球统计11---正确---' + str(a02.count('11')))
        else:
            print('第三球统计11---错误---' + str(a02.count('11')))

        # 出现次数 第四球0~9
        ball_4_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 34)
        ball_4_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 35)
        ball_4_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 36)
        ball_4_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 37)
        ball_4_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 38)
        ball_4_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 39)
        ball_4_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 40)
        ball_4_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 41)
        ball_4_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 42)
        ball_4_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 43)
        ball_4_10 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 44)
        if str(ball_4_0) == str(a03.count('01')):
            print('第四球统计01---正确---' + str(a03.count('01')))
        else:
            print('第四球统计01---错误---' + str(a03.count('01')))
        if str(ball_4_1) == str(a03.count('02')):
            print('第四球统计02---正确---' + str(a03.count('02')))
        else:
            print('第一球统计02---错误---' + str(a03.count('02')))
        if str(ball_4_2) == str(a03.count('03')):
            print('第四球统计03---正确---' + str(a03.count('03')))
        else:
            print('第四球统计03---错误---' + str(a03.count('03')))
        if str(ball_4_3) == str(a03.count('04')):
            print('第四球统计04---正确---' + str(a03.count('04')))
        else:
            print('第四球统计04---错误---' + str(a03.count('04')))
        if str(ball_4_4) == str(a03.count('05')):
            print('第四球统计05---正确---' + str(a03.count('05')))
        else:
            print('第四球统计05---错误---' + str(a03.count('05')))
        if str(ball_4_5) == str(a03.count('06')):
            print('第四球统计06---正确---' + str(a03.count('06')))
        else:
            print('第四球统计06---错误---' + str(a03.count('06')))
        if str(ball_4_6) == str(a03.count('07')):
            print('第四球统计07---正确---' + str(a03.count('07')))
        else:
            print('第四球统计07---错误---' + str(a03.count('07')))
        if str(ball_4_7) == str(a03.count('08')):
            print('第四球统计08---正确---' + str(a03.count('08')))
        else:
            print('第四球统计08---错误---' + str(a03.count('08')))
        if str(ball_4_8) == str(a03.count('09')):
            print('第四球统计09---正确---' + str(a03.count('09')))
        else:
            print('第四球统计09---错误---' + str(a03.count('09')))
        if str(ball_4_9) == str(a03.count('10')):
            print('第四球统计10---正确---' + str(a03.count('10')))
        else:
            print('第四球统计10---错误---' + str(a03.count('10')))
        if str(ball_4_10) == str(a03.count('11')):
            print('第四球统计11---正确---' + str(a03.count('11')))
        else:
            print('第四球统计11---错误---' + str(a03.count('11')))

        # 出现次数 第五球0~9
        ball_5_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 45)
        ball_5_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 46)
        ball_5_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 47)
        ball_5_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 48)
        ball_5_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 49)
        ball_5_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 50)
        ball_5_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 51)
        ball_5_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 52)
        ball_5_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 53)
        ball_5_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 54)
        ball_5_10 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 55)
        if str(ball_5_0) == str(a04.count('01')):
            print('第五球统计01---正确---' + str(a04.count('01')))
        else:
            print('第五球统计01---错误---' + str(a04.count('01')))
        if str(ball_5_1) == str(a04.count('02')):
            print('第五球统计02---正确---' + str(a04.count('02')))
        else:
            print('第五球统计02---错误---' + str(a04.count('02')))
        if str(ball_5_2) == str(a04.count('03')):
            print('第五球统计03---正确---' + str(a04.count('03')))
        else:
            print('第五球统计03---错误---' + str(a04.count('03')))
        if str(ball_5_3) == str(a04.count('04')):
            print('第五球统计04---正确---' + str(a04.count('04')))
        else:
            print('第五球统计04---错误---' + str(a04.count('04')))
        if str(ball_5_4) == str(a04.count('05')):
            print('第五球统计05---正确---' + str(a04.count('05')))
        else:
            print('第五球统计05---错误---' + str(a04.count('05')))
        if str(ball_5_5) == str(a04.count('06')):
            print('第五球统计06---正确---' + str(a04.count('06')))
        else:
            print('第五球统计06---错误---' + str(a04.count('06')))
        if str(ball_5_6) == str(a04.count('07')):
            print('第五球统计07---正确---' + str(a04.count('07')))
        else:
            print('第五球统计07---错误---' + str(a04.count('07')))
        if str(ball_5_7) == str(a04.count('08')):
            print('第五球统计08---正确---' + str(a04.count('08')))
        else:
            print('第五球统计08---错误---' + str(a04.count('08')))
        if str(ball_5_8) == str(a04.count('09')):
            print('第五球统计09---正确---' + str(a04.count('09')))
        else:
            print('第五球统计09---错误---' + str(a04.count('09')))
        if str(ball_5_9) == str(a04.count('10')):
            print('第五球统计10---正确---' + str(a04.count('10')))
        else:
            print('第五球统计10---错误---' + str(a04.count('10')))
        if str(ball_5_10) == str(a04.count('11')):
            print('第五球统计11---正确---' + str(a04.count('11')))
        else:
            print('第五球统计11---错误---' + str(a04.count('11')))

    def lotteryhall_trend_position(self):
        # 走势图
        # 定位走势
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '定位走势')
        # # 日期选择
        # self.base_driver.clicks_by_text(self.config_dict_tmmcq['DATA_SELECT'], '90期')
        # self.base_driver.forced_wait(1)
        # 球号选择
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['BALL_SELECT'], '第一球')
        self.base_driver.forced_wait(3)

        a00 = []

        a10 = []
        a11 = []
        a12 = []
        a13 = []
        a14 = []
        a15 = []
        a16 = []
        a17 = []
        a18 = []
        a19 = []
        a20 = []
        a21 = []

        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d'):
                    # 开奖号码~第一个号码
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_LOTTERY_NUM_01'], i)

                    # 形态特征---大小-单双-合质
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_1'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_2'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_3'], i)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_4'], i)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_5'], i)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_6'], i)

                    # 012路
                    # s16 = self.base_driver.get_attribute(self.config_dict_tmmcq['LU_0'], 'class')
                    # s17 = self.base_driver.get_attribute_text(self.config_dict_tmmcq['LU_1'], 'class', i)
                    # s18 = self.base_driver.get_attribute_text(self.config_dict_tmmcq['LU_2'], 'class', i)

                    # 升平降
                    s19 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_10'], i)
                    s20 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_11'], i)
                    s21 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_1'], i)
                    # print(s19)
                    # print(s20)
                    # print(s21)
                    a00.append(s00)

                    a10.append(s10)
                    a11.append(s11)
                    a12.append(s12)
                    a13.append(s13)
                    a14.append(s14)
                    a15.append(s15)

                    # a16.append(s16)
                    # a17.append(s17)
                    # a18.append(s18)
                    #
                    a19.append(s19)
                    a20.append(s20)
                    a21.append(s21)

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a00)
        # 数据统计
        # 出现次数 第一球0~9
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 22)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 23)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 24)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 25)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 26)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 27)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 28)
        ball_1_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 29)
        ball_1_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 30)
        ball_1_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 31)
        ball_1_10 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 32)
        ss = [ball_1_0, ball_1_1, ball_1_2, ball_1_3, ball_1_4, ball_1_5, ball_1_6, ball_1_7, ball_1_8, ball_1_9]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_0))
        print('a00.count:  ' + str(a00.count('01')))
        if str(ball_1_0) == str(a00.count('01')):
            print('第一球号码走势统计01---正确---' + str(a00.count('01')))
        else:
            print('第一球号码走势统计01---错误---' + str(a00.count('01')))
        if str(ball_1_1) == str(a00.count('02')):
            print('第一球号码走势统计02---正确---' + str(a00.count('02')))
        else:
            print('第一球号码走势统计02---错误---' + str(a00.count('02')))
        if str(ball_1_2) == str(a00.count('03')):
            print('第一球号码走势统计03---正确---' + str(a00.count('03')))
        else:
            print('第一球号码走势统计03---错误---' + str(a00.count('03')))
        if str(ball_1_3) == str(a00.count('04')):
            print('第一球号码走势统计04---正确---' + str(a00.count('04')))
        else:
            print('第一球号码走势统计04---错误---' + str(a00.count('04')))
        if str(ball_1_4) == str(a00.count('05')):
            print('第一球号码走势统计05---正确---' + str(a00.count('05')))
        else:
            print('第一球号码走势统计05---错误---' + str(a00.count('05')))
        if str(ball_1_5) == str(a00.count('06')):
            print('第一球号码走势统计06---正确---' + str(a00.count('06')))
        else:
            print('第一球号码走势统计06---错误---' + str(a00.count('06')))
        if str(ball_1_6) == str(a00.count('07')):
            print('第一球号码走势统计07---正确---' + str(a00.count('07')))
        else:
            print('第一球号码走势统计07---错误---' + str(a00.count('07')))
        if str(ball_1_7) == str(a00.count('08')):
            print('第一球号码走势统计08---正确---' + str(a00.count('08')))
        else:
            print('第一球号码走势统计08---错误---' + str(a00.count('08')))
        if str(ball_1_8) == str(a00.count('09')):
            print('第一球号码走势统计09---正确---' + str(a00.count('09')))
        else:
            print('第一球号码走势统计09---错误---' + str(a00.count('09')))
        if str(ball_1_9) == str(a00.count('10')):
            print('第一球号码走势统计10---正确---' + str(a00.count('10')))
        else:
            print('第一球号码走势统计10---错误---' + str(a00.count('10')))
        if str(ball_1_10) == str(a00.count('11')):
            print('第一球号码走势统计11---正确---' + str(a00.count('11')))
        else:
            print('第一球号码走势统计11---错误---' + str(a00.count('11')))
        # 形态特征
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 33)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 34)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 35)
        ball_2_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 36)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 37)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 38)

        # print('ball_2_0:   ' + str(ball_2_0))
        # print('-----' + str(a10.count('0')))
        if str(ball_2_0) == str(a10.count('大')):
            print('形态特征大---正确---' + str(a10.count('大')))
        else:
            print('形态特征大---错误---' + str(a10.count('大')))
        if str(ball_2_1) == str(a11.count('小')):
            print('形态特征小---正确---' + str(a11.count('小')))
        else:
            print('形态特征小---错误---' + str(a11.count('小')))
        if str(ball_2_2) == str(a12.count('单')):
            print('形态特征单---正确---' + str(a12.count('单')))
        else:
            print('形态特征单---错误---' + str(a12.count('单')))
        if str(ball_2_3) == str(a13.count('双')):
            print('形态特征双---正确---' + str(a13.count('双')))
        else:
            print('形态特征双---错误---' + str(a13.count('双')))
        if str(ball_2_4) == str(a14.count('合')):
            print('形态特征合---正确---' + str(a14.count('合')))
        else:
            print('形态特征合---错误---' + str(a14.count('合')))
        if str(ball_2_5) == str(a15.count('质')):
            print('形态特征质---正确---' + str(a15.count('质')))
        else:
            print('形态特征质---错误---' + str(a15.count('质')))

        # # 012路
        # ball_2_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 39)
        # ball_2_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 40)
        # ball_2_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 41)
        # if str(ball_2_6) == str(a16.count('yellowbg')):
        #     print('012路0---正确---' + str(a16.count('yellowbg')))
        # else:
        #     print('012路0---错误---' + str(a16.count('yellowbg')))
        # if str(ball_2_7) == str(a17.count('bluebg')):
        #     print('012路1---正确---' + str(a17.count('bluebg')))
        # else:
        #     print('012路1---错误---' + str(a17.count('bluebg')))
        # if str(ball_2_8) == str(a18.count('yellowbg')):
        #     print('012路2---正确---' + str(a18.count('yellowbg')))
        # else:
        #     print('012路2---错误---' + str(a18.count('yellowbg')))

        # 升平降
        ball_2_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 42)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 43)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 44)
        if str(ball_2_9) == str(a19.count('升')):
            print('升平降-升---正确---' + str(a19.count('升')))
        else:
            print('升平降-升---错误---' + str(a19.count('升')))
        if str(ball_3_0) == str(a20.count('平')):
            print('升平降-平---正确---' + str(a20.count('平')))
        else:
            print('升平降-平---错误---' + str(a20.count('平')))
        if str(ball_3_1) == str(a21.count('降')):
            print('升平降-降---正确---' + str(a21.count('降')))
        else:
            print('升平降-降---错误---' + str(a21.count('降')))

    def lotteryhall_trend_size(self):
        # 走势图
        # 大小走势
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '大小走势')
        self.base_driver.forced_wait(5)
        a00 = []
        a01 = []
        a02 = []
        a03 = []
        a04 = []
        a05 = []
        a06 = []
        a07 = []
        a08 = []
        a09 = []
        a10 = []

        aaa = []
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i+1)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d'):
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)
                    # 第一位~第五位
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_0'], i+1)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_1'], i+1)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_0'], i+1)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_1'], i+1)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_0'], i+1)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_1'], i+1)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_0'], i+1)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_1'], i+1)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_0'], i+1)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_1'], i)

                    # a00.append(s00[0])
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)
                    a07.append(s07)
                    a08.append(s08)
                    a09.append(s09)
                    a10.append(s10)
                    aaa = [s01, s02, s03, s04, s05, s06]
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

        print(a01)
        print('aaa   ' + str(aaa))
        # 号码分布
        ball_0_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 0)
        ball_0_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 1)
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 2)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 3)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 4)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 5)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 6)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 7)
        ball_4_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 8)
        ball_4_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 9)

        ss = [ball_0_0, ball_0_1, ball_1_0, ball_1_1, ball_2_0, ball_2_1]
        print(ss)
        print('ball_0_0:   ' + str(ball_0_0))
        print('a00.count:  ' + str(a01.count('大')))
        if str(ball_0_0) == str(a01.count('大')):
            print('第一位统计大---正确---' + str(a01.count('大')))
        else:
            print('第一位统计大---错误---' + str(a01.count('大')))
        if str(ball_0_1) == str(a02.count('小')):
            print('第一位统计小---正确---' + str(a02.count('小')))
        else:
            print('第一位统计小---错误---' + str(a02.count('小')))
        if str(ball_1_0) == str(a03.count('大')):
            print('第二位统计大---正确---' + str(a03.count('大')))
        else:
            print('第二位统计大---错误---' + str(a03.count('大')))
        if str(ball_1_1) == str(a04.count('小')):
            print('第二位统计小---正确---' + str(a04.count('小')))
        else:
            print('第二位统计小---错误---' + str(a04.count('小')))
        if str(ball_2_0) == str(a05.count('大')):
            print('第三位统计大---正确---' + str(a05.count('大')))
        else:
            print('第三位统计大---错误---' + str(a05.count('大')))
        if str(ball_2_1) == str(a06.count('小')):
            print('第三位统计小---正确---' + str(a06.count('小')))
        else:
            print('第三位统计小---错误---' + str(a06.count('小')))

        if str(ball_3_0) == str(a07.count('大')):
            print('第四位统计大---正确---' + str(a07.count('大')))
        else:
            print('第四位统计大---错误---' + str(a07.count('大')))
        if str(ball_3_1) == str(a08.count('小')):
            print('第四位统计小---正确---' + str(a08.count('小')))
        else:
            print('第四位统计小---错误---' + str(a08.count('小')))
        if str(ball_4_0) == str(a09.count('大')):
            print('第五位统计大---正确---' + str(a09.count('大')))
        else:
            print('第五位统计大---错误---' + str(a09.count('大')))
        if str(ball_4_1) == str(a10.count('小')):
            print('第五位统计小---正确---' + str(a10.count('小')))
        else:
            print('第五位统计小---错误---' + str(a10.count('小')))

    def lotteryhall_trend_double(self):
        # 走势图
        # 单双走势
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '单双走势')
        self.base_driver.forced_wait(5)
        a00 = []
        a01 = []
        a02 = []
        a03 = []
        a04 = []
        a05 = []
        a06 = []
        a07 = []
        a08 = []
        a09 = []
        a10 = []

        aaa = []
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i+1)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d'):
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)
                    # 第一位~第五位
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_0'], i+1)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_1'], i+1)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_0'], i+1)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_1'], i+1)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_0'], i+1)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_1'], i+1)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_0'], i+1)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_1'], i+1)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_0'], i+1)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_1'], i)

                    # a00.append(s00[0])
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)
                    a07.append(s07)
                    a08.append(s08)
                    a09.append(s09)
                    a10.append(s10)
                    aaa = [s01, s02, s03, s04, s05, s06]
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

        print(a01)
        print('aaa   ' + str(aaa))
        # 号码分布
        ball_0_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 0)
        ball_0_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 1)
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 2)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 3)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 4)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 5)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 6)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 7)
        ball_4_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 8)
        ball_4_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM_DX'], 9)

        ss = [ball_0_0, ball_0_1, ball_1_0, ball_1_1, ball_2_0, ball_2_1]
        print(ss)
        print('ball_0_0:   ' + str(ball_0_0))
        print('a00.count:  ' + str(a01.count('单')))
        if str(ball_0_0) == str(a01.count('单')):
            print('第一位统计单---正确---' + str(a01.count('单')))
        else:
            print('第一位统计单---错误---' + str(a01.count('单')))
        if str(ball_0_1) == str(a02.count('双')):
            print('第一位统计双---正确---' + str(a02.count('双')))
        else:
            print('第一位统计双---错误---' + str(a02.count('双')))
        if str(ball_1_0) == str(a03.count('单')):
            print('第二位统计单---正确---' + str(a03.count('单')))
        else:
            print('第二位统计单---错误---' + str(a03.count('单')))
        if str(ball_1_1) == str(a04.count('双')):
            print('第二位统计双---正确---' + str(a04.count('双')))
        else:
            print('第二位统计双---错误---' + str(a04.count('双')))
        if str(ball_2_0) == str(a05.count('单')):
            print('第三位统计单---正确---' + str(a05.count('单')))
        else:
            print('第三位统计单---错误---' + str(a05.count('单')))
        if str(ball_2_1) == str(a06.count('双')):
            print('第三位统计双---正确---' + str(a06.count('双')))
        else:
            print('第三位统计双---错误---' + str(a06.count('双')))
        if str(ball_3_0) == str(a07.count('单')):
            print('第四位统计单---正确---' + str(a07.count('单')))
        else:
            print('第四位统计单---错误---' + str(a07.count('单')))
        if str(ball_3_1) == str(a08.count('双')):
            print('第四位统计双---正确---' + str(a08.count('双')))
        else:
            print('第四位统计双---错误---' + str(a08.count('双')))
        if str(ball_4_0) == str(a09.count('单')):
            print('第五位统计单---正确---' + str(a09.count('单')))
        else:
            print('第五位统计单---错误---' + str(a09.count('单')))
        if str(ball_4_1) == str(a10.count('双')):
            print('第五位统计双---正确---' + str(a10.count('双')))
        else:
            print('第五位统计双---错误---' + str(a10.count('双')))

    def plan_winkillnum_w(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 万位杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '万位杀号')
        self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/万位杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/万位杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_tmmcq['WYQISHU'], i+1)

                # 开奖号码
                # s1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM00'], i)
                a1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM01'], i)
                a2 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM02'], i)
                a3 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM03'], i)
                a4 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM04'], i)
                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM00'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM01'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM02'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM03'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM04'], i+1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM04'], i+1)

                m0 = [a0, a1, a2, a3, a4]
                f = open("/fusion/lottery_hall/pk10/万位杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a0) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a0) or (c0 == '杀错' and b0[2:] == a0):
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b0) + str(c0) + '  万号正确' + str(b0))
                if (c1 == '杀对' and b1[2:] != a0) or (c1 == '杀错' and b1[2:] == a0):
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b1) + str(c1) + '  万号正确' + str(b1))
                if (c2 == '杀对' and b2[2:] != a0) or (c2 == '杀错' and b2[2:] == a0):
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b2) + str(c2) + '  万号正确' + str(b2))
                if (c3 == '杀对' and b3[2:] != a0) or (c3 == '杀错' and b3[2:] == a0):
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b3) + str(c3) + '  万号正确' + str(b3))
                if (c4 == '杀对' and b4[2:] != a0) or (c4 == '杀错' and b4[2:] == a0):
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b4) + str(c4) + '  万号正确' + str(b4))
                else:
                    print('期数' + str(s0) + '万号错误')
            except Exception as e:
                print(e)
                print('稳赢杀号万位杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_q(self):
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(2)
        # 千位杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '千位杀号')
        self.base_driver.forced_wait(2)
        if os.path.exists("/fusion/lottery_hall/pk10/千位杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/千位杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_tmmcq['WYQISHU'], i + 1)

                # 开奖号码
                # s1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM00'], i)
                a1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM01'], i)
                a2 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM02'], i)
                a3 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM03'], i)
                a4 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM04'], i)
                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM00'], i + 1)
                b1 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM01'], i + 1)
                b2 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM02'], i + 1)
                b3 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM03'], i + 1)
                b4 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM04'], i + 1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM00'], i + 1)
                c1 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM01'], i + 1)
                c2 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM02'], i + 1)
                c3 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM03'], i + 1)
                c4 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM04'], i + 1)

                m0 = [a0, a1, a2, a3, a4]

                f = open("/fusion/lottery_hall/pk10/千位杀号.txt", 'a', encoding='utf-8')

                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a1) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a1) or (c0 == '杀错' and b0[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b0) + str(c0) + '  千号正确' + str(b0))
                if (c1 == '杀对' and b1[2:] != a1) or (c1 == '杀错' and b1[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b1) + str(c1) + '  千号正确' + str(b1))
                if (c2 == '杀对' and b2[2:] != a1) or (c2 == '杀错' and b2[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b2) + str(c2) + '  千号正确' + str(b2))
                if (c3 == '杀对' and b3[2:] != a1) or (c3 == '杀错' and b3[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b3) + str(c3) + '  千号正确' + str(b3))
                if (c4 == '杀对' and b4[2:] != a1) or (c4 == '杀错' and b4[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b4) + str(c4) + '  千号正确' + str(b4))
                else:
                    print('期数' + str(s0) + '千号错误')
            except Exception as e:
                print(e)
                print('稳赢杀号千万位杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_b(self):
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(2)
        # 百位杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '百位杀号')
        self.base_driver.forced_wait(2)
        if os.path.exists("/fusion/lottery_hall/pk10/百位杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/百位杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_tmmcq['WYQISHU'], i+1)

                # 开奖号码
                # s1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM00'], i)
                a1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM01'], i)
                a2 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM02'], i)
                a3 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM03'], i)
                a4 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM04'], i)
                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM00'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM01'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM02'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM03'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM04'], i+1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM04'], i+1)

                m0 = [a0, a1, a2, a3, a4]

                f = open("/fusion/lottery_hall/pk10/百位杀号.txt", 'a', encoding='utf-8')

                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a2) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a2) or (c0 == '杀错' and b0[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b0) + str(c0) + '  百号正确' + str(b0))
                if (c1 == '杀对' and b1[2:] != a2) or (c1 == '杀错' and b1[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b1) + str(c1) + '  百号正确' + str(b1))
                if (c2 == '杀对' and b2[2:] != a2) or (c2 == '杀错' and b2[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b2) + str(c2) + '  百号正确' + str(b2))
                if (c3 == '杀对' and b3[2:] != a2) or (c3 == '杀错' and b3[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b3) + str(c3) + '  百号正确' + str(b3))
                if (c4 == '杀对' and b4[2:] != a2) or (c4 == '杀错' and b4[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b4) + str(c4) + '  百号正确' + str(b4))
                else:
                    print('期数' + str(s0) + '百号错误')
            except Exception as e:
                print(e)
                print('稳赢杀号百位杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_s(self):
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(2)
        # 十位杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '十位杀号')
        self.base_driver.forced_wait(2)
        if os.path.exists("/fusion/lottery_hall/pk10/十位杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/十位杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_tmmcq['WYQISHU'], i+1)

                # 开奖号码
                # s1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM00'], i)
                a1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM01'], i)
                a2 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM02'], i)
                a3 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM03'], i)
                a4 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM04'], i)
                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM00'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM01'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM02'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM03'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM04'], i+1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM04'], i+1)

                m0 = [a0, a1, a2, a3, a4]

                f = open("/fusion/lottery_hall/pk10/十位杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a3) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a3) or (c0 == '杀错' and b0[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b0) + str(c0) + '  十号正确' + str(b0))
                if (c1 == '杀对' and b1[2:] != a3) or (c1 == '杀错' and b1[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b1) + str(c1) + '  十号正确' + str(b1))
                if (c2 == '杀对' and b2[2:] != a3) or (c2 == '杀错' and b2[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b2) + str(c2) + '  十号正确' + str(b2))
                if (c3 == '杀对' and b3[2:] != a3) or (c3 == '杀错' and b3[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b3) + str(c3) + '  十号正确' + str(b3))
                if (c4 == '杀对' and b4[2:] != a3) or (c4 == '杀错' and b4[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b4) + str(c4) + '  十号正确' + str(b4))
                else:
                    print('期数' + str(s0) + '十号错误')
            except Exception as e:
                print(e)
                print('稳赢杀号十位杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_g(self):
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(2)
        # 个位杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '个位杀号')
        self.base_driver.forced_wait(2)
        if os.path.exists("/fusion/lottery_hall/pk10/个位杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/个位杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_tmmcq['WYQISHU'], i+1)

                # 开奖号码
                # s1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM00'], i)
                a1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM01'], i)
                a2 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM02'], i)
                a3 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM03'], i)
                a4 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM04'], i)
                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM00'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM01'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM02'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM03'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_tmmcq['KILLNUM04'], i+1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_tmmcq['ZHANJINUM04'], i+1)

                m0 = [a0, a1, a2, a3, a4]

                f = open("/fusion/lottery_hall/pk10/个位杀号.txt", 'a', encoding='utf-8')

                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a4) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a4) or (c0 == '杀错' and b0[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b0) + str(c0) + '  个号正确' + str(b0))
                if (c1 == '杀对' and b1[2:] != a4) or (c1 == '杀错' and b1[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b1) + str(c1) + '  个号正确' + str(b1))
                if (c2 == '杀对' and b2[2:] != a4) or (c2 == '杀错' and b2[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b2) + str(c2) + '  个号正确' + str(b2))
                if (c3 == '杀对' and b3[2:] != a4) or (c3 == '杀错' and b3[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b3) + str(c3) + '  个号正确' + str(b3))
                if (c4 == '杀对' and b4[2:] != a4) or (c4 == '杀错' and b4[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b4) + str(c4) + '  个号正确' + str(b4))
                else:
                    print('期数' + str(s0) + '个号错误')
            except Exception as e:
                print(e)
                print('稳赢杀号个位杀号运行' + str(i) + '行')
                break









