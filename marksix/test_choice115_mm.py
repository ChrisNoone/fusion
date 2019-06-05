import csv
import unittest


from common.box import TestCase, BoxDriver, Browser
from marksix.choice11_5_mm import Choice11_5_Mm
from marksix.lottery import Lottery
from marksix.marksix_minute import MinuteMarkSix
from marksix.time_mm import TimeMinute


class Choice115MnTest(TestCase):
    # 分分11选5
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        # self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        #self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/24')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_success_01(self):
        # 下注
        self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/31')

        # print("成功打开网址")
        self.base_driver.forced_wait(50)
        # 滑动浏览器右边滑动条
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.base_driver.execute_js(js)
        # # 下注
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.choice11_5()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.chmm = Choice11_5_Mm(self.base_driver)
                # ---------------------------------------
                # ---------------------------------------
                # ---------------------------------------
                # 三码
                # 三码---前三直选---复式
                self.chmm.ch11_5_q3zhixfs(row)
                self.chmm.radoms(row)
                print('三码---前三直选---复式')

                # 三码
                # 三码---前三直选---单式
                self.chmm.ch11_5_q3zhixds(row)
                self.chmm.radoms(row)
                print('三码---前三直选---单式')

                # 三码
                # 三码---前三组选---复式
                self.chmm.ch11_5_q3zuxfs(row)
                self.chmm.radoms(row)
                print('三码---前三组选---复式')

                # 三码
                # 三码---前三组选---单式
                self.chmm.ch11_5_q3zuxds(row)
                self.chmm.radoms(row)
                print('二星---前三组选---单式')

                # ---------------------------------------
                # ---------------------------------------
                # ---------------------------------------
                # 三码
                # 三码---前二直选---复式
                self.chmm.ch11_5_q2zhixfs(row)
                self.chmm.radoms(row)
                print('三码---前二直选---复式')

                # 三码
                # 三码---前二直选---单式
                self.chmm.ch11_5_q2zhixds(row)
                self.chmm.radoms(row)
                print('三码---前二直选---单式')

                # 三码
                # 三码---前二组选---复式
                self.chmm.ch11_5_q2zuxfs(row)
                self.chmm.radoms(row)
                print('三码---前二组选---复式')

                # 三码
                # 三码---前二组选---单式
                self.chmm.ch11_5_q2zuxds(row)
                self.chmm.radoms(row)
                print('二星---前二组选---单式')

                # ---------------------------------------
                # ---------------------------------------
                # ---------------------------------------

                # 不定胆
                # 不定胆---不定胆---前三位
                self.chmm.ch11_5_bddan(row)
                self.chmm.radoms(row)
                print('不定胆---不定胆---前三位')

                # 定位胆
                # 定位胆---定位胆---定位胆
                self.chmm.ch11_5_dwd(row)
                self.chmm.radoms(row)
                print('定位胆---定位胆---定位胆')

                # 任选
                # 任选---复式---一中一
                self.chmm.ch11_5_rxfs_1z1(row)
                self.chmm.radoms(row)
                print('任选---复式---一中一')

                # 任选
                # 任选---复式---二中二
                self.chmm.ch11_5_rxfs_2z2(row)
                self.chmm.radoms(row)
                print('任选---复式---二中二')

                # 任选
                # 任选---复式---三中三
                self.chmm.ch11_5_rxfs_3z3(row)
                self.chmm.radoms(row)
                print('任选---复式---三中三')

                # 任选
                # 任选---复式---四中四
                self.chmm.ch11_5_rxfs_4z4(row)
                self.chmm.radoms(row)
                print('任选---复式---四中四')

                # 任选
                # 任选---复式---五中五
                self.chmm.ch11_5_rxfs_5z5(row)
                self.chmm.radoms(row)
                print('任选---复式---五中五')

                # 任选
                # 任选---复式---六中五
                self.chmm.ch11_5_rxfs_6z5(row)
                self.chmm.radoms(row)
                print('任选---复式---六中五')

                # 任选
                # 任选---复式---七中五
                self.chmm.ch11_5_rxfs_7z5(row)
                self.chmm.radoms(row)
                print('任选---复式---七中五')

                # 任选
                # 任选---复式---八中五
                self.chmm.ch11_5_rxfs_8z5(row)
                self.chmm.radoms(row)
                print('任选---复式---八中五')

                # 任选
                # 任选---单式---一中一
                self.chmm.ch11_5_rxds_1z1(row)
                self.chmm.radoms(row)
                print('任选---单式---一中一')

                # 任选
                # 任选---单式---二中二
                self.chmm.ch11_5_rxds_2z2(row)
                self.chmm.radoms(row)
                print('任选---单式---二中二')

                # 任选
                # 任选---单式---三中三
                self.chmm.ch11_5_rxds_3z3(row)
                self.chmm.radoms(row)
                print('任选---单式---三中三')

                # 任选
                # 任选---单式---四中四
                self.chmm.ch11_5_rxds_4z4(row)
                self.chmm.radoms(row)
                print('任选---单式---四中四')

                # 任选
                # 任选---单式---五中五
                self.chmm.ch11_5_rxds_5z5(row)
                self.chmm.radoms(row)
                print('任选---单式---五中五')

                # 任选
                # 任选---单式---六中五
                self.chmm.ch11_5_rxds_6z5(row)
                self.chmm.radoms(row)
                print('任选---单式---六中五')

                # 任选
                # 任选---单式---七中五
                self.chmm.ch11_5_rxds_7z5(row)
                self.chmm.radoms(row)
                print('任选---单式---七中五')

                # 任选
                # 任选---单式---八中五
                self.chmm.ch11_5_rxds_8z5(row)
                self.chmm.radoms(row)
                print('任选---单式---八中五')

                # # 三星
                # # 三星---后三直选---复式
                # self.timemm.choice_10()
                # self.timemm.addnote_button()
                # self.timemm.radoms(row)
                # self.timemm.surebet()
                # print('三星---后三直选---复式')

                # self.base_driver.forced_wait(10)
                # get_tips = self.timemm.get_tips()
                # print('获取的文字是：' + get_tips)
                # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')

    # 测试用例
