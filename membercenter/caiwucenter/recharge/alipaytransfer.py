from common.box import TestCase, BasePage, YamlHelper


class AlipayTransfer(BasePage):
    # 支付包转账
    # 导入fusion文件中AlipayTransfer
    config_dict_alipt = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['AlipayTransfer']

    def alipaytransfer(self, row):
        print("输入和选择金额")
        # self.base_driver.forced_wait(0.5)
        # 充值金额
        # if row['susuamount'] == '充值金额':
        #     self.base_driver.type(self.config_dict_susudep['REAMOUNT'], row['susuamount'])
        # 50,100,300,500,800,1000,2000,3000
        if row['alipaymount'] == '50':
            self.base_driver.click(self.config_dict_alipt['50YUAN'])
        if row['alipaymount'] == '100':
            self.base_driver.click(self.config_dict_alipt['100YUAN'])
        if row['alipaymount'] == '300':
            self.base_driver.click(self.config_dict_alipt['300YUAN'])
        if row['alipaymount'] == '500':
            self.base_driver.click(self.config_dict_alipt['500YUAN'])
        if row['alipaymount'] == '800':
            self.base_driver.click(self.config_dict_alipt['800YUAN'])
        if row['alipaymount'] == '1000':
            self.base_driver.click(self.config_dict_alipt['1000YUAN'])
        if row['alipaymount'] == '2000':
            self.base_driver.click(self.config_dict_alipt['2000YUAN'])
        if row['alipaymount'] == '3000':
            self.base_driver.click(self.config_dict_alipt['3000YUAN'])
        print('你选择的金额是' + row['alipaymount'])

    def buildbank(self, row):
        # 建设银行-戚念
        # 充值银行
        self.base_driver.forced_wait(0.5)
        if row['rechargemethod'] == '建设银行-戚念':
            self.base_driver.click(self.config_dict_alipt['BUILDBANK'])
        print('你选择的银行是' + row['rechargemethod'])

    def next_buttion(self):
        # 下一步按钮
        print('点击按钮')
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

    def get_tips(self):
        # 捕捉充值金额不符合提示
        print('进入捕捉')
        tips = self.base_driver.get_text(self.config_dict_alipt['TIPS'])
        print('捕捉到的提示' + tips)
        return tips

    def get_tips01(self):
        # 捕捉 充值金额
        sumtip = self.base_driver.get_text(self.config_dict_alipt['TIPS'])
        print('下一步')
        return sumtip

    def get_ornum(self):
        # 获得的订单号是
        orn = self.base_driver.get_text(self.config_dict_alipt['ORDERSUCC'])
        print('获得订单号是' + orn)
        return orn

    def get_ordertips(self):
        # 订单提交成功，请扫描以下二维码付款！
        orn = self.base_driver.get_text(self.config_dict_alipt['ORDERTIPS'])
        print('获得订单号是' + orn)
        return orn
