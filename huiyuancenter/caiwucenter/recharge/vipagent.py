from common.box import TestCase, BasePage, YamlHelper


class VipAgent(BasePage):
    # vip代理充值
    # 导入fusion.yaml中VipAgent

    config_dict_alipt = YamlHelper().get_config_dict('/fusion/fusion.yamlf')['VipAgent']

    def vipagent(self, aliaytr):
        # 充值金额
        if aliaytr == '充值金额':
            self.base_driver.get_text(self.config_dict_alipt['REAMOUNT'])
        # 50,100,300,500,800,1000,2000,3000
        if aliaytr == '50':
            self.base_driver.click(self.config_dict_alipt['50YUAN'])
        if aliaytr == '100':
            self.base_driver.click(self.config_dict_alipt['100YUAN'])
        if aliaytr == '300':
            self.base_driver.click(self.config_dict_alipt['300YUAN'])
        if aliaytr == '500':
            self.base_driver.click(self.config_dict_alipt['500YUAN'])
        if aliaytr == '800':
            self.base_driver.click(self.config_dict_alipt['800YUAN'])
        if aliaytr == '1000':
            self.base_driver.click(self.config_dict_alipt['1000YUAN'])
        if aliaytr == '2000':
            self.base_driver.click(self.config_dict_alipt['2000YUAN'])
        if aliaytr == '3000':
            self.base_driver.click(self.config_dict_alipt['3000YUAN'])

    def susu00(self):
        # susususu000000
        susu00 = self.base_driver.click(self.config_dict_alipt['BUILDBANK'])
        return susu00

    def next_buttion(self):
        # 下一步按钮
        nt = self.base_driver.click(self.config_dict_alipt['NEXTBUTTON'])
        return nt

    def coupou(self):
        # 优惠劵
        cp = self.base_driver.click(self.config_dict_alipt['COUPON'])
        return cp

    def savemoney(self):

        # 存款金额
        self.base_driver.get_text(self.config_dict_alipt['SAVEMONEY'])
        # 存款时间
        self.base_driver.get_text(self.config_dict_alipt['SAVETIME'])
        # 转账时间
        self.base_driver.get_text(self.config_dict_alipt['TRANSFERNOTE'])
        # 充值验证信息
        self.base_driver.get_text(self.config_dict_alipt['TRANINFO'])

    def vbuttion(self):
        # 下一步按钮
        vb = self.base_driver.click(self.config_dict_alipt['VBUTTON'])
        return vb


'''
    def hyzx_cwzx_idem_rk_bank(self, hyzx_cwzx_idem_rk_bank):
        # 充值入款方式
        if hyzx_cwzx_idem_rk_bank == '测试0306':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[1]')
        if hyzx_cwzx_idem_rk_bank == 'alipay2bank':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[2]')
        if hyzx_cwzx_idem_rk_bank == 'alipay=receipt':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[3]')
        if hyzx_cwzx_idem_rk_bank == '腾云支付':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[4]')
        if hyzx_cwzx_idem_rk_bank == 'alipay-redpack':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[5]')
        if hyzx_cwzx_idem_rk_bank == 'alipay-qrcode':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[6]')
        if hyzx_cwzx_idem_rk_bank == '686':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[7]')
        if hyzx_cwzx_idem_rk_bank == 'susususu':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[8]')
'''



