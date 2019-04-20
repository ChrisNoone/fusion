# coding: utf-8

from common.box import YamlHelper, BasePage
import time


class UserCenterPageElement(BasePage):
    cd = YamlHelper().get_config_dict('./yaml/user_center.yaml')['UserCenter']

    def check_exist(self):
        self.base_driver.explicitly_wait(self.cd['TAB_GRZX'], 5)
        try:
            info = self.base_driver.get_text(self.cd['TAB_GRZX'])
        except:
            info = ''
        if info:
            return True
        else:
            return False

    def click_tab(self, tab_name):
        if tab_name == '个人中心':
            self.base_driver.click(self.cd['TAB_GRZX'])
        elif tab_name == '财务中心':
            self.base_driver.click(self.cd['TAB_CWZX'])
        elif tab_name == '代理中心':
            self.base_driver.click(self.cd['TAB_DLZX'])
        elif tab_name == '电子游艺':
            self.base_driver.click(self.cd['TAB_DZYY'])
        elif tab_name == '交易记录':
            self.base_driver.click(self.cd['TAB_JYJL'])
        elif tab_name == '信息公告':
            self.base_driver.click(self.cd['TAB_XXGG'])
        elif tab_name == '帮助反馈':
            self.base_driver.click(self.cd['TAB_BZFK'])
        elif tab_name == '我的优惠券':
            self.base_driver.click(self.cd['TAB_WDYHQ'])
        else:
            self.logger.error('%s: 菜单不存在' % tab_name)
