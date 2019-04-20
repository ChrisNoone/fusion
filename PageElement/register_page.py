# coding: utf-8

import time
from common.box import BasePage, YamlHelper


class RegisterPageElement(BasePage):
    config_dict_register = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionReg']

    def register(self):
        self.base_driver.explicitly_wait(self.config_dict_register['USERNAME'], 5)
        info = self.gen_user_info()
        self.logger.info(info)
        self.base_driver.type(self.config_dict_register['USERNAME'], info['username'])
        self.base_driver.type(self.config_dict_register['PASSWORD'], info['password'])
        if self.check_el_req(self.config_dict_register['TELEPHONE']):
            self.base_driver.type(self.config_dict_register['TELEPHONE'], info['telephone'])
        else:
            pass
        if self.check_el_req(self.config_dict_register['EMAIL']):
            self.base_driver.type(self.config_dict_register['EMAIL'], info['email'])
        else:
            pass
        if self.check_el_req(self.config_dict_register['RECCODE']):
            self.base_driver.type(self.config_dict_register['RECCODE'], info['reccode'])
        else:
            pass
        if self.check_el_req(self.config_dict_register['QQ']):
            self.base_driver.type(self.config_dict_register['QQ'], info['qq'])
        else:
            pass
        self.base_driver.type(self.config_dict_register['VERIFYCODE'], info['verifycode'])
        self.base_driver.click(self.config_dict_register['REGBUTTON'])
        self.base_driver.forced_wait(3)

    def register_data(self, row):
        #  进入注册页面
        #  用户名   6-16之间，由字母/数字/下划线组成6-16个字
        self.base_driver.type(self.config_dict_register['USERNAME'], row['username'])
        #  密码    长度为6位以上，由数字/字母/下划线组成
        self.base_driver.type(self.config_dict_register['PASSWORD'], row['password'])
        #  邮件
        self.base_driver.type(self.config_dict_register['EMAIL'], row['email'])
        #  推荐ID
        self.base_driver.type(self.config_dict_register['RECCODE'], row['tjid'])
        #  QQ
        self.base_driver.type(self.config_dict_register['QQ'], row['qq'])
        #  验证码
        self.base_driver.type(self.config_dict_register['VERIFYCODE'], row['yzm'])
        #  立即注册按钮
        self.base_driver.click(self.config_dict_register['REGBUTTON'])
        self.base_driver.forced_wait(3)

    def get_text_hy_sign(self):
        # 获取注册页面title
        hy_sign = self.base_driver.get_text(self.config_dict_register['REGTITLE'])
        return hy_sign

    @staticmethod
    def gen_user_info():
        """
        随机生成一组用户注册信息
        :return: type: dict
        """
        user = {
            'username': 'test' + str(time.time())[2:10],
            'password': 'pwd123456',
            'telephone': '130' + str(time.time())[2:10],
            'email': str(time.time())[2:10] + '@gmail.com',
            'reccode': '264622',
            'qq': str(time.time())[2:10],
            'verifycode': '1234'
        }
        return user

    def check_el_req(self, selector):
        try:
            el = self.base_driver.select_by_element(selector, './parent::div/preceding-sibling::div/span')
        except:
            el = ''

        if el:
            # 若input前有星号，代表是必填，为True
            return True
        else:
            # 若input前无星号，代表为非必填，为False
            return False
