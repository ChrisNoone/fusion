import csv
import unittest


from common.box import TestCase, BoxDriver, Browser
from marksix.lottery import Lottery
from marksix.lowfrequency_speed3d import LowfSpeed3D
from marksix.marksix_minute import MinuteMarkSix
from marksix.time_mm import TimeMinute


class Speed3DTest(TestCase):
    # 极速3d
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        #self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

    # 测试用例
    def test_success_01(self):
        # 下注
        self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/30')
        # print("成功打开网址")
        self.base_driver.forced_wait(60)
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
                self.timemm = LowfSpeed3D(self.base_driver)
                # ---------------------------------------
                # 三码
                # 三码---直选---复式
                self.timemm.sp3_3_zhxfs(row)
                self.timemm.radoms(row)
                print('三码---直选---复式')

                # 三码
                # 三码---直选---单式
                self.timemm.sp3_3_zhxds(row)
                self.timemm.radoms(row)
                print('三码---直选---单式')

                # 三码
                # 三码---直选---直选和值
                self.timemm.sp3_3_zhxzxhezhi(row)
                self.timemm.radoms(row)
                print('三码---直选---直选和值')

                # 三码
                # 三码---组选---组三
                self.timemm.sp3_3_zuxzu3(row)
                self.timemm.radoms(row)
                print('三码---组选---组三')

                # 三码
                # 三码---组选---组六
                self.timemm.sp3_3_zuxzu6(row)
                self.timemm.radoms(row)
                print('三码---组选---组六')

                # 三码
                # 三码---组选---混合组选
                self.timemm.sp3_3_zuxhhzx(row)
                self.timemm.radoms(row)
                print('三码---组选---混合组选')
                # ---------------------------------------------------
                # ---------------------------------------------------
                # ---------------------------------------------------
                # ---------------------------------------------------

                # 二码
                # 二码---后二码直选---复式
                self.timemm.sp3_2_h2zhixfs(row)
                self.timemm.radoms(row)
                print('二码---后二码直选---复式')

                # 二码
                # 二码---后二码直选---单式
                self.timemm.sp3_2_h2zhixds(row)
                self.timemm.radoms(row)
                print('二码---后二码直选---单式')

                # 二码
                # 二码---后二码直选---直选和值
                self.timemm.sp3_2_h2zhixzhixhzhi(row)
                self.timemm.radoms(row)
                print('二码---后二码直选---直选和值')

                # 二码
                # 二码---后二码组选---复式
                self.timemm.sp3_2_h2zuxfs(row)
                self.timemm.radoms(row)
                print('二码---后二码组选---复式')

                # 二码
                # 二码---后二码组选---单式
                self.timemm.sp3_2_h2zuxds(row)
                self.timemm.radoms(row)
                print('二码---后二码组选---单式')

                # ---------------------------------------------------
                # ---------------------------------------------------
                # ---------------------------------------------------
                # ---------------------------------------------------
                #
                # 二码
                # 二码---前二码直选---复式
                self.timemm.sp3_2_q2zhixfs(row)
                self.timemm.radoms(row)
                print('二码---前二码直选---复式')

                # 二码
                # 二码---前二码直选---单式
                self.timemm.sp3_2_q2zhixds(row)
                self.timemm.radoms(row)
                print('二码---前二码直选---单式')

                # 二码
                # 二码---前二码直选---直选和值
                self.timemm.sp3_2_q2zhixzhixhzhi(row)
                self.timemm.radoms(row)
                print('二码---前二码直选---直选和值')

                # 二码
                # 二码---前二码组选---复式
                self.timemm.sp3_2_q2zuxfs(row)
                self.timemm.radoms(row)
                print('二码---前二码组选---复式')

                # 二码
                # 二码---前二码组选---单式
                self.timemm.sp3_2_q2zuxds(row)
                self.timemm.radoms(row)
                print('二码---前二码组选---单式')

                # 定位胆
                # 定位单---定位胆---定位胆
                self.timemm.sp3_dwd(row)
                self.timemm.radoms(row)
                print('定位单---定位胆---定位胆')

                # 不定胆
                # 不定胆---不定胆---一码不定胆
                self.timemm.sp3_bddan(row)
                self.timemm.radoms(row)
                print('不定胆---不定胆---一码不定胆')

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
'''
    def test_fail_01(self):
            # 下注
            self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/30')
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
            # 打开csv文件
            csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
            # 读取csv文件
            csv_date = csv.DictReader(csv_file)
            print('打开csv')
            for row in csv_date:
                if row['msg'] == 'succ01':
                    print('进入数据循环succ01')
                    # 登陆模块，调用CommonRecharge中的login()
                    self.timemm = LowfSpeed3D(self.base_driver)
                    # ---------------------------------------
                    # 三码
                    # 三码---直选---复式
                    self.timemm.sp3_3_zhxfs_error(row)
                    print('三码---直选---复式')

                    # 三码
                    # 三码---直选---单式
                    self.timemm.sp3_3_zhxds_error(row)
                    print('三码---直选---单式')

                    # 三码
                    # 三码---组选---组三
                    self.timemm.sp3_3_zuxzu3_error(row)
                    print('三码---组选---组三')

                    # 三码
                    # 三码---组选---组六
                    self.timemm.sp3_3_zuxzu6_error(row)
                    print('三码---组选---组六')

                    # 三码
                    # 三码---组选---混合组选
                    self.timemm.sp3_3_zuxhhzx_error(row)
                    print('三码---组选---混合组选')
                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    # ---------------------------------------------------

                    # 二码
                    # 二码---后二码直选---复式
                    self.timemm.sp3_2_h2zhixfs_error(row)
                    print('二码---后二码直选---复式')

                    # 二码
                    # 二码---后二码直选---单式
                    self.timemm.sp3_2_h2zhixds_error(row)
                    print('二码---后二码直选---单式')

                    # 二码
                    # 二码---后二码组选---复式
                    self.timemm.sp3_2_h2zuxfs_error(row)
                    self.timemm.radoms(row)
                    print('二码---后二码组选---复式')

                    # 二码
                    # 二码---后二码组选---单式
                    self.timemm.sp3_2_h2zuxds_error(row)
                    self.timemm.radoms(row)
                    print('二码---后二码组选---单式')

                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    #
                    # 二码
                    # 二码---前二码直选---复式
                    self.timemm.sp3_2_q2zhixfs_error(row)
                    print('二码---前二码直选---复式')

                    # 二码
                    # 二码---前二码直选---单式
                    self.timemm.sp3_2_q2zhixds_error(row)
                    print('二码---前二码直选---单式')

                    # 二码
                    # 二码---前二码组选---复式
                    self.timemm.sp3_2_q2zuxfs_error(row)
                    print('二码---前二码组选---复式')

                    # 二码
                    # 二码---前二码组选---单式
                    self.timemm.sp3_2_q2zuxds_error(row)
                    print('二码---前二码组选---单式')

                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    # ---------------------------------------------------
                    # ---------------------------------------------------

                    # 定位胆
                    # 定位单---定位胆---定位胆
                    self.timemm.sp3_dwd(row)
                    self.timemm.radoms(row)
                    print('定位单---定位胆---定位胆')

                    # 不定胆
                    # 不定胆---不定胆---一码不定胆
                    self.timemm.sp3_bddan(row)
                    self.timemm.radoms(row)
                    print('不定胆---不定胆---一码不定胆')

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
'''

if __name__ == '__main__':

    unittest.main()

