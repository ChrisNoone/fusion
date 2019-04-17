# coding: utf-8

from common.box import YamlHelper, BasePage


class HelpPageElement(BasePage):
    cd_help = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionHelp']

    def check_exist(self):
        self.base_driver.explicitly_wait(self.cd_help['SUBNAV'], 5)
        try:
            info = self.base_driver.get_text(self.cd_help['SUBNAV'])
        except:
            info = ''
        if info:
            return True
        else:
            return False
