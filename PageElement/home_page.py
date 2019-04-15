# coding: utf-8

from common.box import YamlHelper, BasePage
import time


class HomePageElement(BasePage):
    config_dict_login = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionHome']

    def free_trial(self):
        self.base_driver.click(self.config_dict_login['FREE_TRIAL']['A'])
        self.base_driver.click(self.config_dict_login['FREE_TRIAL']['BUTTON'])
        time.sleep(2)
        try:
            user_info = self.base_driver.get_text(self.config_dict_login['USERINFO'])
        except:
            user_info = ''
        return user_info

    def sign(self):
        """
        点击注册按钮
        """
        self.base_driver.click(self.config_dict_login['SIGNUPBUTTON'])
        self.base_driver.forced_wait(2)

    def swt_frame(self):
        """
        跳转frame
        :return: 跳转之后的frame对象
        """
        swf = self.base_driver.switch_to_frame(self.config_dict_login['SWFRAME'])
        self.base_driver.forced_wait(3)
        return swf

    def logout(self):
        """
        退出登录（登录状态下）
        """
        self.base_driver.click(self.config_dict_login['LOGOUT_BUTTON'])
        self.base_driver.forced_wait(4)

    def get_user_center_text(self):
        """
        获取会员中心按钮的文案（登录状态下）
        :return: 会员中心按钮文案
        """
        try:
            name = self.base_driver.get_text(self.config_dict_login['ASSERT_KUIYUANZHONGXIN'])
        except:
            name = ''
        return name

    def get_tips(self):
        """
        获取登录失败的提示文案
        :return: 登录失败提示文案
        """
        tips = self.base_driver.get_text(self.config_dict_login['ASSERT_TIPS'])
        self.base_driver.forced_wait(1)
        return tips

    def login(self, row):
        """
        登录流程
        :param row: 用例数据字典dict
        """
        self.base_driver.clear_cookies()
        self.base_driver.type(self.config_dict_login['USERNAME'], row['username'])
        self.base_driver.type(self.config_dict_login['PASSWORD'], row['password'])
        self.base_driver.type(self.config_dict_login['RECCODE'], row['yzm'])
        self.base_driver.click(self.config_dict_login['LOGINBUTTON'])
        self.base_driver.forced_wait(2)
        try:
            user_info = self.base_driver.get_text(self.config_dict_login['LOGINBUTTON'])
        except:
            user_info = ''
        return user_info


"""
class HomeMainElement(BasePage):
    config_dict_fusion_main = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionMain']

    def main_menu(self, menus):
        # 首页
        # 主标题栏
        if menus == '首页':
            self.base_driver.click(self.config_dict_fusion_main['HOME'])
        if menus == '数字彩':
            self.base_driver.click(self.config_dict_fusion_main['LOTTERY'])
        if menus == '体彩':
            self.base_driver.click(self.config_dict_fusion_main['SPORT'])
        if menus == '电子游艺':
            self.base_driver.click(self.config_dict_fusion_main['GAME'])
        if menus == '手机购彩':
            self.base_driver.click(self.config_dict_fusion_main['PHONE'])
        if menus == '优惠活动':
            self.base_driver.click(self.config_dict_fusion_main['ACTIVITY'])
        if menus == '开奖公告':
            self.base_driver.click(self.config_dict_fusion_main['LOTTNOTE'])
        if menus == '走势图表':
            self.base_driver.click(self.config_dict_fusion_main['TRENDCHART'])
            self.base_driver.forced_wait(1)

    def main_items(self, items):
        # 小标题导航
        # 免费试玩
        if items == '免费试玩':
            self.base_driver.click(self.config_dict_fusion_main['FREETRY'])
        if items == '特殊代理':
            self.base_driver.click(self.config_dict_fusion_main['SPEAGENT'])
        if items == '加入代理':
            self.base_driver.click(self.config_dict_fusion_main['ADDAGENT'])
        if items == '帮助中心':
            self.base_driver.click(self.config_dict_fusion_main['FREETRY'])
        if items == '玩法':
            self.base_driver.click(self.config_dict_fusion_main['SPEAGENT'])
        if items == '资讯':
            self.base_driver.click(self.config_dict_fusion_main['NEWS'])
        if items == '快速充值通道':
            self.base_driver.click(self.config_dict_fusion_main['FASTCHANNEL'])
            self.base_driver.forced_wait(1)

        # 登陆注册前

    def login_before(self, row):
        # 用户名
        self.base_driver.type(self.config_dict_fusion_main['USERNAME'], row['username'])
        # 密码
        self.base_driver.type(self.config_dict_fusion_main['PASSERROR'], row['password'])
        # 验证码
        self.base_driver.type(self.config_dict_fusion_main['YZM'], row['yzm'])
        # 登陆按钮
        self.base_driver.click(self.config_dict_fusion_main['LOGINBUTTON'])

    def login_buttin(self, lb):
        # 注册按钮
        if lb == '注册':
            self.base_driver.click(self.config_dict_fusion_main['REGISTERED'])
        self.base_driver.forced_wait(1)
        print("登陆注册期前")

    # 登陆成功后
    def login_success(self, lg_succ):
        if lg_succ == '刷新':
            self.base_driver.click(self.config_dict_fusion_main['REFRESL'])
        if lg_succ == '会员中心':
            self.base_driver.click(self.config_dict_fusion_main['PERCENTER'])
        if lg_succ == '充值':
            self.base_driver.click(self.config_dict_fusion_main['DEPOIST'])
        if lg_succ == '提现':
            self.base_driver.click(self.config_dict_fusion_main['WITHDRAW'])
        if lg_succ == '投注记录':
            self.base_driver.click(self.config_dict_fusion_main['BETRECORD'])
        if lg_succ == '退出':
            self.base_driver.click(self.config_dict_fusion_main['DROPOUT'])
        self.base_driver.forced_wait(1)
        print("登陆注册后")

    # 断言
    def get_login_tips01(self):
        # 请填写用户名
        tip01 = self.base_driver.get_text(self.config_dict_fusion_main['FILLNAME'])
        return tip01

    def get_login_tips022(self):
        # 请填写密码
        tip021 = self.base_driver.get_text(self.config_dict_fusion_main['FILLNAME'])
        return tip021

    def get_login_tips02(self):
        # 登陆按钮
        tip02 = self.base_driver.get_text(self.config_dict_fusion_main['LOGINBUTTON'])
        return tip02
"""