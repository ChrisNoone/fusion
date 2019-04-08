from common.box import TestCase, BasePage, YamlHelper


class VipAgentDeposit(BasePage):
    # vip代理充值
    # 导入fusion.yaml中VipAgent

    config_dict_vade = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['VipAgent']

    def vipagent(self, row):
        # 充值金额
        print("输入和选择金额")
        # self.base_driver.forced_wait(0.5)
        # 充值金额
        if row['susuamount'] == '充值金额':
            self.base_driver.get_text(self.config_dict_vade['REAMOUNT'])
        # 50,100,300,500,800,1000,2000,3000
        if row['susuamount'] == '50':
            self.base_driver.click(self.config_dict_vade['50YUAN'])
        if row['susuamount'] == '100':
            self.base_driver.click(self.config_dict_vade['100YUAN'])
        if row['susuamount'] == '300':
            self.base_driver.click(self.config_dict_vade['300YUAN'])
        if row['susuamount'] == '500':
            self.base_driver.click(self.config_dict_vade['500YUAN'])
        if row['susuamount'] == '800':
            self.base_driver.click(self.config_dict_vade['800YUAN'])
        if row['susuamount'] == '1000':
            self.base_driver.click(self.config_dict_vade['1000YUAN'])
        if row['susuamount'] == '2000':
            self.base_driver.click(self.config_dict_vade['2000YUAN'])
        if row['susuamount'] == '3000':
            self.base_driver.click(self.config_dict_vade['3000YUAN'])
        print('你选择的金额是' + row['susuamount'])

    def susu00(self,row):
        # susususu000000
        if row['rechargemethod'] == 'susususu000000':
            self.base_driver.click(self.config_dict_vade['BUILDBANK'])

    def next_buttion(self):
        # 下一步按钮
        nt = self.base_driver.click(self.config_dict_vade['NEXTBUTTON'])
        return nt

    def coupou(self):
        # 优惠劵
        cp = self.base_driver.click(self.config_dict_vade['COUPON'])
        return cp

    def savemoney(self):

        # 存款金额
        self.base_driver.get_text(self.config_dict_vade['SAVEMONEY'])
        # 存款时间
        self.base_driver.get_text(self.config_dict_vade['SAVETIME'])
        # 转账时间
        self.base_driver.get_text(self.config_dict_vade['TRANSFERNOTE'])
        # 充值验证信息
        self.base_driver.get_text(self.config_dict_vade['TRANINFO'])

    def vbuttion(self):
        # 下一步按钮
        vb = self.base_driver.click(self.config_dict_vade['VBUTTON'])
        return vb

    def get_tips01(self):
        # 捕捉 充值金额
        # self.base_driver.forced_wait(10)
        sumtip = self.base_driver.get_text(self.config_dict_vade['TIPS01'])
        print('下一步')
        return sumtip



