# coding: utf-8

from common.box import YamlHelper, BasePage
import time


class HomePageElement(BasePage):
    cd_home = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionHome']

    def free_trial(self):
        """
        免费试玩注册-登录流程
        :return: 登录后的用户栏信息
        """
        self.base_driver.click(self.cd_home['FREE_TRIAL']['A'])
        self.base_driver.click(self.cd_home['FREE_TRIAL']['BUTTON'])
        self.base_driver.explicitly_wait(self.cd_home['USERINFO'], 5)
        try:
            user_info = self.base_driver.get_text(self.cd_home['USERINFO'])
        except:
            user_info = ''
        return user_info

    def special_agent(self):
        """
        特殊代理登录流程
        :return: 登录后的用户栏信息
        """
        self.base_driver.click(self.cd_home['SPEAGENT']['A'])
        self.base_driver.type(self.cd_home['SPEAGENT']['USERNAME'], 'specialsuper')
        self.base_driver.type(self.cd_home['SPEAGENT']['PASSWORD'], 'a123456')
        time.sleep(1)
        self.base_driver.click(self.cd_home['SPEAGENT']['BUTTON'])
        self.base_driver.explicitly_wait(self.cd_home['USERINFO'], 5)
        try:
            user_info = self.base_driver.get_text(self.cd_home['USERINFO'])
        except:
            user_info = ''
        return user_info

    def help_center(self):
        """
        点击帮助中心
        """
        self.base_driver.click(self.cd_home['HELP'])

    def play_rule(self):
        """
        点击玩法
        """
        self.base_driver.click(self.cd_home['PLAY'])

    def infomation(self):
        """
        点击资讯
        """
        self.base_driver.click(self.cd_home['NEWS'])

    def sign(self):
        """
        点击注册按钮
        """
        self.base_driver.click(self.cd_home['SIGNUPBUTTON'])
        self.base_driver.forced_wait(2)

    def login(self, row):
        """
        登录流程
        :param row: 用例数据字典dict
        """
        self.base_driver.clear_cookies()
        self.base_driver.type(self.cd_home['USERNAME'], row['username'])
        self.base_driver.type(self.cd_home['PASSWORD'], row['password'])
        self.base_driver.type(self.cd_home['RECCODE'], row['yzm'])
        self.base_driver.click(self.cd_home['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        try:
            user_info = self.base_driver.get_text(self.cd_home['LOGINBUTTON'])
        except:
            user_info = ''
        return user_info

    def logout(self):
        """
        退出登录（登录状态下）
        """
        self.base_driver.click(self.cd_home['LOGOUT_BUTTON'])
        self.base_driver.forced_wait(4)

    def get_userinfo(self):
        """
        获取登录后的用户信息一栏
        :return:
        """
        self.base_driver.explicitly_wait(self.cd_home['USERINFO'], 5)
        try:
            info = self.base_driver.get_text(self.cd_home['USERINFO'])
        except:
            info = ''
        return info

    def user_center(self):
        self.base_driver.click(self.cd_home['PERCENTER'])
        time.sleep(2)

    def get_user_center_text(self):
        """
        获取会员中心按钮的文案（登录状态下）
        :return: 会员中心按钮文案
        """
        try:
            name = self.base_driver.get_text(self.cd_home['ASSERT_KUIYUANZHONGXIN'])
        except:
            name = ''
        return name

    def get_tips(self):
        """
        获取登录失败的提示文案
        :return: 登录失败提示文案
        """
        tips = self.base_driver.get_text(self.cd_home['ASSERT_TIPS'])
        self.base_driver.forced_wait(1)
        return tips

    def swt_frame(self):
        """
        跳转frame
        :return: 跳转之后的frame对象
        """
        swf = self.base_driver.switch_to_frame(self.cd_home['SWFRAME'])
        self.base_driver.forced_wait(3)
        return swf
