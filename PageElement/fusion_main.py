from common.box import BasePage, YamlHelper
import os


class FusionMain(BasePage):
    # 导入fusion.yaml中的FusionMain
    print(os.getcwd())
    config_dict_fusionmain = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionMain']

    def main_menu(self, menus):

        # 首页
        # 主标题栏
        if menus == '首页':
            self.base_driver.click(self.config_dict_fusionmain['HOME'])
        if menus == '数字彩':
            self.base_driver.click(self.config_dict_fusionmain['LOTTERY'])
        if menus == '体彩':
            self.base_driver.click(self.config_dict_fusionmain['SPORT'])
        if menus == '电子游艺':
            self.base_driver.click(self.config_dict_fusionmain['GAME'])
        if menus == '手机购彩':
            self.base_driver.click(self.config_dict_fusionmain['PHONE'])
        if menus == '优惠活动':
            self.base_driver.click(self.config_dict_fusionmain['ACTIVITY'])
        if menus == '开奖公告':
            self.base_driver.click(self.config_dict_fusionmain['LOTTNOTE'])
        if menus == '走势图表':
            self.base_driver.click(self.config_dict_fusionmain['TRENDCHART'])
            self.base_driver.forced_wait(1)

    def main_items(self, items):
        # 小标题导航
        # 免费试玩
        if items == '免费试玩':
            self.base_driver.click(self.config_dict_fusionmain['FREETRY'])
        if items == '特殊代理':
            self.base_driver.click(self.config_dict_fusionmain['SPEAGENT'])
        if items == '加入代理':
            self.base_driver.click(self.config_dict_fusionmain['ADDAGENT'])
        if items == '帮助中心':
            self.base_driver.click(self.config_dict_fusionmain['FREETRY'])
        if items == '玩法':
            self.base_driver.click(self.config_dict_fusionmain['SPEAGENT'])
        if items == '资讯':
            self.base_driver.click(self.config_dict_fusionmain['NEWS'])
        if items == '快速充值通道':
            self.base_driver.click(self.config_dict_fusionmain['FASTCHANNEL'])
            self.base_driver.forced_wait(1)

        # 登陆注册前
    def login_before(self, row):
        # 用户名

        self.base_driver.type(self.config_dict_fusionmain['USERNAME'], row['username'])
        print("username")
        # 密码
        self.base_driver.type(self.config_dict_fusionmain['PASSERROR'], row['password'])
        # 验证码
        self.base_driver.type(self.config_dict_fusionmain['YZM'], row['yzm'])
        # 登陆按钮
        self.base_driver.click(self.config_dict_fusionmain['LOGINBUTTON'])

    def login_buttin(self, lb):
        # 注册按钮
        if lb == '注册':
            self.base_driver.click(self.config_dict_fusionmain['REGISTERED'])
        self.base_driver.forced_wait(1)
        print("登陆注册期前")

    # 登陆成功后
    def login_success(self, lg_succ):
        if lg_succ == '刷新':
            self.base_driver.click(self.config_dict_fusionmain['REFRESL'])
        if lg_succ == '会员中心':
            self.base_driver.click(self.config_dict_fusionmain['PERCENTER'])
        if lg_succ == '充值':
            self.base_driver.click(self.config_dict_fusionmain['DEPOIST'])
        if lg_succ == '提现':
            self.base_driver.click(self.config_dict_fusionmain['WITHDRAW'])
        if lg_succ == '投注记录':
            self.base_driver.click(self.config_dict_fusionmain['BETRECORD'])
        if lg_succ == '退出':
            self.base_driver.click(self.config_dict_fusionmain['DROPOUT'])
        self.base_driver.forced_wait(1)
        print("登陆注册后")

    # 断言
    def get_login_tips01(self):
        # 请填写用户名
        tip01 = self.base_driver.get_text(self.config_dict_fusionmain['FILLNAME'])
        return tip01

    def get_login_tips022(self):
        # 请填写密码
        tip021 = self.base_driver.get_text(self.config_dict_fusionmain['FILLNAME'])
        return tip021

    def get_login_tips02(self):
        # 登陆按钮
        tip02 = self.base_driver.get_text(self.config_dict_fusionmain['LOGINBUTTON'])
        print(tip02)
        return tip02


