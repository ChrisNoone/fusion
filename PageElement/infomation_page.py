# coding: utf-8

from common.box import YamlHelper, BasePage


class InfoPageElement(BasePage):
    cd_info = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionIntomation']

    def check_exist(self):
        self.base_driver.explicitly_wait(self.cd_info['SUBNAV'], 5)
        try:
            info = self.base_driver.get_text(self.cd_info['SUBNAV'])
        except:
            info = ''
        if info:
            return True
        else:
            return False
