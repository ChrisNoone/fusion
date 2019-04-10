import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from membercenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from membercenter.caiwucenter.withdrawrecord.withdrawrecord import WithdrawRecord


class WithdrawRecordTest(TestCase):

    # 充值记录
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        # self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/memberCenter#/home/rechargeRecord')
        print("打开网址")

        # 休眠
        #  self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_fail_registered_01(self):
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        self.base_driver.forced_wait(3)
        ''' 新用户层级20-100元 '''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login031()
        # 点击提现记录
        self.base_driver.click('x,//*[@id="main"]/div/ul/li[2]/ul/li[4]')
        print('进入提现记录页面')
        # 打开csv文件
        csv_file = open('/fusion/csv/withdrawrecord.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'fail01':
                print('进入数据循环')
                # 登陆模块，调用CommonRecharge中的login()
                self.base_driver.forced_wait(3)
                self.base_driver.rech = WithdrawRecord(self.base_driver)
                # 输入查询的单号
                self.base_driver.forced_wait(1)
                self.base_driver.rech.ordernumber(row)
                # 点击查询按钮
                self.base_driver.rech.withdraw_button()
                get_rech_tips03 = self.base_driver.rech.get_rech_tips03()
                # 断言，断言方法在TestCase类中
                # 获取在登录成功之后的用户名
                print('获取的文字是：' + get_rech_tips03)
                self.assertEqual(get_rech_tips03, row['ordernum'], '查询不到该订单！')
                self.base_driver.refresh()
                print('刷新网页')
                print('      ')
                print('      ')
                print('      ')
                print('      ')
                self.base_driver.forced_wait(1)
                # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')

    # def test_fail_registered01_01(self):
    #     self.base_driver.navigate('https://fusion.spmobileapi.net/memberCenter#/home/rechargeRecord')
    #     self.base_driver.forced_wait(3)
    #     ''' 新用户层级20-100元 '''
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/rechagre_rechargerecord.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     print('打开csv')
    #     for row in csv_date:
    #         if row['msg'] == 'fail01':
    #             print('进入数据循环')
    #             # 登陆模块，调用CommonRecharge中的login()
    #             self.base_driver.forced_wait(3)
    #             self.base_driver.rech = WithdrawRecord(self.base_driver)
    #             # 输入查询的单号
    #             self.base_driver.forced_wait(1)
    #             self.base_driver.rech.ordernumber(row)
    #             # 点击查询按钮
    #             self.base_driver.rech.withdraw_button()
    #             get_rech_tips03 = self.base_driver.rech.get_rech_tips03()
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('获取的文字是：' + get_rech_tips03)
    #             self.assertEqual(get_rech_tips03, row['ordernum'], '查询不到该订单！')
    #             self.base_driver.refresh()
    #             print('刷新网页')
    #             print('      ')
    #             print('      ')
    #             print('      ')
    #             print('      ')
    #             self.base_driver.forced_wait(1)
                # 关闭浏览器
    #     self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     print('test_fail_registered_01 运行完毕')
    #     # 日志
    #     self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()



