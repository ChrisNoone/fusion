from common.box import TestCase, BasePage, YamlHelper


class Everyday(BasePage):
    # 导入fusion.yaml文件中Everyday
    config_dict_everyday = YamlHelper().get_config_dict('/fusion/fusion.yaml')['Everyday']

    def personalcenter(self):
        # 每日签到
        self.base_driver.click(self.config_dict_everyday['EVERY'])

    def percenter_login(self, perclogin):
        # 立即签到
        self.base_driver.click(self.config_dict_everyday['NOW'])
        # 第一天
        self.base_driver.click(self.config_dict_everyday['ONE'])
        # 第二天
        self.base_driver.click(self.config_dict_everyday['TWO'])
        # 第三天
        self.base_driver.click(self.config_dict_everyday['THREE'])
        # 第四天
        self.base_driver.click(self.config_dict_everyday['FORTH'])
        # 第五天
        self.base_driver.click(self.config_dict_everyday['FIVE'])
        # 第六天
        self.base_driver.click(self.config_dict_everyday['SIX'])
        # 第七天
        self.base_driver.click(self.config_dict_everyday['SEVERN'])
        # 第八天
        self.base_driver.click(self.config_dict_everyday['EIGHT'])

    def get_tips(self):
        # 今日已签到
        tips = self.base_driver.get_text(self.config_dict_everyday['TODAY'])
        self.base_driver.forced_wait(1)
        return tips




