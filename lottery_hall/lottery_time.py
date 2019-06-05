import os
import random
import time
from _operator import length_hint

from common.box import BasePage, YamlHelper


class LotteryTime(BasePage):

    config_dict_tmmcq = YamlHelper().get_config_dict('/fusion/lottery_hall/yaml/lottery_time.yaml')['PLAN_TIMELOTTERT']

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

    def lotteryhall_today_double_count(self):
        # 彩票大厅
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '今日开奖')
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
        for i in range(100):
            try:
                # 时间
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TIME_NUM'], i)
                # print(time.strftime('%Y-%m-%d'))
                if datetime[:10] == time.strftime('%Y-%m-%d'):
                    # 总和大小
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_DX_NUM'], i)
                    # 总和单双
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_DS_NUM'], i)
                    # 1-5龙虎
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['SUM_LH_NUM'], i)

                    # 开奖号码1-5
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['LOEEERY_NUM01'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['LOEEERY_NUM02'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['LOEEERY_NUM03'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['LOEEERY_NUM04'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['LOEEERY_NUM05'], i)

                    a00.append(s00)
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)
                    a07.append(s07)
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

        # 获取表格号码统计的数据
        m00 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 1)
        m01 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 2)
        m02 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 3)
        m03 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 4)
        m04 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 5)
        m05 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 6)
        m06 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 7)
        m07 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 8)
        m08 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 9)
        m09 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 10)

        # 获取表格球次统计的数据
        n00 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 1)
        n01 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 2)
        n02 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 3)
        n03 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 4)
        n04 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 5)
        n05 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 6)
        n06 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 7)
        n07 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 8)
        n08 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 9)
        n09 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 10)
        n10 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 11)
        n11 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 12)
        n12 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 13)
        n13 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 14)
        n14 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 15)
        n15 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 16)
        n16 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 17)
        n17 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 18)
        n18 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 19)
        n19 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 20)
        n20 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 21)
        n21 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 22)
        n22 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 23)
        n23 = self.base_driver.get_texts(self.config_dict_tmmcq['BALLS_APPEAR'], 24)

        b00 = a02.count('0') + a03.count('0') + a04.count('0') + a05.count('0') + a06.count('0')
        b01 = a02.count('1') + a03.count('1') + a04.count('1') + a05.count('1') + a06.count('1')
        b02 = a02.count('2') + a03.count('2') + a04.count('2') + a05.count('2') + a06.count('2')
        b03 = a02.count('3') + a03.count('3') + a04.count('3') + a05.count('3') + a06.count('3')
        b04 = a02.count('4') + a03.count('4') + a04.count('4') + a05.count('4') + a06.count('4')
        b05 = a02.count('5') + a03.count('5') + a04.count('5') + a05.count('5') + a06.count('5')
        b06 = a02.count('6') + a03.count('6') + a04.count('6') + a05.count('6') + a06.count('6')
        b07 = a02.count('7') + a03.count('7') + a04.count('7') + a05.count('7') + a06.count('7')
        b08 = a02.count('8') + a03.count('8') + a04.count('8') + a05.count('8') + a06.count('8')
        b09 = a02.count('9') + a03.count('9') + a04.count('9') + a05.count('9') + a06.count('9')

        print('        ')
        if str(m00) == str(b00):
            print(' 号码0出现次数统计正确：' + str(b00))
        else:
            print(' 号码0出现次数统计错误：' + str(b00))
        if str(m01) == str(b01):
            print(' 号码1出现次数统计正确：' + str(b01))
        else:
            print(' 号码1出现次数统计错误：' + str(b01))
        if str(m02) == str(b02):
            print(' 号码2出现次数统计正确：' + str(b02))
        else:
            print(' 号码2出现次数统计错误：' + str(b02))
        if str(m03) == str(b03):
            print(' 号码3出现次数统计正确：' + str(b03))
        else:
            print(' 号码3出现次数统计错误：' + str(b03))
        if str(m04) == str(b04):
            print(' 号码4出现次数统计正确：' + str(b04))
        else:
            print(' 号码4出现次数统计错误：' + str(b04))
        if str(m05) == str(b05):
            print(' 号码5出现次数统计正确：' + str(b05))
        else:
            print(' 号码5出现次数统计错误：' + str(b05))
        if str(m06) == str(b06):
            print(' 号码6出现次数统计正确：' + str(b06))
        else:
            print(' 号码6出现次数统计错误：' + str(b02))
        if str(m07) == str(b07):
            print(' 号码7出现次数统计正确：' + str(b07))
        else:
            print(' 号码7出现次数统计错误：' + str(b07))
        if str(m08) == str(b08):
            print(' 号码8出现次数统计正确：' + str(b08))
        else:
            print(' 号码8出现次数统计错误：' + str(b08))
        if str(m09) == str(b09):
            print(' 号码9出现次数统计正确：' + str(b09))
        else:
            print(' 号码7出现次数统计错误：' + str(b09))

        print('        ')
        if str(n00) == str(a01.count('单')):
            print(' 球次总和单的总数统计正确： ' + str(a01.count('单')))
        else:
            print(' 球次总和单的总数统计错误： ' + str(a01.count('单')))
        if str(n01) == str(a01.count('双')):
            print(' 球次总和双的总数统计正确： ' + str(a01.count('双')))
        else:
            print(' 球次总和双的总数统计错误： ' + str(a01.count('双')))

        if str(n02) == str(a00.count('大')):
            print(' 球次总和大的总数统计正确： ' + str(a00.count('大')))
        else:
            print(' 球次总和大的总数统计错误： ' + str(a00.count('大')))

        if str(n03) == str(a00.count('小')):
            print(' 球次总和小的总数统计正确： ' + str(a00.count('小')))
        else:
            print(' 球次总和小的总数统计错误： ' + str(a00.count('小')))

        print('        ')
        c00 = a02.count('1') + a02.count('3') + a02.count('5') + a02.count('7') + a02.count('9')
        c01 = a02.count('0') + a02.count('2') + a02.count('4') + a02.count('6') + a02.count('8')
        c02 = a02.count('5') + a02.count('6') + a02.count('7') + a02.count('8') + a02.count('9')
        c03 = a02.count('0') + a02.count('1') + a02.count('2') + a02.count('3') + a02.count('4')

        if str(n04) == str(c00):
            print(' 球次第一球单的统计正确： ' + str(c00))
        else:
            print(' 球次第一球单的统计错误： ' + str(c00))
        if str(n05) == str(c01):
            print(' 球次第一球双的统计正确： ' + str(c01))
        else:
            print(' 球次第一球双的统计错误： ' + str(c01))
        if str(n06) == str(c02):
            print(' 球次第一球大的统计正确： ' + str(c02))
        else:
            print(' 球次第一球大的统计错误： ' + str(c02))
        if str(n07) == str(c03):
            print(' 球次第一球小的统计正确： ' + str(c03))
        else:
            print(' 球次第一球小的统计错误： ' + str(c03))

        print('        ')
        c04 = a03.count('1') + a03.count('3') + a03.count('5') + a03.count('7') + a03.count('9')
        c05 = a03.count('0') + a03.count('2') + a03.count('4') + a03.count('6') + a03.count('8')
        c06 = a03.count('5') + a03.count('6') + a03.count('7') + a03.count('8') + a03.count('9')
        c07 = a03.count('0') + a03.count('1') + a03.count('2') + a03.count('3') + a03.count('4')
        if str(n08) == str(c04):
            print(' 球次第二球单的统计正确： ' + str(c04))
        else:
            print(' 球次第二球单的统计错误： ' + str(c04))
        if str(n09) == str(c05):
            print(' 球次第二球双的统计正确： ' + str(c05))
        else:
            print(' 球次第二球双的统计错误： ' + str(c05))
        if str(n10) == str(c06):
            print(' 球次第二球大的统计正确： ' + str(c06))
        else:
            print(' 球次第二球大的统计错误： ' + str(c06))
        if str(n11) == str(c07):
            print(' 球次第二球小的统计正确： ' + str(c07))
        else:
            print(' 球次第二球小的统计错误： ' + str(c07))

        print('        ')
        c08 = a04.count('1') + a04.count('3') + a04.count('5') + a04.count('7') + a04.count('9')
        c09 = a04.count('0') + a04.count('2') + a04.count('4') + a04.count('6') + a04.count('8')
        c10 = a04.count('5') + a04.count('6') + a04.count('7') + a04.count('8') + a04.count('9')
        c11 = a04.count('0') + a04.count('1') + a04.count('2') + a04.count('3') + a04.count('4')

        if str(n12) == str(c08):
            print(' 球次第三球单的统计正确： ' + str(c08))
        else:
            print(' 球次第三球单的统计错误： ' + str(c08))
        if str(n13) == str(c09):
            print(' 球次第三球双的统计正确： ' + str(c09))
        else:
            print(' 球次第三球双的统计错误： ' + str(c09))
        if str(n14) == str(c10):
            print(' 球次第三球大的统计正确： ' + str(c10))
        else:
            print(' 球次第三球大的统计错误： ' + str(c10))
        if str(n15) == str(c11):
            print(' 球次第三球小的统计正确： ' + str(c11))
        else:
            print(' 球次第三球小的统计错误： ' + str(c11))

        print('                                                                               ')
        c12 = a05.count('1') + a05.count('3') + a05.count('5') + a05.count('7') + a05.count('9')
        c13 = a05.count('0') + a05.count('2') + a05.count('4') + a05.count('6') + a05.count('8')
        c14 = a05.count('5') + a05.count('6') + a05.count('7') + a05.count('8') + a05.count('9')
        c15 = a05.count('0') + a05.count('1') + a05.count('2') + a05.count('3') + a05.count('4')

        if str(n16) == str(c12):
            print(' 球次第四球单的统计正确： ' + str(c12))
        else:
            print(' 球次第四球单的统计错误： ' + str(c12))
        if str(n17) == str(c13):
            print(' 球次第四球双的统计正确： ' + str(c13))
        else:
            print(' 球次第四球双的统计错误： ' + str(c13))
        if str(n18) == str(c14):
            print(' 球次第四球大的统计正确： ' + str(c14))
        else:
            print(' 球次第四球大的统计错误： ' + str(c14))
        if str(n19) == str(c15):
            print(' 球次第四球小的统计正确： ' + str(c15))
        else:
            print(' 球次第四球小的统计错误： ' + str(c15))

        print('        ')
        c16 = a06.count('1') + a06.count('3') + a06.count('5') + a06.count('7') + a06.count('9')
        c17 = a06.count('0') + a06.count('2') + a06.count('4') + a06.count('6') + a06.count('8')
        c18 = a06.count('5') + a06.count('6') + a06.count('7') + a06.count('8') + a06.count('9')
        c19 = a06.count('0') + a06.count('1') + a06.count('2') + a06.count('3') + a06.count('4')

        if str(n20) == str(c16):
            print(' 球次第五球单的统计正确： ' + str(c16))
        else:
            print(' 球次第五球单的统计错误： ' + str(c16))
        if str(n21) == str(c17):
            print(' 球次第五球双的统计正确： ' + str(c17))
        else:
            print(' 球次第五球双的统计错误： ' + str(c17))
        if str(n22) == str(c18):
            print(' 球次第五球大的统计正确： ' + str(c18))
        else:
            print(' 球次第五球大的统计错误： ' + str(c18))
        if str(n23) == str(c19):
            print(' 球次第五球小的统计正确： ' + str(c19))
        else:
            print(' 球次第五球小的统计错误： ' + str(c19))

        ''' 数据统计当天的数据 '''

        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '数据统计')

        self.base_driver.forced_wait(10)
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['IDLENUM01'], '历史号码统计')

        self.base_driver.forced_wait(10)

        # 0~9出现号码次数
        c20 = a02.count('0') + a03.count('0') + a04.count('0') + a05.count('0') + a06.count('0')
        c21 = a02.count('1') + a03.count('1') + a04.count('1') + a05.count('1') + a06.count('1')
        c22 = a02.count('2') + a03.count('2') + a04.count('2') + a05.count('2') + a06.count('2')
        c23 = a02.count('3') + a03.count('3') + a04.count('3') + a05.count('3') + a06.count('3')
        c24 = a02.count('4') + a03.count('4') + a04.count('4') + a05.count('4') + a06.count('4')
        c25 = a02.count('5') + a03.count('5') + a04.count('5') + a05.count('5') + a06.count('5')
        c26 = a02.count('6') + a03.count('6') + a04.count('6') + a05.count('6') + a06.count('6')
        c27 = a02.count('7') + a03.count('7') + a04.count('7') + a05.count('7') + a06.count('7')
        c28 = a02.count('8') + a03.count('8') + a04.count('8') + a05.count('8') + a06.count('8')
        c29 = a02.count('9') + a03.count('9') + a04.count('9') + a05.count('9') + a06.count('9')

        # 单双大小
        # 单
        c30 = c00 + c04 + c08 + c12 + c16
        c31 = c01 + c05 + c09 + c13 + c17
        c32 = c02 + c06 + c10 + c14 + c18
        c33 = c03 + c07 + c11 + c15 + c19

        # 1-5 龙虎和
        c34 = a07.count('龙')
        c35 = a07.count('虎')
        c36 = a07.count('和')

        print('----------------')
        d00 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 0)
        d01 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 1)
        d02 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 2)
        d03 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 3)
        d04 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 4)
        d05 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 5)
        d06 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 6)
        d07 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 7)
        d08 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 8)
        d09 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 9)

        d10 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 10)
        d11 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 11)
        d12 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 12)
        d13 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 13)
        d14 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 14)
        d15 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 15)
        d16 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 16)
        d17 = self.base_driver.get_texts(self.config_dict_tmmcq['HISTORY_NUM'], 17)

        if str(d00) == time.strftime('%Y-%m-%d'):
            if str(d01) == str(c20):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码0正确：' + str(c20))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码0错误：' + str(c20))
            if str(d02) == str(c21):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码1正确：' + str(c21))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码1错误：' + str(c21))
            if str(d03) == str(c22):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码2正确：' + str(c22))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码2错误：' + str(c22))
            if str(d04) == str(c23):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码3正确：' + str(c23))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码3错误：' + str(c23))
            if str(d05) == str(c24):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码4正确：' + str(c24))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码4错误：' + str(c24))
            if str(d06) == str(c25):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码5正确：' + str(c25))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码5错误：' + str(c25))
            if str(d07) == str(c26):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码6正确：' + str(c26))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码6错误：' + str(c26))
            if str(d08) == str(c27):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码7正确：' + str(c27))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码7错误：' + str(c27))
            if str(d09) == str(c28):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码8正确：' + str(c28))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码8错误：' + str(c28))
            if str(d10) == str(c29):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码9正确：' + str(c29))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  号码9错误：' + str(c29))
            if str(d11) == str(c30):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  单正确：' + str(c30))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  单错误：' + str(c30))
            if str(d12) == str(c31):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  双正确：' + str(c31))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  双错误：' + str(c31))
            if str(d13) == str(c32):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  大正确：' + str(c32))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  大错误：' + str(c32))
            if str(d14) == str(c33):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  小正确：' + str(c33))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  小错误：' + str(c33))
            if str(d15) == str(c34):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  龙正确：' + str(c34))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  龙错误：' + str(c34))
            if str(d16) == str(c35):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  虎正确：' + str(c35))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  虎错误：' + str(c35))
            if str(d17) == str(c36):
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  和正确：' + str(c36))
            else:
                print('日期' + str(time.strftime('%Y-%m-%d')) + '  和错误：' + str(c36))

    def lotteryhall_trend_basic(self):
        # 走势图
        # 基本走势
        self.base_driver.forced_wait(1)
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')

        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '基本走势')
        self.base_driver.forced_wait(3)

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
        a17 = []
        a18 = []
        a19 = []
        a20 = []
        a21 = []
        a22 = []
        a23 = []
        a24 = []
        a25 = []
        a26 = []
        a27 = []
        a28 = []
        a29 = []
        a30 = []
        a31 = []
        a32 = []
        a33 = []
        a34 = []
        a35 = []
        a36 = []
        a37 = []
        a38 = []
        a39 = []
        a40 = []
        a41 = []
        a42 = []
        a43 = []
        a44 = []
        a45 = []
        a46 = []
        a47 = []
        a48 = []
        a49 = []
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                # 因新疆时时彩特殊改成匹配月
                # if datetime[:8] == time.strftime('%Y%m%d'):
                if datetime[:6] == time.strftime('%Y%m'):
                    # 第一球0~9
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_0'], i)
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_1'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_2'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_3'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_4'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_5'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_6'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_7'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_8'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_9'], i)

                    # 第二球0~9
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_0'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_1'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_2'], i)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_3'], i)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_4'], i)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_5'], i)
                    s16 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_6'], i)
                    s17 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_7'], i)
                    s18 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_8'], i)
                    s19 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_9'], i)

                    # 第三球0~9
                    s20 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_0'], i)
                    s21 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_1'], i)
                    s22 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_2'], i)
                    s23 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_3'], i)
                    s24 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_4'], i)
                    s25 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_5'], i)
                    s26 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_6'], i)
                    s27 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_7'], i)
                    s28 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_8'], i)
                    s29 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_9'], i)

                    # 第四球0~9
                    s30 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_0'], i)
                    s31 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_1'], i)
                    s32 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_2'], i)
                    s33 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_3'], i)
                    s34 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_4'], i)
                    s35 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_5'], i)
                    s36 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_6'], i)
                    s37 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_7'], i)
                    s38 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_8'], i)
                    s39 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_4_9'], i)

                    # 第五球0~9
                    s40 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_0'], i)
                    s41 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_1'], i)
                    s42 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_2'], i)
                    s43 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_3'], i)
                    s44 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_4'], i)
                    s45 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_5'], i)
                    s46 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_6'], i)
                    s47 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_7'], i)
                    s48 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_8'], i)
                    s49 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_5_9'], i)

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
                    a11.append(s11)
                    a12.append(s12)
                    a13.append(s13)
                    a14.append(s14)
                    a15.append(s15)
                    a16.append(s16)
                    a17.append(s17)
                    a18.append(s18)
                    a19.append(s19)

                    a20.append(s20)
                    a21.append(s21)
                    a22.append(s22)
                    a23.append(s23)
                    a24.append(s24)
                    a25.append(s25)
                    a26.append(s26)
                    a27.append(s27)
                    a28.append(s28)
                    a29.append(s29)

                    a30.append(s30)
                    a31.append(s31)
                    a32.append(s32)
                    a33.append(s33)
                    a34.append(s34)
                    a35.append(s35)
                    a36.append(s36)
                    a37.append(s37)
                    a38.append(s38)
                    a39.append(s39)

                    a40.append(s40)
                    a41.append(s41)
                    a42.append(s42)
                    a43.append(s43)
                    a44.append(s44)
                    a45.append(s45)
                    a46.append(s46)
                    a47.append(s47)
                    a48.append(s48)
                    a49.append(s49)
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a00)
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
        # ss = [ball_1_0, ball_1_1, ball_1_2, ball_1_2, ball_1_3, ball_1_4,
        #       ball_1_5, ball_1_6, ball_1_7, ball_1_8, ball_1_9]
        # print(ss)
        # print('ball_1_0:   ' + str(ball_1_0))
        # print('a00.count:  ' + str(a00.count('0')))
        if str(ball_1_0) == str(a00.count('0')):
            print('第一球统计0---正确---' + str(a00.count('0')))
        else:
            print('第一球统计0---错误---' + str(a00.count('0')))
        if str(ball_1_1) == str(a01.count('1')):
            print('第一球统计1---正确---' + str(a01.count('1')))
        else:
            print('第一球统计1---错误---' + str(a01.count('1')))
        if str(ball_1_2) == str(a02.count('2')):
            print('第一球统计2---正确---' + str(a02.count('2')))
        else:
            print('第一球统计2---错误---' + str(a02.count('2')))
        if str(ball_1_3) == str(a03.count('3')):
            print('第一球统计3---正确---' + str(a03.count('3')))
        else:
            print('第一球统计3---错误---' + str(a03.count('3')))
        if str(ball_1_4) == str(a04.count('4')):
            print('第一球统计4---正确---' + str(a04.count('4')))
        else:
            print('第一球统计4---错误---' + str(a04.count('4')))
        if str(ball_1_5) == str(a05.count('5')):
            print('第一球统计5---正确---' + str(a05.count('5')))
        else:
            print('第一球统计5---错误---' + str(a05.count('5')))
        if str(ball_1_6) == str(a06.count('6')):
            print('第一球统计6---正确---' + str(a06.count('6')))
        else:
            print('第一球统计6---错误---' + str(a06.count('6')))
        if str(ball_1_7) == str(a07.count('7')):
            print('第一球统计7---正确---' + str(a07.count('7')))
        else:
            print('第一球统计7---错误---' + str(a07.count('7')))
        if str(ball_1_8) == str(a08.count('8')):
            print('第一球统计8---正确---' + str(a08.count('8')))
        else:
            print('第一球统计8---错误---' + str(a08.count('8')))
        if str(ball_1_9) == str(a09.count('9')):
            print('第一球统计9---正确---' + str(a09.count('9')))
        else:
            print('第一球统计9---错误---' + str(a09.count('9')))
        # 第二球0~9
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 11)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 12)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 13)
        ball_2_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 14)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 15)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 16)
        ball_2_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 17)
        ball_2_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 18)
        ball_2_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 19)
        ball_2_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 20)
        # print('ball_2_0:   ' + str(ball_2_0))
        # print('-----' + str(a10.count('0')))
        if str(ball_2_0) == str(a10.count('0')):
            print('第二球统计0---正确---' + str(a10.count('0')))
        else:
            print('第二球统计0---错误---' + str(a10.count('0')))
        if str(ball_2_1) == str(a11.count('1')):
            print('第二球统计1---正确---' + str(a11.count('1')))
        else:
            print('第一球统计1---错误---' + str(a11.count('1')))
        if str(ball_2_2) == str(a12.count('2')):
            print('第二球统计2---正确---' + str(a12.count('2')))
        else:
            print('第二球统计2---错误---' + str(a12.count('2')))
        if str(ball_2_3) == str(a13.count('3')):
            print('第二球统计3---正确---' + str(a13.count('3')))
        else:
            print('第二球统计3---错误---' + str(a13.count('3')))
        if str(ball_2_4) == str(a14.count('4')):
            print('第一球统计4---正确---' + str(a14.count('4')))
        else:
            print('第二球统计4---错误---' + str(a14.count('4')))
        if str(ball_2_5) == str(a15.count('5')):
            print('第二球统计5---正确---' + str(a15.count('5')))
        else:
            print('第二球统计5---错误---' + str(a15.count('5')))
        if str(ball_2_6) == str(a16.count('6')):
            print('第二球统计6---正确---' + str(a16.count('6')))
        else:
            print('第二球统计6---错误---' + str(a16.count('6')))
        if str(ball_2_7) == str(a17.count('7')):
            print('第二球统计7---正确---' + str(a17.count('7')))
        else:
            print('第二球统计7---错误---' + str(a17.count('7')))
        if str(ball_2_8) == str(a18.count('8')):
            print('第二球统计8---正确---' + str(a18.count('8')))
        else:
            print('第二球统计8---错误---' + str(a18.count('8')))
        if str(ball_2_9) == str(a19.count('9')):
            print('第二球统计9---正确---' + str(a19.count('9')))
        else:
            print('第二球统计9---错误---' + str(a19.count('9')))

        # 出现次数 第三球0~9
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 21)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 22)
        ball_3_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 23)
        ball_3_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 24)
        ball_3_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 25)
        ball_3_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 26)
        ball_3_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 27)
        ball_3_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 28)
        ball_3_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 29)
        ball_3_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 30)
        # print('ball_3_0:   ' + str(ball_3_0))
        # print('-----' + str(a20.count('0')))
        if str(ball_3_0) == str(a20.count('0')):
            print('第三球统计0---正确---' + str(a20.count('0')))
        else:
            print('第三球统计0---错误---' + str(a20.count('0')))
        if str(ball_3_1) == str(a21.count('1')):
            print('第三球统计1---正确---' + str(a21.count('1')))
        else:
            print('第三球统计1---错误---' + str(a21.count('1')))
        if str(ball_3_2) == str(a22.count('2')):
            print('第三球统计2---正确---' + str(a22.count('2')))
        else:
            print('第一球统计2---错误---' + str(a22.count('2')))
        if str(ball_3_3) == str(a23.count('3')):
            print('第三球统计3---正确---' + str(a23.count('3')))
        else:
            print('第三球统计3---错误---' + str(a23.count('3')))
        if str(ball_3_4) == str(a24.count('4')):
            print('第三球统计4---正确---' + str(a24.count('4')))
        else:
            print('第三球统计4---错误---' + str(a24.count('4')))
        if str(ball_3_5) == str(a25.count('5')):
            print('第三球统计5---正确---' + str(a25.count('5')))
        else:
            print('第三球统计5---错误---' + str(a25.count('5')))
        if str(ball_3_6) == str(a26.count('6')):
            print('第三球统计6---正确---' + str(a26.count('6')))
        else:
            print('第三球统计6---错误---' + str(a26.count('6')))
        if str(ball_3_7) == str(a27.count('7')):
            print('第三球统计7---正确---' + str(a27.count('7')))
        else:
            print('第三球统计7---错误---' + str(a27.count('7')))
        if str(ball_3_8) == str(a28.count('8')):
            print('第三球统计8---正确---' + str(a28.count('8')))
        else:
            print('第三球统计8---错误---' + str(a28.count('8')))
        if str(ball_3_9) == str(a29.count('9')):
            print('第三球统计9---正确---' + str(a29.count('9')))
        else:
            print('第三球统计9---错误---' + str(a29.count('9')))

        # 出现次数 第四球0~9
        ball_4_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 31)
        ball_4_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 32)
        ball_4_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 33)
        ball_4_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 34)
        ball_4_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 35)
        ball_4_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 36)
        ball_4_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 37)
        ball_4_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 38)
        ball_4_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 39)
        ball_4_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 40)
        # print('ball_4_0:   ' + str(ball_4_0))
        # print('-----' + str(a30.count('0')))
        if str(ball_4_0) == str(a30.count('0')):
            print('第四球统计0---正确---' + str(a30.count('0')))
        else:
            print('第四球统计0---错误---' + str(a30.count('0')))
        if str(ball_4_1) == str(a31.count('1')):
            print('第四球统计1---正确---' + str(a31.count('1')))
        else:
            print('第一球统计1---错误---' + str(a31.count('1')))
        if str(ball_4_2) == str(a32.count('2')):
            print('第四球统计2---正确---' + str(a32.count('2')))
        else:
            print('第四球统计2---错误---' + str(a32.count('2')))
        if str(ball_4_3) == str(a33.count('3')):
            print('第四球统计3---正确---' + str(a33.count('3')))
        else:
            print('第四球统计3---错误---' + str(a33.count('3')))
        if str(ball_4_4) == str(a34.count('4')):
            print('第四球统计4---正确---' + str(a34.count('4')))
        else:
            print('第四球统计4---错误---' + str(a34.count('4')))
        if str(ball_4_5) == str(a35.count('5')):
            print('第四球统计5---正确---' + str(a35.count('5')))
        else:
            print('第四球统计5---错误---' + str(a35.count('5')))
        if str(ball_4_6) == str(a36.count('6')):
            print('第四球统计6---正确---' + str(a36.count('6')))
        else:
            print('第四球统计6---错误---' + str(a36.count('6')))
        if str(ball_4_7) == str(a37.count('7')):
            print('第四球统计7---正确---' + str(a37.count('7')))
        else:
            print('第四球统计7---错误---' + str(a37.count('7')))
        if str(ball_4_8) == str(a38.count('8')):
            print('第四球统计8---正确---' + str(a38.count('8')))
        else:
            print('第四球统计8---错误---' + str(a38.count('8')))
        if str(ball_4_9) == str(a39.count('9')):
            print('第四球统计9---正确---' + str(a39.count('9')))
        else:
            print('第四球统计9---错误---' + str(a39.count('9')))

        # 出现次数 第五球0~9
        ball_5_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 41)
        ball_5_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 42)
        ball_5_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 43)
        ball_5_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 44)
        ball_5_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 45)
        ball_5_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 46)
        ball_5_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 47)
        ball_5_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 48)
        ball_5_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 49)
        ball_5_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 50)
        # print('ball_5_0:   ' + str(ball_5_0))
        # print('-----' + str(a40.count('0')))
        if str(ball_5_0) == str(a40.count('0')):
            print('第五球统计0---正确---' + str(a40.count('0')))
        else:
            print('第五球统计0---错误---' + str(a40.count('0')))
        if str(ball_5_1) == str(a41.count('1')):
            print('第五球统计1---正确---' + str(a41.count('1')))
        else:
            print('第五球统计1---错误---' + str(a41.count('1')))
        if str(ball_5_2) == str(a42.count('2')):
            print('第五球统计2---正确---' + str(a42.count('2')))
        else:
            print('第五球统计2---错误---' + str(a42.count('2')))
        if str(ball_5_3) == str(a43.count('3')):
            print('第五球统计3---正确---' + str(a43.count('3')))
        else:
            print('第五球统计3---错误---' + str(a43.count('3')))
        if str(ball_5_4) == str(a44.count('4')):
            print('第五球统计4---正确---' + str(a44.count('4')))
        else:
            print('第五球统计4---错误---' + str(a44.count('4')))
        if str(ball_5_5) == str(a45.count('5')):
            print('第五球统计5---正确---' + str(a45.count('5')))
        else:
            print('第五球统计5---错误---' + str(a45.count('5')))
        if str(ball_5_6) == str(a46.count('6')):
            print('第五球统计6---正确---' + str(a46.count('6')))
        else:
            print('第五球统计6---错误---' + str(a46.count('6')))
        if str(ball_5_7) == str(a47.count('7')):
            print('第五球统计7---正确---' + str(a47.count('7')))
        else:
            print('第五球统计7---错误---' + str(a47.count('7')))
        if str(ball_5_8) == str(a48.count('8')):
            print('第五球统计8---正确---' + str(a48.count('8')))
        else:
            print('第五球统计8---错误---' + str(a48.count('8')))
        if str(ball_5_9) == str(a49.count('9')):
            print('第五球统计9---正确---' + str(a49.count('9')))
        else:
            print('第五球统计9---错误---' + str(a49.count('9')))

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
                # 因新疆时时彩特殊改成匹配月
                # if datetime[:8] == time.strftime('%Y%m%d'):
                if datetime[:6] == time.strftime('%Y%m'):
                    # 第一球0~9
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_0'], i)
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_1'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_2'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_3'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_4'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_5'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_6'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_7'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_8'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_1_9'], i)

                    # 形态特征---大小-单双-合质
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_0'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_1'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_2'], i)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_3'], i)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_4'], i)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_5'], i)

                    # 012路
                    # s16 = self.base_driver.get_attribute(self.config_dict_tmmcq['LU_0'], 'class')
                    # s17 = self.base_driver.get_attribute_text(self.config_dict_tmmcq['LU_1'], 'class', i)
                    # s18 = self.base_driver.get_attribute_text(self.config_dict_tmmcq['LU_2'], 'class', i)
                    # print(s16)
                    # print(s17)
                    # print(s18)
                    # 升平降
                    s19 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_9'], i)
                    s20 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_0'], i)
                    s21 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_1'], i)

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
                    a11.append(s11)
                    a12.append(s12)
                    a13.append(s13)
                    a14.append(s14)
                    a15.append(s15)

                    # a16.append(s16)
                    # a17.append(s17)
                    # a18.append(s18)

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
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 1)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 2)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 3)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 4)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 5)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 6)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 7)
        ball_1_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 8)
        ball_1_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 9)
        ball_1_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 10)
        ss = [ball_1_0, ball_1_1, ball_1_2, ball_1_3, ball_1_4, ball_1_5, ball_1_6, ball_1_7, ball_1_8, ball_1_9]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_0))
        print('a00.count:  ' + str(a00.count('0')))
        if str(ball_1_0) == str(a00.count('0')):
            print('第一球号码走势统计0---正确---' + str(a00.count('0')))
        else:
            print('第一球号码走势统计0---错误---' + str(a00.count('0')))
        if str(ball_1_1) == str(a01.count('1')):
            print('第一球号码走势统计1---正确---' + str(a01.count('1')))
        else:
            print('第一球号码走势统计1---错误---' + str(a01.count('1')))
        if str(ball_1_2) == str(a02.count('2')):
            print('第一球号码走势统计2---正确---' + str(a02.count('2')))
        else:
            print('第一球号码走势统计2---错误---' + str(a02.count('2')))
        if str(ball_1_3) == str(a03.count('3')):
            print('第一球号码走势统计3---正确---' + str(a03.count('3')))
        else:
            print('第一球号码走势统计3---错误---' + str(a03.count('3')))
        if str(ball_1_4) == str(a04.count('4')):
            print('第一球号码走势统计4---正确---' + str(a04.count('4')))
        else:
            print('第一球号码走势统计4---错误---' + str(a04.count('4')))
        if str(ball_1_5) == str(a05.count('5')):
            print('第一球号码走势统计5---正确---' + str(a05.count('5')))
        else:
            print('第一球号码走势统计5---错误---' + str(a05.count('5')))
        if str(ball_1_6) == str(a06.count('6')):
            print('第一球号码走势统计6---正确---' + str(a06.count('6')))
        else:
            print('第一球号码走势统计6---错误---' + str(a06.count('6')))
        if str(ball_1_7) == str(a07.count('7')):
            print('第一球号码走势统计7---正确---' + str(a07.count('7')))
        else:
            print('第一球号码走势统计7---错误---' + str(a07.count('7')))
        if str(ball_1_8) == str(a08.count('8')):
            print('第一球号码走势统计8---正确---' + str(a08.count('8')))
        else:
            print('第一球号码走势统计8---错误---' + str(a08.count('8')))
        if str(ball_1_9) == str(a09.count('9')):
            print('第一球号码走势统计9---正确---' + str(a09.count('9')))
        else:
            print('第一球号码走势统计9---错误---' + str(a09.count('9')))
        # 形态特征
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 11)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 12)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 13)
        ball_2_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 14)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 15)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 16)

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
        # ball_2_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 17)
        # ball_2_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 18)
        # ball_2_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 19)
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
        ball_2_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 20)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 21)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM1'], 22)
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
        self.base_driver.forced_wait(3)

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
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)
                if datetime[:6] == time.strftime('%Y%m'):
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)

                    # 第一位、第二位、第三位
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_0'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_1'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_0'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_1'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_0'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_1'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_0'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_1'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_0'], i)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_1'], i)
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

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a01)
        # 号码分布
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 0)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 1)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 2)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 3)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 4)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 5)
        ball_1_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 6)
        ball_1_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 7)
        ball_1_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 8)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 9)

        ss = [ball_1_1, ball_1_2, ball_1_3, ball_1_4, ball_1_5, ball_1_6]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_1))
        print('a00.count:  ' + str(a01.count('大')))
        if str(ball_1_1) == str(a01.count('大')):
            print('第一位统计大---正确---' + str(a01.count('大')))
        else:
            print('第一位统计大---错误---' + str(a01.count('大')))
        if str(ball_1_2) == str(a02.count('小')):
            print('第一位统计小---正确---' + str(a02.count('小')))
        else:
            print('第一位统计小---错误---' + str(a02.count('小')))
        if str(ball_1_3) == str(a03.count('大')):
            print('第二位统计大---正确---' + str(a03.count('大')))
        else:
            print('第二位统计大---错误---' + str(a03.count('大')))
        if str(ball_1_4) == str(a04.count('小')):
            print('第二位统计小---正确---' + str(a04.count('小')))
        else:
            print('第二位统计小---错误---' + str(a04.count('小')))
        if str(ball_1_5) == str(a05.count('大')):
            print('第三位统计大---正确---' + str(a05.count('大')))
        else:
            print('第三位统计大---错误---' + str(a05.count('大')))
        if str(ball_1_6) == str(a06.count('小')):
            print('第三位统计小---正确---' + str(a06.count('小')))
        else:
            print('第三位统计小---错误---' + str(a06.count('小')))

        if str(ball_1_7) == str(a07.count('大')):
            print('第四位统计大---正确---' + str(a07.count('大')))
        else:
            print('第四位统计大---错误---' + str(a07.count('大')))
        if str(ball_1_8) == str(a08.count('小')):
            print('第四位统计小---正确---' + str(a08.count('小')))
        else:
            print('第四位统计小---错误---' + str(a08.count('小')))
        if str(ball_1_9) == str(a09.count('大')):
            print('第五位统计大---正确---' + str(a09.count('大')))
        else:
            print('第五位统计大---错误---' + str(a09.count('大')))
        print(ball_2_0)
        print(str(a10.count('小')))
        if str(ball_2_0) == str(a10.count('小')):
            print('第五位统计小---正确---' + str(a10.count('小')))
        else:
            print('第五位统计小---错误---' + str(a10.count('小')))

    def lotteryhall_trend_double(self):
        # 走势图
        # 大小走势
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '单双走势')
        self.base_driver.forced_wait(3)

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
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)
                if datetime[:6] == time.strftime('%Y%m'):
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)

                    # 第一位、第二位、第三位
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_0'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_1'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_0'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_1'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_0'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_1'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_0'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_1'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_0'], i)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_1'], i-1)
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

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a01)
        # 号码分布
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 0)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 1)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 2)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 3)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 4)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 5)
        ball_1_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 6)
        ball_1_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 7)
        ball_1_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 8)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 9)

        ss = [ball_1_1, ball_1_2, ball_1_3, ball_1_4, ball_1_5, ball_1_6]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_1))
        print('a00.count:  ' + str(a01.count('单')))
        if str(ball_1_1) == str(a01.count('单')):
            print('第一位统计单---正确---' + str(a01.count('单')))
        else:
            print('第一位统计单---错误---' + str(a01.count('单')))
        if str(ball_1_2) == str(a02.count('双')):
            print('第一位统计双---正确---' + str(a02.count('双')))
        else:
            print('第一位统计双---错误---' + str(a02.count('双')))
        if str(ball_1_3) == str(a03.count('单')):
            print('第二位统计单---正确---' + str(a03.count('单')))
        else:
            print('第二位统计单---错误---' + str(a03.count('单')))
        if str(ball_1_4) == str(a04.count('双')):
            print('第二位统计双---正确---' + str(a04.count('双')))
        else:
            print('第二位统计双---错误---' + str(a04.count('双')))
        if str(ball_1_5) == str(a05.count('单')):
            print('第三位统计单---正确---' + str(a05.count('单')))
        else:
            print('第三位统计单---错误---' + str(a05.count('单')))
        if str(ball_1_6) == str(a06.count('双')):
            print('第三位统计双---正确---' + str(a06.count('双')))
        else:
            print('第三位统计双---错误---' + str(a06.count('双')))

        if str(ball_1_7) == str(a07.count('单')):
            print('第四位统计单---正确---' + str(a07.count('单')))
        else:
            print('第四位统计单---错误---' + str(a07.count('单')))
        if str(ball_1_8) == str(a08.count('双')):
            print('第四位统计双---正确---' + str(a08.count('双')))
        else:
            print('第四位统计双---错误---' + str(a08.count('双')))
        if str(ball_1_9) == str(a09.count('单')):
            print('第五位统计单---正确---' + str(a09.count('单')))
        else:
            print('第五位统计单---错误---' + str(a09.count('单')))
        # print(ball_2_0)
        # print(str(a10.count('双')))
        if str(ball_2_0) == str(a10.count('双')):
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
        if os.path.exists("/fusion/lottery_hall/time/万位杀号.txt"):
            os.remove("/fusion/lottery_hall/time/万位杀号.txt")
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
                a1 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM01'], i+1)
                a2 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM02'], i+1)
                a3 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM03'], i+1)
                a4 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM04'], i+1)
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

                m0 = [b0, b1, b2, b3, b4]
                x0 = [c0, c1, c2, c3, c4]
                f = open("/fusion/lottery_hall/time/万位杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a0) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a0) or (c0 == '杀错' and b0[2:] == a0):
                    pass
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b0) + str(c0) + '  万号正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b0) + str(c0) + '--万号错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a0) or (c1 == '杀错' and b1[2:] == a0):
                    pass
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b1) + str(c1) + '  万号正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b1) + str(c1) + '--万号错误' + str(b1))

                if (c2 == '杀对' and b2[2:] != a0) or (c2 == '杀错' and b2[2:] == a0):
                    pass
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b2) + str(c2) + '  万号正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b2) + str(c2) + '--万号错误' + str(b2))

                if (c3 == '杀对' and b3[2:] != a0) or (c3 == '杀错' and b3[2:] == a0):
                    pass
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b3) + str(c3) + '  万号正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b3) + str(c3) + '--万号错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a0) or (c4 == '杀错' and b4[2:] == a0):
                    pass
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b4) + str(c4) + '  万号正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '  万号是：' + str(a0) + '  ' + str(b4) + str(c4) + '--万号错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号万位杀号运行' + str(i) + '行')
                # self.base_driver.forced_wait()
                break

    def plan_winkillnum_q(self):
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(2)
        # 千位杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '千位杀号')
        self.base_driver.forced_wait(2)
        if os.path.exists("/fusion/lottery_hall/time/千位杀号.txt"):
            os.remove("/fusion/lottery_hall/time/千位杀号.txt")
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

                f = open("/fusion/lottery_hall/time/千位杀号.txt", 'a', encoding='utf-8')

                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a1) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a1) or (c0 == '杀错' and b0[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b0) + str(c0) + '  千号正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b0) + str(c0) + '--千号错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a1) or (c1 == '杀错' and b1[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b1) + str(c1) + '  千号正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b1) + str(c1) + '--千号错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a1) or (c2 == '杀错' and b2[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b2) + str(c2) + '  千号正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b2) + str(c2) + '--千号错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a1) or (c3 == '杀错' and b3[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b3) + str(c3) + '  千号正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b3) + str(c3) + '--千号错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a1) or (c4 == '杀错' and b4[2:] == a1):
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b4) + str(c4) + '  千号正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '  千号是：' + str(a1) + '  ' + str(b4) + str(c4) + '--千号错误' + str(b4))
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
        if os.path.exists("/fusion/lottery_hall/time/百位杀号.txt"):
            os.remove("/fusion/lottery_hall/time/百位杀号.txt")
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

                f = open("/fusion/lottery_hall/time/百位杀号.txt", 'a', encoding='utf-8')

                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a2) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a2) or (c0 == '杀错' and b0[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b0) + str(c0) + '  百号正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b0) + str(c0) + '--百号错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a2) or (c1 == '杀错' and b1[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b1) + str(c1) + '  百号正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b1) + str(c1) + '--百号错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a2) or (c2 == '杀错' and b2[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b2) + str(c2) + '  百号正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b2) + str(c2) + '--百号错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a2) or (c3 == '杀错' and b3[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b3) + str(c3) + '  百号正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b3) + str(c3) + '--百号错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a2) or (c4 == '杀错' and b4[2:] == a2):
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b4) + str(c4) + '  百号正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '  百号是：' + str(a2) + '  ' + str(b4) + str(c4) + '--百号错误' + str(b4))
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
        if os.path.exists("/fusion/lottery_hall/time/十位杀号.txt"):
            os.remove("/fusion/lottery_hall/time/十位杀号.txt")
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

                f = open("/fusion/lottery_hall/time/十位杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a3) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a3) or (c0 == '杀错' and b0[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b0) + str(c0) + '  十号正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b0) + str(c0) + '--十号错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a3) or (c1 == '杀错' and b1[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b1) + str(c1) + '  十号正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b1) + str(c1) + '--十号错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a3) or (c2 == '杀错' and b2[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b2) + str(c2) + '  十号正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b2) + str(c2) + '--十号错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a3) or (c3 == '杀错' and b3[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b3) + str(c3) + '  十号正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b3) + str(c3) + '--十号错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a3) or (c4 == '杀错' and b4[2:] == a3):
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b4) + str(c4) + '  十号正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '  十号是：' + str(a3) + '  ' + str(b4) + str(c4) + '--十号错误' + str(b4))
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
        if os.path.exists("/fusion/lottery_hall/time/个位杀号.txt"):
            os.remove("/fusion/lottery_hall/time/个位杀号.txt")
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

                f = open("/fusion/lottery_hall/time/个位杀号.txt", 'a', encoding='utf-8')

                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a4) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a4) or (c0 == '杀错' and b0[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b0) + str(c0) + '  个号正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b0) + str(c0) + '--个号错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a4) or (c1 == '杀错' and b1[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b1) + str(c1) + '  个号正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b1) + str(c1) + '--个号错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a4) or (c2 == '杀错' and b2[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b2) + str(c2) + '  个号正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b2) + str(c2) + '--个号错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a4) or (c3 == '杀错' and b3[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b3) + str(c3) + '  个号正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b3) + str(c3) + '--个号错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a4) or (c4 == '杀错' and b4[2:] == a4):
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b4) + str(c4) + '  个号正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '  个号是：' + str(a4) + '  ' + str(b4) + str(c4) + '--个号错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号个位杀号运行' + str(i) + '行')
                break











