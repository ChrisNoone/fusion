from common.box import TestCase, BasePage, YamlHelper


class WithdrawRecord(BasePage):
    # 导入fusion文件中WithdrawRecord
    config_dict_withdrawrecord = YamlHelper().get_config_dict('/fusion/fusion.yaml')['WithdrawRecord']

    def withdrawrecord(self):
        # 提款方式
        # 全部
        self.base_driver.type(self.config_dict_withdrawrecord['ALL'])
        # 提交
        self.base_driver.type(self.config_dict_withdrawrecord['ONLINE'])
        # 处理中
        self.base_driver.type(self.config_dict_withdrawrecord['TRANSFER'])
        # 确认
        self.base_driver.type(self.config_dict_withdrawrecord['SYSTEM'])
        # 取消
        self.base_driver.type(self.config_dict_withdrawrecord['ORDERNUM'])
        # 拒绝
        self.base_driver.type(self.config_dict_withdrawrecord['ONLINE'])
        # 请选择修改日期
        self.base_driver.type(self.config_dict_withdrawrecord['DATAW'])

    def withdraw_button(self):
        # 查询按钮
        withdraw = self.base_driver.click(self.config_dict_withdrawrecord['CHACKBUTTONW'])
        return withdraw

    def get_rech_tips01(self):
        # 没有更多的数据了
        tips01 = self.base_driver.click(self.config_dict_withdrawrecord['NODATA'])
        return tips01



