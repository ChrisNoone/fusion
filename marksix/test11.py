import csv
import unittest

from common.box import TestCase, BoxDriver, Browser, BasePage


class Test(BasePage):
    # 注册用例汇总
    def a(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('file:///C:/Users/Administrator/Desktop/fusion后台-会员中心.html')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

       # self.base_driver.click('x,//*[@id="main"]/header/div/ul/section/div/select/option[2]')
        self.base_driver.select_by_index('x,//*[@id="main"]/header/div/ul/section/div/select/option[2]', '1')



if __name__ == '__main__':
    t = Test(driver)
    t.a()




