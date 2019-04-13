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
                self.home_page = home_page.HomePageElement(self.base_driver)
                self.home_page.login(row)
                # 获取登录操作之后的登录按钮
                get_text = self.home_page.get_user_center_text()
                self.assertEqual(get_text, row['expectation'], '预期结果：%s，实际结果：%s' % (row['expectation'], get_text))
                time.sleep(1)
        csv_file.close()
        self.logger.info('关闭CSV文件')
        self.base_driver.quit()
        self.logger.info('关闭浏览器')
