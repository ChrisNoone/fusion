from common.box import TestCase, BasePage, YamlHelper


class FundPassword(BasePage):
    # 导入fusion文件中FundPassword
    config_dict_fundpassword = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['FundPassword']

    def fundpassword(self, row):
        # 资金密码
        # 密码规则：6位纯数字
        # 请输入新资金密码
        print('进入资金密码填写')
        print(row['tips'])
        self.base_driver.type(self.config_dict_fundpassword['NOWFUND'], row['nowfund'])
        self.base_driver.type(self.config_dict_fundpassword['NEWFUND'], row['newfund'])
        # 请再次输入新资金密码
        self.base_driver.type(self.config_dict_fundpassword['AGENTFUND'], row['agentfund'])
        print('请输入新资金密码：' + row['nowfund'])
        print('请输入新资金密码：' + row['newfund'])
        print('请再次输入新资金密码：' + row['agentfund'])

    def sub_button(self):
        # 确认按钮
        sub = self.base_driver.click(self.config_dict_fundpassword['SUMBITFUND'])
        return sub

    def get_tips(self):
        # 获取提示
        tps0 = self.base_driver.get_text(self.config_dict_fundpassword['ALLTIPS'])
        print('获取的提示' + tps0)
        return tps0

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

    def click_login(self):
        # 再次点击资金密码
        cl = self.base_driver.click(self.config_dict_fundpassword['FUND_PASSWORD'])
        return cl
