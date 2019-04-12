import csv
import unittest
from common.box import TestCase, BoxDriver, Browser
from PageElement.huiyuancenter.caiwucenter.recharge.commonrecharge import CommonRecharge
from PageElement.huiyuancenter.caiwucenter.recharge.susudeposit import SuSuDeposit


class SuSu(TestCase):
    # susu入款用例汇总

    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # 休眠
        self.base_driver.forced_wait(4)

    def tear_down(self):
        self.base_driver.quit()

    # 测试用例
    def test_fail_registered_01(self):
        ''' row[examples] '''
        # 打开csv文件
        csv_file = open('/fusion/csv_case/susudeposit.csv_case', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        for row in csv_date:
            #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
            if row['msg'] == 'fail01':
                # 实例化fusion_regiseter()，调用registered()方法
                print("打开网址")
                # 实例化CommonRecharge()
                self.commonrecharge = CommonRecharge(self.base_driver)
                # 登陆模块，调用CommonRecharge中的login()
                self.commonrecharge.login(row)
                print('进入数据循环')
                # 选择入款公司
                self.commonrecharge.hyzx_cwzx_idem_rk(row)
                self.commonrecharge.cwbutton()
                # 实例化
                self.base_driver.susude = SuSuDeposit(self.base_driver)
                # 充值金额选择
                self.base_driver.susude.susudeposit(row)
                # 充值银行选择
                self.base_driver.susude.rechargemethod(row)
                self.base_driver.susude.next_buttion()
                #
                # get_ckm = self.base_driver.susude.get_ckmoney()
                # # 断言，断言方法在TestCase类中
                # # 获取在登录成功之后的用户名
                # print('获取到的金额是：' + get_ckm)
                # self.assertEqual(get_ckm, row['ckmoney'], '注册失败')

                # 存款信息
                self.base_driver.susude.depoistname(row)
                self.base_driver.susude.rechgebutton()
                # 关闭浏览器
                self.base_driver.quit()
        # 使用完csv文件后，关闭
        csv_file.close()
        # 日志
        self.logger.info('关闭CSV文件')
       # self.base_driver.quit()
    #
    # def test_fail_registered_02(self):
    #
    #     '''用户名少于6位---注册失败 '''
    #
    #     # 打开csv文件
    #     csv_file = open('Fusion_Register.csv_case', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv_case.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail02':
    #             # 实例化fuion_login_page中login()，sign()方法
    #             self.fusion_login_page = FusionLoginPage(self.base_driver)
    #             self.fusion_login_page.sign()
    #             print('22222')
    #             self.fusion_regiseter = Registered(self.base_driver)
    #             self.fusion_regiseter.registered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('22222')
    #             get_text_hysign = self.fusion_regiseter.get_text_hysign()
    #             print('获取到的用户名是：' + get_text_hysign)
    #             self.assertEqual(get_text_hysign, row['tips'], '注册失败')
    #             # 关闭浏览器
    #             self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #
    # def test_fail_registered_03(self):
    #
    #     '''用户名多于16位---注册失败 '''
    #
    #     # 打开csv文件
    #     csv_file = open('Fusion_Register.csv_case', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv_case.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail03':
    #             # 实例化fuion_login_page中login()，sign()方法
    #             self.fusion_login_page = FusionLoginPage(self.base_driver)
    #             self.fusion_login_page.sign()
    #             print('22222')
    #             self.fusion_regiseter = Registered(self.base_driver)
    #             self.fusion_regiseter.registered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('22222')
    #             get_text_hysign = self.fusion_regiseter.get_text_hysign()
    #             print('获取到的用户名是：' + get_text_hysign)
    #             self.assertEqual(get_text_hysign, row['tips'], '注册失败')
    #             # 关闭浏览器
    #             self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #
    # def test_fail_registered_04(self):
    #     '''用户名特殊字符---注册失败 '''
    #
    #     # 打开csv文件
    #     csv_file = open('Fusion_Register.csv_case', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv_case.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail04':
    #             # 实例化fuion_login_page中login()，sign()方法
    #             self.fusion_login_page = FusionLoginPage(self.base_driver)
    #             self.fusion_login_page.sign()
    #             print('22222')
    #             self.fusion_regiseter = Registered(self.base_driver)
    #             self.fusion_regiseter.registered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('22222')
    #             get_text_hysign = self.fusion_regiseter.get_text_hysign()
    #             print('获取到的用户名是：' + get_text_hysign)
    #             self.assertEqual(get_text_hysign, row['tips'], '注册失败')
    #             # 关闭浏览器
    #             self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #
    # def test_fail_registered_05(self):
    #     '''用户名正确，密码为空---注册失败 '''
    #
    #     # 打开csv文件
    #     csv_file = open('Fusion_Register.csv_case', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv_case.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail05':
    #             # 实例化fuion_login_page中login()，sign()方法
    #             self.fusion_login_page = FusionLoginPage(self.base_driver)
    #             self.fusion_login_page.sign()
    #             print('22222')
    #             self.fusion_regiseter = Registered(self.base_driver)
    #             self.fusion_regiseter.registered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('22222')
    #             get_text_hysign = self.fusion_regiseter.get_text_hysign()
    #             print('获取到的用户名是：' + get_text_hysign)
    #             self.assertEqual(get_text_hysign, row['tips'], '注册失败')
    #             # 关闭浏览器
    #             self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #
    # def test_fail_registered_06(self):
    #     '''用户名正确，密码少6位---注册失败 '''
    #
    #     # 打开csv文件
    #     csv_file = open('Fusion_Register.csv_case', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv_case.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail06':
    #             # 实例化fuion_login_page中login()，sign()方法
    #             self.fusion_login_page = FusionLoginPage(self.base_driver)
    #             self.fusion_login_page.sign()
    #             print('22222')
    #             self.fusion_regiseter = Registered(self.base_driver)
    #             self.fusion_regiseter.registered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('22222')
    #             get_text_hysign = self.fusion_regiseter.get_text_hysign()
    #             print('获取到的用户名是：' + get_text_hysign)
    #             self.assertEqual(get_text_hysign, row['tips'], '注册失败')
    #             # 关闭浏览器
    #             self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')
    #
    # def test_fail_registered_07(self):
    #     '''用户名正确，特殊字符---注册失败 '''
    #
    #     # 打开csv文件
    #     csv_file = open('Fusion_Register.csv_case', 'r', encoding='utf8')
    #     # 读取csv文件
    #     csv_date = csv_case.DictReader(csv_file)
    #     for row in csv_date:
    #         #  判断 tpshop_login.csv中row['msg']状态为'success'执行的数据
    #         if row['msg'] == 'fail07':
    #             # 实例化fuion_login_page中login()，sign()方法
    #             self.fusion_login_page = FusionLoginPage(self.base_driver)
    #             self.fusion_login_page.sign()
    #             print('22222')
    #             self.fusion_regiseter = Registered(self.base_driver)
    #             self.fusion_regiseter.registered(row)
    #             # 断言，断言方法在TestCase类中
    #             # 获取在登录成功之后的用户名
    #             print('22222')
    #             get_text_hysign = self.fusion_regiseter.get_text_hysign()
    #             print('获取到的用户名是：' + get_text_hysign)
    #             self.assertEqual(get_text_hysign, row['tips'], '注册失败')
    #             # 关闭浏览器
    #             self.base_driver.quit()
    #     # 使用完csv文件后，关闭
    #     csv_file.close()
    #     # 日志
    #     self.logger.info('关闭CSV文件')



if __name__ == '__main__':

    unittest.main()


