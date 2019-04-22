# coding: utf-8

import csv
import time
from common.box import TestCase, BoxDriver, Browser
from PageElement import *


class RegisterTest(TestCase):
    """
    注册用例汇总
    """
    url = 'https://fusion.spmobileapi.net/#/home'

    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)

        # 全屏浏览器
        self.base_driver.maximize_window()

        # 输入网址
        self.base_driver.navigate(self.url)

        # 休眠
        self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()

    def test_register_check(self):
        """
        row[examples]
        :return:
        """
        self.logger.info('>>>>>> 执行RegisterTest.test_register_check')
        # 打开csv文件
        csv_file = open('./TestData/csv_case/register_case.csv', 'r', encoding='utf8')
        self.logger.info('打开CSV文件')
        # 读取csv文件
        csv_data = csv.DictReader(csv_file)

        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.sign()
        self.register_page = register_page.RegisterPageElement(self.base_driver)
        for row in csv_data:
            self.logger.debug('用例数据：%s' % row)
            if row['msg'] == 'fail':
                self.register_page.register_data(row)
                get_text_hy_sign = self.register_page.get_text_hy_sign()
                # 断言：注册失败，页面中找到“会员注册”title
                self.assertEqual(get_text_hy_sign, row['tips'], '预期结果：%s，实际结果：%s' % (row['tips'], get_text_hy_sign))
                self.logger.debug('test_register_check断言：')
                self.base_driver.refresh()
                time.sleep(1)
                # 截屏
                self.images.append(self.base_driver.save_window_snapshot_by_io())
        # 关闭csv文件
        csv_file.close()
        self.logger.info('关闭CSV文件')

    def test_register_success(self):
        self.logger.info('>>>>>> 执行RegisterTest.test_register_success')
        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.sign()
        self.register_page = register_page.RegisterPageElement(self.base_driver)
        self.register_page.register()
        info = self.home_page.get_userinfo()
        self.assertIn('可用余额', info, '注册失败')
        self.logger.debug('test_register_success断言：')
