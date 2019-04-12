from common.box import  BasePage, YamlHelper


class CommonRecharge(BasePage):
    # 充值公共页面
    # 导入fusion文件中CommonRecharge
    config_dict_commonre = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['CommonRecharge']

    def login(self, row):
        print('开始进入登陆')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], row['username'])
        print(row['username'])
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], row['password'])
        print(row['password'])
        self.base_driver.type(self.config_dict_commonre['YZM'], row['yzm'])
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        print('等待')

        # 点击会员中心
        self.base_driver.click(self.config_dict_commonre['PERCENTER'])
        self.base_driver.forced_wait(1)
        self.base_driver.switch_to_window_by_index(2)

        print("会员")
        self.base_driver.forced_wait(5)

        # 跳转会员中心，fusion后台标签定位
        self.base_driver.click(self.config_dict_commonre['FUSIONBACK'])
        self.base_driver.forced_wait(1)
        #  点击财务中心
        self.base_driver.click(self.config_dict_commonre['FINANCIAL'])
        self.base_driver.forced_wait(5)
        print('点击财务中心')
        # # 点击充值
        self.base_driver.click(self.config_dict_commonre['RECHARGE'])
        self.base_driver.forced_wait(2)
        print('充值入款')

    def hyzx_cwzx_idem_rk(self, row):
        # 充值入款方式
        if row['pymethod'] == 'SUSU公司入款':
            self.base_driver.click(self.config_dict_commonre['SUSURECHARGE'])
        if row['pymethod'] == '支付宝转账':
            self.base_driver.click(self.config_dict_commonre['ALIPAY'])
        if row['pymethod'] == '公司入款':
            self.base_driver.click(self.config_dict_commonre['COMPANYDEPOSIT'])
        if row['pymethod'] == 'VIP代理充值':
            self.base_driver.click(self.config_dict_commonre['VIPAGENT'])
        print("选择充值入款方式")

    def cwbutton(self):
        # 下一步按钮
        cwb = self.base_driver.click(self.config_dict_commonre['CONETBUTTON'])
        print('进入充值页面')
        return cwb
