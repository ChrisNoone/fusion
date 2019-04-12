import csv
import unittest
from common.box import TestCase, BoxDriver, Browser


from membercenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from membercenter.caiwucenter.recharge.susudeposit import SuSuDeposit


class RechargeSuSuTest1(TestCase):
    # susu公司充值
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        print("打开网址")
        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_fail__01(self):
        ''' 用户充值susu公司入款失败 '''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login03()
        # 点击第一个 susu公司入款
        self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[1]/p[1]')
        self.commonrecharge.cwbutton()
        # 打开csv文件
        csv_file = open('/fusion/csv/recharge_susudeposit1.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'fail01':
                print('进入数据循环')
                try:
                    self.base_driver.forced_wait(1)
                    self.base_driver.susude = SuSuDeposit(self.base_driver)
                    self.base_driver.susude.susudeposit(row)
                    # 默认选择第一个
                    # self.base_driver.susude.rechargemethod(row)
                    self.base_driver.susude.next_buttion()
                    self.base_driver.forced_wait(3)
                    get_ckmoney = self.base_driver.susude.get_ckmoney()
                    # 获取在登录成功之后的用户名
                    print(get_ckmoney)
                    print('获取的文字是：' + str(get_ckmoney))
                    self.assertEqual(get_ckmoney, row['tips02'], '充值金额不符合！')
                    # 日志
                    self.logger.info('执行成功，执行用例是：' + row['examples'] )
                except Exception as e:
                    print(e)
                    # 日志
                    self.logger.info('执行失败，执行用例是：' + row['examples'])
                finally:
                    # 点击充值
                    self.base_driver.click('x,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
                    self.base_driver.forced_wait(2)
                    # 点击susu公司入款
                    self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[1]/p[1]')
                    self.commonrecharge.cwbutton()
                self.base_driver.refresh()
                print('刷新网页')
                self.base_driver.forced_wait(1)
                # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        # 日志
        self.logger.info('关闭CSV文件')
        print('test_fail_registered_01 运行完毕')

    def test_success_01(self):
        ''' 用户充值susu公司入款 成功'''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login03()
        # 点击第一个 susu公司入款
        self.base_driver.click_last_one('x,//*[@id="main"]/div/section/ul/li[1]/p[1]')
        self.commonrecharge.cwbutton()
        # 打开csv文件
        csv_file = open('/fusion/csv/recharge_susudeposit1.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环')
                try:
                    self.base_driver.forced_wait(1)
                    self.base_driver.susude = SuSuDeposit(self.base_driver)
                    self.base_driver.susude.susudeposit(row)
                    # 默认选择第一个
                    # self.base_driver.susude.rechargemethod(row)
                    self.base_driver.susude.next_buttion()
                    self.base_driver.forced_wait(3)
                    self.base_driver.susude.depoistname(row)
                    # self.base_driver.forced_wait(1)
                    self.base_driver.susude.rechgebutton()
                    self.base_driver.forced_wait(1)
                    # sum_tips = self.base_driver.susude.sum_tips()
                    # # 获取在登录成功之后的用户名
                    # print(sum_tips)
                    # print('获取的文字是：' + sum_tips)
                    # self.assertEqual(sum_tips, row['tips03'], '提交成功！')
                    self.logger.info('执行成功，执行用例是：' + row['examples'] )
                except Exception as e:
                    print(e)
                    self.logger.info('执行失败，执行用例是：' + row['examples'])
                finally:
                    # 点击充值
                    self.base_driver.click('x,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
                    self.base_driver.forced_wait(2)
                    # 点击susu公司入款
                    self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[1]/p[1]')
                    self.commonrecharge.cwbutton()
                # self.base_driver.refresh()
                print('刷新网页')
                self.base_driver.forced_wait(1)
                # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()



