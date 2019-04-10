from common.box import TestCase, BasePage, YamlHelper


class Withdraw(BasePage):
    # 导入fusion文件中Withdraw
    config_dict_withdraw = YamlHelper().get_config_dict('/fusion/fusion.yamlf')['Withdraw']

    def withdraw(self, row):
       # 提现金额
        self.base_driver.type(self.config_dict_withdraw['WITHDRAW'], row['withdraw'])
       # 资金密码
        self.base_driver.type(self.config_dict_withdraw['FUNDPASSWORD'], row['fundpassword'])

    def withdraw_button(self):
        # 提现按钮
        withdraw = self.base_driver.click(self.config_dict_withdraw['WITHDRAWBUTTON'])
        return withdraw

    def get_withdraw_tips01(self):
        # 金额格式错误
        tips01 = self.base_driver.click(self.config_dict_withdraw['AMOUNTERROR'])
        return tips01

    def get_withdraw_tips02(self):
        # 余额不足
        tips02 = self.base_driver.click(self.config_dict_withdraw['NOTENOUTH'])
        return tips02

    def get_withdraw_tips03(self):
        # 资金密码有6位数字组成
        tips03 = self.base_driver.click(self.config_dict_withdraw['PASSERROR'])
        return tips03

    def get_withdraw_tips04(self):
        # 提现过于频繁或重复提交,1分钟后再试
        tips04 = self.base_driver.click(self.config_dict_withdraw['PINFAN'])
        return tips04

    def get_withdraw_tips05(self):
        # 当前用户最低可提现金额为10.00元
        tips05 = self.base_driver.click(self.config_dict_withdraw['LOWEST'])
        return tips05

    def get_withdraw_tips06(self):
        # 提现周期内次数限制
        tips06 = self.base_driver.click(self.config_dict_withdraw['NUMLIMIT'])
        return tips06

    def get_withdraw_tips07(self):
        # 提现成功！
        tips07 = self.base_driver.click(self.config_dict_withdraw['WSUCCESS'])
        return tips07

    def checkbutton(self):
        # 查看稽查详情
        cb = self.base_driver.click(self.config_dict_withdraw['FUNDPASSWORD'])
        return cb



