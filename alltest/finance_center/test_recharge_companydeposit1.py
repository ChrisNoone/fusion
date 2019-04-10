import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from login.home_registered import HomeRegistered

from membercenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from membercenter.caiwucenter.recharge.compaydeposit import CompanyDeposit
from membercenter.caiwucenter.recharge.susudeposit import SuSuDeposit


class RechargeCompanyTest(TestCase):
    # susu公司充值汇总
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
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
    def test_fail_registered_01(self):
        ''' 新用户层级20-100元 '''
        self.commonrecharge = CommonRecharge(self.base_driver)
        self.commonrecharge.login03()
        # 点击公司入款
        self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[3]/p[1]')
        self.commonrecharge.cwbutton()
        # 打开csv文件
        csv_file = open('/fusion/csv/rechagre_companydeposit.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'fail01':
                try:
                    print('进入数据循环3333')
                    # 登陆模块，调用CommonRecharge中的login()
                    # self.commonrecharge.hyzx_cwzx_idem_rk(row)
                    self.base_driver.forced_wait(1)
                    self.base_driver.comde = CompanyDeposit(self.base_driver)
                    self.base_driver.comde.companydeposit(row)
                    self.base_driver.comde.comde_bank(row)
                    self.base_driver.comde.next_buttion()
                    get_tips01 = self.base_driver.comde.get_tips()
                    # 断言，断言方法在TestCase类中
                    # 获取在登录成功之后的用户名
                    print('获取的文字是：' + get_tips01)
                    self.assertEqual(get_tips01, row['tips'], '充值金额不符合！')
                    # self.base_driver.refresh()
                    print('刷新网页')
                    self.base_driver.forced_wait(1)
                    self.logger.info('用例成功:' + row['examples'])
                except Exception as e:
                    print(e)
                    self.logger.info('用例失败:' + row['examples'])
                finally:

                    print('进入finally')
                    self.base_driver.forced_wait(1)

                    # 财务中心--点击充值

                    self.base_driver.click('x,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
                    self.base_driver.forced_wait(1)

                    # 点击公司入款
                    self.base_driver.click('x,//*[@id="main"]/div/section/ul/li[3]/p[1]')
                    self.base_driver.forced_wait(1)

                    self.base_driver.click('x,//*[@id="main"]/div/section/div[2]/button')
                    self.base_driver.forced_wait(4)


                # 关闭浏览器
        self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()



