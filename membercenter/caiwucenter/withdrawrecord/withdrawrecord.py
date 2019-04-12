from common.box import TestCase, BasePage, YamlHelper


class WithdrawRecord(BasePage):

    # 提现记录
    # 导入fusion文件中WithdrawRecord
    config_dict_withdrawrecord = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['WithdrawRecord']

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

    def ordernumber(self, row):
        #  请输入订单号
        order = row['ordernum']
        print('没切片前是：      '+row['ordernum'])
        # 切掉表格的第一为N
        neworder = order[1:]
        self.base_driver.type(self.config_dict_withdrawrecord['ORDERNUM'], neworder)
        # self.base_driver.type(self.config_dict_rechargerecord['ORDERNUM'], row['ordernum'])
        # print('输入中的订单号是' + row['ordernum'])
        print('输入中的订单号是：   ' + neworder)
        print(neworder)

    def get_rech_tips03(self):
        # 列表中的订单号
        # 增加N跟数据表格匹配
        tips02 = self.base_driver.get_text(self.config_dict_withdrawrecord['ORDERNUMLIST'])
        tips03 = 'N' + tips02
        print('列表中的订单号是' + tips03)
        return tips03


