from common.box import BasePage, YamlHelper


class CommonRecharge(BasePage):
    # 充值公共页面
    # 导入fusion文件中CommonRecharge
    config_dict_commonre = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['CommonRecharge']

    def login01(self, row):
        print('开始进入登陆--会员中心--充值')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], row['username'])
        print(row['username'])
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], row['password'])
        print(row['password'])
        self.base_driver.type(self.config_dict_commonre['YZM'], row['yzm'])
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        print('充值等待')

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

    def login02(self, row):
        print('开始进入登陆---直接点击充值')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], row['username'])
        print(row['username'])
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], row['password'])
        print(row['password'])
        self.base_driver.type(self.config_dict_commonre['YZM'], row['yzm'])
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        print('点击充值等待')

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

    def login03(self):
        print('开始进入登陆---直接点击充值')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], 'lee123456789')
        print('输入的用户名是:lee6281376')
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], 'lee123')
        print('输入的密  码是:lee123')
        self.base_driver.type(self.config_dict_commonre['YZM'], '1')
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(3)
        print('登陆等待')
      # 点击充值文字
        self.base_driver.click(self.config_dict_commonre['CHONGZHI'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转充值页面')

    def login031(self):
        print('开始进入登陆---直接点击充值')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], 'lee123456789')
        print('输入的用户名是:lee6281376')
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], 'lee123')
        print('输入的密  码是:lee123')
        self.base_driver.type(self.config_dict_commonre['YZM'], '1')
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(3)
        print('登陆等待')

        # 点击充值文字
        self.base_driver.click(self.config_dict_commonre['CHONGZHI'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转充值页面')

    def login032(self):

        print('开始进入登陆---直接点击会员中心')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], 'lee123456789')
        print('输入的用户名是:lee123456789')
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], 'lee123')
        print('输入的密  码是:lee123')
        self.base_driver.type(self.config_dict_commonre['YZM'], '1')
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(4)
        print('登陆等待')

        # 点击会员中心文字
        self.base_driver.click(self.config_dict_commonre['PERCENTER'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转登陆页面')

    def login04(self):
        print('开始进入登陆---直接点击提现')
        # 登陆

        self.base_driver.type(self.config_dict_commonre['USERNAME'], 'lee1000000')
        print(['username'])
        self.base_driver.type(self.config_dict_commonre['PASSWORD'], 'lee123')
        print(['password'])
        self.base_driver.type(self.config_dict_commonre['YZM'], '1')
        self.base_driver.click(self.config_dict_commonre['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        print('提现等待')

        # 点击提现文字
        self.base_driver.click(self.config_dict_commonre['TIXIANWENZI'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转提现页面')

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
        self.base_driver.forced_wait(1)

    def cwbutton(self):
        # 下一步按钮
        cwb = self.base_driver.click(self.config_dict_commonre['CONETBUTTON'])
        print('进入充值页面')
        return cwb
