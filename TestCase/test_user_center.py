# coding: utf-8

import csv
import time
from configparser import ConfigParser
from common.box import TestCase, BoxDriver, Browser
from PageElement import *


class UserCenterTest(TestCase):
    def set_up(self):
        conf = ConfigParser()
        conf.read('fusion.conf')
        self.url = conf.get('fusion', 'home_url')
        self.logger.debug(self.url)

        self.logger.info('>>> UserCenterTest开始执行，初始化浏览器')
        self.base_driver = BoxDriver(Browser.Chrome)
        self.base_driver.maximize_window()
        self.base_driver.navigate(self.url)
        self.base_driver.forced_wait(4)

        self.home_page = home_page.HomePageElement(self.base_driver)
        csv_file = open('./TestData/csv_case/user_center_case.csv', 'r', encoding='utf8')
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            if row['function'] == 'change_pwd':
                self.home_page.login(row)
        self.home_page.user_center()
        self.user_center_page = user_center_page.UserCenterPageElement(self.base_driver)

    def tear_down(self):
        self.base_driver.quit()
        self.logger.info('>>> RegisterTest执行结束，清除数据')

    def test_check_menu(self):
        pass
