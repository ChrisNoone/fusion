from common.box import BasePage, YamlHelper


class FusionHallLogin(BasePage):
    # 导入fusion.yaml中的FusionMain
    config_dict_fulottery = YamlHelper().get_config_dict('/fusion/fusion.yaml')['FusionHallLogin']

    # 进入购彩大厅后的登陆注册
    def menu(self, menu):
        # 登陆页面、会员注册
        if menu == '登陆页面':
            self.base_driver.click(self.config_dict_fulottery['LOGINPAGE'])
        if menu == '会员注册':
            self.base_driver.click(self.config_dict_fulottery['MEMBERPAGE'])

    def loginpage(self, row):
        # 用户账号
        self.base_driver.get_text(self.config_dict_fulottery['USERNAME'], row['username'])
        # 密码
        self.base_driver.get_text(self.config_dict_fulottery['PASSWORD'], row['password'])
        # 验证码
        self.base_driver.get_text(self.config_dict_fulottery['YZM'], row['yzm'])
        # 登陆按钮
        self.base_driver.click(self.config_dict_fulottery['FASTTHREE'])
        self.base_driver.forced_wait(1)

    def memberpage(self, row):
        # 用户账号
        self.base_driver.get_text(self.config_dict_fulottery['USERNAME'], row['usernam'])
        # 密码
        self.base_driver.get_text(self.config_dict_fulottery['PASSWORD'], row['password'])
        # 邮箱
        self.base_driver.get_text(self.config_dict_fulottery['EMAL'], row['email'])
        # 推荐人ID
        self.base_driver.get_text(self.config_dict_fulottery['REFFERID'], row['refferid'])
        # QQ号码
        self.base_driver.get_text(self.config_dict_fulottery['QQNUMBER'], row['qqnumber'])
        # 验证码
        self.base_driver.get_text(self.config_dict_fulottery['YZM'], row['yzm'])
        # 立即注册
        self.base_driver.click(self.config_dict_fulottery['SIGNUP'])