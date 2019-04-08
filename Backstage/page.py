from common.box import BasePage, YamlHelper


class Page(BasePage):
    # 充值公共页面
    # 导入fusion文件中CommonRecharge
    config_dict_page = YamlHelper().get_config_dict('/fusion/yaml/Page.yaml')['Page']

    def login(self):
        # 登陆
        self.base_driver.click(self.config_dict_page['ZHUCE'])
        self.base_driver.type(self.config_dict_page['USERNAME'], '123456763')
        self.base_driver.type(self.config_dict_page['PASSWORD'], 'lee123')
        self.base_driver.click(self.config_dict_page['YZM'])

    def chongzhi(self):
        # 点击充值文字
        self.base_driver.click(self.config_dict_page['CHONGZHI'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转充值页面')

    def alipay(self):
        # 点击充值文字
        self.base_driver.click(self.config_dict_page['ALIPAY'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转充值页面')

    def chongzhi50(self):
        # 点击选择50
        self.base_driver.click(self.config_dict_page['FITY'])
        # 选择银行
        self.base_driver.click(self.config_dict_page['BANK'])

    def dingdan(self):
        # 获取订单好
        s = self.base_driver.get_text(self.config_dict_page['DINGDAN'])
        news = s[4:]
        print('获取到的订单号' + news)
        print(news)
        # 点击充值记录
        self.base_driver.click(self.config_dict_page['RECODES'])
        # 请输入订单号
        self.base_driver.type(self.config_dict_page['SHURU'], news)
        # 点击查询按钮
        self.base_driver.click(self.config_dict_page['CHECK'])
        return s

    def tipsdingdanhao(self):
        # 列表中订单号
        t = self.base_driver.get_text(self.base_driver['DA'])
        return t

    def login04(self):
        print('开始进入登陆---直接点击提现')
        # 登陆

        self.base_driver.type(self.config_dict_page['USERNAME'], 'lee1000000')
        print(['username'])
        self.base_driver.type(self.config_dict_page['PASSWORD'], 'lee123')
        print(['password'])
        self.base_driver.type(self.config_dict_page['YZM'], '1')
        self.base_driver.click(self.config_dict_page['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        print('等待')

        # 点击提现文字
        self.base_driver.click(self.config_dict_page['TIXIANWENZI'])
        self.base_driver.switch_to_window_by_index(2)
        self.base_driver.forced_wait(5)
        print('跳转提现页面')

