from common.box import BasePage, YamlHelper


class CompanyDeposit(BasePage):
    # 公司入款
    # 导入fusion文件中CommonRecharge
    config_dict_companyde = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['CompanyDeposit']

    def companydeposit(self, row):
        print("输入和选择金额")
        # self.base_driver.forced_wait(0.5)
        # 充值金额
        if row['susuamount'] == '充值金额':
            self.base_driver.get_text(self.config_dict_companyde['REAMOUNT'])
        # 50,100,300,500,800,1000,2000,3000
        if row['susuamount'] == '50':
            self.base_driver.click(self.config_dict_companyde['50YUAN'])
        if row['susuamount'] == '100':
            self.base_driver.click(self.config_dict_companyde['100YUAN'])
        if row['susuamount'] == '300':
            self.base_driver.click(self.config_dict_companyde['300YUAN'])
        if row['susuamount'] == '500':
            self.base_driver.click(self.config_dict_companyde['500YUAN'])
        if row['susuamount'] == '800':
            self.base_driver.click(self.config_dict_companyde['800YUAN'])
        if row['susuamount'] == '1000':
            self.base_driver.click(self.config_dict_companyde['1000YUAN'])
        if row['susuamount'] == '2000':
            self.base_driver.click(self.config_dict_companyde['2000YUAN'])
        if row['susuamount'] == '3000':
            self.base_driver.click(self.config_dict_companyde['3000YUAN'])
        print('你选择的金额是' + row['susuamount'])

    def comde_bank(self, row):
        # 充值银行
        if row['rechargemethod'] == '中国工商银行我测试啊':
            self.base_driver.click(self.config_dict_companyde['ICBC_MYTEST'])
        if row['rechargemethod'] == '中国工商银行李洁':
            self.base_driver.click(self.config_dict_companyde['ICBC_LEEJIE'])
        if row['rechargemethod'] == '中国光大银行':
            self.base_driver.click(self.config_dict_companyde['EVERBRIGHT'])
        if row['rechargemethod'] == '中国工商银行_susu':
            self.base_driver.click(self.config_dict_companyde['ICBC_SUSU'])
        if row['rechargemethod'] == '中国银行':
            self.base_driver.click(self.config_dict_companyde['CHINABANK'])
        if row['rechargemethod'] == '江苏银行-123':
            self.base_driver.click(self.config_dict_companyde['JIANGSU'])
        if row['rechargemethod'] == '恒丰银行':
            self.base_driver.click(self.config_dict_companyde['HENGFENG'])
        self.base_driver.forced_wait(0.5)
        print('选择银行' + row['rechargemethod'])

    def depoistname(self, row):

        # 存入时间
        self.base_driver.click(self.config_dict_companyde['DEPOISTTIME'], row['depoisttime'])
        # 存款人姓名
        self.base_driver.click(self.config_dict_companyde['DEPOISTNAME'], row['depoistname'])
        # 存款金额
        self.base_driver.click(self.config_dict_companyde['DEPOISTAMOUNT'], row['depoistamount'])

    def next_buttion(self):
        # 下一步按钮
        nextbutton = self.base_driver.click(self.config_dict_companyde['NEXTBUTTON'])
        print('点击下一步')
        return nextbutton

    def coupon(self):
        # 优惠劵
        coupon = self.base_driver.click(self.config_dict_companyde['COUPON'])
        return coupon

    def ckmoney(self):
        # 充值金额不符合！
        ckmoney = self.base_driver.click(self.config_dict_companyde['AMOUNTMATCH'])
        return ckmoney

    def get_tips(self):
        # 捕捉提示信息
        # self.base_driver.forced_wait(10)
        sumtip = self.base_driver.get_text(self.config_dict_companyde['TIPS'])
        print('下一步')
        return sumtip

    def get_tips02(self):
        # 捕捉 充值金额
        # self.base_driver.forced_wait(10)
        sumtip = self.base_driver.get_text(self.config_dict_companyde['TIPS02'])
        print('下一步')
        return sumtip



