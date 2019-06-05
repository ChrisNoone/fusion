import csv
import unittest


from common.box import TestCase, BoxDriver, Browser
from marksix.fast3_mm import Fast3Mm
from marksix.lottery import Lottery
from marksix.marksix_minute import MinuteMarkSix
from marksix.pcdd_lucky28 import PcddLucky28


class Fast3MmTest(TestCase):
    # 分分快3
    # 分分快3
    # 分分快3
    # 分分快3
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        # self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_success_01(self):
        # 下注
        self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/29')
        # print("成功打开网址")
        self.base_driver.forced_wait(40)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        ''' 下注 '''
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.time()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.fast3mm = Fast3Mm(self.base_driver)

                # 二同号单选---标准选号
                self.fast3mm.num_s2_ds(row)
                self.fast3mm.radoms(row)
                print('二同号单选---标准选号')
                # ---------------------------------------------------------------------
                # 二同号单选---手动选号---输入框
                self.fast3mm.num_s2_sd(row)
                self.fast3mm.radoms(row)
                print('二同号单选---手动选号---输入框')
                # ---------------------------------------------------------------------
                # 二同号复选---二同号复选
                self.fast3mm.num_s2_fx(row)
                self.fast3mm.radoms(row)
                print('二同号复选---二同号复选')

                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # 二不同号---标准选号
                self.fast3mm.num_n2(row)
                self.fast3mm.radoms(row)
                print('二不同号---标准选号')
                #
                # 二不同号---手动选号
                self.fast3mm.num_n2_sd(row)
                self.fast3mm.radoms(row)
                print('二不同号---手动选号')
                #
                # 二不同号---胆拖选号
                self.fast3mm.num_n2_dt(row)
                self.fast3mm.radoms(row)
                print('二不同号---胆拖选号')
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                
                # 三不同号---标准选号
                self.fast3mm.num3_n3_bz(row)
                self.fast3mm.radoms(row)
                print('三不同号---标准选号')

                # 三不同号---手动选号---输入框
                self.fast3mm.num3_n3_sd(row)
                self.fast3mm.radoms(row)
                print('三不同号---手动选号---输入框')

                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # 三同号--三同号单选
                self.fast3mm.num_s3_ds(row)
                self.fast3mm.radoms(row)
                print('三同号--三同号单选')

                # 三同号--三同号通选
                self.fast3mm.num_s3_ts(row)
                self.fast3mm.radoms(row)
                print('三同号--三同号通选')

                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------

                # 三连号
                self.fast3mm.num_s3_l(row)
                self.fast3mm.radoms(row)
                print('三连号')
                #
                # 和值--大小单双
                self.fast3mm.num_hh_dxds(row)
                self.fast3mm.radoms(row)
                print('和值--大小单双')

                # 和值--大小单双
                self.fast3mm.num_hh_hezhi(row)
                self.fast3mm.radoms(row)
                print('和值--大小单双--和值')

                # self.base_driver.forced_wait(10)
                # get_tips = self.fast3mm.get_tips()
                # print('获取的文字是：' + get_tips)
                # # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')
'''
    def test_fail_01(self):
        # 下注
        self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/29')
        # print("成功打开网址")
        self.base_driver.forced_wait(3)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注 
        # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.time()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.fast3mm = Fast3Mm(self.base_driver)

                # 二同号单选---标准选号
                self.fast3mm.num_s2_ds_error(row)
                print('二同号单选---标准选号')

                # ---------------------------------------------------------------------
                # 二同号单选---手动选号---输入框
                self.fast3mm.num_s2_sd_error(row)
                
                print('二同号单选---手动选号---输入框')
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                
                # # 二不同号---标准选号
                self.fast3mm.num_n2_error(row)
                print('二不同号---胆拖选号')

                # 二不同号---手动选号
                self.fast3mm.num_s2_sd_error(row)
                print('二不同号---手动选号')
                
                # 二不同号---胆拖选号
                self.fast3mm.num_n2_dt_error(row)
                print('二不同号---胆拖选号')
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                
                # 三不同号---标准选号
                self.fast3mm.num3_n3_bz_error(row)
                print('三不同号---标准选号')
                
                # 三不同号---手动选号---输入框
                self.fast3mm.num3_n3_sd_error(row)
                print('三不同号---手动选号---输入框')

                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------
                # ---------------------------------------------------------------------

                # self.base_driver.forced_wait(10)
                # get_tips = self.fast3mm.get_tips()
                # print('获取的文字是：' + get_tips)
                # # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')

'''
if __name__ == '__main__':

    unittest.main()
