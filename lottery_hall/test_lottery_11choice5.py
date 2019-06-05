import unittest


from common.box import TestCase, BoxDriver, Browser
from lottery_hall.lottery_11choice5 import Lottery11Choice5


class Lottery11Choice5Test(TestCase):
    # 彩种11选5系列
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

        # 山东十一选五
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sd11x5')

        # 上海十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sh11x5')

        # 江西十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=jx11x5')
        #
        # 广大十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=gd11x5')

        # 安徽十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ah11x5)

        # 极速十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ff11x5')

        # 三分十一选五
        # self.base_driver.navigate(''https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sf11x5')

        # 五分十一选五
        # self.base_driver.navigate(''https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=wf11x5')

        # 初始化Lottery11Choice5
        self.lottery_11choice5 = Lottery11Choice5(self.base_driver)

        # 今日开奖---双面统计
        try:
            self.lottery_11choice5.double_count()
            print('今日开奖---双面统计')
        except Exception as e:
            print(e)

    def test_lottery_plan(self):

        # 稳赢杀号
        # 山东十一选五
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=sd11x5')

        # 上海十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=sh11x5')

        # 江西十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=jx11x5')

        # 广大十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=gd11x5')

        # 安徽十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=ah11x5')

        # 极速十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=js11x5')

        # 三分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=sf11x5')

        # 五分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=wf11x5')

        self.lottery_11choice5 = Lottery11Choice5(self.base_driver)
        print('进入稳赢杀号统计')
        try:
            self.lottery_11choice5.plan_winkillnum_w()
        except Exception as e:
            print(e)

        try:
            self.lottery_11choice5.plan_winkillnum_q()
        except Exception as e:
            print(e)

        try:
            self.lottery_11choice5.plan_winkillnum_b()
        except Exception as e:
            print(e)

        try:
            self.lottery_11choice5.plan_winkillnum_s()
        except Exception as e:
            print(e)

        try:
            self.lottery_11choice5.plan_winkillnum_g()
        except Exception as e:
            print(e)
    
    def test_lotteryhall_trend_basic(self):

        #  # 山东十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sd11x5')

        # 上海十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sh11x5')

        # 江西十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=jx11x5')

        # 广大十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=gd11x5')

        # 安徽十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ah11x5')

        # 分分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ff11x5')

        # 三分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sf11x5')

        # 五分十一选五
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=wf11x5')

        # 初始化LotteryTime
        self.lottery_11choice5 = Lottery11Choice5(self.base_driver)
        print('进入走势图---基本走势')
        self.lottery_11choice5.lotteryhall_trend_basic()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)
   

    def test_lotteryhall_trend_position(self):

        # 走势图---定位走势
        # 山东十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sd11x5')

        # 上海十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sh11x5')

        # 江西十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=jx11x5')

        # 广东十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=gd11x5')

        # 安徽十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ah11x5')

        # 分分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ff11x5')

        # 三分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sf11x5')

        # 五分十一选五
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=wf11x5')
        # 初始化LotteryTime
        self.lottery_11choice5 = Lottery11Choice5(self.base_driver)
        print('进入走势图---定位走势')
        self.lottery_11choice5.lotteryhall_trend_position()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)
    

    def test_lotteryhall_trend_size(self):

        # 走势图---大小走势
        # 山东十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sd11x5')

        # 上海十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sh11x5')

        # 江西十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=jx11x5')

        # 广东十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=gd11x5')

        # 安徽十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ah11x5')

        # 分分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ff11x5')

        # 三分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sf11x5')

        # 五分十一选五
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=wf11x5')

        # 初始化LotteryTime
        self.lottery_11choice5 = Lottery11Choice5(self.base_driver)
        print('进入走势图---大小走势')
        self.lottery_11choice5.lotteryhall_trend_size()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)

    '''
    def test_lotteryhall_trend_double(self):

        # 走势图---大小走势
        # 山东十一选五
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sd11x5')

        # 上海十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sh11x5')

        # 江西十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=jx11x5')
        #
        # 广东十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=gd11x5')

        # 安徽十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ah11x5')

        # 极速十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=ff11x5')

        # 三分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=sf11x5')

        # 五分十一选五
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/11xuan5/js_11_5?code=wf11x5')

        # 初始化LotteryTime
        self.lottery_11choice5 = Lottery11Choice5(self.base_driver)
        print('进入走势图---单双走势')
        self.lottery_11choice5.lotteryhall_trend_double()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)

if __name__ == '__main__':

    unittest.main()


