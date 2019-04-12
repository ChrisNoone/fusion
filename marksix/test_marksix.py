import csv
import unittest

from marksix.lottery import Lottery
from common.box import TestCase, BoxDriver, Browser
from marksix.minute_marksix import MinuteMarkSix
from membercenter.caiwucenter.withdraw.withdraw import Withdraw


class MarkSixTest(TestCase):
    # 六合彩
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_success_01(self):
        # 下注
        self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("成功打开网址")
        self.base_driver.forced_wait(5)
        ''' 下注 '''
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.marksix()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.mmsix = MinuteMarkSix(self.base_driver)
                # 两面下注
                # 添加注单
                # 随机1注和随机5注
                # self.mmsix.twosidesall(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print("两面注单提交完毕")
                # print('两面玩法下注完毕')
                # 七码五行--七码
                # self.mmsix.sevenyards_qm(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('七码五行--七码下注完毕')
                # # 七码五行--五行
                # self.mmsix.sevenyards_wx(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('七码五行--五行下注完毕')

                # 尾数--头尾数
                # self.mmsix.tailnum_htnum(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('尾数--头尾数')

                # # 尾数--正特尾数
                # self.mmsix.tailnum_potnum(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('尾数--头尾数')

                # 色波---三色波
                # self.mmsix.sebo_3(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('色波---三色波')

                # # 色波---半波
                # self.mmsix.sebo_h(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('色波---半波')
                #
                # # 色波---半半波
                # self.mmsix.sebo_hh(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('色波---半半波')
                #
                # # 色波---七色波
                # self.mmsix.sebo_7(row)
                # self.mmsix.addnote_button()
                # self.mmsix.radoms()
                # self.mmsix.surebet()
                # print('色波---七色波')

                # 合肖
                self.mmsix.sebo_7(row)
                self.mmsix.addnote_button()
                self.mmsix.radoms()
                self.mmsix.surebet()
                print('色波---七色波')





                self.base_driver.forced_wait(10)
                get_tips = self.mmsix.get_tips()
                print('获取的文字是：' + get_tips)
                self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # self.base_driver.refresh()
                print('刷新网页')
                self.base_driver.forced_wait(1)
                self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')

    # def test_success_01(self):
    #     self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
    #     ''' 下注 '''
    #     # 指定某一个用户登陆
    #     self.lottery = Lottery(self.base_driver)
    #     # 登陆
    #     self.lottery.login()
    #     # 点击六合彩
    #     self.lottery.marksix()
    #
    #     # 打开csv文件
    #     csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv.DictReader(csv_file)
    #     print('打开csv')
    #     for row in csv_date:
    #         if row['msg'] == 'succ01':
    #             print('进入数据循环')
    #             # 登陆模块，调用CommonRecharge中的login()
    #             self.mmsix = MinuteMarkSix(self.base_driver)
    #             # 两面
    #             self.mmsix.twosidesall(row)
    #             # 添加注单
    #             self.mmsix.addnote_button()
    #             self.base_driver.forced_wait(1)
    #             self.mmsix.surebet()
    #             get_tips01 = self.mmsix.get_tips02()
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('获取的文字是：' + get_tips01)
    #             self.assertEqual(get_tips01, row['tips01'], '充值金额不符合！')
    #             self.base_driver.refresh()
    #             print('刷新网页')
    #             self.base_driver.forced_wait(1)
    #
    #             # 关闭浏览器
    #     self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     print('test_fail_registered_01 运行完毕')
    #     # 日志
    #     self.logger.info('关闭CSV文件')

if __name__ == '__main__':

    unittest.main()



