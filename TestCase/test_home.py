# coding: utf-8

import csv
from configparser import ConfigParser
from common.box import TestCase, BoxDriver, Browser
from PageElement import *


class HomeTest(TestCase):
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

    def tear_down(self):
        self.base_driver.quit()

    def test_help_center(self):
        self.logger.info('>>>>>> 执行HomeTest.test_help_center')
        self.home_page.help_center()
        self.help_page = help_page.HelpPageElement(self.base_driver)
        result = self.help_page.check_exist()
        # 断言：点击帮助中心跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '帮助中心跳转失败')
        self.logger.debug('test_help_center断言：')

    def test_play_rule(self):
        self.logger.info('>>>>>> 执行HomeTest.test_play_rules')
        self.home_page.play_rule()
        self.rule_page = rule_page.RulePageElement(self.base_driver)
        result = self.rule_page.check_exist()
        # 断言：点击玩法跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '玩法页面跳转失败')
        self.logger.debug('test_play_rules断言：')

    def test_information(self):
        self.logger.info('>>>>>> 执行HomeTest.test_information')
        self.home_page.infomation()
        self.infomation_page = infomation_page.InfoPageElement(self.base_driver)
        result = self.infomation_page.check_exist()
        # 断言：点击资讯跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '资讯页面跳转失败')
        self.logger.debug('test_information断言：')

    def test_user_center(self):
        self.logger.info('>>>>>> 执行HomeTest.user_center')
        csv_file = open('./TestData/csv_case/user_center_case.csv', 'r', encoding='utf8')
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            if row['function'] == 'change_pwd':
                self.home_page.login(row)
        self.home_page.user_center()
        self.user_center_page = user_center_page.UserCenterPageElement(self.base_driver)
        result = self.user_center_page.check_exist()
        # 断言：点击会员中心跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '会员中心跳转失败')
