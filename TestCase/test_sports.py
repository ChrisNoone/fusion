# coding: utf-8

import csv
from configparser import ConfigParser
from common.box import TestCase, BoxDriver, Browser
from PageElement import *


class SportsTest(TestCase):
    def set_up(self):
        conf = ConfigParser()
        conf.read('fusion.conf')
        self.url = conf.get('fusion', 'home_url')
        self.logger.debug(self.url)

        self.base_driver = BoxDriver(Browser.Chrome)
        self.base_driver.maximize_window()
        self.base_driver.navigate(self.url)
        self.base_driver.forced_wait(4)

        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.close_dialog()
        csv_file = open('./TestData/csv_case/sports_center_case.csv', 'r', encoding='utf8')
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            if row['function'] == 'login':
                self.logger.info(row)
                self.home_page.login_with_ruokuai(row)
        self.home_page.sports_center()
        self.base_driver.forced_wait(2)
        self.sports_center = sports_page.SportsPageElement(self.base_driver)
        self.sports_center.close_dialog()

    def tear_down(self):
        self.base_driver.quit()

    def test_football_random_bet(self):
        pass
