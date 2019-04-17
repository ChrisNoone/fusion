# coding: utf-8

from common.box import YamlHelper, BasePage


class RulePageElement(BasePage):
    cd_rule = YamlHelper().get_config_dict('./yaml/fusion.yaml')['FusionRule']

    def check_exist(self):
        self.base_driver.explicitly_wait(self.cd_rule['CQSSC'], 5)
        try:
            info = self.base_driver.get_text(self.cd_rule['CQSSC'])
        except:
            info = ''
        if info:
            return True
        else:
            return False
