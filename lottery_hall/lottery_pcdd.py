import os
import time
from common.box import BasePage, YamlHelper


class LotteryPCDD(BasePage):

    config_dict_pcdd = YamlHelper().get_config_dict('/fusion/lottery_hall/yaml/lottery_pcdd.yaml')['PCDD_LUCKY']

    def today_lottery_rules(self):
        # 今日开奖---规则校对
        self.base_driver.clicks_by_text(self.config_dict_pcdd['MENU'], '今日开奖')
        for i in range(100):
            try:
                # 时间
                datetime = self.base_driver.get_texts(self.config_dict_pcdd['TIME_NUM'], i)
                qishu = self.base_driver.get_texts(self.config_dict_pcdd['PERIODS_NUM'], i)
                # print(time.strftime('%Y-%m-%d'))
                if datetime[:10] == time.strftime('%Y-%m-%d'):
                    # 总和
                    s0 = self.base_driver.get_texts(self.config_dict_pcdd['SUM_SUM'], i)
                    # 总和大小
                    s1 = self.base_driver.get_texts(self.config_dict_pcdd['SUM_DX_NUM'], i)
                    # 总和单双
                    s2 = self.base_driver.get_texts(self.config_dict_pcdd['SUM_DS_NUM'], i)

                    # 开奖号码1-5
                    s3 = self.base_driver.get_texts(self.config_dict_pcdd['LOTTERY_NUM01'], i)
                    s4 = self.base_driver.get_texts(self.config_dict_pcdd['LOTTERY_NUM02'], i)
                    s5 = self.base_driver.get_texts(self.config_dict_pcdd['LOTTERY_NUM03'], i)
                    # print(s0)
                    # print(str(s3) + str(s4) + str(s5))
                    m0 = [int(s3), int(s4), int(s5)]
                   # print(sum(m0))
                    if str(s0) == str(sum(m0)):
                        pass
                        if sum(m0) > 13:
                            if s1 == '大':
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和大正确')
                            else:
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和大错误')
                            if sum(m0) % 2 == 0:
                                if s2 == '双':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双错误')
                            if sum(m0) % 2 == 1:
                                if s2 == '单':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单错误')
                        if sum(m0) < 14:
                            if s1 == '小':
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和小正确')
                            else:
                                print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和小错误')
                            if sum(m0) % 2 == 0:
                                if s2 == '双':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和双错误')
                            if sum(m0) % 2 == 1:
                                if s2 == '单':
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单正确')
                                else:
                                    print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和单错误')

                    else:
                        print('期数' + str(qishu) + '  ' + str(sum(m0)) + '  总和错误')

            except Exception as e:
                print(e)
                print('运行的数据有:' + str(i) + '行')
                break



    def plan_winkillnum_w(self):
        # 站长推荐
        # 稳赢杀号
        self.base_driver.clicks_by_text(self.config_dict_pcdd['WYKILLNUM'], '稳赢杀号')
        self.base_driver.forced_wait(1)
        # 最近10期
        self.base_driver.clicks_by_text(self.config_dict_pcdd['RECNET_PERIOD'], '最近100期')
        self.base_driver.forced_wait(1)
        # 万位杀号
        self.base_driver.clicks_by_text(self.config_dict_pcdd['NUMKILLNUM'], '和值杀号')
        self.base_driver.forced_wait(10)
        if os.path.exists("/fusion/lottery_hall/pcdd/和值杀号.txt"):
            os.remove("/fusion/lottery_hall/pddd/和值杀号.txt")
        else:
            pass
        for i in range(100):
            try:
                # 开奖期数
                s0 = self.base_driver.get_texts(self.config_dict_pcdd['WYQISHU'], i+1)


                # 开奖号码
                # s1 = self.base_driver.get_texts(self.config_dict_pcdd['KJNUM'], i)

                # 开奖号码1-5
                a0 = self.base_driver.get_texts(self.config_dict_pcdd['KJNUM00'], i)
                a1 = self.base_driver.get_texts(self.config_dict_pcdd['KJNUM01'], i+1)
                a2 = self.base_driver.get_texts(self.config_dict_pcdd['KJNUM02'], i+1)
                a3 = self.base_driver.get_texts(self.config_dict_pcdd['KJNUM03'], i+1)
                a4 = self.base_driver.get_texts(self.config_dict_pcdd['KJNUM04'], i+1)
                # 杀N
                b0 = self.base_driver.get_texts(self.config_dict_pcdd['KILLNUM00'], i+1)
                b1 = self.base_driver.get_texts(self.config_dict_pcdd['KILLNUM01'], i+1)
                b2 = self.base_driver.get_texts(self.config_dict_pcdd['KILLNUM02'], i+1)
                b3 = self.base_driver.get_texts(self.config_dict_pcdd['KILLNUM03'], i+1)
                b4 = self.base_driver.get_texts(self.config_dict_pcdd['KILLNUM04'], i+1)

                # 杀对--错
                c0 = self.base_driver.get_texts(self.config_dict_pcdd['ZHANJINUM00'], i+1)
                c1 = self.base_driver.get_texts(self.config_dict_pcdd['ZHANJINUM01'], i+1)
                c2 = self.base_driver.get_texts(self.config_dict_pcdd['ZHANJINUM02'], i+1)
                c3 = self.base_driver.get_texts(self.config_dict_pcdd['ZHANJINUM03'], i+1)
                c4 = self.base_driver.get_texts(self.config_dict_pcdd['ZHANJINUM04'], i+1)

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




