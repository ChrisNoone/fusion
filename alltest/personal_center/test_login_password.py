import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from membercenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from membercenter.personalcenter.fund_password import FundPassword
from membercenter.personalcenter.login_password import LoginPassword


class LoginPassTest(TestCase):
    # 会员中心--个人中心--登录密码
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')

        # 休眠
        self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()

    # 测试用例s
    # def test_fail_01(self):
    #     ''' 用户名空---修改失败 '''
    #     self.commonrecharge = CommonRecharge(self.base_driver)
    #     self.commonrecharge.login032()
    #     # 点击个人中心
    #     self.base_driver.click('x,//*[@id="main"]/div/ul/li[1]')
    #     print('点击个人中心')
    #     # 点击登陆密码
    #     self.base_driver.click('x,//*[@id="main"]/div/section/div[1]/div[1]/div[1]')
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/percenter/login_password.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'fail01'执行的数据
    #         if row['msg'] == 'fail01':
    #             # 实例化FusionMain
    #             print('开始数据循环')
    #             self.base_driver.forced_wait(1)
    #             self.fusion_login_main = LoginPassword(self.base_driver)
    #             # 调用登陆前方法login_before
    #             self.fusion_login_main.percenter_login(row)
    #             # 确定按钮
    #             self.fusion_login_main.sub_button()
    #             self.base_driver.forced_wait(1)
    #             # 断言s
    #             get_login_tips02 = self.fusion_login_main.get_tips()
    #             print('获取到提示：' + get_login_tips02)
    #             self.assertEqual(get_login_tips02, row['tips'], '修改失败')
    #             self.base_driver.refresh()
    #             self.base_driver.forced_wait(3)
    #             print('修改登陆密码失败')
    #             self.fusion_login_main.click_login()
    #             print('------')
    #             print('------')
    #             print('------')
    #
    #             # 关闭浏览器
    #     print('fail01运行完毕')
    #     self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')

    # 测试用例s
    def test_success_01(self):
        ''' 用户登陆密码---修改成功 '''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login032()
        # 点击个人中心
        self.base_driver.click('x,//*[@id="main"]/div/ul/li[1]')
        print('点击个人中心')
        # 点击登陆密码
        self.base_driver.click('x,//*[@id="main"]/div/section/div[1]/div[1]/div[1]')
        # 打开csv文件
        csv_file = open('/fusion/csv/percenter/login_password.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        for row in csv_date:
            #  判断 tpshop_login.csv中row['msg']状态为'fail01'执行的数据
            if row['msg'] == 'succ01':
                # 实例化FusionMain
                try:
                    print('开始数据循环')
                    self.base_driver.forced_wait(1)
                    self.fusion_login_main = LoginPassword(self.base_driver)
                    # 调用登陆前方法login_before
                    self.fusion_login_main.percenter_login(row)
                    # 确定按钮
                    self.fusion_login_main.sub_button()
                    self.base_driver.forced_wait(2)
                    # 断言
                    get_login_tips02 = self.fusion_login_main.get_tips()
                    print('获取到提示：' + get_login_tips02)
                    self.assertEqual(get_login_tips02, row['tips'], '修改失败')
                    self.base_driver.refresh()
                    self.base_driver.forced_wait(3)
                    print('修改登陆密码成功')
                    self.fusion_login_main.click_login()
                    print('------')
                    print('------')
                    print('------')
                    # 日志
                    self.logger.info('本次修改成功，用例是' + row['examples'])
                except Exception as e:
                    print(e)
                    self.logger.info('本次修改失败，用例是' + row['examples'])

        # 关闭浏览器
        print('fsucc01运行完毕')
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        # 日志
        # self.logger.info('本次执行的用例如下'+row['examples']+' 关闭CSV文件')


if __name__ == '__main__':

    unittest.main()


