from common.box import BasePage, YamlHelper


class FusionLotteryHall(BasePage):
    # 导入fusion.yaml中的FusionMain
    config_dict_fulottery = YamlHelper().get_config_dict('/fusion/fusion.yaml')['FusionLotteryHall']

    def hall_menu(self, menu):
        # 点击数字彩
        # 购彩大厅
        if menu == '购彩大厅':
            self.base_driver.click(self.config_dict_fulottery['LOTTERYHALL'])
        if menu == '低频彩':
            self.base_driver.click(self.config_dict_fulottery['LOWCOLOR'])
        if menu == '六合彩':
            self.base_driver.click(self.config_dict_fulottery['MARKSIX'])
        if menu == '时时彩':
            self.base_driver.click(self.config_dict_fulottery['TIMOCOLOR'])
        if menu == 'PK10':
            self.base_driver.click(self.config_dict_fulottery['PK10'])
        if menu == '10选5':
            self.base_driver.click(self.config_dict_fulottery['CHOICE'])
        if menu == '快3':
            self.base_driver.click(self.config_dict_fulottery['FASTTHREE'])
        if menu == 'PC蛋蛋':
            self.base_driver.click(self.config_dict_fulottery['PCEGG'])
            self.base_driver.forced_wait(1)

    def hall_lowcolor(self, lowcolor):
        # 低频彩
        if lowcolor == '福彩3D':
            self.base_driver.click(self.config_dict_fulottery['FULOTTERY'])
        if lowcolor == '极速3D':
            self.base_driver.click(self.config_dict_fulottery['SPEED'])
        if lowcolor == '排列三':
            self.base_driver.click(self.config_dict_fulottery['ARRANGE'])
        self.base_driver.forced_wait(1)

    def hall_marksix(self, marksix):
        # 六合彩
        if marksix == '五分六合彩':
            self.base_driver.click(self.config_dict_fulottery['FIVEMARKSIX'])
        if marksix == '分分六合彩':
            self.base_driver.click(self.config_dict_fulottery['MIMARKSIX'])
        if marksix == '香港六合彩':
            self.base_driver.click(self.config_dict_fulottery['HKMARKSIX'])
        if marksix == '三分六合彩':
            self.base_driver.click(self.config_dict_fulottery['THREEMARKSIX'])
        self.base_driver.forced_wait(1)
        print("选择完成")

    def hall_timecolor(self, timecolor):
        # 时时彩
        if timecolor == '天津时时彩':
            self.base_driver.click(self.config_dict_fulottery['TIANJINTIME'])
        if timecolor == '分分时时彩':
            self.base_driver.click(self.config_dict_fulottery['MIMITIME'])
        if timecolor == '北京时时彩':
            self.base_driver.click(self.config_dict_fulottery['BEIJINGTIME'])
        if timecolor == '五分时时彩':
            self.base_driver.click(self.config_dict_fulottery['FIVEMITIME'])
        if timecolor == '重庆时时彩':
            self.base_driver.click(self.config_dict_fulottery['CHONGQING'])
        if timecolor == '三分时时彩':
            self.base_driver.click(self.config_dict_fulottery['THREETIME'])
        if timecolor == '新疆时时彩':
            self.base_driver.click(self.config_dict_fulottery['XINJIANG'])
        self.base_driver.forced_wait(1)

    def hall_pk10(self, pk10):
        # PK10
        if pk10 == '北京PK拾':
            self.base_driver.click(self.config_dict_fulottery['BEIJINGPK10'])
        if pk10 == '幸运飞艇':
            self.base_driver.click(self.config_dict_fulottery['LUCKYPK10'])
        if pk10 == '五分PK拾':
            self.base_driver.click(self.config_dict_fulottery['FIVEMIPK10'])
        if pk10 == '分分PK拾':
            self.base_driver.click(self.config_dict_fulottery['MIMIPK10'])
        if pk10 == '三分PK拾':
            self.base_driver.click(self.config_dict_fulottery['THREEPK10'])
        self.base_driver.forced_wait(1)

    def hall_ecfive(self, ecfive):
        # 11选5
        if ecfive == '广东11选5':
            self.base_driver.click(self.config_dict_fulottery['GUANGDONGC'])
        if ecfive == '山东11选5':
            self.base_driver.click(self.config_dict_fulottery['SHANDONGC'])
        if ecfive == '安徽11选5':
            self.base_driver.click(self.config_dict_fulottery['ANHUIC'])
        if ecfive == '上海11选5':
            self.base_driver.click(self.config_dict_fulottery['SHANGHAIC'])
        if ecfive == '江西11选5':
            self.base_driver.click(self.config_dict_fulottery['SHANXIC'])
        if ecfive == '分分11选5':
            self.base_driver.click(self.config_dict_fulottery['MIMICHOICE'])
        self.base_driver.forced_wait(1)

    def hall_fastthree(self, fastthree):
        #   快3
        if fastthree == '安徽快3':
            self.base_driver.click(self.config_dict_fulottery['AHFAST'])
        if fastthree == '广西快3':
            self.base_driver.click(self.config_dict_fulottery['GXFAST'])
        if fastthree == '湖北快3':
            self.base_driver.click(self.config_dict_fulottery['HBFAST'])
        if fastthree == '三分快3':
            self.base_driver.click(self.config_dict_fulottery['THFAST'])
        if fastthree == '吉林快3':
            self.base_driver.click(self.config_dict_fulottery['JLFAST'])
        if fastthree == '江苏快3':
            self.base_driver.click(self.config_dict_fulottery['JSFAST'])
        if fastthree == '分分快3':
            self.base_driver.click(self.config_dict_fulottery['MMFAST'])
        if fastthree == '五分快3':
            self.base_driver.click(self.config_dict_fulottery['FMFAST'])
        self.base_driver.forced_wait(1)

    def hall_pcegg(self,pcegg):
        #   PC蛋蛋
        if pcegg == '北京28':
            self.base_driver.click(self.config_dict_fulottery['BJEGG'])
        if pcegg == '分分28':
            self.base_driver.click(self.config_dict_fulottery['MMEGG'])
        if pcegg == '五分28':
            self.base_driver.click(self.config_dict_fulottery['FMEGG'])
        if pcegg == '幸运28':
            self.base_driver.click(self.config_dict_fulottery['LCEGG'])
        if pcegg == '三分28':
            self.base_driver.click(self.config_dict_fulottery['THEGG'])



