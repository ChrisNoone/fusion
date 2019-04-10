import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from login.home_registered import HomeRegistered
from membercenter.caiwucenter.recharge.alipaytransfer import AlipayTransfer

from membercenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from membercenter.caiwucenter.recharge.susudeposit import SuSuDeposit


class RechargeAlipay(TestCase):
    # 支付宝转账
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
    # def test_fail_registered_01(self):
    #     ''' 新用户层级20-100元 '''
    #     self.commonrecharge = CommonRecharge(self.base_driver)
    #     self.commonrecharge.login03()
    #     # 点击支付宝
    #     self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[2]/p[1]')
    #     self.commonrecharge.cwbutton()
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/recharge_alipaytransfer.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     print('打开csv')
    #     for row in csv_date:
    #         if row['msg'] == 'fail01':
    #             print('进入数据循环')
    #             # 登陆模块，调用CommonRecharge中的login()
    #             # self.commonrecharge.hyzx_cwzx_idem_rk(row)
    #             self.base_driver.forced_wait(1)
    #             self.base_driver.ali = AlipayTransfer(self.base_driver)
    #             self.base_driver.ali.alipaytransfer(row)
    #             # self.base_driver.ali.buildbank(row)
    #             self.base_driver.ali.next_buttion()
    #             self.base_driver.forced_wait(1)
    #             # 断言，断言方法在TestCase类中
    #             # 获取不成功的提示信息
    #             # get_tips00 = self.base_driver.ali.get_tips00()
    #             # print('获取的文字是：' + get_tips00)
    #             # self.assertEqual(get_tips00, row['tips00'], '充值金额不符合！')
    #             # self.base_driver.refresh()
    #             # print('刷新网页')
    #             # self.base_driver.forced_wait(1)
    #             get_ornum = self.base_driver.ali.get_ordertips()
    #             print('获取的提示信息：' + get_ornum)
    #             self.assertEqual(get_ornum, row['tips02'], '充值成功')
    #             self.logger.info('用例运行成功，充值失败：' + row['examples'])
    #             # 关闭浏览器
    #     self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     print('test_fail_registered_01 运行完毕')
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    # 测试用例
    def test_fail_registered_01(self):
        ''' 支付宝转账用例 '''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login03()
        # 点击支付宝转账
        self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[2]/p[1]')
        self.commonrecharge.cwbutton()
        # 打开csv文件
        csv_file = open('/fusion/csv/recharge_alipaytransfer.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'fail01':
                print('进入数据循环')
                try:
                    # 登陆模块，调用CommonRecharge中的login()
                    self.base_driver.ali = AlipayTransfer(self.base_driver)
                    self.base_driver.ali.alipaytransfer(row)
                    self.base_driver.ali.buildbank(row)
                    self.base_driver.ali.next_buttion()
                    self.base_driver.forced_wait(2)
                    get_tips100 = self.base_driver.ali.get_tips()
                    # 获取不成功的提示信息
                    print('获取的文字是：' + get_tips100)
                    self.assertEqual(get_tips100, row['tips00'], '充值金额不符合！')
                    self.base_driver.refresh()

                    # 浏览器后退移步
                    self.base_driver.back()
                    print('刷新网页')
                    # self.base_driver.forced_wait(1)
                    # self.base_driver.click('x,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
                    # # 点击支付宝转账
                    # self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[2]/p[1]')
                    # self.commonrecharge.cwbutton()
                    self.logger.info('用例运行成功，充值失败：' + row['examples'])
                except Exception as e:
                    print(e)
                    # 日志
                    self.logger.info('用例运行失败，充值成功' + row['examples'] + '本次充值' + row['examples'])
                    # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')




    # def test_fail_registered_01(self):
    #     ''' 新用户层级20-100元 '''
    #     self.commonrecharge = CommonRecharge(self.base_driver)
    #     self.commonrecharge.login03()
    #     # 点击支付宝
    #     self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[2]/p[1]')
    #     self.commonrecharge.cwbutton()
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/recharge_alipaytransfer.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     print('打开csv')
    #     for row in csv_date:
    #         if row['msg'] == 'fail01':
    #             print('进入数据循环')
    #             try:
    #                 # 登陆模块，调用CommonRecharge中的login()
    #                 # self.commonrecharge.hyzx_cwzx_idem_rk(row)
    #                 self.base_driver.forced_wait(1)
    #                 self.base_driver.ali = AlipayTransfer(self.base_driver)
    #                 self.base_driver.ali.alipaytransfer(row)
    #                 self.base_driver.ali.buildbank(row)
    #                 self.base_driver.ali.next_buttion()
    #
    #                 get_tips00 = self.base_driver.ali.get_tips00()
    #                 # 断言，断言方法在TestCase类中
    #                 # 获取不成功的提示信息
    #                 print('获取的文字是：' + get_tips00)
    #                 self.assertEqual(get_tips00, row['tips00'], '充值金额不符合！')
    #                 # self.base_driver.refresh()
    #                 # print('刷新网页')
    #                 self.base_driver.forced_wait(1)
    #                 self.logger.info('用例运行成功，充值失败：' + row['examples'])
    #                 self.base_driver.forced_wait(3)
    #                 get_ornum = self.base_driver.ali.get_ordertips()
    #                 self.assertEqual(get_ornum, row['tips02'], '充值成功')
    #
    #             except Exception as e:
    #                 print('cccccccc')
    #                 self.base_driver.forced_wait(1)
    #                 get_ornum = self.base_driver.ali.get_ordertips()
    #                 self.assertEqual(get_ornum, row['tips02'], '充值成功')
    #                 # 重新点击充值
    #                 self.base_driver.click('x,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
    #                 # 点击支付宝转账
    #                 self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[2]/p[1]')
    #                 self.commonrecharge.cwbutton()
    #                 # self.base_driver.refresh()
    #                 print('刷新网页')
    #                 # self.base_driver.forced_wait(1)
    #                 print(e)
    #                 # 日志
    #                 self.logger.info('用例运行失败' + row['examples'])
    #                 # 关闭浏览器
    #     self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     print('test_fail_registered_01 运行完毕')
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #

if __name__ == '__main__':

    unittest.main()



