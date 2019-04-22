# coding: utf-8

from common.box import TestCase, BoxDriver, Browser
from PageElement import *


class HomeTest(TestCase):
    url = 'https://fusion.spmobileapi.net/#/home'

    def set_up(self):
        self.logger.info('>>> HomeTest开始执行，初始化浏览器')
        self.base_driver = BoxDriver(Browser.Chrome)
        self.base_driver.maximize_window()
        self.base_driver.navigate(self.url)
        self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()
        self.logger.info('>>> HomeTest执行结束，清除数据')

    def test_help_center(self):
        self.logger.info('>>>>>> 执行test_help_center')
        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.help_center()
        self.help_page = help_page.HelpPageElement(self.base_driver)
        result = self.help_page.check_exist()
        # 断言：点击帮助中心跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '帮助中心跳转失败')
        self.logger.debug('test_help_center断言：')

    def test_play_rule(self):
        self.logger.info('>>>>>> 执行test_play_rules')
        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.play_rule()
        self.rule_page = rule_page.RulePageElement(self.base_driver)
        result = self.rule_page.check_exist()
        # 断言：点击玩法跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '玩法页面跳转失败')
        self.logger.debug('test_play_rules断言：')

    def test_information(self):
        self.logger.info('>>>>>> 执行test_information')
        self.home_page = home_page.HomePageElement(self.base_driver)
        self.home_page.infomation()
        self.infomation_page = infomation_page.InfoPageElement(self.base_driver)
        result = self.infomation_page.check_exist()
        # 断言：点击资讯跳转成功，成功获取该页面某信息
        self.assertEqual(result, True, '资讯页面跳转失败')
        self.logger.debug('test_information断言：')
