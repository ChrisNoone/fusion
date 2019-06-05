import unittest

from lottery_hall.lottery_time import LotteryTime
from common.box import TestCase, BoxDriver, Browser


class LotteryTimeTest(TestCase):
    # 时时彩
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
    def test_lotteryhall_today_rules(self):

        # 今天开奖---双面统计

        # 重庆时时彩
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=cqssc')

        # 新疆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=wfssc')

        # 初始化LotteryTime
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入今天开奖---数据校对')
        self.lottery_hall.lotteryhall_today_rules()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)
 
    def test_lotteryhall_today_double_count(self):

        # 今天开奖---双面统计

        # 重庆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=cqssc')

        # 新疆时时彩
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=wfssc')

        # 初始化LotteryTime
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入今天开奖---双面统计')
        self.lottery_hall.lotteryhall_today_double_count()
        # try:
        #     self.lotrrery_hall.lotteryhall_today_double_count()
        # except Exception as e:
        #     print(e)
    
    def test_lottery_plan(self):

        # 稳赢杀号

        # 重庆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=cqssc')

        # 新疆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=wfssc')

        # 打开csv文件
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入稳赢杀号统计')
        try:
            self.lottery_hall.plan_winkillnum_w()
        except Exception as e:
            print(e)
        try:
            self.lottery_hall.plan_winkillnum_q()
        except Exception as e:
            print(e)

        try:
            self.lottery_hall.plan_winkillnum_b()

        except Exception as e:
            print(e)

        try:
            self.lottery_hall.plan_winkillnum_s()
        except Exception as e:
            print(e)
        try:
            self.lottery_hall.plan_winkillnum_g()
        except Exception as e:
            print(e)
        # self.base_driver.quit()
        # self.base_driver.quit()

    
    def test_lotteryhall_trend_basic(self):

        # 今天开奖---双面统计

        # 重庆时时彩
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=cqssc')

        # 新疆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=wfssc')

        # 初始化LotteryTime
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入走势图---基本走势')
        self.lottery_hall.lotteryhall_trend_basic()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)
    
    def test_lotteryhall_trend_position(self):

        # 今天开奖---双面统计

        # 重庆时时彩
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=cqssc')

        # 新疆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=wfssc')

        # 初始化LotteryTime
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入走势图---基本走势')
        self.lottery_hall.lotteryhall_trend_position()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)
    
    def test_lotteryhall_trend_size(self):

        # 走势图---大小走势
        # 重庆时时彩
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=cqssc')

        # 新疆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=wfssc')

        # 初始化LotteryTime
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入走势图---大小走势')
        self.lottery_hall.lotteryhall_trend_size()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)
    '''
    def test_lotteryhall_trend_double(self):

        # 走势图---大小走势
        # 重庆时时彩
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=cqssc')

        # 新疆时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=xjssc')

        # 天津时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=tjssc')

        # 分分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=ffssc')

        # 两分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=lfssc')

        # 五分时时彩
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/ssc/index?code=wfssc')

        # 初始化LotteryTime
        self.lottery_hall = LotteryTime(self.base_driver)
        print('进入走势图---单双走势')
        self.lottery_hall.lotteryhall_trend_double()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)


if __name__ == '__main__':

    unittest.main()


