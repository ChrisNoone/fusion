from common.box import YamlHelper, BasePage
import os


class FusionLoginPage(BasePage):

    path = os.path.split(os.path.abspath(__file__))[0]
    config_dict_loginpage = YamlHelper().get_config_dict('../yamlf/fusion.yaml')['FusionLoginPage']
    # print('进入FusionLoginPage')

    def login(self, row):
        # '''登录业务流程'''
        self.base_driver.clear_cookies(self.config_dict_loginpage['LOGIN_USERNAME'])
        self.base_driver.type(self.config_dict_loginpage['LOGIN_USERNAME'], row['username'])
        self.base_driver.type(self.config_dict_loginpage['LOGIN_PASSWORD'], row['password'])
        self.base_driver.type(self.config_dict_loginpage['LOGIN_YZM'], row['yzm'])
        self.base_driver.click(self.config_dict_loginpage['LOGIN_BUTTON'])
        self.base_driver.forced_wait(4)
        print("获取数据完毕")

    def sign(self):
        # 注册流程
        self.base_driver.click(self.config_dict_loginpage['SIGN_BUTTON'])
        self.base_driver.forced_wait(2)

    def swtframe(self):
        # 跳转
        swf = self.base_driver.switch_to_frame(self.config_dict_loginpage['SWFRAME'])
        self.base_driver.forced_wait(3)
        return swf

    def logout(self):
        # 退出系统
        self.base_driver.click(self.config_dict_loginpage['LOGOUT_BUTTON'])
        self.base_driver.forced_wait(4)

    def get_username(self):
        # 获取登录成功后的会员中心
        name = self.base_driver.get_text(self.config_dict_loginpage['ASSERT_KUIYUANZHONGXIN'])
        return name

    def get_tips(self):
         # 获取登录失败提示语
        tips = self.base_driver.get_text(self.config_dict_loginpage['ASSERT_TIPS'])
        self.base_driver.forced_wait(1)
        return tips


