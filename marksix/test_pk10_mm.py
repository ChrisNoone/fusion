import csv
import unittest


from common.box import TestCase, BoxDriver, Browser
from marksix.lottery import Lottery
from marksix.marksix_minute import MinuteMarkSix
from marksix.pcdd_lucky28 import PcddLucky28
from marksix.pk10_mm import PK10Mm


class PK10MmTest(TestCase):
    # 分分pk10
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
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/25')

        self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/25')
        # # print("成功打开网址")
        self.base_driver.forced_wait(40)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # # 登陆
        # self.lottery.login()
        # # # 点击六合彩
        # self.lottery.pk10_mm()
        # 打开csv文件
        csv_file = open('/fusion/csv/pk10_mm.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.pk10mm = PK10Mm(self.base_driver)
                print('第一层表格' + row['msg'])
                '''
                # 前一
                self.pk10mm.qian_1(row)
                self.pk10mm.radoms(row)
                print('定位胆')

                # 前二---复式
                self.pk10mm.qian_2_fs(row)
                self.pk10mm.radoms(row)
                print('前二---复式')

                # 前二---单式
                self.pk10mm.qian_2_ds(row)
                self.pk10mm.radoms(row)
                self.pk10mm.surebet()
                print('前二---单式')

                # 前三---单式
                self.pk10mm.qian_3_fs(row)
                self.pk10mm.radoms(row)
                print('前二---单式')

                # 定位胆---定位胆第1-5名
                self.pk10mm.dwd_1_5(row)
                self.pk10mm.radoms(row)

                print('定位胆---定位胆第1-5名')

                # 定位胆---定位胆第6-10名
                self.pk10mm.dwd_6_10(row)
                self.pk10mm.radoms(row)
                print('定位胆---定位胆第6-10名')

                # 定位胆---定位胆第1-10名
                self.pk10mm.dwd_1_10(row)
                self.pk10mm.radoms(row)
                print('定位胆---定位胆第1-10名')
                '''
                # 冠亚和
                self.pk10mm.gjh(row)
                self.pk10mm.radoms(row)
                print('冠亚和---和值')

                # 龙虎---龙虎---冠军
                self.pk10mm.longhu01(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('龙虎---龙虎---冠军')

                # 龙虎---龙虎---季军
                self.pk10mm.longhu02(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('龙虎---龙虎---季军')

                # 龙虎---龙虎---亚军
                self.pk10mm.longhu03(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('龙虎---龙虎---亚军')

                # 龙虎---龙虎---第四名
                self.pk10mm.longhu04(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('龙虎---龙虎---第四名')

                # 龙虎---龙虎---第四名
                self.pk10mm.longhu05(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('龙虎---龙虎---第五名')

                # 五行---冠军---金木水火土
                self.pk10mm.wx_g(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('五行---冠军---金木水火土')

                # 五行---亚军---金木水火土
                self.pk10mm.wx_y(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('五行---亚军---金木水火土')

                # 五行---季军---金木水火土
                self.pk10mm.wx_j(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('五行---季军---金木水火土')

                # 大小单双---大小---冠军
                self.pk10mm.dxds_dx_g(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---大小---冠军')

                # 大小单双---大小---亚军
                self.pk10mm.dxds_dx_y(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---大小---亚军')

                # 大小单双---大小---季军
                self.pk10mm.dxds_dx_j(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---大小---季军')

                # 大小单双---单双---冠军
                self.pk10mm.dxds_ds_g(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---单双---冠军')

                # 大小单双---单双---亚军
                self.pk10mm.dxds_ds_y(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---单双---亚军')

                # 大小单双---单双---季军
                self.pk10mm.dxds_ds_j(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---单双---季军')

                # 大小单双---冠军和
                self.pk10mm.dxds_ds_j(row)
                self.pk10mm.radoms(row)
                # self.pk10mm.surebet()
                print('大小单双---冠军和')

                # self.base_driver.forced_wait(10)
                # get_tips = self.pk10mm.get_tips()
                # print('获取的文字是：' + get_tips)
                # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        # self.logger.info('关闭CSV文件')
'''
    def test_fail_01(self):
        # 下注
        self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/25')
        # # print("成功打开网址")
        self.base_driver.forced_wait(4)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        #  下注
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # # 登陆
        # self.lottery.login()
        # # # 点击六合彩
        # self.lottery.pk10_mm()
        # 打开csv文件
        csv_file = open('/fusion/csv/pk10_mm.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.pk10mm = PK10Mm(self.base_driver)

                # 前二---复式
                self.pk10mm.qian_2_fs_error(row)
                print('前二---复式')

                # 前二---单式
                self.pk10mm.qian_2_ds_error(row)
                print('前二---单式')

                # 前三---复式
                self.pk10mm.qian_3_fs_error(row)
                print('前三---复式')

                # 前三---单式
                self.pk10mm.qian_3_ds_error(row)
                print('前三---单式')

                # ----------------------------------------------------------------------------
                # ----------------------------------------------------------------------------

                # self.base_driver.forced_wait(10)
                # get_tips = self.pk10mm.get_tips()
                # print('获取的文字是：' + get_tips)
                # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        # self.logger.info('关闭CSV文件')

'''
if __name__ == '__main__':

    unittest.main()

