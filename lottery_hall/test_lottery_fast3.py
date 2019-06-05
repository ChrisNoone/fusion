import unittest
from lottery_hall.lottery_fast3 import LotteryFast3
from common.box import TestCase, BoxDriver, Browser


class LotteryFast3Test(TestCase):
    # 计划站---快三系列
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
    #  测试用例
    def test_lottery_today(self):
        # 安徽快三
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ahk3')

        # 广西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=gxk3')

        # 江西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=jsk3')

        # 湖北快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=hubk3')

        # 分分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ffk3')

        # 三分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=sfk3')

        # 五分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=wfk3')

        self.base_driver.forced_wait(5)
        print('进入快三系列今天开奖')
        # 打开csv文件
        self.lottery_fast3 = Fast3(self.base_driver)
        self.lottery_fast3.today_count()
        # self.base_driver.quit()
    
    def test_plan_winkillnum(self):
        # 安徽快三
        s0 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=ahk3&categoryId=6'
        self.base_driver.navigate(s0)

        # 广西快三
        # s1 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=gxk3&categoryId=6'
        # self.base_driver.navigate(s1)

        # 江苏快三
        # s2 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=jsk3&categoryId=6'
        # self.base_driver.navigate(s2)

        # 湖北快三
        # s3 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=hubk3&categoryId=6'
        # self.base_driver.navigate(s3)

        # 分分快三
        # s4 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=ffk3&categoryId=6'
        # self.base_driver.navigate(s4)

        # 三分快三
        # s5 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=sfk3&categoryId=6'
        # self.base_driver.navigate(s5)

        # 五分快三
        # s6 = 'https://tipster-frontend.spmobileapi.net/#/webmasterTJ/pk10tjmain?code=wfk3&categoryId=6'
        # self.base_driver.navigate(s6)
        # 打开csv文件
        self.lottery_fast3 = Fast3(self.base_driver)
        print('进入稳赢杀号统计')
        print('综合杀号')
        try:
            self.lottery_fast3.plan_winkillnum_complex()
        except Exception as e:
            print(e)
        print('和值杀号')
        self.lottery_fast3.plan_winkillnum_sum()
        # try:
        #     self.lottery_fast3.plan_winkillnum_sum()
        # except Exception as e:
        #     print(e)

    

    def test_lotteryhall_trend_basic(self):

        # 安徽快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ahk3')

        # 广西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=gxk3')

        # 江西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=jsk3')

        # 湖北快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=hubk3')

        # 分分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ffk3')

        # 三分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=sfk3')

        # 五分快三
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=wfk3')

        self.base_driver.forced_wait(3)

        print('进入走势图---基本走势')
        # 初始化LotteryTime
        self.lottery_fast3 = LotteryFast3(self.base_driver)
        self.lottery_fast3.lotteryhall_trend_basic()
        # try:
        #     self.lotrrery_hall.today_lottery_rules()
        # except Exception as e:
        #     print(e)


    def test_lotteryhall_trend_position(self):
    
        # 走势图---定位走势
        # 安徽快三
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ahk3')

        # 广西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=gxk3')

        # 江西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=jsk3')

        # 湖北快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=hubk3')

        # 分分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ffk3')

        # 三分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=sfk3')

        # 五分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=wfk3')

        self.lottery_fast3 = LotteryFast3(self.base_driver)
        print('进入走势图---定位走势')
        try:
            self.lottery_fast3.lotteryhall_trend_position()
        except Exception as e:
            print(e)

    
    def test_lotteryhall_trend_size(self):
    
        # 走势图---大小走势
         # 走势图---定位走势
        # 安徽快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ahk3')

        # 广西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=gxk3')

        # 江西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=jsk3')

        # 湖北快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=hubk3')

        # 分分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ffk3')

        # 三分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=sfk3')

        # 五分快三
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=wfk3')

        self.base_driver.forced_wait(3)
        self.lottery_fast3 = LotteryFast3(self.base_driver)
        print('进入走势图---大小走势')
        try:
            self.lottery_fast3.lotteryhall_trend_size()
        except Exception as e:
            print(e)
            
   '''
    def test_lotteryhall_trend_sum(self):

        # 走势图---大小走势
         # 走势图---定位走势
        # 安徽快三
        self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ahk3')

        # 广西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=gxk3')

        # 江西快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=jsk3')

        # 湖北快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=hubk3')

        # 分分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=ffk3')

        # 三分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=sfk3')

        # 五分快三
        # self.base_driver.navigate('https://tipster-frontend.spmobileapi.net/#/kuai3/js_kuai3?code=wfk3')

        self.base_driver.forced_wait(1)
        self.lottery_fast3 = LotteryFast3(self.base_driver)
        print('进入走势图---和值走势')
        try:
            self.lottery_fast3.lotteryhall_trend_sum()
        except Exception as e:
            print(e)



if __name__ == '__main__':

    unittest.main()


