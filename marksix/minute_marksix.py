from common.box import BasePage, YamlHelper


class MinuteMarkSix(BasePage):
    # 分六合彩
    config_dict_marksix = YamlHelper().get_config_dict('/fusion/yaml/lottery_marksix.yaml')['MarkSix']

    def menu(self):
        self.base_driver.click(self.config_dict_marksix['MENU'])

    # 两面-------------
    def twosides(self, row):
        self.base_driver.click(self.config_dict_marksix['TWOSIDES'])
        if row['twosides'] == '特双':
            self.base_driver.type(self.config_dict_marksix['TESHUANG'], row['money'])
        if row['twosides'] == '特单':
            self.base_driver.type(self.config_dict_marksix['TEDAN'], row['money'])
        if row['twosides'] == '特大':
            self.base_driver.type(self.config_dict_marksix['TESDA'], row['money'])
        if row['twosides'] == '特小':
            self.base_driver.type(self.config_dict_marksix['TEXIAO'], row['money'])
        if row['twosides'] == '特合单':
            self.base_driver.type(self.config_dict_marksix['TEHEDAN'], row['money'])

    def twosidesall(self, row):
        # 两面
        self.base_driver.click(self.config_dict_marksix['TWOSIDES'])
        print('进入玩法两面')
        self.base_driver.forced_wait(1)
        # 特双
        self.base_driver.type(self.config_dict_marksix['TESHUANG'], row['money'])
        # 特单
        self.base_driver.type(self.config_dict_marksix['TEDAN'], row['money'])
        # 特大
        self.base_driver.type(self.config_dict_marksix['TESDA'], row['money'])
        # 特小
        self.base_driver.type(self.config_dict_marksix['TEXIAO'], row['money'])
        # 特合单
        self.base_driver.type(self.config_dict_marksix['TEHEDAN'], row['money'])
        # 特合双
        self.base_driver.type(self.config_dict_marksix['TEHESHUANG'], row['money'])
        # 特合大
        self.base_driver.type(self.config_dict_marksix['TEHEDA'], row['money'])
        # 特合小
        self.base_driver.type(self.config_dict_marksix['TEHEXIAO'], row['money'])
        # 特尾大
        self.base_driver.type(self.config_dict_marksix['TEHTAILDA'], row['money'])
        # 特尾小
        self.base_driver.type(self.config_dict_marksix['TETAILXIAO'], row['money'])
        # 特天肖
        self.base_driver.type(self.config_dict_marksix['TIANXIAO'], row['money'])
        # 特地肖
        self.base_driver.type(self.config_dict_marksix['DIXIAO'], row['money'])
        # 特前肖
        self.base_driver.type(self.config_dict_marksix['QIANXIAO'], row['money'])
        # 特后肖
        self.base_driver.type(self.config_dict_marksix['HOUXIAO'], row['money'])
        # 特家肖
        self.base_driver.type(self.config_dict_marksix['JIAXIAO'], row['money'])
        # 特野肖
        self.base_driver.type(self.config_dict_marksix['YEXIAO'], row['money'])
        # 总单
        self.base_driver.type(self.config_dict_marksix['ZONGDAN'], row['money'])
        # 总双
        self.base_driver.type(self.config_dict_marksix['ZONGSHUANG'], row['money'])
        # 总大
        self.base_driver.type(self.config_dict_marksix['ZONGDA'], row['money'])
        # 总小
        self.base_driver.type(self.config_dict_marksix['ZONGXIAO'], row['money'])
        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def sevenyards_qm(self, row):
        # 点击七码五行
        self.base_driver.click(self.config_dict_marksix['SEVENYARDS'])
        # 点击 七码
        self.base_driver.click(self.config_dict_marksix['SEVENY'])
        print('进入七码五行---七码')
        self.base_driver.forced_wait(1)
        # 单0双7
        self.base_driver.type(self.config_dict_marksix['DS07'], row['money'])
        # 单1双6
        self.base_driver.type(self.config_dict_marksix['DS16'], row['money'])
        # 单2双5
        self.base_driver.type(self.config_dict_marksix['DS25'], row['money'])
        # 单3双4
        self.base_driver.type(self.config_dict_marksix['DS34'], row['money'])
        # 单4双3
        self.base_driver.type(self.config_dict_marksix['DS43'], row['money'])
        # 单5双2
        self.base_driver.type(self.config_dict_marksix['DS52'], row['money'])
        # 单6双1
        self.base_driver.type(self.config_dict_marksix['DS61'], row['money'])
        # 单7双0
        self.base_driver.type(self.config_dict_marksix['DS70'], row['money'])

        # 单0双7
        self.base_driver.type(self.config_dict_marksix['DX07'], row['money'])
        # 单1双6
        self.base_driver.type(self.config_dict_marksix['DX16'], row['money'])
        # 单2双5
        self.base_driver.type(self.config_dict_marksix['DX25'], row['money'])
        # 单3双4
        self.base_driver.type(self.config_dict_marksix['DX34'], row['money'])
        # 单4双3
        self.base_driver.type(self.config_dict_marksix['DX43'], row['money'])
        # 单5双2
        self.base_driver.type(self.config_dict_marksix['DX52'], row['money'])
        # 单6双1
        self.base_driver.type(self.config_dict_marksix['DX61'], row['money'])
        # 单7双0
        self.base_driver.type(self.config_dict_marksix['DX70'], row['money'])
        self.base_driver.forced_wait(1)

    def sevenyards_wx(self, row):
        # 点击七码五行
        self.base_driver.click(self.config_dict_marksix['SEVENYARDS'])
        # 点击 五行
        self.base_driver.click(self.config_dict_marksix['FIVEPATH'])
        # 金
        self.base_driver.type(self.config_dict_marksix['JIN'], row['money'])
        # 木
        self.base_driver.type(self.config_dict_marksix['MU'], row['money'])
        # 水
        self.base_driver.type(self.config_dict_marksix['SHUI'], row['money'])
        # 火
        self.base_driver.type(self.config_dict_marksix['HUO'], row['money'])
        # 土
        self.base_driver.type(self.config_dict_marksix['TU'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def tailnum_htnum(self, row):
        # 尾数----头尾数字
        self.base_driver.click(self.config_dict_marksix['TAILNUM'])
        # 点击 头尾数
        self.base_driver.click(self.config_dict_marksix['HTNUM'])
        # 头0,1,2，3，4
        self.base_driver.type(self.config_dict_marksix['H0'], row['money'])
        self.base_driver.type(self.config_dict_marksix['H1'], row['money'])
        self.base_driver.type(self.config_dict_marksix['H2'], row['money'])
        self.base_driver.type(self.config_dict_marksix['H3'], row['money'])
        self.base_driver.type(self.config_dict_marksix['H4'], row['money'])
        # 为0,1,2,3,4,5,6,7,8,9
        self.base_driver.type(self.config_dict_marksix['T0'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T1'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T2'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T3'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T4'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T5'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T6'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T7'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T8'], row['money'])
        self.base_driver.type(self.config_dict_marksix['T9'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def tailnum_potnum(self, row):
        # 尾数----正特尾数
        self.base_driver.click(self.config_dict_marksix['TAILNUM'])
        # 点击 正特数
        self.base_driver.click(self.config_dict_marksix['POTNUM'])
        # 为0,1,2,3,4,5,6,7,8,9
        self.base_driver.type(self.config_dict_marksix['PT0'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT1'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT2'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT3'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT4'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT5'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT6'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT7'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT8'], row['money'])
        self.base_driver.type(self.config_dict_marksix['PT9'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def sebo_3(self, row):
        # 色波---三色波
        self.base_driver.click(self.config_dict_marksix['SEBO'])
        # 色波---三色波
        self.base_driver.click(self.config_dict_marksix['SEBO3'])
        # 色波---三色波---红波
        self.base_driver.type(self.config_dict_marksix['SEBO3R'], row['money'])
        # 色波---三色波---蓝波
        self.base_driver.type(self.config_dict_marksix['SEBO3B'], row['money'])
        # 色波---三色波---绿波
        self.base_driver.type(self.config_dict_marksix['SEBO3G'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def sebo_h(self, row):
        # 色波---半波
        self.base_driver.click(self.config_dict_marksix['SEBO'])
        # 色波---半波
        self.base_driver.click(self.config_dict_marksix['SEBOH'])
        # 色波---半波---红单
        self.base_driver.type(self.config_dict_marksix['SEBOHRDAN'], row['money'])
        # 色波---半波---红双
        self.base_driver.type(self.config_dict_marksix['SEBOHRSHU'], row['money'])
        # 色波---半波---红大
        self.base_driver.type(self.config_dict_marksix['SEBOHRDA'], row['money'])
        # 色波---半波---红小
        self.base_driver.type(self.config_dict_marksix['SEBOHRXIAO'], row['money'])

        # 色波---半波---绿单
        self.base_driver.type(self.config_dict_marksix['SEBOHGDAN'], row['money'])
        # 色波---半波---绿双
        self.base_driver.type(self.config_dict_marksix['SEBOHGSHU'], row['money'])
        # 色波---半波---绿大
        self.base_driver.type(self.config_dict_marksix['SEBOHGDA'], row['money'])
        # 色波---半波---绿小
        self.base_driver.type(self.config_dict_marksix['SEBOHGXIAO'], row['money'])

        # 色波---半波---蓝单
        self.base_driver.type(self.config_dict_marksix['SEBOHBDAN'], row['money'])
        # 色波---半波---蓝双
        self.base_driver.type(self.config_dict_marksix['SEBOHBSHU'], row['money'])
        # 色波---半波---蓝大
        self.base_driver.type(self.config_dict_marksix['SEBOHBDA'], row['money'])
        # 色波---半波---蓝小
        self.base_driver.type(self.config_dict_marksix['SEBOHBXIAO'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def sebo_hh(self, row):
        # 色波---半半波
        self.base_driver.click(self.config_dict_marksix['SEBO'])
        # 色波---半半波
        self.base_driver.click(self.config_dict_marksix['SEBOHH'])
        # 色波---半半波---红大单
        self.base_driver.type(self.config_dict_marksix['SEBOHHRDAN'], row['money'])
        # 色波---半半波---红大双
        self.base_driver.type(self.config_dict_marksix['SEBOHHRSHU'], row['money'])
        # 色波---半半波---红小单
        self.base_driver.type(self.config_dict_marksix['SEBOHHRXDAN'], row['money'])
        # 色波---半半波---红小双
        self.base_driver.type(self.config_dict_marksix['SEBOHHRXIAO'], row['money'])

        # 色波---半半波---绿大单
        self.base_driver.type(self.config_dict_marksix['SEBOHHGDAN'], row['money'])
        # 色波---半半波---绿大双
        self.base_driver.type(self.config_dict_marksix['SEBOHHGSHU'], row['money'])
        # 色波---半半波---绿小单
        self.base_driver.type(self.config_dict_marksix['SEBOHHGXDAN'], row['money'])
        # 色波---半半波---绿小双
        self.base_driver.type(self.config_dict_marksix['SEBOHHGXIAO'], row['money'])

        # 色波---半半波---蓝大单
        self.base_driver.type(self.config_dict_marksix['SEBOHHBDAN'], row['money'])
        # 色波---半半波---蓝大双
        self.base_driver.type(self.config_dict_marksix['SEBOHHBSHU'], row['money'])
        # 色波---半半波---蓝小单
        self.base_driver.type(self.config_dict_marksix['SEBOHHBXDAN'], row['money'])
        # 色波---半半波---蓝小双
        self.base_driver.type(self.config_dict_marksix['SEBOHHBXIAO'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def sebo_7(self, row):
        # 色波---七色波
        self.base_driver.click(self.config_dict_marksix['SEBO'])
        # 色波---七色波
        self.base_driver.click(self.config_dict_marksix['SEBO37'])
        # 色波---七色波---红波
        self.base_driver.type(self.config_dict_marksix['SEBO37R'], row['money'])
        # 色波---七色波---蓝波
        self.base_driver.type(self.config_dict_marksix['SEBO37B'], row['money'])
        # 色波---七色波---绿波
        self.base_driver.type(self.config_dict_marksix['SEBO37G'], row['money'])
        # 色波---七色波---和局
        self.base_driver.type(self.config_dict_marksix['SEBO37H'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)

    def hexiao_1(self, row):
        # 合肖
        self.base_driver.click(self.config_dict_marksix['HEXIAO'])
        # 合肖---家禽
        self.base_driver.click(self.config_dict_marksix['YESHOU'])
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        self.base_driver.forced_wait(0.1)
        # 色波---七色波---红波
        self.base_driver.type(self.config_dict_marksix['SEBO37R'], row['money'])
        # 色波---七色波---蓝波
        self.base_driver.type(self.config_dict_marksix['SEBO37B'], row['money'])
        # 色波---七色波---绿波
        self.base_driver.type(self.config_dict_marksix['SEBO37G'], row['money'])
        # 色波---七色波---和局
        self.base_driver.type(self.config_dict_marksix['SEBO37H'], row['money'])

        print('下注金额为:' + row['money'])
        self.base_driver.forced_wait(1)













































    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(5)

    def radoms(self):
        # 随机一注
        self.base_driver.click(self.config_dict_marksix['RANDOM1'])
        print('随机1注')
        self.base_driver.forced_wait(1)
        # 随机5注
        self.base_driver.click(self.config_dict_marksix['RANDOM5'])
        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        self.base_driver.forced_wait(1)
        print('随机5注')

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_marksix['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(3)
        return surebet

    def get_tips(self):
        tips = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips01(self):
        # 提示请先添加投注内容
        tips = self.base_driver.get_text(self.config_dict_marksix['TIPS01'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips02(self):
        # 提示下注成功
        tips = self.base_driver.get_text(self.config_dict_marksix['TIPS02'])
        print('捕捉到的信息是：' + tips)
        return tips