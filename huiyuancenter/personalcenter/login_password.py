from common.box import TestCase, YamlHelper, BasePage


class LoginPassword(BasePage):
    # 导入fusion.yaml文件中的LoginPassword
    config_dict_loginpassword = YamlHelper().get_config_dict('/fusion/fusion.yamlf')['LoginPassword']

    def per_center(self, percenter):
        # 个人中心
        if percenter == '登陆密码':
            self.base_driver.click(self.config_dict_loginpassword['LOGIN_PASSWORD'])
        if percenter == '资金密码':
            self.base_driver.click(self.config_dict_loginpassword['FUND_PASSWORD'])
        if percenter == '我的银行卡':
            self.base_driver.click(self.config_dict_loginpassword['MY_CARD'])

    def percenter_login(self, row):
        # 登录密码
        # 密码规则：密码为6位以上，由数字/字母/下划线组成
        # 请输入原始密码
        self.base_driver.type(self.config_dict_loginpassword['OLDPASSWORD'], row['oldpassword'])
        # 请输入登陆密码
        self.base_driver.type(self.config_dict_loginpassword['NEWPASSWORD'], row['newpassword'])
        # 请输入确认密码':
        self.base_driver.type(self.config_dict_loginpassword['NEWPASSWORD1'], row['newpassword1'])

    def get_lp_tips0(self):

        # 旧密码不能为空
        tps0 = self.base_driver.get_text(self.config_dict_loginpassword['OLDPASSWORD_TIP'])
        return tps0

    def get_lp_tips1(self):
        # 密码不能为空
        tps1 = self.base_driver.get_text(self.config_dict_loginpassword['NEWPASSWORD_TIP'])
        return tps1

    def get_lp_tips2(self):
        # 密码确认不能为空
        tps2 = self.base_driver.get_text(self.config_dict_loginpassword['NEWPASSWORD1_TIP'])
        return tps2

    def get_lp_tips3(self):
        # 两次输入密码不一样
        tps3 = self.base_driver.get_text(self.config_dict_loginpassword['NEWPASSWORD2_TIP'])
        return tps3

    def get_lp_tips4(self):
        # 原密码不正确
        tps4 = self.base_driver.get_text(self.config_dict_loginpassword['OLDFAIL'])
        return tps4

    def get_lp_tips5(self):
        # 修改成功
        tps5 = self.base_driver.get_text(self.config_dict_loginpassword['CHANGER_SUCCESS'])
        return tps5



