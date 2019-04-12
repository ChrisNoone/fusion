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
        self.logger.info('RegisterTest初始化浏览器')
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

    # 测试用例
    def test_fail_registered_01(self):
        """
        row[examples]
        :return:
        """
        # 打开csv文件
        csv_file = open('./TestData/csv_case/register_case.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_data = csv.DictReader(csv_file)

        # 点击注册按钮
        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.sign()
        for row in csv_data:
            if row['msg'] == 'fail':
                self.register_page = register_page.RegisterPageElement(self.base_driver)
                self.register_page.register(row)
                # 获取注册操作之后的“会员注册”标题
                get_text_hy_sign = self.register_page.get_text_hy_sign()
                self.assertEqual(get_text_hy_sign, row['tips'], '注册失败')
                self.base_driver.refresh()
                time.sleep(1)
                # 截屏
                self.images.append(self.base_driver.save_window_snapshot_by_io())
        # 关闭csv文件
        csv_file.close()
        self.logger.info('关闭CSV文件')
        # 关闭浏览器
        self.base_driver.quit()
        self.logger.info('关闭浏览器')
