import unittest

from common.box import TestCase, BoxDriver, Browser
from lottery_hall.lottery_pk10 import LotteryPK10


class LotteryPK10Test(TestCase):
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

    '''
    def test_double_count(self):

        # 北京PK10
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=bjpk10')
        # 分分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=ffpk10')

        # 三分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=sfpk10')

        # 五分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=wfpk10')

        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/ssc?code=xjssc')
        self.base_driver.forced_wait(5)
        # 打开csv文件
        try:
            self.lottery_pk10 = LotteryPK10(self.base_driver)
            self.lottery_pk10.double_count()
            # self.base_driver.quit()
        except Exception as e:
            print(e)
    
    def test_lottery_plan(self):

        # 稳赢杀号
        # 北京PK10
        # s0 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=bjpk10&categoryId=2'
        # self.base_driver.navigate(s0)
        # # 分分PK10
        # s0 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=ffpk10&categoryId=2'
        # self.base_driver.navigate(s0)

        # 三分PK10
        s0 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=sfpk10&categoryId=2'
        self.base_driver.navigate(s0)

        # 五分PK10
        # s0 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=wfpk10&categoryId=2'
        # self.base_driver.navigate(s0)

        # 打开csv文件
        self.lottery_pk10 = LotteryPK10(self.base_driver)
        print('进入稳赢杀号统计')
        try:
            self.lottery_pk10.plan_winkillnum_ball_00()
        except Exception as e:
            print(e)
        try:
            self.lottery_pk10.plan_winkillnum_ball_01()
        except Exception as e:
            print(e)

        try:
            self.lottery_pk10.plan_winkillnum_ball_02()

        except Exception as e:
            print(e)

        try:
            self.lottery_pk10.plan_winkillnum_ball_03()
        except Exception as e:
            print(e)
        try:
            self.lottery_pk10.plan_winkillnum_ball_04()
        except Exception as e:
            print(e)
        try:
            self.lottery_pk10.plan_winkillnum_ball_05()
        except Exception as e:
            print(e)
        try:
            self.lottery_pk10.plan_winkillnum_ball_06()
        except Exception as e:
            print(e)

        try:
            self.lottery_pk10.plan_winkillnum_ball_07()

        except Exception as e:
            print(e)

        try:
            self.lottery_pk10.plan_winkillnum_ball_08()
        except Exception as e:
            print(e)
        try:
            self.lottery_pk10.plan_winkillnum_ball_09()
        except Exception as e:
            print(e)


    
    
    def test_lotteryhall_trend_postion(self):

        # 北京PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=bjpk10')
        # 分分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=ffpk10')

        # 三分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=sfpk10')

        # 五分PK10
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=wfpk10')

        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/ssc?code=xjssc')
        self.base_driver.forced_wait(3)
        self.lottery_pk10 = LotteryPK10(self.base_driver)
        self.lottery_pk10.lotteryhall_trend_position()
        # 打开csv文件
        # try:
        #
        #     self.lottery_pk10.lotteryhall_trend_position()
        #     # self.base_driver.quit()
        # except Exception as e:
        #     print(e)
    
    def test_lotteryhall_trend_size(self):

        # 北京PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=bjpk10')
        # 分分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=ffpk10')

        # 三分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=sfpk10')

        # 五分PK10
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=wfpk10')

        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/ssc?code=xjssc')
        self.base_driver.forced_wait(3)
        self.lottery_pk10 = LotteryPK10(self.base_driver)
        self.lottery_pk10.lotteryhall_trend_size()
        # 打开csv文件
        # try:
        #
        #     self.lottery_pk10.lotteryhall_trend_position()
        #     # self.base_driver.quit()
        # except Exception as e:
        #     print(e)
    
    def test_lotteryhall_trend_double(self):

        # 北京PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=bjpk10')
        # 分分PK10
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=ffpk10')

        # 三分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=sfpk10')

        # 五分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=wfpk10')

        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/ssc?code=xjssc')
        self.base_driver.forced_wait(3)
        self.lottery_pk10 = LotteryPK10(self.base_driver)
        self.lottery_pk10.lotteryhall_trend_double()
        # 打开csv文件
        # try:
        #
        #     self.lottery_pk10.lotteryhall_trend_position()
        #     # self.base_driver.quit()
        # except Exception as e:
        #     print(e)
    '''
    def test_lotteryhall_trend_gyh(self):

        # 北京PK10
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=bjpk10')
        # 分分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=ffpk10')

        # 三分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=sfpk10')

        # 五分PK10
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/PK10/bj_pk10?code=wfpk10')

        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/ssc?code=xjssc')
        self.base_driver.forced_wait(5)
        # 打开csv文件
        try:
            self.lottery_pk10 = LotteryPK10(self.base_driver)
            self.lottery_pk10.lotteryhall_trend_gyh()
        except Exception as e:
            print(e)


if __name__ == '__main__':

    unittest.main()


