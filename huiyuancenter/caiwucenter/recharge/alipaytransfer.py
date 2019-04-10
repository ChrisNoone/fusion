from common.box import TestCase, BasePage, YamlHelper


class AlipayTransfer(BasePage):
    # 支付包转账
    # 导入fusion文件中AlipayTransfer
    config_dict_alipt = YamlHelper().get_config_dict('/fusion/yamlf/fusion.yamlf')['AlipayTransfer']

    def alipaytransfer(self, aliaytr):
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
    '''
    def zhifusaoma(self, cwcenter_idems):
        # 支付扫码
        if cwcenter_idems == '发财酥':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[1]')
        if cwcenter_idems == '交通银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[2]')
        if cwcenter_idems == '建设银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[3]')
        if cwcenter_idems == '支付宝转账码':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[4]')
        if cwcenter_idems == '苏宁钱包':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[5]')
        if cwcenter_idems == 'A':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[6]')
        if cwcenter_idems == 'alipay2bank':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[7]')
        if cwcenter_idems == 'alipay-receipt':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[8]')
        if cwcenter_idems == 'alipay-redpack':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[9]')
        if cwcenter_idems == 'alipay-qrcode':
    '''

    def buildbank(self):
        # 建设银行-戚念
        nt = self.base_driver.click(self.config_dict_alipt['BUILDBANK'])
        return nt

    def next_buttion(self):
        # 下一步按钮
        nt = self.base_driver.click(self.config_dict_alipt['NEXTBUTTON'])
        return nt

    def coupou(self):
        # 优惠劵
        cp = self.base_driver.click(self.config_dict_alipt['COUPON'])
        return cp

    def qrcode(self):
        # 二维码
        qr = self.base_driver.get_text(self.config_dict_alipt['3000YUAN'])
        return qr
