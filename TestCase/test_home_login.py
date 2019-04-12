import csv
from common.box import TestCase, BoxDriver, Browser
from PageElement import *
import time


class HomeLoginTest(TestCase):
    url = 'https://fusion.spmobileapi.net/#/home'

    def set_up(self):
        self.logger.info('HomeLoginTest初始化浏览器')
        self.base_driver = BoxDriver(Browser.Chrome)
        self.base_driver.maximize_window()
        self.base_driver.navigate(self.url)
        self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()

    def test_fail_login(self):
        """
        用户名空，登录失败
        """
        csv_file = open('./TestData/csv_case/home_login_case.csv', 'r', encoding='utf8')
        csv_data = csv.DictReader(csv_file)

        for row in csv_data:
            if row['msg'] == 'fail':
                self.home_page = home_page.HomeMainElement(self.base_driver)
                self.home_page.login_before(row)
                # 获取登录操作之后的登录按钮
                get_login_tips02 = self.home_page.get_login_tips02()
                self.assertEqual(get_login_tips02, row['tips'], '登陆失败')
                time.sleep(1)
        csv_file.close()
        self.logger.info('关闭CSV文件')
        self.base_driver.quit()
        self.logger.info('关闭浏览器')
