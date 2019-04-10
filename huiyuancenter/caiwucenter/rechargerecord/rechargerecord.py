from common.box import TestCase, BasePage, YamlHelper


class RechargeRecord(BasePage):
    # 导入fusion文件中RechargeRecord
    config_dict_rechargerecord = YamlHelper().get_config_dict('/fusion/fusion.yamlf')['RechargeRecord']

    def rechargerecord(self):
        # 充值方式
        # 全部
        self.base_driver.type(self.config_dict_rechargerecord['ALL'])
        # 在线充值
        self.base_driver.type(self.config_dict_rechargerecord['ONLINE'])
        # 转账汇款
        self.base_driver.type(self.config_dict_rechargerecord['TRANSFER'])
        # 系统充值
        self.base_driver.type(self.config_dict_rechargerecord['SYSTEM'])
        # 红包领取
        self.base_driver.type(self.config_dict_rechargerecord['ORDERNUM'])
        # 请输入订单号
        self.base_driver.type(self.config_dict_rechargerecord['ONLINE'])
        # 请选择修改日期
        self.base_driver.type(self.config_dict_rechargerecord['DATAR'])

    def rech_button(self):
        # 查询按钮
        withdraw = self.base_driver.click(self.config_dict_rechargerecord['CHACKBUTTONR'])
        return withdraw

    def get_rech_tips01(self):
        # orderNo必须是数字
        tips01 = self.base_driver.click(self.config_dict_rechargerecord['ORDERNO'])
        return tips01

    def get_rech_tips02(self):
        # 没有更多的数据了
        tips02 = self.base_driver.click(self.config_dict_rechargerecord['NODATAR'])
        return tips02



