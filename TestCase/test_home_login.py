import csv
from common.box import TestCase, BoxDriver, Browser
from PageElement import *
import time


class HomeLoginTest(TestCase):
    url = 'https://fusion.spmobileapi.net/#/home'

    def set_up(self):
        self.logger.info('>>> HomeLoginTest开始执行，初始化浏览器')
        self.base_driver = BoxDriver(Browser.Chrome)
        self.base_driver.maximize_window()
        self.base_driver.navigate(self.url)
        self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()
        self.logger.info('>>> HomeLoginTest执行结束，清除数据')

    def test_login_check(self):
        """
        用户名空，登录失败
        """
        self.logger.info('>>>>>> 执行test_login_check')
        csv_file = open('./TestData/csv_case/home_login_case.csv', 'r', encoding='utf8')
        self.logger.info('打开CSV文件')
        csv_data = csv.DictReader(csv_file)

        for row in csv_data:
            self.logger.debug('用例数据：%s' % row)
            if row['msg'] == 'fail':
                time.sleep(1)
                self.home_page = home_page.HomePageElement(self.base_driver)
                user_info = self.home_page.login(row)
                # 登录失败，页面中找得到登录按钮
                self.assertEqual(user_info, '登录', '登录成功，页面中找不到登录按钮')
                self.logger.debug('test_login_check断言：')
        csv_file.close()
        self.logger.info('关闭CSV文件')

    def test_free_trial(self):
        self.logger.info('>>>>>> 执行test_free_trial')
        self.home_page = home_page.HomePageElement(self.base_driver)
        user_info = self.home_page.free_trial()
        # 断言：注册试玩成功，页面中账号信息中包含“Guest”
        self.assertIn('Guest', user_info, '未成功注册试玩')
        self.logger.debug('test_free_trial断言：')

    def test_special_agent_login(self):
        self.logger.info('>>>>>> 执行test_special_agent_login')
        self.home_page = home_page.HomePageElement(self.base_driver)
        user_info = self.home_page.special_agent()
        # 断言：特殊代理登录成功，页面中账号信息中包含特殊代理账号
        self.assertIn('specialsuper', user_info, '特殊代理登录失败')
        self.logger.debug('test_special_agent_login断言：')

    def test_help_center(self):
        self.logger.info('>>>>>> 执行test_help_center')
        self.home_page = home_page.HomePageElement(self.base_driver)
        info = self.home_page.help_center()
        # 断言：点击帮助中心跳转成功，成功获取该页面某信息
        self.assertIn('帮助中心', info, '帮助中心跳转失败')
        self.logger.debug('test_help_center断言：')

    def test_play_rules(self):
        self.logger.info('>>>>>> 执行test_play_rules')
        self.home_page = home_page.HomePageElement(self.base_driver)
        info = self.home_page.play_rules()
        # 断言：点击帮助中心跳转成功，成功获取该页面某信息
        self.assertIn('所有彩票', info, '玩法页面跳转失败')
        self.logger.debug('test_play_rules断言：')

    def test_information(self):
        self.logger.info('>>>>>> 执行test_information')
        self.home_page = home_page.HomePageElement(self.base_driver)
        info = self.home_page.infomation()
        # 断言：点击帮助中心跳转成功，成功获取该页面某信息
        self.assertIn('资讯', info, '资讯页面跳转失败')
        self.logger.debug('test_information断言：')
