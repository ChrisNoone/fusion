import csv
import unittest


from common.box import TestCase, BoxDriver, Browser, BasePage
from marksix.lottery import Lottery
from marksix.marksix_minute import MinuteMarkSix
from marksix.pcdd_lucky28 import PcddLucky28


class PcddLucky28Test(TestCase):
    # PC蛋蛋幸运28
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        # self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("打开网址")

        # 休眠
        #self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()



    def test_fail_01(self):
        # 下注
        #self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/22')
        self.base_driver.navigate('file:///C:/Users/Administrator/Desktop/AAA.HTML')
        # print("成功打开网址")
        #self.base_driver.forced_wait(5)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.time()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.pclucky28 = PcddLucky28(self.base_driver)


                # 特码包三
                self.pclucky28.move_to_gap(row)
                print('特码特码包三')
                #

                #
                # self.base_driver.forced_wait(10)
                # get_tips = self.pclucky28.get_tips()
                # print('获取的文字是：' + get_tips)
                # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()

