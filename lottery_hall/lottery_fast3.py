import os
import random
import time

import numpy as np
from common.box import YamlHelper, BasePage


class LotteryFast3(BasePage):

    config_dict_fast3 = YamlHelper().get_config_dict('/fusion/lottery_hall/yaml/lottery_fast3.yaml')['LOTTERY_FAST3']

    def today_count(self):
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_fast3['MENU'], '今日开奖')
        self.base_driver.forced_wait(10)
        for i in range(100):
            try:
                # 时间
                date = self.base_driver.get_texts(self.config_dict_fast3['TIME_NUM'], i)
                # print(date1[:10])
                if date[:10] == time.strftime('%Y-%m-%d'):
                    # 期数
                    ss = self.base_driver.get_texts(self.config_dict_fast3['PERIODS_NUM'], i)
                    # 总和
                    s0 = self.base_driver.get_texts(self.config_dict_fast3['SUM_SUM'], i)
                    # 总和大小
                    s1 = self.base_driver.get_texts(self.config_dict_fast3['SUM_DX_NUM'], i)
                    # 总和单双
                    s2 = self.base_driver.get_texts(self.config_dict_fast3['SUM_DS_NUM'], i)
                    # 开奖号码骰子
                    s3 = self.base_driver.get_attribute_text(self.config_dict_fast3['LOTTERY_NUM01'], 'class', i)
                    s4 = self.base_driver.get_attribute_text(self.config_dict_fast3['LOTTERY_NUM02'], 'class', i)
                    s5 = self.base_driver.get_attribute_text(self.config_dict_fast3['LOTTERY_NUM03'], 'class', i)
                    # 鱼虾蟹
                    s6 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUMYU'], i)
                    s7 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUMXIA'], i)
                    s8 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUMXIE'], i)

                    a0 = int(s3[7:]) + int(s4[7:]) + int(s5[7:])
                    #print('a0' + ' ' + str(a0))
                    # print('s0' + str(s0))
                    if str(s0) == str(a0):
                        print('期数' + str(ss) + '总和计算正确' + str(a0))
                    else:
                        print('期数' + str(ss) + '总和计算错误' + str(a0))

                    if (str(a0) >= '11') and (s1 == '大'):
                        #print(str(ss))
                        pass
                        print('期数' + str(ss) + '总和大正确' + str(a0))
                    elif (str(a0) <= '10') and (s1 == '小'):
                        # print(str(ss))
                        pass
                        print('期数' + str(ss) + '总和小正确' + str(a0))
                    # else:
                    #     # print('a0' + str(a0))
                    #     # print('s1' + str(s1))
                    #     print('期数' + str(ss) + '总和大小错误' + str(a0))

            except Exception as e:
                print(e)
                print('运行行数' + str(i))
                break

    def plan_winkillnum_complex(self):
        # 综合杀号
        self.base_driver.clicks_by_text(self.config_dict_fast3['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近100期
        self.base_driver.clicks_by_text(self.config_dict_fast3['RECNET_PERIOD'], '最近100次')
        self.base_driver.forced_wait(1)
        # 冠军杀号
        self.base_driver.clicks_by_text(self.config_dict_fast3['NUMKILLNUM'], '综合杀号')
        self.base_driver.forced_wait(5)
        if os.path.exists("/fusion/lottery_hall/fast3/综合杀号.txt"):
            os.remove("/fusion/lottery_hall/fast3/综合杀号.txt")
        else:
            pass

        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_fast3['WYQISHU'], i+1)

                # 开奖号码
                #  s1 = self.base_driver.get_texts(self.config_dict_fast3['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_attribute_text(self.config_dict_fast3['KJNUM00'], 'class', i)
                a1 = self.base_driver.get_attribute_text(self.config_dict_fast3['KJNUM01'], 'class', i)
                a2 = self.base_driver.get_attribute_text(self.config_dict_fast3['KJNUM02'], 'class', i)
                #
                # print(a0)
                # print(a0[13:])

                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM00'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM01'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM02'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM03'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM04'], i+1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM04'], i+1)

                # 读取名字
                b00 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 2)
                b01 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 4)
                b02 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 6)
                b03 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 8)
                b04 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 10)

                m0 = [a0[13:], a1[13:], a2[13:]]
                arr = np.array(m0)
                # 是否含有对应的值，True
                if c0 == '杀对':
                    if (arr == b0[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(b0) + '  综合杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(b0) + '  综合杀号杀对---正确')
                if c0 == '杀错':
                    if (arr == b0[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(b0) + '  综合杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(b0) + '  综合杀号杀错---错误')

                if c1 == '杀对':
                    if (arr == b1[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(b1) + '  综合杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(b1) + '  综合杀号杀对---正确')
                if c1 == '杀错':
                    if (arr == b1[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(b1) + '  综合杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(b1) + '  综合杀号杀错---错误')

                if c2 == '杀对':
                    if (arr == b2[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(b2) + '  综合杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(b2) + '  综合杀号杀对---正确')
                if c2 == '杀错':
                    if (arr == b2[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(b2) + '  综合杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(b2) + '  综合杀号杀错---错误')

                if c3 == '杀对':
                    if (arr == b3[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(b3) + '  综合杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(b3) + '  综合杀号杀对---正确')
                if c3 == '杀错':
                    if (arr == b3[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(b3) + '  综合杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(b3) + '  综合杀号杀错---错误')

                if c4 == '杀对':
                    if (arr == b4[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(b4) + '  综合杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(b4) + '  综合杀号杀对---正确')

                    # 是否含有对应的值，True
                if c4 == '杀错':
                    if (arr == b4[2:]).any():
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(b4) + '  综合杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(b4) + '  综合杀号杀错---错误')

                # 导出文件
                f = open("/fusion/lottery_hall/fast3/综合杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0)  + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()
            except Exception as e:
                print(e)
                print('稳赢杀号---综合杀号运行了' + str(i))
                break

    def plan_winkillnum_sum(self):
        # 和值杀号
        self.base_driver.clicks_by_text(self.config_dict_fast3['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近100期
        self.base_driver.clicks_by_text(self.config_dict_fast3['RECNET_PERIOD'], '最近100次')
        self.base_driver.forced_wait(1)
        # 冠军杀号
        self.base_driver.clicks_by_text(self.config_dict_fast3['NUMKILLNUM'], '和值杀号')
        self.base_driver.forced_wait(5)
        if os.path.exists("/fusion/lottery_hall/fast3/和值杀号.txt"):
            os.remove("/fusion/lottery_hall/fast3/和值杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_fast3['WYQISHU'], i+1)

                # 开奖号码
                #  s1 = self.base_driver.get_texts(self.config_dict_fast3['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_attribute_text(self.config_dict_fast3['KJNUM00'], 'class', i)
                a1 = self.base_driver.get_attribute_text(self.config_dict_fast3['KJNUM01'], 'class', i)
                a2 = self.base_driver.get_attribute_text(self.config_dict_fast3['KJNUM02'], 'class', i)

                # 杀对--错
                b0 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM01'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM02'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM03'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM04'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_fast3['KILLNUM05'], i+1)

                # 杀
                c0 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_fast3['ZHANJINUM04'], i+1)

                # 读取名字
                b00 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 3)
                b01 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 5)
                b02 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 7)
                b03 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 9)
                b04 = self.base_driver.get_texts(self.config_dict_fast3['NAME00'], 11)
                # print('期数:' + str(s0) + str(b4) + str(c4))
                m0 = [int(a0[13:]), int(a1[13:]), int(a2[13:])]
                # print(sum(m0))
                # print(c0[2:])
                # print(c1[2:])
                # print(c2[2:])
                # print(c3[2:])
                # print(c4[2:])
                # print(b0)
                if b0 == '杀对':
                    if sum(m0) == c0[2:]:
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(c0) + '  和值杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(c0) + '  和值杀号杀对---正确')
                if b0 == '杀错':
                    if sum(m0) != c0[2:]:
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(c0) + '  和值杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b00) + '  ' + str(c0) + '  和值杀号杀错---错误')

                if b1 == '杀对':
                    if sum(m0) == c1[2:]:
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(c1) + '  和值杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(c1) + '  和值杀号杀对---正确')
                if b1 == '杀错':
                    if sum(m0) != c1[2:]:
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(c1) + '  杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b01) + '  ' + str(c1) + '  杀错---错误')

                if b2 == '杀对':
                    if sum(m0) == c2[2:]:
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(c2) + '  和值杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(c2) + '  和值杀号杀对---正确')
                if b2 == '杀错':
                    if sum(m0) != c2[2:]:
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(c2) + '  和值杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b02) + '  ' + str(c2) + '  和值杀号杀错---错误')

                if b3 == '杀对':
                    if sum(m0) == c3[2:]:
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(c3) + '  和值杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(c3) + '  和值杀号杀对---正确')
                if b3 == '杀错':
                    if sum(m0) != c3[2:]:
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(c3) + '  和值杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b03) + '  ' + str(c3) + '  和值杀号杀错---错误')

                if b4 == '杀对':
                    if sum(m0) == c4[2:]:
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(c4) + '  和值杀号杀对---错误')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(c4) + '  和值杀号杀对---正确')
                if b4 == '杀错':
                    if sum(m0) != c4[2:]:
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(c4) + '  和值杀号杀错---正确')
                    else:
                        print('期数:' + str(s0) + ' ' + str(b04) + '  ' + str(c4) + '  和值杀号杀错---错误')

                # 导出文件
                f = open("/fusion/lottery_hall/fast3/和值杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()
            except Exception as e:
                print(e)
                print('稳赢杀号---和值杀号运行了' + str(i))
                break

    def lotteryhall_trend_basic(self):
        # 走势图
        self.base_driver.clicks_by_text(self.config_dict_fast3['MENU'], '走势图')
        # 基本走势
        self.base_driver.clicks_by_text(self.config_dict_fast3['VIEWTREND'], '基本走势')
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

        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_fast3['TREND_QH'], i)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                # 因新疆时时彩特殊改成匹配月
                # if datetime[:8] == time.strftime('%Y%m%d'):
                if datetime[:6] == time.strftime('%Y%m'):

                    # 开奖号码
                    s00 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUM'], i)

                    # 号码形态---豹子、、三不同、对子
                    s01 = self.base_driver.get_texts(self.config_dict_fast3['NUM_FORM_1'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_fast3['NUM_FORM_2'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_fast3['NUM_FORM_3'], i)

                    # 和值走势
                    s04 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_3'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_4'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_5'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_6'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_7'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_8'], i)
                    s10 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_9'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_10'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_11'], i)
                    s13 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_12'], i)
                    s14 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_13'], i)
                    s15 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_14'], i)
                    s16 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_15'], i)
                    s17 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_16'], i)
                    s18 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_17'], i)
                    s19 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_18'], i)

                    # 开奖号码
                    a00.extend(s00)
                    # 号码形态---豹子、、三不同、对子
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)

                    # 和值走势3~18
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

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        # 数据统计
        # 开奖号码分布1~6
        NUM_FB_1 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 25)
        NUM_FB_2 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 26)
        NUM_FB_3 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 27)
        NUM_FB_4 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 28)
        NUM_FB_5 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 29)
        NUM_FB_6 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 30)
        ss = [NUM_FB_1, NUM_FB_2, NUM_FB_3, NUM_FB_4, NUM_FB_5, NUM_FB_6]
        # print(ss)
        # print('ball_1_0:   ' + str(ball_1_0))
        # print('a00.count:  ' + str(a00.count('0')))
        print(a00)
        print(ss)
        print(a00.count('1'))
        if str(NUM_FB_1) == str(a00.count('1')):
            print('开奖号码分布统计1---正确---' + str(a00.count('1')))
        else:
            print('开奖号码分布统计1---错误---' + str(a00.count('1')))
        if str(NUM_FB_2) == str(a00.count('2')):
            print('开奖号码分布统计2---正确---' + str(a00.count('2')))
        else:
            print('开奖号码分布统计2---错误---' + str(a00.count('2')))
        if str(NUM_FB_3) == str(a00.count('3')):
            print('开奖号码分布统计3---正确---' + str(a00.count('3')))
        else:
            print('开奖号码分布统计3---错误---' + str(a00.count('3')))
        if str(NUM_FB_4) == str(a00.count('4')):
            print('开奖号码分布统计4---正确---' + str(a00.count('4')))
        else:
            print('开奖号码分布统计4---错误---' + str(a00.count('4')))
        if str(NUM_FB_5) == str(a00.count('5')):
            print('开奖号码分布统计5---正确---' + str(a00.count('5')))
        else:
            print('开奖号码分布统计5---错误---' + str(a00.count('5')))
        if str(NUM_FB_6) == str(a00.count('6')):
            print('开奖号码分布统计6---正确---' + str(a00.count('6')))
        else:
            print('开奖号码分布统计6---错误---' + str(a00.count('6')))

        # 号码形态---豹子、、三不同、对子
        NUM_FORM_1 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 31)
        NUM_FORM_2 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 32)
        NUM_FORM_3 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 33)
        if str(NUM_FORM_1) == str(a01.count('豹子')):
            print('号码形态统计豹子---正确---' + str(a01.count('豹子')))
        else:
            print('号码形态统计豹子---错误---' + str(a01.count('豹子')))
        if str(NUM_FORM_2) == str(a02.count('三不同')):
            print('号码形态统计三不同---正确---' + str(a02.count('三不同')))
        else:
            print('号码形态统计三不同---错误---' + str(a02.count('三不同')))
        if str(NUM_FORM_3) == str(a03.count('对子')):
            print('号码形态统计对子---正确---' + str(a03.count('对子')))
        else:
            print('号码形态统计对子---错误---' + str(a03.count('对子')))

        TREND_NUM_3 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 34)
        TREND_NUM_4 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 35)
        TREND_NUM_5 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 36)
        TREND_NUM_6 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 37)
        TREND_NUM_7 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 38)
        TREND_NUM_8 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 39)
        TREND_NUM_9 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 40)
        TREND_NUM_10 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 41)
        TREND_NUM_11 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 42)
        TREND_NUM_12 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 43)
        TREND_NUM_13 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 44)
        TREND_NUM_14 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 45)
        TREND_NUM_15 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 46)
        TREND_NUM_16 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 47)
        TREND_NUM_17 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 48)
        TREND_NUM_18 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 49)

        # 和值走势3~18
        if str(TREND_NUM_3) == str(a04.count('3')):
            print('和值走势3统计---正确---' + str(a04.count('3')))
        else:
            print('和值走势3统计---错误---' + str(a04.count('3')))

        if str(TREND_NUM_4) == str(a05.count('4')):
            print('和值走势4统计---正确---' + str(a05.count('4')))
        else:
            print('和值走势4统计---错误---' + str(a05.count('4')))
        if str(TREND_NUM_5) == str(a06.count('5')):
            print('和值走势5统计---正确---' + str(a06.count('5')))
        else:
            print('和值走势5统计---错误---' + str(a06.count('5')))
        if str(TREND_NUM_6) == str(a07.count('6')):
            print('和值走势6统计---正确---' + str(a07.count('6')))
        else:
            print('和值走势6统计---错误---' + str(a07.count('6')))
        if str(TREND_NUM_7) == str(a08.count('7')):
            print('和值走势7统计---正确---' + str(a08.count('7')))
        else:
            print('和值走势7统计---错误---' + str(a08.count('7')))
        if str(TREND_NUM_8) == str(a09.count('8')):
            print('和值走势8统计---正确---' + str(a09.count('8')))
        else:
            print('和值走势8统计---错误---' + str(a09.count('8')))
        if str(TREND_NUM_9) == str(a10.count('9')):
            print('和值走势9统计---正确---' + str(a10.count('9')))
        else:
            print('和值走势9统计---错误---' + str(a10.count('9')))
        if str(TREND_NUM_10) == str(a11.count('10')):
            print('和值走势10统计---正确---' + str(a11.count('10')))
        else:
            print('和值走势10统计---错误---' + str(a11.count('10')))
        if str(TREND_NUM_11) == str(a12.count('11')):
            print('和值走势11统计---正确---' + str(a12.count('11')))
        else:
            print('和值走势11统计---错误---' + str(a12.count('11')))
        if str(TREND_NUM_12) == str(a13.count('12')):
            print('和值走势12统计---正确---' + str(a13.count('12')))
        else:
            print('和值走势12统计---错误---' + str(a13.count('12')))
        if str(TREND_NUM_13) == str(a14.count('13')):
            print('和值走势13统计---正确---' + str(a14.count('13')))
        else:
            print('和值走势13统计---错误---' + str(a14.count('13')))
        if str(TREND_NUM_14) == str(a15.count('14')):
            print('和值走势14统计---正确---' + str(a15.count('14')))
        else:
            print('和值走势14统计---错误---' + str(a15.count('14')))
        if str(TREND_NUM_15) == str(a16.count('15')):
            print('和值走势15统计---正确---' + str(a16.count('15')))
        else:
            print('和值走势15统计---错误---' + str(a16.count('15')))
        if str(TREND_NUM_16) == str(a17.count('16')):
            print('和值走势16统计---正确---' + str(a17.count('16')))
        else:
            print('和值走势16统计---错误---' + str(a17.count('16')))
        if str(TREND_NUM_17) == str(a18.count('17')):
            print('和值走势17统计---正确---' + str(a18.count('17')))
        else:
            print('和值走势17统计---错误---' + str(a18.count('17')))
        if str(TREND_NUM_18) == str(a19.count('18')):
            print('和值走势18统计---正确---' + str(a19.count('18')))
        else:
            print('和值走势18统计---错误---' + str(a19.count('18')))

    def lotteryhall_trend_position(self):
        # 走势图
        # 定位走势
        self.base_driver.clicks_by_text(self.config_dict_fast3['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_fast3['VIEWTREND'], '定位走势')
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
                datetime = self.base_driver.get_texts(self.config_dict_fast3['TREND_QH'], i)
                if datetime[:6] == time.strftime('%Y%m'):
                    # 开奖号码
                    s00 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUM'], i)

                    # 形态特征---大小单双和质
                    s01 = self.base_driver.get_texts(self.config_dict_fast3['NUM_FORM_1'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_fast3['NUM_FORM_2'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_fast3['NUM_FORM_3'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_3'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_4'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_5'], i)
                    # # 012路
                    # s07 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_6'], i)
                    # s08 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_7'], i)
                    # s09 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_8'], i)
                    # 升平降
                    s10 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_9'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_10'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_fast3['TREND_NUM_11'], i)

                    a00.append(s00[0])

                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)

                    # a07.append(s07)
                    # a08.append(s08)
                    # a09.append(s09)

                    a10.append(s10)
                    a11.append(s11)
                    a12.append(s12)
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a00)
        # 冠军分布
        ball_1_1 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 18)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 19)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 20)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 21)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 22)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 23)

        ss = [ball_1_1, ball_1_2, ball_1_3, ball_1_4, ball_1_5, ball_1_6]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_1))
        print('a00.count:  ' + str(a00.count('1')))
        if str(ball_1_1) == str(a00.count('1')):
            print('冠军分布走势统计1---正确---' + str(a00.count('1')))
        else:
            print('冠军分布走势统计1---错误---' + str(a00.count('1')))
        if str(ball_1_2) == str(a00.count('2')):
            print('冠军分布走势统计2---正确---' + str(a00.count('2')))
        else:
            print('冠军分布走势统计2---错误---' + str(a00.count('2')))
        if str(ball_1_3) == str(a00.count('3')):
            print('冠军分布走势统计3---正确---' + str(a00.count('3')))
        else:
            print('冠军分布走势统计3---错误---' + str(a00.count('3')))
        if str(ball_1_4) == str(a00.count('4')):
            print('冠军分布走势统计4---正确---' + str(a00.count('4')))
        else:
            print('冠军分布走势统计4---错误---' + str(a00.count('4')))
        if str(ball_1_5) == str(a00.count('5')):
            print('冠军分布走势统计5---正确---' + str(a00.count('5')))
        else:
            print('冠军分布走势统计5---错误---' + str(a00.count('5')))
        if str(ball_1_6) == str(a00.count('6')):
            print('冠军分布走势统计6---正确---' + str(a00.count('6')))
        else:
            print('冠军分布走势统计6---错误---' + str(a00.count('6')))

        # 形态特征---大小单双和质
        ball_1_7 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 24)
        ball_1_8 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 25)
        ball_1_9 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 26)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 27)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 28)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 29)

        if str(ball_1_7) == str(a01.count('大')):
            print('形态特征大---正确---' + str(a01.count('大')))
        else:
            print('形态特征大---错误---' + str(a01.count('大')))
        if str(ball_1_8) == str(a02.count('小')):
            print('形态特征小---正确---' + str(a02.count('小')))
        else:
            print('形态特征小---错误---' + str(a02.count('小')))
        if str(ball_1_9) == str(a03.count('单')):
            print('形态特征单---正确---' + str(a03.count('单')))
        else:
            print('形态特征单---错误---' + str(a03.count('单')))
        if str(ball_2_0) == str(a04.count('双')):
            print('形态特征双---正确---' + str(a04.count('双')))
        else:
            print('形态特征双---错误---' + str(a04.count('双')))
        if str(ball_2_1) == str(a05.count('合')):
            print('形态特征合---正确---' + str(a05.count('合')))
        else:
            print('形态特征合---错误---' + str(a05.count('合')))
        if str(ball_2_2) == str(a06.count('质')):
            print('形态特征质---正确---' + str(a06.count('质')))
        else:
            print('形态特征质---错误---' + str(a06.count('质')))


        # 012路
        ball_2_3 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 30)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 31)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 32)
        # if str(ball_2_3) == str(a07.count('yellowbg')):
        #     print('012路0---正确---' + str(a07.count('yellowbg')))
        # else:
        #     print('012路0---错误---' + str(a07.count('yellowbg')))
        # if str(ball_2_4) == str(a08.count('bluebg')):
        #     print('012路1---正确---' + str(a08.count('bluebg')))
        # else:
        #     print('012路1---错误---' + str(a08.count('bluebg')))
        # if str(ball_2_5) == str(a09.count('yellowbg')):
        #     print('012路2---正确---' + str(a09.count('yellowbg')))
        # else:
        #     print('012路2---错误---' + str(a09.count('yellowbg')))

        ball_2_6 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 33)
        ball_2_7 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 34)
        ball_2_8 = self.base_driver.get_texts(self.config_dict_fast3['DATA_BALL_NUM'], 35)

        if str(ball_2_6) == str(a10.count('升')):
            print('升平降-升---正确---' + str(a10.count('升')))
        else:
            print('升平降-升---错误---' + str(a10.count('升')))
        if str(ball_2_7) == str(a11.count('平')):
            print('升平降-平---正确---' + str(a11.count('平')))
        else:
            print('升平降-平---错误---' + str(a11.count('平')))
        if str(ball_2_8) == str(a12.count('降')):
            print('升平降-降---正确---' + str(a12.count('降')))
        else:
            print('升平降-降---错误---' + str(a12.count('降')))

    def lotteryhall_trend_size(self):
        # 走势图
        # 大小走势
        self.base_driver.clicks_by_text(self.config_dict_fast3['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_fast3['VIEWTREND'], '大小走势')
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
                datetime = self.base_driver.get_texts(self.config_dict_fast3['TREND_QH'], i)
                if datetime[:6] == time.strftime('%Y%m'):
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUM'], i)

                    # 第一位、第二位、第三位
                    s01 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_1_0'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_1_1'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_2_0'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_2_1'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_3_0'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_3_1'], i-1)
                    # a00.append(s00[0])
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print(a01)
        # 冠军分布
        ball_1_1 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 0)
        ball_1_2 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 1)
        ball_1_3 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 2)
        ball_1_4 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 3)
        ball_1_5 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 4)
        ball_1_6 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 5)

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
        print(ball_1_6)
        print(str(a06.count('小')))
        if str(ball_1_6) == str(a06.count('小')):
            print('第三位统计小---正确---' + str(a06.count('小')))
        else:
            print('第三位统计小---错误---' + str(a06.count('小')))

    def lotteryhall_trend_sum(self):
        # 走势图
        # 和值走势
        self.base_driver.clicks_by_text(self.config_dict_fast3['MENU'], '走势图')
        self.base_driver.clicks_by_text(self.config_dict_fast3['VIEWTREND'], '和值走势')
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
        a11 = []
        a12 = []
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_fast3['TREND_QH'], i)
                if datetime[:6] == time.strftime('%Y%m'):
                    # 开奖号码
                    s00 = self.base_driver.get_texts(self.config_dict_fast3['LOTTERY_NUM'], i)
                    '''
                    # 第一位、第二位、第三位
                    s01 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_1_0'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_1_1'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_2_0'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_2_1'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_3_0'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_3_1'], i-1)
                    
                    a01.append(s01)
                    a02.append(s02)
                    a03.append(s03)
                    a04.append(s04)
                    a05.append(s05)
                    a06.append(s06)
                    '''
                    sss = str(int(s00[0]) + int(s00[1]) + int(s00[2]))
                    a00.append(sss)

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

        print(a00)
        # 冠军分布
        ball_3 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 1)
        ball_4 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 2)
        ball_5 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 3)
        ball_6 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 4)
        ball_7 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 5)
        ball_8 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 6)
        ball_9 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 7)
        ball_10 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 8)
        ball_11 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 9)
        ball_12 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 10)
        ball_13 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 11)
        ball_14 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 12)
        ball_15 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 13)
        ball_16 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 14)
        ball_17 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 15)
        ball_18 = self.base_driver.get_texts(self.config_dict_fast3['DX_SIZE_SUM'], 16)

        ss = [ball_3, ball_4, ball_5, ball_6, ball_7, ball_8]
        print(ss)
        print('ball_1_0:   ' + str(ball_3))
        print('a00.count:  ' + str(a00.count('3')))
        if ball_3 == a00.count('3'):
            print('和值走势统计3---正确---' + str(a00.count('3')))
        else:
            print('和值走势统计3---错误---' + str(a00.count('3')))
        if str(ball_4) == str(a00.count('4')):
            print('和值走势统计4---正确---' + str(a00.count('4')))
        else:
            print('和值走势统计4---错误---' + str(a00.count('4')))
        if str(ball_5) == str(a03.count('5')):
            print('和值走势统计5---正确---' + str(a00.count('5')))
        else:
            print('和值走势统计5---错误---' + str(a00.count('5')))
        if str(ball_6) == str(a00.count('6')):
            print('和值走势统计6---正确---' + str(a00.count('6')))
        else:
            print('和值走势统计6---错误---' + str(a00.count('6')))
        if str(ball_7) == str(a00.count('7')):
            print('和值走势统计7---正确---' + str(a00.count('7')))
        else:
            print('和值走势统计7---错误---' + str(a00.count('7')))
        if str(ball_8) == str(a00.count('8')):
            print('和值走势统计8---正确---' + str(a00.count('8')))
        else:
            print('和值走势统计8---错误---' + str(a00.count('8')))
        if str(ball_9) == a00.count('9'):
            print('和值走势统计9---正确---' + str(a00.count('9')))
        else:
            print('和值走势统计9---错误---' + str(a00.count('9')))
        if str(ball_10) == str(a00.count('10')):
            print('和值走势统计10---正确---' + str(a00.count('10')))
        else:
            print('和值走势统计10---错误---' + str(a00.count('10')))
        if str(ball_11) == str(a03.count('11')):
            print('和值走势统计11---正确---' + str(a00.count('11')))
        else:
            print('和值走势统计11---错误---' + str(a00.count('11')))
        if str(ball_12) == str(a00.count('12')):
            print('和值走势统计12---正确---' + str(a00.count('12')))
        else:
            print('和值走势统计12---错误---' + str(a00.count('12')))
        if str(ball_13) == str(a00.count('13')):
            print('和值走势统计13---正确---' + str(a00.count('13')))
        else:
            print('和值走势统计13---错误---' + str(a00.count('13')))
        if str(ball_14) == str(a00.count('14')):
            print('和值走势统计14---正确---' + str(a00.count('14')))
        else:
            print('和值走势统计14---错误---' + str(a00.count('14')))
        if str(ball_15) == str(a00.count('15')):
            print('和值走势统计15---正确---' + str(a00.count('15')))
        else:
            print('和值走势统计15---错误---' + str(a00.count('15')))
        if str(ball_16) == str(a00.count('6')):
            print('和值走势统计16---正确---' + str(a00.count('16')))
        else:
            print('和值走势统计16---错误---' + str(a00.count('16')))
        if str(ball_17) == str(a00.count('7')):
            print('和值走势统计17---正确---' + str(a00.count('17')))
        else:
            print('和值走势统计17---错误---' + str(a00.count('17')))
        if str(ball_18) == str(a00.count('8')):
            print('和值走势统计18---正确---' + str(a00.count('18')))
        else:
            print('和值走势统计18---错误---' + str(a00.count('18')))



