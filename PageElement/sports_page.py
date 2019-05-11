# coding: utf-8

from common.box import YamlHelper, BasePage
import time


class SportsPageElement(BasePage):
    cd_sports = YamlHelper().get_config_dict('./yaml/sports_center.yaml')['SPORTS']

    def close_dialog(self):
        self.base_driver.explicitly_wait(self.cd_sports['CLOSEDIALOG'], 5)
        self.base_driver.click(self.cd_sports['CLOSEDIALOG'])

