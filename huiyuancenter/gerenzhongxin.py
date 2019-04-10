import csv

from common.box import TestCase, YamlHelper


class GeRenZhongXin(TestCase):

    config_dict_hyzx = YamlHelper().get_config_dict('/fusion/fusion.yamlf')['HuiYuanZhongXin']
    def hyzx_menu(self,hyzx_menus):
        # 个人中心、财务中心、代理中心、电子游艺、交易记录、信息公告、帮助反馈、我的优惠劵
        if hyzx_menus == '个人中心':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[1]')
        if hyzx_menus == '财务中心':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]')
        if hyzx_menus == '代理中心':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[3]')
        if hyzx_menus == '电子游艺':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[4]')
        if hyzx_menus == '交易记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[5]')
        if hyzx_menus == '信息公告':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[6]')
        if hyzx_menus == '帮助反馈':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[7]')
        if hyzx_menus == '我的优惠劵':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[8]')

    def hyzx_grzx_idem(self, hyzx_grzx_idem):
        # 个人中心
        if hyzx_grzx_idem == '登陆密码':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[1]')
        if hyzx_grzx_idem == '资金密码':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]')
        if hyzx_grzx_idem == '我的银行卡':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[3]')

    def hyzx_grzx_idem_dl(self, hyzx_grzx_idem_dl):
        # 密码规则：密码为6位以上，由数字/字母/下划线组成
        if hyzx_grzx_idem_dl == '请输入原始密码':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[1]/div[2]/form/input[1]')
        if hyzx_grzx_idem_dl == '请输入登陆密码':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[1]/div[2]/form/input[2]')
        if hyzx_grzx_idem_dl == '请输入确认密码':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[1]/div[2]/form/input[3]')

    def hyzx_cwzx_idem(self, hyzx_cwzx_idem):

        # 财务中心

        if hyzx_cwzx_idem == '充值':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
        if hyzx_cwzx_idem == '提现':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[2]')
        if hyzx_cwzx_idem == '充值记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[3]')
        if hyzx_cwzx_idem == '提现记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[4]')

    def hyzx_cwzx_idem_rk(self, hyzx_cwzx_idem_rk):

        # 充值入款方式
        if hyzx_cwzx_idem_rk == 'SUSU公司入款':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[1]')
        if hyzx_cwzx_idem_rk == '支付宝转账':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[2]')
        if hyzx_cwzx_idem_rk == '公司入款':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[3]')
        if hyzx_cwzx_idem_rk == 'VIP代理充值':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[4]')

    def hyzx_cwzx_idem_rk_bank(self, hyzx_cwzx_idem_rk_bank):
        # 充值入款方式
        if hyzx_cwzx_idem_rk_bank == '中国工商银行_susu':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[1]')
        if hyzx_cwzx_idem_rk_bank == '中国工商银行我测试啊':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[2]')
        if hyzx_cwzx_idem_rk_bank == '中国工商银行李洁':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[3]')
        if hyzx_cwzx_idem_rk_bank == '中国光大银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[4]')
        if hyzx_cwzx_idem_rk_bank == '中国银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[5]')
        if hyzx_cwzx_idem_rk_bank == '江苏银行-123':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[6]')
        if hyzx_cwzx_idem_rk_bank == '恒丰银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[7]')

    def hyzx_cwzx_idem_rk_yuan(self, hyzx_cwzx_idem_rk_yuan):
        # 50,100,300,500,800,1000,2000,3000
        if hyzx_cwzx_idem_rk_yuan == '50':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[1]')
        if hyzx_cwzx_idem_rk_yuan == '100':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[2]')
        if hyzx_cwzx_idem_rk_yuan == '300':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[3]')
        if hyzx_cwzx_idem_rk_yuan == '500':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[4]')
        if hyzx_cwzx_idem_rk_yuan == '800':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[5]')
        if hyzx_cwzx_idem_rk_yuan == '1000':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[6]')
        if hyzx_cwzx_idem_rk_yuan == '2000':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[7]')
        if hyzx_cwzx_idem_rk_yuan == '3000':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[8]')





