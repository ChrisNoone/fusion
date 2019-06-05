import os
import random
import time


from common.box import BasePage, YamlHelper


class LotteryPK10(BasePage):

    config_dict_tmmcq = YamlHelper().get_config_dict('/fusion/lottery_hall/yaml/lottery_pk10.yaml')['PLAN_PK10_LOTTERT']

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
                date = self.base_driver.get_texts(self.config_dict_tmmcq['TIME_NUM'], i)
                # print(date[:10])
                if date[:10] == time.strftime('%Y-%m-%d'):
                    # 开奖号码
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM00'], i)
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM01'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM02'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM03'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM04'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM05'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM06'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM07'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM08'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM09'], i)

                    # 冠亚和---单双
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_DS_NUM'], i)
                    # 冠亚和---大小
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_DX_NUM'], i)

                    # 龙虎1-5
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_LH_NUM00'], i)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_LH_NUM01'], i)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_LH_NUM02'], i)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_LH_NUM03'], i)
                    s16 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_LH_NUM04'], i)

                    # 开奖号码
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

                    # 冠亚和---单双大小
                    a10.append(s10)
                    a11.append(s11)

                    a12.append(s12)
                    a13.append(s13)
                    a14.append(s14)
                    a15.append(s15)
                    a16.append(s16)
            except Exception as e:
                print(e)
                print('今日开奖双面统计运行' + str(i) + '行')
                break
        # 冠军---单双大小
        b00 = a00.count('01') + a00.count('03') + a00.count('05') + a00.count('07') + a00.count('09')
        b01 = a00.count('02') + a00.count('04') + a00.count('06') + a00.count('08') + a00.count('10')
        b02 = a00.count('06') + a00.count('07') + a00.count('08') + a00.count('09') + a00.count('10')
        b03 = a00.count('01') + a00.count('02') + a00.count('03') + a00.count('04') + a00.count('05')

        # 亚军---单双大小
        b04 = a01.count('01') + a01.count('03') + a01.count('05') + a01.count('07') + a01.count('09')
        b05 = a01.count('02') + a01.count('04') + a01.count('06') + a01.count('08') + a01.count('10')
        b06 = a01.count('06') + a01.count('07') + a01.count('08') + a01.count('09') + a01.count('10')
        b07 = a01.count('01') + a01.count('02') + a01.count('03') + a01.count('04') + a01.count('05')

        # 第三名---单双大小
        b08 = a02.count('01') + a02.count('03') + a02.count('05') + a02.count('07') + a02.count('09')
        b09 = a02.count('02') + a02.count('04') + a02.count('06') + a02.count('08') + a02.count('10')
        b10 = a02.count('06') + a02.count('07') + a02.count('08') + a02.count('09') + a02.count('10')
        b11 = a02.count('01') + a02.count('02') + a02.count('03') + a02.count('04') + a02.count('05')

        # 第四名---单双大小
        b12 = a03.count('01') + a03.count('03') + a03.count('05') + a03.count('07') + a03.count('09')
        b13 = a03.count('02') + a03.count('04') + a03.count('06') + a03.count('08') + a03.count('10')
        b14 = a03.count('06') + a03.count('07') + a03.count('08') + a03.count('09') + a03.count('10')
        b15 = a03.count('01') + a03.count('02') + a03.count('03') + a03.count('04') + a03.count('05')

        # 第五名---单双大小
        b16 = a04.count('01') + a04.count('03') + a04.count('05') + a04.count('07') + a04.count('09')
        b17 = a04.count('02') + a04.count('04') + a04.count('06') + a04.count('08') + a04.count('10')
        b18 = a04.count('06') + a04.count('07') + a04.count('08') + a04.count('09') + a04.count('10')
        b19 = a04.count('01') + a04.count('02') + a04.count('03') + a04.count('04') + a04.count('05')

        # 第六名---单双大小
        b20 = a05.count('01') + a05.count('03') + a05.count('05') + a05.count('07') + a05.count('09')
        b21 = a05.count('02') + a05.count('04') + a05.count('06') + a05.count('08') + a05.count('10')
        b22 = a05.count('06') + a05.count('07') + a05.count('08') + a05.count('09') + a05.count('10')
        b23 = a05.count('01') + a05.count('02') + a05.count('03') + a05.count('04') + a05.count('05')

        # 第七名---单双大小
        b24 = a06.count('01') + a06.count('03') + a06.count('05') + a06.count('07') + a06.count('09')
        b25 = a06.count('02') + a06.count('04') + a06.count('06') + a06.count('08') + a06.count('10')
        b26 = a06.count('06') + a06.count('07') + a06.count('08') + a06.count('09') + a06.count('10')
        b27 = a06.count('01') + a06.count('02') + a06.count('03') + a06.count('04') + a06.count('05')

        # 第八名---单双大小
        b28 = a07.count('01') + a07.count('03') + a07.count('05') + a07.count('07') + a07.count('09')
        b29 = a07.count('02') + a07.count('04') + a07.count('06') + a07.count('08') + a07.count('10')
        b30 = a07.count('06') + a07.count('07') + a07.count('08') + a07.count('09') + a07.count('10')
        b31 = a07.count('01') + a07.count('02') + a07.count('03') + a07.count('04') + a07.count('05')

        # 第就名---单双大小
        b32 = a08.count('01') + a08.count('03') + a08.count('05') + a08.count('07') + a08.count('09')
        b33 = a08.count('02') + a08.count('04') + a08.count('06') + a08.count('08') + a08.count('10')
        b34 = a08.count('06') + a08.count('07') + a08.count('08') + a08.count('09') + a08.count('10')
        b35 = a08.count('01') + a08.count('02') + a08.count('03') + a08.count('04') + a08.count('05')

        # 第十名---单双大小
        b36 = a09.count('01') + a09.count('03') + a09.count('05') + a09.count('07') + a09.count('09')
        b37 = a09.count('02') + a09.count('04') + a09.count('06') + a09.count('08') + a09.count('10')
        b38 = a09.count('06') + a09.count('07') + a09.count('08') + a09.count('09') + a09.count('10')
        b39 = a09.count('01') + a09.count('02') + a09.count('03') + a09.count('04') + a09.count('05')

        c00 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 1)
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
        c11 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 12)
        c12 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 13)
        c13 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 14)
        c14 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 15)
        c15 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 16)
        c16 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 17)
        c17 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 18)
        c18 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 19)
        c19 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 20)
        c20 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 21)
        c21 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 22)
        c22 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 23)
        c23 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 24)
        c24 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 25)
        c25 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 26)
        c26 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 27)
        c27 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 28)
        c28 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 29)
        c29 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 30)
        c30 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 31)
        c31 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 32)
        c32 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 33)
        c33 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 34)
        c34 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 35)
        c35 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 36)
        c36 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 37)
        c37 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 38)
        c38 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 39)
        c39 = self.base_driver.get_texts(self.config_dict_tmmcq['NUMS_APPEARA'], 40)

        print(' ')
        if str(c00) == str(b00):
            print('冠军单统计正确 ' + str(b00))
        else:
            print('冠军单统计错误 ' + str(b00))
        if str(c01) == str(b01):
            print('冠军双统计正确 ' + str(b01))
        else:
            print('冠军双统计错误 ' + str(b01))
        if str(c02) == str(b02):
            print('冠军大统计正确 ' + str(b02))
        else:
            print('冠军大统计错误 ' + str(b02))
        if str(c03) == str(b03):
            print('冠军小统计正确 ' + str(b03))
        else:
            print('冠军小统计错误 ' + str(b03))

        if str(c04) == str(b04):
            print('亚军单统计正确 ' + str(b04))
        else:
            print('亚军单统计错误 ' + str(b04))
        if str(c05) == str(b05):
            print('亚军双统计正确 ' + str(b05))
        else:
            print('亚军双统计错误 ' + str(b05))
        if str(c06) == str(b06):
            print('亚军大统计正确 ' + str(b06))
        else:
            print('亚军大统计错误 ' + str(b06))
        if str(c07) == str(b07):
            print('亚军小统计正确 ' + str(b07))
        else:
            print('亚军小统计错误 ' + str(b07))

        if str(c08) == str(b08):
            print('第三名单统计正确 ' + str(b08))
        else:
            print('第三名单统计错误 ' + str(b08))
        if str(c09) == str(b09):
            print('第三名双统计正确 ' + str(b09))
        else:
            print('第三名双统计错误 ' + str(b09))
        if str(c10) == str(b10):
            print('第三名大统计正确 ' + str(b10))
        else:
            print('第三名大统计错误 ' + str(b10))
        if str(c11) == str(b11):
            print('第三名小统计正确 ' + str(b11))
        else:
            print('第三名小统计错误 ' + str(b11))

        if str(c12) == str(b12):
            print('第四名单统计正确 ' + str(b12))
        else:
            print('第四名单统计错误 ' + str(b12))
        if str(c13) == str(b13):
            print('第四名双统计正确 ' + str(b13))
        else:
            print('第四名双统计错误 ' + str(b13))
        if str(c14) == str(b14):
            print('第四名大统计正确 ' + str(b14))
        else:
            print('第四名大统计错误 ' + str(b14))
        if str(c15) == str(b15):
            print('第四名小统计正确 ' + str(b15))
        else:
            print('第四名小统计错误 ' + str(b15))

        if str(c16) == str(b16):
            print('第五名单统计正确 ' + str(b16))
        else:
            print('第五名单统计错误 ' + str(b16))
        if str(c17) == str(b17):
            print('第五名双统计正确 ' + str(b17))
        else:
            print('第五名双统计错误 ' + str(b17))
        if str(c18) == str(b18):
            print('第五名大统计正确 ' + str(b18))
        else:
            print('第五名大统计错误 ' + str(b18))
        if str(c19) == str(b19):
            print('第五名小统计正确 ' + str(b19))
        else:
            print('第五名小统计错误 ' + str(b19))

        if str(c20) == str(b20):
            print('第六名单统计正确 ' + str(b20))
        else:
            print('第六名单统计错误 ' + str(b20))
        if str(c21) == str(b21):
            print('第六名双统计正确 ' + str(b21))
        else:
            print('第六名双统计错误 ' + str(b21))
        if str(c22) == str(b22):
            print('第六名大统计正确 ' + str(b22))
        else:
            print('第六名大统计错误 ' + str(b22))
        if str(c23) == str(b23):
            print('第六名小统计正确 ' + str(b23))
        else:
            print('第六名小统计错误 ' + str(b23))

        if str(c24) == str(b24):
            print('第七名单统计正确 ' + str(b24))
        else:
            print('第七名单统计错误 ' + str(b24))
        if str(c25) == str(b25):
            print('第七名双统计正确 ' + str(b25))
        else:
            print('第七名双统计错误 ' + str(b25))
        if str(c26) == str(b26):
            print('第七名大统计正确 ' + str(b26))
        else:
            print('第七名大统计错误 ' + str(b26))
        if str(c27) == str(b27):
            print('第七名小统计正确 ' + str(b27))
        else:
            print('第七名小统计错误 ' + str(b27))

        if str(c28) == str(b28):
            print('第八名单统计正确 ' + str(b28))
        else:
            print('第八名单统计错误 ' + str(b28))
        if str(c29) == str(b29):
            print('第八名双统计正确 ' + str(b29))
        else:
            print('第八名双统计错误 ' + str(b29))
        if str(c30) == str(b30):
            print('第八名大统计正确 ' + str(b30))
        else:
            print('第八名大统计错误 ' + str(b30))
        if str(c31) == str(b34):
            print('第八名小统计正确 ' + str(b31))
        else:
            print('第八名小统计错误 ' + str(b31))

        if str(c32) == str(b32):
            print('第九名单统计正确 ' + str(b32))
        else:
            print('第九名单统计错误 ' + str(b32))
        if str(c33) == str(b33):
            print('第九名双统计正确 ' + str(b33))
        else:
            print('第九名双统计错误 ' + str(b33))
        if str(c34) == str(b34):
            print('第九名大统计正确 ' + str(b34))
        else:
            print('第九名大统计错误 ' + str(b34))
        if str(c35) == str(b35):
            print('第九名小统计正确 ' + str(b35))
        else:
            print('第九名小统计错误 ' + str(b35))

        if str(c36) == str(b36):
            print('第十名单统计正确 ' + str(b36))
        else:
            print('第十名单统计错误 ' + str(b36))
        if str(c37) == str(b37):
            print('第十名双统计正确 ' + str(b37))
        else:
            print('第十名双统计错误 ' + str(b37))
        if str(c38) == str(b38):
            print('第十名大统计正确 ' + str(b38))
        else:
            print('第十名大统计错误 ' + str(b38))
        if str(c39) == str(b39):
            print('第十名小统计正确 ' + str(b39))
        else:
            print('第十名小统计错误 ' + str(b39))

        # 冠亚龙虎
        m00 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 1)
        m01 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 2)
        m02 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 3)
        m03 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 4)
        m04 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 5)
        m05 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 6)
        m06 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 7)
        m07 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 8)
        m08 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 9)
        m09 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 10)
        m10 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 11)
        m11 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 12)
        m12 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 13)
        m13 = self.base_driver.get_texts(self.config_dict_tmmcq['GYLH_NUM'], 14)

        # 冠亚和---单双大小
        print(' ')
        d00 = a10.count('单')
        d01 = a10.count('双')
        d02 = a11.count('大')
        d03 = a11.count('小')

        if str(m00) == str(d00):
            print('冠亚和单统计正确' + str(d00))
        else:
            print('冠亚和单统计错误' + str(d00))
        if str(m01) == str(d01):
            print('冠亚和双统计正确' + str(d01))
        else:
            print('冠亚和双统计错误' + str(d01))
        if str(m02) == str(d02):
            print('冠亚和大统计正确' + str(d02))
        else:
            print('冠亚和大统计错误' + str(d02))
        if str(m03) == str(d03):
            print('冠亚和小统计正确' + str(d03))
        else:
            print('冠亚和小统计错误' + str(d03))

        print(' ')
        # 第一名龙虎
        d04 = a12.count('龙')
        d05 = a12.count('虎')
        if str(m04) == str(d04):
            print('第一名龙统计正确' + str(d04))
        else:
            print('第一名龙统计错误' + str(d04))
        if str(m05) == str(d05):
            print('第一名虎统计正确' + str(d05))
        else:
            print('第一名虎统计错误' + str(d05))

        # 第二名龙虎
        d06 = a13.count('龙')
        d07 = a13.count('虎')
        if str(m06) == str(d06):
            print('第二名龙统计正确' + str(d06))
        else:
            print('第二名龙统计错误' + str(d06))
        if str(m07) == str(d07):
            print('第二名虎统计正确' + str(d07))
        else:
            print('第二名虎统计错误' + str(d07))

        # 第三名龙虎
        d08 = a14.count('龙')
        d09 = a14.count('虎')
        if str(m08) == str(d08):
            print('第三名龙统计正确' + str(d08))
        else:
            print('第三名龙统计错误' + str(d08))
        if str(m09) == str(d09):
            print('第三名虎统计正确' + str(d09))
        else:
            print('第三名虎统计错误' + str(d09))

        # 第四名龙虎
        d10 = a15.count('龙')
        d11 = a15.count('虎')
        if str(m10) == str(d10):
            print('第四名龙统计正确' + str(d10))
        else:
            print('第四名龙统计错误' + str(d10))
        if str(m11) == str(d11):
            print('第四名虎统计正确' + str(d11))
        else:
            print('第四名虎统计错误' + str(d11))

        # 第五名龙虎
        d12 = a16.count('龙')
        d13 = a16.count('虎')
        if str(m12) == str(d12):
            print('第五名龙统计正确' + str(d12))
        else:
            print('第五名龙统计错误' + str(d12))
        if str(m13) == str(d13):
            print('第五名虎统计正确' + str(d13))
        else:
            print('第五名虎统计错误' + str(d13))

    def lotteryhall_trend_gyh(self):
        # 走势图
        # 基本走势
        self.base_driver.forced_wait(1)
        # 今日开奖
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['MENU'], '走势图')

        self.base_driver.clicks_by_text(self.config_dict_tmmcq['VIEWTREND'], '冠亚和走势')
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

        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)

                # print(time.strftime('%Y%m%d'))
                # 因新疆时时彩特殊改成匹配月
                # if datetime[:8] == time.strftime('%Y%m%d'):
                if datetime[:8] == time.strftime('%Y%m%d') or int(datetime[:2]) == 73:
                    # 冠亚和值
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_3'], i)
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_4'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_5'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_6'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_7'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_8'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_9'], i)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_10'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_11'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_12'], i)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_13'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_14'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_15'], i)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_16'], i)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_17'], i)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_18'], i)
                    s16 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_19'], i)

                    # 冠亚和走势 - --冠亚和尾
                    s17 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_0'], i)
                    s18 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_1'], i)
                    s19 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_2'], i)
                    s20 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_3'], i)
                    s21 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_4'], i)
                    s22 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_5'], i)
                    s23 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_6'], i)
                    s24 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_7'], i)
                    s25 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_8'], i)
                    s26 = self.base_driver.get_texts(self.config_dict_tmmcq['GYH_SUM_T_9'], i)

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
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 11)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 12)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 13)
        ball_2_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 14)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 15)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 16)
        ball_2_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 17)

        ss = [ball_1_0, ball_1_1, ball_1_2, ball_1_2, ball_1_3, ball_1_4,
              ball_1_5, ball_1_6, ball_1_7, ball_1_8, ball_1_9]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_0))
        print('a00.count:  ' + str(a01.count('3')))
        if str(ball_1_0) == str(a00.count('3')):
            print('冠亚和值统计3---正确---' + str(a00.count('3')))
        else:
            print('冠亚和值统计3---错误---' + str(a00.count('3')))
        if str(ball_1_1) == str(a01.count('4')):
            print('冠亚和值统计4---正确---' + str(a01.count('4')))
        else:
            print('冠亚和值统计4---错误---' + str(a01.count('4')))
        if str(ball_1_2) == str(a02.count('5')):
            print('冠亚和值统计5---正确---' + str(a02.count('5')))
        else:
            print('冠亚和值统计5---错误---' + str(a02.count('5')))
        if str(ball_1_3) == str(a03.count('6')):
            print('冠亚和值统计6---正确---' + str(a03.count('6')))
        else:
            print('冠亚和值统计6---错误---' + str(a03.count('6')))
        if str(ball_1_4) == str(a04.count('7')):
            print('冠亚和值统计7---正确---' + str(a04.count('7')))
        else:
            print('冠亚和值统计7---错误---' + str(a04.count('7')))
        if str(ball_1_5) == str(a05.count('8')):
            print('冠亚和值统计8---正确---' + str(a05.count('8')))
        else:
            print('冠亚和值统计8---错误---' + str(a05.count('8')))
        if str(ball_1_6) == str(a06.count('9')):
            print('冠亚和值统计9---正确---' + str(a06.count('9')))
        else:
            print('冠亚和值统计9---错误---' + str(a06.count('9')))
        if str(ball_1_7) == str(a07.count('10')):
            print('冠亚和值统计10---正确---' + str(a07.count('10')))
        else:
            print('冠亚和值统计10---错误---' + str(a07.count('10')))
        if str(ball_1_8) == str(a08.count('11')):
            print('冠亚和值统计11---正确---' + str(a08.count('11')))
        else:
            print('冠亚和值统计11---错误---' + str(a08.count('11')))
        if str(ball_1_9) == str(a09.count('12')):
            print('冠亚和值统计12---正确---' + str(a09.count('12')))
        else:
            print('冠亚和值统计12---错误---' + str(a09.count('12')))
        if str(ball_2_0) == str(a10.count('13')):
            print('冠亚和值统计13---正确---' + str(a10.count('13')))
        else:
            print('冠亚和值统计13---错误---' + str(a10.count('13')))
        if str(ball_2_1) == str(a11.count('14')):
            print('冠亚和值统计14---正确---' + str(a11.count('14')))
        else:
            print('冠亚和值统计14---错误---' + str(a11.count('14')))
        if str(ball_2_2) == str(a12.count('15')):
            print('冠亚和值统计15---正确---' + str(a12.count('15')))
        else:
            print('冠亚和值统计15---错误---' + str(a12.count('15')))
        if str(ball_2_3) == str(a13.count('16')):
            print('冠亚和值统计16---正确---' + str(a13.count('16')))
        else:
            print('冠亚和值统计16---错误---' + str(a13.count('16')))
        if str(ball_2_4) == str(a14.count('17')):
            print('冠亚和值统计17---正确---' + str(a14.count('17')))
        else:
            print('冠亚和值统计17---错误---' + str(a14.count('17')))
        if str(ball_2_5) == str(a15.count('18')):
            print('冠亚和值统计18---正确---' + str(a15.count('18')))
        else:
            print('冠亚和值统计18---错误---' + str(a15.count('18')))
        if str(ball_2_6) == str(a16.count('19')):
            print('冠亚和值统计19---正确---' + str(a16.count('19')))
        else:
            print('冠亚和值统计19---错误---' + str(a16.count('19')))

        ball_2_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 18)
        ball_2_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 19)
        ball_2_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 20)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 21)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 22)
        ball_3_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 23)
        ball_3_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 24)
        ball_3_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 25)
        ball_3_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 26)
        ball_3_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 27)

        # 冠亚和尾
        if str(ball_2_7) == str(a17.count('0')):
            print('冠亚和尾统计0---正确---' + str(a17.count('0')))
        else:
            print('冠亚和尾统计0---错误---' + str(a17.count('0')))
        if str(ball_2_8) == str(a18.count('1')):
            print('冠亚和尾统计1---正确---' + str(a18.count('1')))
        else:
            print('冠亚和尾统计1---错误---' + str(a18.count('1')))
        if str(ball_2_9) == str(a19.count('2')):
            print('冠亚和尾统计2---正确---' + str(a19.count('2')))
        else:
            print('冠亚和尾统计2---错误---' + str(a19.count('2')))
        if str(ball_3_0) == str(a20.count('3')):
            print('冠亚和尾统计3---正确---' + str(a20.count('3')))
        else:
            print('冠亚和尾统计3---错误---' + str(a20.count('3')))
        if str(ball_3_1) == str(a21.count('4')):
            print('冠亚和尾统计4---正确---' + str(a21.count('4')))
        else:
            print('冠亚和尾统计4---错误---' + str(a21.count('4')))
        if str(ball_3_2) == str(a22.count('5')):
            print('冠亚和尾统计5---正确---' + str(a22.count('5')))
        else:
            print('冠亚和尾统计5---错误---' + str(a22.count('5')))
        if str(ball_3_3) == str(a23.count('6')):
            print('冠亚和尾统计6---正确---' + str(a23.count('6')))
        else:
            print('冠亚和尾统计6---错误---' + str(a23.count('6')))
        if str(ball_3_4) == str(a24.count('7')):
            print('冠亚和尾统计7---正确---' + str(a24.count('7')))
        else:
            print('冠亚和尾统计7---错误---' + str(a24.count('7')))
        if str(ball_3_5) == str(a25.count('8')):
            print('冠亚和尾统计8---正确---' + str(a25.count('8')))
        else:
            print('冠亚和尾统计8---错误---' + str(a25.count('8')))
        if str(ball_3_6) == str(a26.count('9')):
            print('冠亚和尾统计9---正确---' + str(a26.count('9')))
        else:
            print('冠亚和尾统计9---错误---' + str(a26.count('9')))

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

        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i)
                # print(datetime)
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d') or int(datetime[:2]) == 73:
                    # 开奖号码冠军
                    s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)

                    # 形态特征---大小-单双-合质
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_0'], i)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_1'], i)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_2'], i)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_3'], i)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_4'], i)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_5'], i)

                    # 02=12路
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_6'], i)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_7'], i)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_8'], i)

                    # 升平降
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_2_9'], i)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_0'], i)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_BALL_3_1'], i)

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

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break
        print('a00  ' + str(a00))
        # 冠军分布
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
        ss = [ball_1_0, ball_1_1, ball_1_2, ball_1_3, ball_1_4, ball_1_5, ball_1_6, ball_1_7, ball_1_8, ball_1_9]
        print(ss)
        print('ball_1_0:   ' + str(ball_1_0))
        print('a00.count:  ' + str(a00.count('01')))
        if str(ball_1_0) == str(a00.count('01')):
            print('冠军分布统计0---正确---' + str(a00.count('01')))
        else:
            print('冠军分布统计0---错误---' + str(a00.count('01')))
        if str(ball_1_1) == str(a00.count('02')):
            print('冠军分布统计1---正确---' + str(a00.count('02')))
        else:
            print('冠军分布统计1---错误---' + str(a00.count('02')))
        if str(ball_1_2) == str(a00.count('03')):
            print('冠军分布统计2---正确---' + str(a00.count('03')))
        else:
            print('冠军分布统计2---错误---' + str(a00.count('03')))
        if str(ball_1_3) == str(a00.count('04')):
            print('冠军分布统计3---正确---' + str(a00.count('04')))
        else:
            print('冠军分布统计3---错误---' + str(a00.count('04')))
        if str(ball_1_4) == str(a00.count('05')):
            print('冠军分布统计4---正确---' + str(a00.count('05')))
        else:
            print('冠军分布统计4---错误---' + str(a00.count('05')))
        if str(ball_1_5) == str(a00.count('06')):
            print('冠军分布统计5---正确---' + str(a00.count('06')))
        else:
            print('冠军分布统计5---错误---' + str(a00.count('06')))
        if str(ball_1_6) == str(a00.count('07')):
            print('冠军分布统计6---正确---' + str(a00.count('07')))
        else:
            print('冠军分布统计6---错误---' + str(a00.count('07')))
        if str(ball_1_7) == str(a00.count('08')):
            print('冠军分布统计7---正确---' + str(a00.count('08')))
        else:
            print('冠军分布统计7---错误---' + str(a00.count('08')))
        if str(ball_1_8) == str(a00.count('09')):
            print('冠军分布统计8---正确---' + str(a00.count('09')))
        else:
            print('冠军分布统计8---错误---' + str(a00.count('09')))
        if str(ball_1_9) == str(a00.count('10')):
            print('冠军分布统计9---正确---' + str(a00.count('10')))
        else:
            print('冠军分布统计9---错误---' + str(a00.count('10')))
        # 形态特征
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 32)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 33)
        ball_2_2 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 34)
        ball_2_3 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 35)
        ball_2_4 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 36)
        ball_2_5 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 37)

        if str(ball_2_0) == str(a01.count('大')):
            print('形态特征大---正确---' + str(a01.count('大')))
        else:
            print('形态特征大---错误---' + str(a01.count('大')))
        if str(ball_2_1) == str(a02.count('小')):
            print('形态特征小---正确---' + str(a02.count('小')))
        else:
            print('形态特征小---错误---' + str(a02.count('小')))
        if str(ball_2_2) == str(a03.count('单')):
            print('形态特征单---正确---' + str(a03.count('单')))
        else:
            print('形态特征单---错误---' + str(a03.count('单')))
        if str(ball_2_3) == str(a04.count('双')):
            print('形态特征双---正确---' + str(a04.count('双')))
        else:
            print('形态特征双---错误---' + str(a04.count('双')))
        if str(ball_2_4) == str(a05.count('合')):
            print('形态特征合---正确---' + str(a05.count('合')))
        else:
            print('形态特征合---错误---' + str(a05.count('合')))
        if str(ball_2_5) == str(a06.count('质')):
            print('形态特征质---正确---' + str(a06.count('质')))
        else:
            print('形态特征质---错误---' + str(a06.count('质')))

        # # 012路
        # ball_2_6 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 38)
        # ball_2_7 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 39)
        # ball_2_8 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 40)
        # if str(ball_2_6) == str(a07.count('yellowbg')):
        #     print('012路0---正确---' + str(a07.count('yellowbg')))
        # else:
        #     print('012路0---错误---' + str(a07.count('yellowbg')))
        # if str(ball_2_7) == str(a08.count('bluebg')):
        #     print('012路1---正确---' + str(a08.count('bluebg')))
        # else:
        #     print('012路1---错误---' + str(a08.count('bluebg')))
        # if str(ball_2_8) == str(a09.count('yellowbg')):
        #     print('012路2---正确---' + str(a09.count('yellowbg')))
        # else:
        #     print('012路2---错误---' + str(a09.count('yellowbg')))

        # 升平降
        ball_2_9 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 41)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 42)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DATA_BALL_NUM'], 43)
        if str(ball_2_9) == str(a10.count('升')):
            print('升平降-升---正确---' + str(a10.count('升')))
        else:
            print('升平降-升---错误---' + str(a10.count('升')))
        if str(ball_3_0) == str(a11.count('平')):
            print('升平降-平---正确---' + str(a11.count('平')))
        else:
            print('升平降-平---错误---' + str(a11.count('平')))
        if str(ball_3_1) == str(a12.count('降')):
            print('升平降-降---正确---' + str(a12.count('降')))
        else:
            print('升平降-降---错误---' + str(a12.count('降')))

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
        aaa = []
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i+1)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d') or int(datetime[:2]) == 73:
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)
                    # 第一位~第十位
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_0'], i+1)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_1'], i+1)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_0'], i+1)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_1'], i+1)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_0'], i+1)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_1'], i+1)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_0'], i+1)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_1'], i+1)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_0'], i+1)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_1'], i+1)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_0'], i+1)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_1'], i+1)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_6_0'], i+1)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_6_1'], i+1)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_7_0'], i+1)
                    s16 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_7_1'], i+1)
                    s17 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_8_0'], i+1)
                    s18 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_8_1'], i+1)
                    s19 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_9_0'], i+1)
                    s20 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_9_1'], i)

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
                    aaa = [s01, s02, s03, s04, s05, s06]
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

        print(a20)
        print('aaa   ' + str(aaa))
        # 号码分布
        ball_0_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 0)
        ball_0_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 1)
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 2)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 3)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 4)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 5)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 6)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 7)
        ball_4_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 8)
        ball_4_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 9)
        ball_5_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 10)
        ball_5_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 11)
        ball_6_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 12)
        ball_6_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 13)
        ball_7_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 14)
        ball_7_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 15)
        ball_8_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 16)
        ball_8_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 17)
        ball_9_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 18)
        ball_9_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 19)

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
        if str(ball_5_0) == str(a11.count('大')):
            print('第六位统计大---正确---' + str(a11.count('大')))
        else:
            print('第六位统计大---错误---' + str(a11.count('大')))
        if str(ball_5_1) == str(a12.count('小')):
            print('第六位统计小---正确---' + str(a12.count('小')))
        else:
            print('第六位统计小---错误---' + str(a12.count('小')))
        if str(ball_6_0) == str(a13.count('大')):
            print('第七位统计大---正确---' + str(a13.count('大')))
        else:
            print('第七位统计大---错误---' + str(a13.count('大')))
        if str(ball_6_1) == str(a14.count('小')):
            print('第七位统计小---正确---' + str(a14.count('小')))
        else:
            print('第七位统计小---错误---' + str(a14.count('小')))
        if str(ball_7_0) == str(a15.count('大')):
            print('第八位统计大---正确---' + str(a15.count('大')))
        else:
            print('第八位统计大---错误---' + str(a15.count('大')))
        if str(ball_7_1) == str(a16.count('小')):
            print('第八位统计小---正确---' + str(a16.count('小')))
        else:
            print('第八位统计小---错误---' + str(a16.count('小')))

        if str(ball_8_0) == str(a17.count('大')):
            print('第九位统计大---正确---' + str(a17.count('大')))
        else:
            print('第九位统计大---错误---' + str(a17.count('大')))
        if str(ball_8_1) == str(a18.count('小')):
            print('第九位统计小---正确---' + str(a18.count('小')))
        else:
            print('第九位统计小---错误---' + str(a18.count('小')))
        if str(ball_9_0) == str(a19.count('大')):
            print('第十位统计大---正确---' + str(a19.count('大')))
        else:
            print('第十位统计大---错误---' + str(a19.count('大')))
        print(ball_9_1)
        print(str(a20.count('小')))
        if str(ball_9_1) == str(a20.count('小')):
            print('第十位统计小---正确---' + str(a20.count('小')))
        else:
            print('第十位统计小---错误---' + str(a20.count('小')))

    def lotteryhall_trend_double(self):
        # 走势图
        # 大小走势
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
        aaa = []
        print('统计中......')
        for i in range(100):
            try:
                # 期号
                datetime = self.base_driver.get_texts(self.config_dict_tmmcq['TREND_QH'], i+1)
                # print(datetime[:8])
                # print(time.strftime('%Y%m%d'))
                if datetime[:8] == time.strftime('%Y%m%d') or int(datetime[:2]) == 73:
                    # 开奖号码
                    # s00 = self.base_driver.get_texts(self.config_dict_tmmcq['LOTTERY_NUM'], i)
                    # 第一位~第十位
                    s01 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_0'], i+1)
                    s02 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_0_1'], i+1)
                    s03 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_0'], i+1)
                    s04 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_1_1'], i+1)
                    s05 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_0'], i+1)
                    s06 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_2_1'], i+1)
                    s07 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_0'], i+1)
                    s08 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_3_1'], i+1)
                    s09 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_0'], i+1)
                    s10 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_4_1'], i+1)
                    s11 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_0'], i+1)
                    s12 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_5_1'], i+1)
                    s13 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_6_0'], i+1)
                    s14 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_6_1'], i+1)
                    s15 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_7_0'], i+1)
                    s16 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_7_1'], i+1)
                    s17 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_8_0'], i+1)
                    s18 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_8_1'], i+1)
                    s19 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_9_0'], i+1)
                    s20 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_9_1'], i)

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
                    aaa = [s01, s02, s03, s04, s05, s06]
            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break

        print(a20)
        print('aaa   ' + str(aaa))
        # 号码分布
        ball_0_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 0)
        ball_0_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 1)
        ball_1_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 2)
        ball_1_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 3)
        ball_2_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 4)
        ball_2_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 5)
        ball_3_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 6)
        ball_3_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 7)
        ball_4_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 8)
        ball_4_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 9)
        ball_5_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 10)
        ball_5_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 11)
        ball_6_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 12)
        ball_6_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 13)
        ball_7_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 14)
        ball_7_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 15)
        ball_8_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 16)
        ball_8_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 17)
        ball_9_0 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 18)
        ball_9_1 = self.base_driver.get_texts(self.config_dict_tmmcq['DX_SIZE_SUM'], 19)

        ss = [ball_0_0, ball_0_1, ball_1_0, ball_1_1, ball_2_0, ball_2_1]
        print(ss)
        print('ball_0_0:   ' + str(ball_0_0))
        print('a00.count:  ' + str(a01.count('单')))
        if str(ball_0_0) == str(a01.count('单')):
            print('第一位统计单---正确---' + str(a01.count('单')))
        else:
            print('第一位统计单---错误---' + str(a01.count('单')))
        if str(ball_0_1) == str(a02.count('小')):
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
        if str(ball_5_0) == str(a11.count('单')):
            print('第六位统计单---正确---' + str(a11.count('单')))
        else:
            print('第六位统计单---错误---' + str(a11.count('单')))
        if str(ball_5_1) == str(a12.count('双')):
            print('第六位统计双---正确---' + str(a12.count('双')))
        else:
            print('第六位统计双---错误---' + str(a12.count('双')))
        if str(ball_6_0) == str(a13.count('单')):
            print('第七位统计单---正确---' + str(a13.count('单')))
        else:
            print('第七位统计单---错误---' + str(a13.count('单')))
        if str(ball_6_1) == str(a14.count('双')):
            print('第七位统计双---正确---' + str(a14.count('双')))
        else:
            print('第七位统计双---错误---' + str(a14.count('双')))
        if str(ball_7_0) == str(a15.count('单')):
            print('第八位统计单---正确---' + str(a15.count('单')))
        else:
            print('第八位统计单---错误---' + str(a15.count('单')))
        if str(ball_7_1) == str(a16.count('双')):
            print('第八位统计双---正确---' + str(a16.count('双')))
        else:
            print('第八位统计双---错误---' + str(a16.count('双')))

        if str(ball_8_0) == str(a17.count('单')):
            print('第九位统计单---正确---' + str(a17.count('单')))
        else:
            print('第九位统计单---错误---' + str(a17.count('单')))
        if str(ball_8_1) == str(a18.count('双')):
            print('第九位统计双---正确---' + str(a18.count('双')))
        else:
            print('第九位统计双---错误---' + str(a18.count('双')))
        if str(ball_9_0) == str(a19.count('单')):
            print('第十位统计单---正确---' + str(a19.count('单')))
        else:
            print('第十位统计单---错误---' + str(a19.count('单')))
        print(ball_9_1)
        print(str(a20.count('双')))
        if str(ball_9_1) == str(a20.count('双')):
            print('第十位统计双---正确---' + str(a20.count('双')))
        else:
            print('第十位统计双---错误---' + str(a20.count('双')))

    def plan_winkillnum_ball_00(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近100期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100次')
        self.base_driver.forced_wait(1)
        # 冠军杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '冠军')
        self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/冠军杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/冠军杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                # print(m0)
                f = open("/fusion/lottery_hall/pk10/冠军杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a0) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a0) or (c0 == '杀错' and b0[2:] == a0):
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b0) + str(c0) + '  冠军正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b0) + str(c0) + '--冠军错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a0) or (c1 == '杀错' and b1[2:] == a0):
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b1) + str(c1) + '  冠军正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b1) + str(c1) + '--冠军错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a0) or (c2 == '杀错' and b2[2:] == a0):
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b2) + str(c2) + '  冠军正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b2) + str(c2) + '--冠军错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a0) or (c3 == '杀错' and b3[2:] == a0):
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b3) + str(c3) + '  冠军正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b3) + str(c3) + '--冠军错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a0) or (c4 == '杀错' and b4[2:] == a0):
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b4) + str(c4) + '  冠军正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--冠军：' + str(a0) + '  ' + str(b4) + str(c4) + '--冠军错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号冠军杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_01(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100次')
        self.base_driver.forced_wait(1)
        # 亚军杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '亚军')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/亚军杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/亚军杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/亚军杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a1) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a1) or (c0 == '杀错' and b0[2:] == a1):
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b0) + str(c0) + '  亚军正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b0) + str(c0) + '--亚军错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a1) or (c1 == '杀错' and b1[2:] == a1):
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b1) + str(c1) + '  亚军正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b1) + str(c1) + '--亚军错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a1) or (c2 == '杀错' and b2[2:] == a1):
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b2) + str(c2) + '  亚军正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b2) + str(c2) + '--亚军错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a1) or (c3 == '杀错' and b3[2:] == a1):
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b3) + str(c3) + '  亚军正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b3) + str(c3) + '--亚军错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a1) or (c4 == '杀错' and b4[2:] == a1):
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b4) + str(c4) + '  亚军正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--亚军：' + str(a1) + '  ' + str(b4) + str(c4) + '--亚军错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号亚军杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_02(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100次')
        self.base_driver.forced_wait(1)
        # 第三球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第三球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第三球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第三球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第三球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a2) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a2) or (c0 == '杀错' and b0[2:] == a2):
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b0) + str(c0) + '  第三球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b0) + str(c0) + '--第三球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a2) or (c1 == '杀错' and b1[2:] == a2):
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b1) + str(c1) + '  第三球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b1) + str(c1) + '--第三球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a2) or (c2 == '杀错' and b2[2:] == a2):
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b2) + str(c2) + '  第三球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b2) + str(c2) + '--第三球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a2) or (c3 == '杀错' and b3[2:] == a2):
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b3) + str(c3) + '  第三球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b3) + str(c3) + '--第三球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a2) or (c4 == '杀错' and b4[2:] == a2):
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b4) + str(c4) + '  第三球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第三球：' + str(a2) + '  ' + str(b4) + str(c4) + '--第三球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第三球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_03(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第四球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第四球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第四球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第四球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第四球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a3) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a3) or (c0 == '杀错' and b0[2:] == a3):
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b0) + str(c0) + '  第四球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b0) + str(c0) + '--第四球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a3) or (c1 == '杀错' and b1[2:] == a3):
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b1) + str(c1) + '  第四球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b1) + str(c1) + '--第四球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a3) or (c2 == '杀错' and b2[2:] == a3):
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b2) + str(c2) + '  第四球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b2) + str(c2) + '--第四球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a3) or (c3 == '杀错' and b3[2:] == a3):
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b3) + str(c3) + '  第四球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b3) + str(c3) + '--第四球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a3) or (c4 == '杀错' and b4[2:] == a3):
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b4) + str(c4) + '  第四球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第四球：' + str(a3) + '  ' + str(b4) + str(c4) + '--第四球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第四球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_04(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第五球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第五球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第五球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第五球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第五球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a4) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a4) or (c0 == '杀错' and b0[2:] == a4):
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b0) + str(c0) + '  第五球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b0) + str(c0) + '--第五球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a4) or (c1 == '杀错' and b1[2:] == a4):
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b1) + str(c1) + '  第五球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b1) + str(c1) + '--第五球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a4) or (c2 == '杀错' and b2[2:] == a4):
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b2) + str(c2) + '  第五球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b2) + str(c2) + '--第五球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a4) or (c3 == '杀错' and b3[2:] == a4):
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b3) + str(c3) + '  第五球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b3) + str(c3) + '--第五球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a4) or (c4 == '杀错' and b4[2:] == a4):
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b4) + str(c4) + '  第五球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第五球：' + str(a4) + '  ' + str(b4) + str(c4) + '--第五球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第五球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_05(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第六球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第六球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第六球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第六球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第六球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a5) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a5) or (c0 == '杀错' and b0[2:] == a5):
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b0) + str(c0) + '  第六球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b0) + str(c0) + '--第六球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a5) or (c1 == '杀错' and b1[2:] == a5):
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b1) + str(c1) + '  第六球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b1) + str(c1) + '--第六球号错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a5) or (c2 == '杀错' and b2[2:] == a5):
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b2) + str(c2) + '  第六球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b2) + str(c2) + '--第六球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a5) or (c3 == '杀错' and b3[2:] == a5):
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b3) + str(c3) + '  第六球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b3) + str(c3) + '--第六球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a5) or (c4 == '杀错' and b4[2:] == a5):
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b4) + str(c4) + '  第六球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第六球：' + str(a5) + '  ' + str(b4) + str(c4) + '--第六球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第六球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_06(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第七球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第七球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第七球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第七球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第七球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a6) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a6) or (c0 == '杀错' and b0[2:] == a6):
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b0) + str(c0) + '  第七球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b0) + str(c0) + '--第七球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a6) or (c1 == '杀错' and b1[2:] == a6):
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b1) + str(c1) + '  第七球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b1) + str(c1) + '--第七球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a6) or (c2 == '杀错' and b2[2:] == a6):
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b2) + str(c2) + '  第七球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b2) + str(c2) + '--第七球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a6) or (c3 == '杀错' and b3[2:] == a6):
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b3) + str(c3) + '  第七球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b3) + str(c3) + '--第七球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a6) or (c4 == '杀错' and b4[2:] == a6):
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b4) + str(c4) + '  第七球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第七球：' + str(a6) + '  ' + str(b4) + str(c4) + '--第七球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第七球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_07(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第七球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第八球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第八球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第八球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第八球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a7) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a7) or (c0 == '杀错' and b0[2:] == a7):
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b0) + str(c0) + '  第八球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b0) + str(c0) + '--第八球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a7) or (c1 == '杀错' and b1[2:] == a7):
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b1) + str(c1) + '  第八球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b1) + str(c1) + '--第八球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a7) or (c2 == '杀错' and b2[2:] == a7):
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b2) + str(c2) + '  第八球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b2) + str(c2) + '--第八球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a7) or (c3 == '杀错' and b3[2:] == a7):
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b3) + str(c3) + '  第八球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b3) + str(c3) + '--第八球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a7) or (c4 == '杀错' and b4[2:] == a7):
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b4) + str(c4) + '  第八球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第八球：' + str(a7) + '  ' + str(b4) + str(c4) + '--第八球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第八球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_08(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第九球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第九球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第九球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第九球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第九球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a8) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a8) or (c0 == '杀错' and b0[2:] == a8):
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b0) + str(c0) + '  第九球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b0) + str(c0) + '--第九球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a8) or (c1 == '杀错' and b1[2:] == a8):
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b1) + str(c1) + '  第九球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b1) + str(c1) + '--第九球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a8) or (c2 == '杀错' and b2[2:] == a8):
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b2) + str(c2) + '  第九球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b2) + str(c2) + '--第九球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a8) or (c3 == '杀错' and b3[2:] == a8):
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b3) + str(c3) + '  第九球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b3) + str(c3) + '--第九球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a8) or (c4 == '杀错' and b4[2:] == a8):
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b4) + str(c4) + '  第九球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第九球：' + str(a8) + '  ' + str(b4) + str(c4) + '--第九球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第九球杀号运行' + str(i) + '行')
                break

    def plan_winkillnum_ball_09(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 第十球杀号
        self.base_driver.clicks_by_text(self.config_dict_tmmcq['NUMKILLNUM'], '第十球')
        # self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pk10/第十球杀号.txt"):
            os.remove("/fusion/lottery_hall/pk10/第十球杀号.txt")
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
                a5 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM05'], i)
                a6 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM06'], i)
                a7 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM07'], i)
                a8 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM08'], i)
                a9 = self.base_driver.get_texts(self.config_dict_tmmcq['KJNUM09'], i)
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

                m0 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
                f = open("/fusion/lottery_hall/pk10/第十球杀号.txt", 'a', encoding='utf-8')
                f.write(str(s0) + "\t" + str(m0) + "\t" + str(a9) + "\t" + str(b0) + str(c0) + "\t" + str(b1) +
                        str(c1) + "\t" + str(b2) + str(c2) + "\t" + str(b3) + str(c3) + "\t" + str(b4) + str(c4) + "\n")
                f.close()

                if (c0 == '杀对' and b0[2:] != a9) or (c0 == '杀错' and b0[2:] == a9):
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b0) + str(c0) + '  第十球正确' + str(b0))
                else:
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b0) + str(c0) + '--第十球错误' + str(b0))
                if (c1 == '杀对' and b1[2:] != a9) or (c1 == '杀错' and b1[2:] == a9):
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b1) + str(c1) + '  第十球正确' + str(b1))
                else:
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b1) + str(c1) + '--第十球错误' + str(b1))
                if (c2 == '杀对' and b2[2:] != a9) or (c2 == '杀错' and b2[2:] == a9):
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b2) + str(c2) + '  第十球正确' + str(b2))
                else:
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b2) + str(c2) + '--第十球错误' + str(b2))
                if (c3 == '杀对' and b3[2:] != a9) or (c3 == '杀错' and b3[2:] == a9):
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b3) + str(c3) + '  第十球正确' + str(b3))
                else:
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b3) + str(c3) + '--第十球错误' + str(b3))
                if (c4 == '杀对' and b4[2:] != a9) or (c4 == '杀错' and b4[2:] == a9):
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b4) + str(c4) + '  第十球正确' + str(b4))
                else:
                    print('期数:' + str(s0) + '--第十球：' + str(a9) + '  ' + str(b4) + str(c4) + '--第十球错误' + str(b4))
            except Exception as e:
                print(e)
                print('稳赢杀号第十球杀号运行' + str(i) + '行')
                break


