from common.box import BasePage, YamlHelper


class Lottery(BasePage):
    # 充值公共页面
    # 导入fusion文件中CommonRecharge
    config_dict_lottery = YamlHelper().get_config_dict('/fusion/yaml/lottery_marksix.yaml')['Lottery']

    def login(self):
        # 登陆
        self.base_driver.type(self.config_dict_lottery['USERNAME'], 'lee123456789')
        self.base_driver.type(self.config_dict_lottery['PASSWORD'], 'lee123')
        self.base_driver.type(self.config_dict_lottery['YZM'], '1')
        self.base_driver.click(self.config_dict_lottery['LOGINBUTTON'])
        self.base_driver.forced_wait(3)
        # 点击数字彩
        self.base_driver.click(self.config_dict_lottery['LOTTERY'])
        self.base_driver.forced_wait(3)
        self.base_driver.switch_to_window_by_index(2)

    def marksix(self):
        # 选择六合彩
        self.base_driver.click(self.config_dict_lottery['MARKSIX'])
        # 选择分分六合彩
        self.base_driver.click(self.config_dict_lottery['MARKSIX_MIN'])

        self.base_driver.forced_wait(3)







