# coding: utf-8

from common.box import BasePage, YamlHelper


class RegisterPageElement(BasePage):
    config_dict_register = YamlHelper().get_config_dict('./yaml/fusion.yaml')['Register']

    def register(self, row):
        #  进入注册页面
        #  用户名   6-16之间，由字母/数字/下划线组成6-16个字
        self.base_driver.type(self.config_dict_register['USERNAME'], row['username'])
        #  密码    长度为6位以上，由数字/字母/下划线组成
        self.base_driver.type(self.config_dict_register['PASSWORD'], row['password'])
        #  邮件
        self.base_driver.type(self.config_dict_register['EMAIL'], row['email'])
        #  推荐ID
        self.base_driver.type(self.config_dict_register['TJID'], row['tjid'])
        #  QQ
        self.base_driver.type(self.config_dict_register['QQNAME'], row['qq'])
        #  验证码
        self.base_driver.type(self.config_dict_register['YZM'], row['yzm'])
        #  立即注册按钮
        self.base_driver.click(self.config_dict_register['BUTTON'])
        self.base_driver.forced_wait(3)

    def get_text_hy_sign(self):
        # 注册不成功 获取注册按钮
        hy_sign = self.base_driver.get_text(self.config_dict_register['HYSIGN'])
        return hy_sign

    def get_yzm_tip(self):
        self.base_driver.forced_wait(4)
        # 注册不成功 获取验证码
        hy_sign = self.base_driver.get_text(self.config_dict_register['YZMTPS'])
        self.base_driver.forced_wait(4)

        return hy_sign
