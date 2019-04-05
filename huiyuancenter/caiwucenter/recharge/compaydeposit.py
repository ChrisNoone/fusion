from common.box import BasePage, YamlHelper


class CompanyDeposit(BasePage):
    # 公司入款
    # 导入fusion文件中CommonRecharge
    config_dict_companyde = YamlHelper().get_config_dict('/fusion/fusion.yaml')['CompanyDeposit']

    def companydeposit(self, companyde):
        # 充值金额
        if companyde == '充值金额':
            self.base_driver.get_text(self.config_dict_companyde['REAMOUNT'])
        # 50,100,300,500,800,1000,2000,3000
        if companyde == '50':
            self.base_driver.click(self.config_dict_companyde['50YUAN'])
        if companyde == '100':
            self.base_driver.click(self.config_dict_companyde['100YUAN'])
        if companyde == '300':
            self.base_driver.click(self.config_dict_companyde['300YUAN'])
        if companyde == '500':
            self.base_driver.click(self.config_dict_companyde['500YUAN'])
        if companyde == '800':
            self.base_driver.click(self.config_dict_companyde['800YUAN'])
        if companyde == '1000':
            self.base_driver.click(self.config_dict_companyde['1000YUAN'])
        if companyde == '2000':
            self.base_driver.click(self.config_dict_companyde['2000YUAN'])
        if companyde == '3000':
            self.base_driver.click(self.config_dict_companyde['3000YUAN'])

    def comde_bank(self, rechargemethod):
        # 充值银行
        if rechargemethod == '中国工商银行_susu':
            self.base_driver.click(self.config_dict_companyde['ICBC_SUSU'])
        if rechargemethod == '中国工商银行我测试啊':
            self.base_driver.click(self.config_dict_companyde['ICBC_MYTEST'])
        if rechargemethod == '中国工商银行李洁':
            self.base_driver.click(self.config_dict_companyde['ICBC_LEEJIE'])
        if rechargemethod == '中国光大银行':
            self.base_driver.click(self.config_dict_companyde['EVERBRIGHT'])
        if rechargemethod == '中国银行':
            self.base_driver.click(self.config_dict_companyde['CHINABANK'])
        if rechargemethod == '江苏银行-123':
            self.base_driver.click(self.config_dict_companyde['JIANGSU'])
        if rechargemethod == '恒丰银行':
            self.base_driver.click(self.config_dict_companyde['HENGFENG'])

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
        return nextbutton

    def coupon(self):
        # 优惠劵
        coupon = self.base_driver.click(self.config_dict_companyde['COUPON'])
        return coupon

    def ckmoney(self):
        # 充值金额不符合！
        ckmoney = self.base_driver.click(self.config_dict_companyde['AMOUNTMATCH'])
        return ckmoney




