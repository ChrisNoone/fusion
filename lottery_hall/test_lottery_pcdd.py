import unittest
from lottery_hall.lottery_fast3 import Fast3
from common.box import TestCase, BoxDriver, Browser
from lottery_hall.lottery_pcdd import LotteryPCDD


class LotteryPCDDTest(TestCase):
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        # self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')

        # 休眠
        # self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()

    #  测试用例
    def test_lottery_today(self):
        # 幸运28
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/pcdd/pcdd?code=lucky28')
        self.base_driver.forced_wait(3)
        print('进入快三系列今天开奖')
        # 打开csv文件
        self.lottery_pcdd = LotteryPCDD(self.base_driver)
        self.lottery_pcdd.today_lottery_rules()
        # self.base_driver.quit()





    



if __name__ == '__main__':

    unittest.main()


