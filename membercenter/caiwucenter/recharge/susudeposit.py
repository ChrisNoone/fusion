from common.box import TestCase, BasePage, YamlHelper


class SuSuDeposit(BasePage):
    # susu公司入款
    # 导入fusion文件中SuSuDeposit
    config_dict_susudep = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['SuSuDeposit']

    def susudeposit(self, row):
        print("输入和选择金额")
        # self.base_driver.forced_wait(0.5)
        # 充值金额
        # if row['susuamount'] == '充值金额':
        #     self.base_driver.type(self.config_dict_susudep['REAMOUNT'], row['susuamount'])
        # 50,100,300,500,800,1000,2000,3000
        if row['susuamount'] == '50':
            self.base_driver.click(self.config_dict_susudep['50YUAN'])
        if row['susuamount'] == '100':
            self.base_driver.click(self.config_dict_susudep['100YUAN'])
        if row['susuamount'] == '300':
            self.base_driver.click(self.config_dict_susudep['300YUAN'])
        if row['susuamount'] == '500':
            self.base_driver.click(self.config_dict_susudep['500YUAN'])
        if row['susuamount'] == '800':
            self.base_driver.click(self.config_dict_susudep['800YUAN'])
        if row['susuamount'] == '1000':
            self.base_driver.click(self.config_dict_susudep['1000YUAN'])
        if row['susuamount'] == '2000':
            self.base_driver.click(self.config_dict_susudep['2000YUAN'])
        if row['susuamount'] == '3000':
            self.base_driver.click(self.config_dict_susudep['3000YUAN'])
        print('你选择的金额是' + row['susuamount'])

    def rechargemethod(self, row):
        # 充值银行
        # self.base_driver.forced_wait(0.5)
        if row['rechargemethod'] == '中国工商银行_susu':
            self.base_driver.click(self.config_dict_susudep['ICBC_SUSU'])
        if row['rechargemethod'] == '中国工商银行我测试啊':
            self.base_driver.click(self.config_dict_susudep['ICBC_MYTEST'])
        if row['rechargemethod'] == '中国工商银行李洁':
            self.base_driver.click(self.config_dict_susudep['ICBC_LEEJIE'])
        if row['rechargemethod'] == '中国光大银行':
            self.base_driver.click(self.config_dict_susudep['EVERBRIGHT'])
        if row['rechargemethod'] == '中国银行':
            self.base_driver.click(self.config_dict_susudep['CHINABANK'])
        if row['rechargemethod'] == '江苏银行-123':
            self.base_driver.click(self.config_dict_susudep['JIANGSU'])
        if row['rechargemethod'] == '恒丰银行':
            self.base_driver.click(self.config_dict_susudep['HENGFENG'])

        print('选择银行' + row['rechargemethod'])
        self.base_driver.forced_wait(0.5)

    def depoistname(self, row):
        print('进入存款信息')
        self.base_driver.forced_wait(5)


        # 存入时间
        # self.base_driver.type(self.config_dict_susudep['DEPOISTTIME'], row['depoisttime'])
        # 存款人姓名
        self.base_driver.type(self.config_dict_susudep['DEPOISTNAME'], row['depoistname'])
        # 存款金额
        # self.base_driver.type(self.config_dict_susudep['DEPOISTAMOUNT'], row['depoistamount'])

    def next_buttion(self):
        # 下一步
        nextbutton = self.base_driver.click(self.config_dict_susudep['NEXTBUTTON'])
        print('下一步')
        return nextbutton

    def coupon(self):
        # 优惠劵
        coupon = self.base_driver.click(self.config_dict_susudep['COUPON'])
        return coupon

    def get_ckmoney(self):
        # 充值金额不符合！
        ckmoney = self.base_driver.get_text(self.config_dict_susudep['AMOUNTMATCH'])
        return ckmoney

    def rechgebutton(self):
        # 确认存款
        nextbutton = self.base_driver.click(self.config_dict_susudep['SURE_MONEY_BUTTON'])
        print('下一步')
        # self.base_driver.forced_wait(10)
        return nextbutton

    def recharge_50(self):
        # 充值金额50
        self.base_driver.forced_wait(10)
        re50 = self.base_driver.get_text(self.config_dict_susudep['RECHANGE50'])
        print('下一步')

    def sum_tips(self):
        # 提交成功
        # self.base_driver.forced_wait(10)
        sumtip = self.base_driver.get_text(self.config_dict_susudep['SUMTIP01'])
        print('下一步')
        return sumtip

    def get_tips01(self):
        # 捕捉 充值金额
        # self.base_driver.forced_wait(10)
        sumtip = self.base_driver.get_text(self.config_dict_susudep['TIPS01'])
        print('下一步')
        return sumtip






