

from common.box import BasePage, YamlHelper
import os


class HomeRegistered(BasePage):
    # 导入fusion.yaml中Registered
    # print(os.getcwd())
    config_dict_regiseter = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['HomeRegistered']

    def homeregistered(self, row):
        print('进入注册页面')
        #  进入注册页面
        #  用户名   6-16之间，由字母/数字/下划线组成6-16个字

        # self.base_driver.clear(self.config_dict_regiseter['USERNAME'])
        print('11111111')
        self.base_driver.type(self.config_dict_regiseter['USERNAME'], row['username'])
        print('获取到的用户名是' + row['username'])
        # self.base_driver.clear(self.config_dict_regiseter['USERNAME'])
        #  密码    长度为6位以上，由数字/字母/下划线组成
        self.base_driver.type(self.config_dict_regiseter['PASSWORD'], row['password'])
        print('获取到的密码是' + row['password'])
        self.base_driver.forced_wait(1)
        #  邮件
        self.base_driver.type(self.config_dict_regiseter['EMAIL'], row['email'])
        #  推荐ID
        self.base_driver.type(self.config_dict_regiseter['TJID'], row['tjid'])
        #  QQ
        self.base_driver.type(self.config_dict_regiseter['QQNAME'], row['qq'])
        #  验证码
        self.base_driver.type(self.config_dict_regiseter['YZM'], row['yzm'])
        #  立即注册按钮
        self.base_driver.click(self.config_dict_regiseter['BUTTON'])
        self.base_driver.forced_wait(1)

        print('点击注册按钮')

    def get_text_hysign(self):
        # 注册不成功 获取注册按钮
        hysign = self.base_driver.get_text(self.config_dict_regiseter['HYSIGN'])
        print('获取到注册按钮信息')

        return hysign

    def get_yzmtip(self):
        # 注册不成功 获取验证码
        hysign = self.base_driver.get_text(self.config_dict_regiseter['YZMTPS'])
        return hysign

    def get_yzmtip01(self):
        # 注册不成功 获取验证码
        tips01 = self.base_driver.get_text(self.config_dict_regiseter['TIPS'])
        return tips01