'''
    def test_fail_01(self):
        # 下注
        self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/31')
        # print("成功打开网址")
        self.base_driver.forced_wait(3)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.time()
        # # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.chmm = Choice11_5_Mm(self.base_driver)
                # ---------------------------------------
                # ---------------------------------------
                # ---------------------------------------
                # 三码
                # 三码---前三直选---复式
                self.chmm.ch11_5_q3zhixfs_error(row)
                print('三码---前三直选---复式')
                
                # 三码
                # 三码---前三直选---单式
                self.chmm.ch11_5_q3zhixds_error(row)
                print('三码---前三直选---单式')

                # 三码
                # 三码---前三组选---复式
                self.chmm.ch11_5_q3zuxfs_error(row)
                print('三码---前三组选---复式')

                # 三码
                # 三码---前三组选---单式
                self.chmm.ch11_5_q3zuxds_error(row)
                print('二星---前三组选---单式')

                # ---------------------------------------
                # ---------------------------------------
                # ---------------------------------------

                # 二码
                # 二码---前二直选---复式
                self.chmm.ch11_5_q2zhixfs_error(row)
                print('三码---前二直选---复式')

                # 二码
                # 二码---前二直选---单式
                self.chmm.ch11_5_q2zhixds_error(row)
                print('三码---前二直选---单式')

                # 二码
                # 二码---前二组选---复式
                self.chmm.ch11_5_q2zuxfs_error(row)
                self.chmm.radoms(row)
                print('三码---前二组选---复式')

                # 二码
                # 二码---前二组选---单式
                self.chmm.ch11_5_q2zuxds_error(row)
                self.chmm.radoms(row)
                print('二星---前二组选---单式')

                # ---------------------------------------
                # ---------------------------------------
                # ---------------------------------------

                # 任选
                # 任选---复式---二中二
                self.chmm.ch11_5_rxfs_2z2_error(row)
                print('任选---复式---二中二')

                # 任选
                # 任选---复式---三中三
                self.chmm.ch11_5_rxfs_3z3_error(row)
                self.chmm.radoms(row)
                print('任选---复式---三中三')

                # 任选
                # 任选---复式---四中四
                self.chmm.ch11_5_rxfs_4z4_error(row)
                self.chmm.radoms(row)
                print('任选---复式---四中四')

                # 任选
                # 任选---复式---五中五
                self.chmm.ch11_5_rxfs_5z5_error(row)
                self.chmm.radoms(row)
                print('任选---复式---五中五')

                # 任选
                # 任选---复式---六中五
                self.chmm.ch11_5_rxfs_6z5_error(row)
                print('任选---复式---六中五')

                # 任选
                # 任选---复式---七中五
                self.chmm.ch11_5_rxfs_7z5_error(row)
                print('任选---复式---七中五')

                # 任选
                # 任选---复式---八中五
                self.chmm.ch11_5_rxfs_8z5_error(row)
                print('任选---复式---八中五')

                # 任选
                # 任选---单式---一中一
                self.chmm.ch11_5_rxds_1z1_error(row)
                print('任选---单式---一中一')
                #
                # 任选
                # 任选---单式---二中二
                self.chmm.ch11_5_rxds_2z2_error(row)
                print('任选---单式---二中二')

                # 任选
                # 任选---单式---三中三
                self.chmm.ch11_5_rxds_3z3_error(row)
                print('任选---单式---三中三')

                # 任选
                # 任选---单式---四中四
                self.chmm.ch11_5_rxds_4z4_error(row)
                print('任选---单式---四中四')

                # 任选
                # 任选---单式---五中五
                self.chmm.ch11_5_rxds_5z5_error(row)
                print('任选---单式---五中五')
                #
                # 任选
                # 任选---单式---六中五
                self.chmm.ch11_5_rxds_6z5_error(row)
                print('任选---单式---六中五')
                #
                # 任选
                # 任选---单式---七中五
                self.chmm.ch11_5_rxds_7z5(row)
                self.chmm.radoms(row)
                print('任选---单式---七中五')

                # 任选
                # 任选---单式---七中五
                self.chmm.ch11_5_rxds_7z5_error(row)
                print('任选---单式---七中五')

                # 任选
                # 任选---单式---八中五
                self.chmm.ch11_5_rxds_8z5(row)
                self.chmm.radoms(row)
                print('任选---单式---八中五')

                # 任选
                # 任选---单式---八中五
                self.chmm.ch11_5_rxds_8z5_error(row)
                print('任选---单式---八中五')
        
        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')
'''

if __name__ == '__main__':

    unittest.main()
