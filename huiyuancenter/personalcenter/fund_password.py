from common.box import TestCase, BasePage, YamlHelper


class FundPassword(BasePage):
    # 导入fusion文件中FundPassword
    config_dict_fundpassword = YamlHelper().get_config_dict('/fusion/fusion.yamlf')['FundPassword']

    def fundpassword(self, row):
        # 资金密码
        # 密码规则：6位纯数字
        # 请输入新资金密码
        self.base_driver.type(self.config_dict_fundpassword['NEWFUND'], row['newfund'])
        # 请再次输入新资金密码
        self.base_driver.type(self.config_dict_fundpassword['AGENTFUND    '], row['agentfund'])



    def get_lp_tips0(self):

        # 新资金密码不能为空
        tps0 = self.base_driver.get_text(self.config_dict_fundpassword['NEWNULL'])
        return tps0

    def get_lp_tips1(self):
        # 旧密码不能为空
        tps1 = self.base_driver.get_text(self.config_dict_fundpassword['OLDNULL'])
        return tps1

    def get_lp_tips2(self):
        # 旧密码错误
        tps2 = self.base_driver.get_text(self.config_dict_fundpassword['OLDERROR'])
        return tps2

    def get_lp_tips3(self):
        # 两次输入密码不一致
        tps3 = self.base_driver.get_text(self.config_dict_fundpassword['PSDIFF'])
        return tps3

    def get_lp_tips4(self):
        # 修改成功
        tps4 = self.base_driver.get_text(self.config_dict_fundpassword['CH_SUCCESS'])
        return tps4

