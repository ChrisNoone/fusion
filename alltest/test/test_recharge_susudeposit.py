import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from login.home_registered import HomeRegistered

from membercenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from membercenter.caiwucenter.recharge.susudeposit import SuSuDeposit


class RechargeSuSuTest(TestCase):
    # susu公司充值汇总
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_fail_registered_01(self):
        ''' 新用户层级20-100元 '''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login03()
        self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[1]/p[1]')
        self.commonrecharge.cwbutton()
        # 打开csv文件
        csv_file = open('/fusion/csv/recharge_susudeposit.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'fail01':
                print('进入数据循环')
                # 登陆模块，调用CommonRecharge中的login()
                self.base_driver.forced_wait(3)
                self.base_driver.susude = SuSuDeposit(self.base_driver)
                self.base_driver.susude.susudeposit(row)
                self.base_driver.susude.rechargemethod(row)
                self.base_driver.susude.next_buttion()
                self.base_driver.forced_wait(3)
                get_ckmoney = self.base_driver.susude.get_ckmoney()
                # 断言，断言方法在TestCase类中
                # 获取在登录成功之后的用户名
                print('获取的文字是：' + get_ckmoney)
                self.assertEqual(get_ckmoney, row['tips01'], '充值金额不符合！')
                self.base_driver.refresh()
                print('刷新网页')
                self.base_driver.forced_wait(1)

                # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')

    # def test_fail_registered_02(self):
    #     ''' 新用户层级20-100元 '''
    #     self.commonrecharge = CommonRecharge(self.base_driver)
    #     self.commonrecharge.login03()
    #     self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[1]/p[1]')
    #     self.commonrecharge.cwbutton()
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/susudeposit.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     print('打开csv')
    #     for row in csv_date:
    #         if row['msg'] == 'fail01':
    #             print('进入数据循环')
    #             # 登陆模块，调用CommonRecharge中的login()
    #             # self.commonrecharge.hyzx_cwzx_idem_rk(row)
    #             self.base_driver.forced_wait(1)
    #             self.base_driver.susude = SuSuDeposit(self.base_driver)
    #             self.base_driver.susude.susudeposit(row)
    #             self.base_driver.susude.rechargemethod(row)
    #             get_tips01 = self.base_driver.susude.get_tips01()
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('获取的文字是：' + get_tips01)
    #             self.assertEqual(get_tips01, row['tips01'], '充值金额不符合！')
    #             self.base_driver.refresh()
    #             print('刷新网页')
    #             self.base_driver.forced_wait(1)
    #
    #             # 关闭浏览器
    #     self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     print('test_fail_registered_01 运行完毕')
    #     # 日志
    #     self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()



