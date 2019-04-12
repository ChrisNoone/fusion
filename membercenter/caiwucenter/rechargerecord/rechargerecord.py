from common.box import TestCase, BasePage, YamlHelper


class RechargeRecord(BasePage):
    # 导入fusion文件中RechargeRecord
    config_dict_rechargerecord = YamlHelper().get_config_dict('/fusion/yaml/fusion.yaml')['RechargeRecord']

    def rechargerecord(self, row):
        # 充值方式

        # 全部
        self.base_driver.select_by_value(self.config_dict_rechargerecord['ALL'], row['all'])

        # 在线充值
        self.base_driver.select_by_value(self.config_dict_rechargerecord['ONLINE'], row['online'] )

        # 转账汇款
        self.base_driver.select_by_value(self.config_dict_rechargerecord['TRANSFER'], row['transfer'])

        # 系统充值
        self.base_driver.select_by_value(self.config_dict_rechargerecord['SYSTEM'], row['system'])

        # 红包领取
        self.base_driver.select_by_value(self.config_dict_rechargerecord['GETRED'], row['getbag'])

        self.base_driver.forced_wait(4)
        print("选择充值方式" + row['rechmethod'])
    #
    # def rechargerecord(self, row):
    #     # 充值方式
    #     if row['rechmethod'] == '全部':
    #         # 全部
    #         self.base_driver.select_by_value(self.config_dict_rechargerecord['ALL'])
    #     if row['rechmethod'] == '在线充值':
    #         # 在线充值
    #         self.base_driver.select_by_value(self.config_dict_rechargerecord['ONLINE'])
    #     if row['rechmethod'] == '转账汇款':
    #         # 转账汇款
    #         self.base_driver.select_by_value(self.config_dict_rechargerecord['TRANSFER'])
    #     if row['rechmethod'] == '系统充值':
    #         # 系统充值
    #         self.base_driver.select_by_value(self.config_dict_rechargerecord['SYSTEM'])
    #     if row['rechmethod'] == '红包领取':
    #         # 红包领取
    #         self.base_driver.select_by_value(self.config_dict_rechargerecord['GETRED'])
    #
    #     self.base_driver.forced_wait(4)
    #     print("选择充值方式" + row['rechmethod'])

    def rechargerecord01(self, row):
        # 会员中心登陆
        self.base_driver.type(self.config_dict_rechargerecord['UESE01'], 'lee6281376')
        self.base_driver.type(self.config_dict_rechargerecord['PASS01'], 'lee123')
        self.base_driver.type(self.config_dict_rechargerecord['YZM01'], '123')

        # 登陆按钮
        self.base_driver.click(self.config_dict_rechargerecord['BUTTON01'])
        print("登陆成功")
        self.base_driver.forced_wait(3)
        print('财务中心')
        self.base_driver.click(self.config_dict_rechargerecord['FINANCIAL'])
        print('充值记录')
        self.base_driver.forced_wait(3)
        self.base_driver.click(self.config_dict_rechargerecord['RECODES'])
        self.base_driver.forced_wait(5)

    def ordernumber(self, row):
        #  请输入订单号
        order = row['ordernum']
        print('没切片前'+row['ordernum'])
        # 切掉表格的第一为N
        neworder = order[1:]
        self.base_driver.type(self.config_dict_rechargerecord['ORDERNUM'], neworder)
        # self.base_driver.type(self.config_dict_rechargerecord['ORDERNUM'], row['ordernum'])
        # print('输入中的订单号是' + row['ordernum'])
        print('输入中的订单号是' + neworder)
        print(neworder)

    def modifydate(self):
        # 请选择修改日期
        self.base_driver.type(self.config_dict_rechargerecord['MODIFYDATA'])

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

    def get_rech_tips03(self):
        # 列表中的订单号
        # 增加N跟数据表格匹配
        tips02 = self.base_driver.get_text(self.config_dict_rechargerecord['ORDERNUMLIST'])
        tips03 = 'N' + tips02
        print('列表中的订单号是' + tips03)
        return tips03

    def get_button(self):
        # 查询按钮
        withdraw = self.base_driver.get_text(self.config_dict_rechargerecord['CHACKBUTTONR'])
        return withdraw

    def get_button1(self):
        # 查询按钮
        withdraw = self.base_driver.get_text(self.config_dict_rechargerecord['ORDERNUM1'])
        print('获取两字是：' + withdraw)
        return withdraw
