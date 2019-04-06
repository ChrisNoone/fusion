from common.box import TestCase, BasePage, YamlHelper


class AlipayTransfer(BasePage):
    # 支付包转账
    # 导入fusion文件中AlipayTransfer
    config_dict_alipt = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['AlipayTransfer']

    def alipaytransfer(self, row):
        # 充值金额
        print("输入和选择金额")
        # self.base_driver.forced_wait(0.5)
        # 充值金额
        if row['susuamount'] == '充值金额':
            self.base_driver.get_text(self.config_dict_alipt['REAMOUNT'])
        # 50,100,300,500,800,1000,2000,3000
        if row['susuamount'] == '50':
            self.base_driver.click(self.config_dict_alipt['50YUAN'])
        if row['susuamount'] == '100':
            self.base_driver.click(self.config_dict_alipt['100YUAN'])
        if row['susuamount'] == '300':
            self.base_driver.click(self.config_dict_alipt['300YUAN'])
        if row['susuamount'] == '500':
            self.base_driver.click(self.config_dict_alipt['500YUAN'])
        if row['susuamount'] == '800':
            self.base_driver.click(self.config_dict_alipt['800YUAN'])
        if row['susuamount'] == '1000':
            self.base_driver.click(self.config_dict_alipt['1000YUAN'])
        if row['susuamount'] == '2000':
            self.base_driver.click(self.config_dict_alipt['2000YUAN'])
        if row['susuamount'] == '3000':
            self.base_driver.click(self.config_dict_alipt['3000YUAN'])
        print('你选择的金额是' + row['susuamount'])

    def buildbank(self,row):
        # 建设银行-戚念
        # 充值银行
        # self.base_driver.forced_wait(0.5)
        if row['rechargemethod'] == '中国工商银行_susu':
            self.base_driver.click(self.config_dict_alipt['BUILDBANK'])

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

    def get_tips01(self):
        # 捕捉 充值金额
        sumtip = self.base_driver.get_text(self.config_dict_alipt['TIPS01'])
        print('下一步')
        return sumtip
