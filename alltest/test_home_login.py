import csv
import unittest
from common.box import TestCase, BoxDriver, Browser

from page.fusion_main import FusionMain


class HomeLoginTest(TestCase):
    # 主页登陆用例
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

    # 测试用例
    def test_fail_registered_01(self):
        ''' 用户名空---登录失败 '''

        # 打开csv文件
        csv_file = open('/fusion/csv/home_login.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        for row in csv_date:
            #  判断 tpshop_login.csv中row['msg']状态为'fail01'执行的数据
            if row['msg'] == 'fail01':
                # 实例化FusionMain
                self.fusion_login_main = FusionMain(self.base_driver)
                # 调用登陆前方法login_before
                self.fusion_login_main.login_before(row)
                # 断言，断言方法在TestCase类中
                # 获取在登录失败之后的用户名
                get_login_tips02 = self.fusion_login_main.get_login_tips02()
                print('获取到登陆按钮：' + get_login_tips02)
                self.assertEqual(get_login_tips02, row['tips01'], '登录失败')
                print('登陆失败')
                # 关闭浏览器
        print('fail01运行完毕')
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        # 日志
        self.logger.info('关闭CSV文件')

    def test_success_registered_01(self):

        '''用户名密码正确---成功登陆 '''

        # 打开csv文件
        csv_file = open('/fusion/csv/home_login.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        for row in csv_date:
            #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
            if row['msg'] == 'succ01':
                # self.base_driver.forced_wait(20)
                # 实例化FusionMain
                self.fusion_login_main = FusionMain(self.base_driver)
                # 调用登陆前方法login_before
                self.fusion_login_main.login_before(row)
                # 断言，断言方法在TestCase类中
                # 获取在登录失败之后的用户名
                # self.base_driver.forced_wait(30)
                print('22222')
                get_login_tips03 = self.fusion_login_main.get_login_tips03()
                print('获取到断线：' + get_login_tips03)
                self.assertEqual(get_login_tips03, row['tips01'], '退出')
                self.fusion_login_main.login_drop()
                print('开始进入下一轮')
        # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        # 日志
        self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()


