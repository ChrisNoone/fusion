import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from login.fusion_home_login import FusionLoginPage

from login.home_registered import HomeRegistered


class HomeRegisterTest(TestCase):
    # 注册用例汇总
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
        ''' 注册失败 '''
        # 点击注册按钮
        self.fusion_login_page = FusionLoginPage(self.base_driver)
        self.fusion_login_page.sign()
        # 打开csv文件
        csv_file = open('/fusion/csv/home_register.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        for row in csv_date:
            #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
            if row['msg'] == 'fail01':
                # 实例化fusion_regiseter()，调用registered()方法
                print('进入数据循环')
                self.fusion_regiseter = HomeRegistered(self.base_driver)
                self.fusion_regiseter.homeregistered(row)
                # 断言，断言方法在TestCase类中
                # 获取在登录成功之后的用户名
                get_text_hysign = self.fusion_regiseter.get_text_hysign()
                print('获取到的用户名是：' + get_text_hysign)
                self.assertEqual(get_text_hysign, row['tips01'], '注册失败')
                self.base_driver.refresh()
                self.base_driver.forced_wait(1)
                # 关闭浏览器
                # self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        # 日志
        self.logger.info('关闭CSV文件')
        self.base_driver.quit()
    #
    # def test_success_registered_01(self):
    #     ''' 注册成功 '''
    #     # 点击注册按钮
    #     self.fusion_login_page = FusionLoginPage(self.base_driver)
    #     self.fusion_login_page.sign()
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/home_register.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail01':
    #             # 实例化fusion_regiseter()，调用registered()方法
    #             print('进入数据循环')
    #             self.fusion_regiseter = HomeRegistered(self.base_driver)
    #             self.fusion_regiseter.homeregistered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             get_tips01 = self.fusion_login_page.get_tips01()
    #             print('获取到的断言是：' + get_tips01)
    #             self.assertEqual(get_tips01, row['tips01'], '注册失败')
    #             self.base_driver.refresh()
    #             # 退出
    #             self.fusion_login_page.logout()
    #             self.base_driver.forced_wait(1)
    #             # 再次点击注册按钮
    #             self.fusion_login_page.sign()
    #             self.base_driver.forced_wait(1)
    #             # 关闭浏览器
    #             # self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #     self.base_driver.quit()


if __name__ == '__main__':

    unittest.main()



