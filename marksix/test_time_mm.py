import csv
import unittest
import ss as ss
from common.box import TestCase, BoxDriver, Browser
from marksix.lottery import Lottery
from marksix.marksix_minute import MinuteMarkSix
from marksix.time_mm import TimeMinute


class TimeMmTest(TestCase):
    # 分分时时彩
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("打开网址")

        # 休眠
        self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例

    def test_success_01(self):
        # 下注
        #self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/24')
        self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/24')
        # print("成功打开网址")
        self.base_driver.forced_wait(50)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注 
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.time()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.timemm = TimeMinute(self.base_driver)
                '''
                # ---------------------------------------
                # 三星
                # 三星---后三直选---复式
                self.timemm.star3_h3zhxfs(row)
                self.timemm.radoms(row)
                print('三星---后三直选---复式')

                # 三星
                # 三星---后三直选---单式
                self.timemm.star3_h3zhxds(row)
                self.timemm.radoms(row)
                print('三星---后三直选---单式')

                # 三星
                # 三星---后三直选---直选和值
                self.timemm.star3_h3zhxzxhz(row)
                self.timemm.radoms(row)
                print('三星---后三直选---直选和值')

                # 三星
                # 三星---后三直选---直选跨度
                self.timemm.star3_h3zhxzxkd(row)
                self.timemm.radoms(row)
                print('三星---后三直选---直选跨度')

                # 三星
                # 三星---后三直选---和值尾数
                self.timemm.star3_h3zhxhzws(row)
                self.timemm.radoms(row)
                print('三星---后三直选---和值尾数')

                # 三星
                # 三星---后三组选---组三
                self.timemm.star3_h3zuxz3(row)
                self.timemm.radoms(row)
                print('三星---后三组选---组三')

                # 三星
                # 三星---后三组选---组六
                self.timemm.star3_h3zuxz6(row)
                self.timemm.radoms(row)
                print('三星---后三组选---组六')

                # 三星
                # 三星---后三组选---混合组选
                self.timemm.star3_h3zuxhhzhix(row)
                self.timemm.radoms(row)
                print('三星---后三组选---混合组选')

                # 三星
                # 三星---后三组选---组选包胆
                self.timemm.star3_h3zuxbd(row)
                self.timemm.radoms(row)
                print('三星---后三组选---组选包胆')

                # ---------------------------
                # ---------------------------
                # ---------------------------
                #
                # 三星
                # 三星---中三直选---复式
                self.timemm.star3_z3zhxfs(row)
                self.timemm.radoms(row)
                print('三星---中三直选---复式')

                # 三星
                # 三星---中三直选---单式
                self.timemm.star3_z3zhxds(row)
                self.timemm.radoms(row)
                print('三星---中三直选---单式')

                # 三星
                # 三星---中三直选---直选和值
                self.timemm.star3_z3zhxzxhz(row)
                self.timemm.radoms(row)
                print('三星---中三直选---直选和值')

                # 三星
                # 三星---中三直选---直选跨度
                self.timemm.star3_z3zhxzxkd(row)
                self.timemm.radoms(row)
                print('三星---中三直选---直选跨度')

                # 三星
                # 三星---中三直选---和值尾数
                self.timemm.star3_z3zhxhzws(row)
                self.timemm.radoms(row)
                print('三星---中三直选---和值尾数')

                # 三星
                # 三星---中三组选---组三
                self.timemm.star3_z3zuxz3(row)
                self.timemm.radoms(row)
                print('三星---中三组选---组三')

                # 三星
                # 三星---中三组选---组六
                self.timemm.star3_z3zuxz6(row)
                self.timemm.radoms(row)
                print('三星---中三组选---组六')

                # 三星
                # 三星---后三组选---混合组选
                self.timemm.star3_z3zuxzx(row)
                self.timemm.radoms(row)
                print('三星---中三组选---混合组选')

                # 三星
                # 三星---中三组选---组选包胆
                self.timemm.star3_z3zuxbd(row)
                self.timemm.radoms(row)
                print('三星---中三组选---组选包胆')

                # ---------------------------
                # ---------------------------
                # ---------------------------
                #
                # 三星
                # 三星---前三直选---复式
                self.timemm.star3_q3zhxfs(row)
                self.timemm.radoms(row)
                print('三星---前三直选---复式')

                # 三星
                # 三星---前三直选---单式
                self.timemm.star3_q3zhxds(row)
                self.timemm.radoms(row)
                print('三星---前三直选---单式')

                # 三星
                # 三星---前三直选---直选和值
                self.timemm.star3_q3zhxzxhz(row)
                self.timemm.radoms(row)
                print('三星---前三直选---直选和值')

                # 三星
                # 三星---前三直选---直选跨度
                self.timemm.star3_q3zhxzxkd(row)
                self.timemm.radoms(row)
                print('三星---前三直选---直选跨度')

                # 三星
                # 三星---前三直选---和值尾数
                self.timemm.star3_q3zhxhzws(row)
                self.timemm.radoms(row)
                print('三星---前三直选---和值尾数')

                # 三星
                # 三星---前三组选---组三
                self.timemm.star3_q3zuxz3(row)
                self.timemm.radoms(row)
                print('三星---前三组选---组三')

                # 三星
                # 三星---前三组选---组六
                self.timemm.star3_q3zuxz6(row)
                self.timemm.radoms(row)
                print('三星---前三组选---组六')

                # 三星
                # 三星---前三组选---混合组选
                self.timemm.star3_q3zuxzx(row)
                self.timemm.radoms(row)
                print('三星---前三组选---混合组选')

                # 三星
                # 三星---前三组选---组选包胆
                self.timemm.star3_q3zuxbd(row)
                self.timemm.radoms(row)
                print('三星---前三组选---组选包胆')
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                #'''
                # 四星
                # 四星---后四直选---复式
                self.timemm.star4_h4zhxfs(row)
                self.timemm.radoms(row)
                print('四星---后四直选---复式')
                '''
                # 四星
                # 四星---后四直选---单式
                self.timemm.star4_h4zhxds(row)
                self.timemm.radoms(row)
                print('四星---后四直选---单式')

                # 四星
                # 四星---后四直选---组合
                self.timemm.star4_h4zhxzuhe(row)
                self.timemm.radoms(row)
                print('四星---后四直选---组合')

                # 四星
                # 四星---后四组选---组选24
                self.timemm.star4_h4zuxz24(row)
                self.timemm.radoms(row)
                print('四星---后四组选---组选24')

                # 四星
                # 四星---后四组选---组选12
                self.timemm.star4_h4zuxz12(row)
                self.timemm.radoms(row)
                print('四星---后四组选---组选12')
                #
                # 四星
                # 四星---后四组选--组选6
                self.timemm.star4_h4zuxz06(row)
                self.timemm.radoms(row)
                print('四星---后四组选---组选6')

                # 四星
                # 四星---后四组选---组选4
                self.timemm.star4_h4zuxz04(row)
                self.timemm.radoms(row)
                print('四星---后四组选---组选4')
                '''
                # 四星
                # 四星---前四直选---复式
                self.timemm.star4_q4zhxfs(row)
                self.timemm.radoms(row)
                print('四星---直四直选---直选4')
                '''
                #
                # 四星
                # 四星---前四直选---单式
                self.timemm.star4_q4zhxds(row)
                self.timemm.radoms(row)
                print('四星---直四直选---单式4')
                '''
                # 四星
                # 四星---前四直选---组合
                self.timemm.star4_q4zhxzuhe(row)
                self.timemm.radoms(row)
                print('四星---直四直选---组合')
                '''

                # 四星
                # 四星---前四组选---组选24
                self.timemm.star4_q4zuxz24(row)
                self.timemm.radoms(row)
                print('四星---前四组选---组选24')

                # 四星
                # 四星---前四组选---组选12
                self.timemm.star4_q4zuxz12(row)
                self.timemm.radoms(row)
                print('四星---前四组选---组选12')

                # 四星
                # 四星---前四组选---组选6
                self.timemm.star4_q4zuxz06(row)
                self.timemm.radoms(row)
                print('四星---前四组选---组选6')

                # 四星
                # 四星---前四组选---组选4
                self.timemm.star4_q4zuxz04(row)
                self.timemm.radoms(row)
                print('四星---前四组选---组选4')

                # 斗牛
                # 斗牛---斗牛
                self.timemm.douniu(row)
                self.timemm.radoms(row)
                print('斗牛---斗牛')

                # 特殊号
                # 特殊号---前三
                self.timemm.teshn_q3(row)
                self.timemm.radoms(row)
                print('特殊号---前三')

                # 特殊号
                # 特殊号---中三
                self.timemm.teshn_z3(row)
                self.timemm.radoms(row)
                print('特殊号---中三')

                # 特殊号
                # 特殊号---后三
                self.timemm.teshn_h3(row)
                self.timemm.radoms(row)
                print('特殊号---后三')

                # 大小单双
                # 大小单双---总和---总和
                self.timemm.dxds_zh(row)
                self.timemm.radoms(row)
                print('大小单双---总和---总和')

                # 大小单双
                # 大小单双---定位---万位
                self.timemm.dxds_dww(row)
                self.timemm.radoms(row)
                print('大小单双---定位---万位')

                # 大小单双
                # 大小单双---定位---千位
                self.timemm.dxds_dwq(row)
                self.timemm.radoms(row)
                print('大小单双---定位---千位')

                # 大小单双
                # 大小单双---定位---百位
                self.timemm.dxds_dwb(row)
                self.timemm.radoms(row)
                print('大小单双---定位---百位')

                # 大小单双
                # 大小单双---定位---十位
                self.timemm.dxds_dws(row)
                self.timemm.radoms(row)
                print('大小单双---定位---十位')

                # 大小单双
                # 大小单双---定位---个位
                self.timemm.dxds_dwg(row)
                self.timemm.radoms(row)
                print('大小单双---定位---个位')

                # 大小单双
                # 大小单双---串关---串关
                self.timemm.dxds_cg(row)
                self.timemm.radoms(row)
                print('大小单双---串关---串关')

                # 龙虎
                # 龙虎--万千
                self.timemm.longhh_wq(row)
                self.timemm.radoms(row)
                print('龙虎--万千')

                # 龙虎
                # 龙虎--万百
                self.timemm.longhh_wb(row)
                self.timemm.radoms(row)
                print('龙虎--万百')

                # 龙虎
                # 龙虎--万十
                self.timemm.longhh_ws(row)
                self.timemm.radoms(row)
                print('龙虎--万十')

                # 龙虎
                # 龙虎--万个
                self.timemm.longhh_wg(row)
                self.timemm.radoms(row)
                print('龙虎--万个')

                # 龙虎
                # 龙虎--千百
                self.timemm.longhh_qb(row)
                self.timemm.radoms(row)
                print('龙虎--千百')

                # 龙虎
                # 龙虎--千十
                self.timemm.longhh_qs(row)
                self.timemm.radoms(row)
                print('龙虎--千十')

                # 龙虎
                # 龙虎--千个
                self.timemm.longhh_qg(row)
                self.timemm.radoms(row)
                print('龙虎--千个')

                # 龙虎
                # 龙虎--百十
                self.timemm.longhh_bs(row)
                self.timemm.radoms(row)
                print('龙虎--百十')

                # 龙虎
                # 龙虎--百个
                self.timemm.longhh_bg(row)
                self.timemm.radoms(row)
                print('龙虎--百个')

                # 龙虎
                # 龙虎--十个
                self.timemm.longhh_sg(row)
                self.timemm.radoms(row)
                print('龙虎--十个')

                # 趣味
                # 趣味---特殊---一帆风顺
                self.timemm.quwei_01(row)
                self.timemm.radoms(row)
                print('趣味---特殊---一帆风顺')

                # 趣味
                # 趣味---特殊---好事成双
                self.timemm.quwei_02(row)
                self.timemm.radoms(row)
                print('趣味---特殊---好事成双')

                # 趣味
                # 趣味---特殊---三星报喜
                self.timemm.quwei_03(row)
                self.timemm.radoms(row)
                print('趣味---特殊---三星报喜')
                
                # 趣味
                # 趣味---特殊---四季平安
                self.timemm.quwei_04(row)
                self.timemm.radoms(row)
                print('趣味---特殊---四季平安')

                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # 任选
                # 任选---任二---复式
                self.timemm.renxur2_fs(row)
                # self.timemm.radoms(row)
                print('任选---任二---复式')
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------

                # 任选
                # 任选---任二---单式
                self.timemm.renxur2_ds(row)
                # self.timemm.radoms(row)
                print('任选---任二---单式')
                
                # 任选
                # 任选---任二---组选
                self.timemm.renxur2_zux(row)
                self.timemm.radoms(row)
                print('任选---任二---组选')

                # 任选
                # 任选---任三---复式
                self.timemm.renxur3_fs(row)
                self.timemm.radoms(row)
                print('任选---任三---复式')

                # 任选
                # 任选---任三---单式
                self.timemm.renxur3_ds(row)
                self.timemm.radoms(row)
                print('任选---任三---单式')

                # 任选
                # 任选---任三---组3
                self.timemm.renxur3_zux3(row)
                self.timemm.radoms(row)
                print('任选---任三---组3')

                # 任选
                # 任选---任三---组6
                self.timemm.renxur3_zux6(row)
                self.timemm.radoms(row)
                print('任选---任三---组6')

                # 任选
                # 任选---任三---混合组选
                self.timemm.renxur3_zuxhh(row)
                self.timemm.radoms(row)
                print('任选---任三---混合组选')

                # 任选
                # 任选---任四---复式
                self.timemm.renxur4_fs(row)
                self.timemm.radoms(row)
                print('任选---任四---复式')

                # 任选
                # 任选---任四---单式
                self.timemm.renxur4_ds(row)
                self.timemm.radoms(row)
                print('任选---任四---单式')

                # 不定位
                # 不定位---三星不定位---后三一码
                self.timemm.bdws3_h31(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---后三一码')

                # 不定位
                # 不定位---三星不定位---中三一码
                self.timemm.bdws3_z31(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---中三一码')

                # 不定位
                # 不定位---三星不定位---前三一码
                self.timemm.bdws3_q31(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---前三一码')

                # 不定位
                # 不定位---三星不定位---后三二码
                self.timemm.bdws3_h32(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---后三二码')

                # 不定位
                # 不定位---三星不定位---中三二码
                self.timemm.bdws3_z32(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---中三二码')

                # 不定位
                # 不定位---三星不定位---前三二码
                self.timemm.bdws3_q32(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---前三二码')

                # 不定位
                # 不定位---四星不定位---前四一码
                self.timemm.bdws4_q41(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---前四一码')

                # 不定位
                # 不定位---四星不定位---后四一码
                self.timemm.bdws4_h41(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---后四一码')

                # 不定位
                # 不定位---四星不定位---前四二码
                self.timemm.bdws4_q42(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---前四二码')

                # 不定位
                # 不定位---四星不定位---后四二码
                self.timemm.bdws4_h42(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---后四二码')
                
                # 不定位
                # 不定位---四星不定位---前四三码
                self.timemm.bdws4_q43(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---前四三码')
                
                # 不定位
                # 不定位---四星不定位---后四三码
                self.timemm.bdws4_h43(row)
                self.timemm.radoms(row)
                print('不定位---三星不定位---后四三码')

                # 不定位
                # 不定位---五星不定位---五星一码
                self.timemm.bdws5_s51(row)
                self.timemm.radoms(row)
                print('不定位---五星不定位---五星一码')

                # 不定位
                # 不定位---五星不定位---五星二码
                self.timemm.bdws5_s52(row)
                self.timemm.radoms(row)
                print('不定位---五星不定位---五星二码')

                # 不定位
                # 不定位---五星不定位---五星三码
                self.timemm.bdws5_s53(row)
                self.timemm.radoms(row)
                print('不定位---五星不定位---五星三码')

                # 不定位
                # 不定位---五星不定位---五星一码
                self.timemm.bdws5_s54(row)
                self.timemm.radoms(row)
                print('不定位---五星不定位---五星四码')
                #
                # ----------------------------------------------
                # ----------------------------------------------
                # ----------------------------------------------
                # 二星
                # 二星---后二直选---复式
                self.timemm.star2_h2zhxfs(row)
                self.timemm.radoms(row)
                print('二星---后二直选---复式')
                
                # 二星
                # 二星---后二直选---单式
                self.timemm.star2_h2zhxds(row)
                self.timemm.radoms(row)
                print('二星---后二直选---单式')
                
                # 二星
                # 二星---后二直选---直选和值
                self.timemm.star2_h2zhxzxhz(row)
                self.timemm.radoms(row)
                print('二星---后二直选---直选和值')
                
                # 二星
                # 二星---后二直选---直选跨度
                self.timemm.star2_h2zhxzxkd(row)
                self.timemm.radoms(row)
                print('二星---后二直选---直选跨度')

                # 二星
                # 二星---后二直选---和值尾数
                self.timemm.star2_h2zhxhzws(row)
                self.timemm.radoms(row)
                print('二星---后二直选---和值尾数')
                
                # 二星
                # 二星---后二组选---复式
                self.timemm.star2_h2zuxfs(row)
                self.timemm.radoms(row)
                print('二星---后二组选---复式')
                
                # 二星
                # 二星---后二组选---单式
                self.timemm.star2_h2zuxds(row)
                self.timemm.radoms(row)
                print('二星---后二组选---单式')

                # 二星
                # 二星---后二组选---组选包胆
                self.timemm.star2_h2zuxbd(row)
                self.timemm.radoms(row)
                print('二星---后二组选---组选包胆')

                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                #
                # 二星
                # 二星---前二直选---复式
                self.timemm.star2_q2zhxfs(row)
                self.timemm.radoms(row)
                print('二星---前二直选---复式')

                # 二星
                # 二星---前二直选---单式
                self.timemm.star2_q2zhxds(row)
                self.timemm.radoms(row)
                print('二星---前二直选---单式')

                # 二星
                # 二星---前二直选---直选和值
                self.timemm.star2_q2zhxzxhz(row)
                self.timemm.radoms(row)
                print('二星---前二直选---直选和值')

                # 二星
                # 二星---前二直选---直选跨度
                self.timemm.star2_q2zhxzxkd(row)
                self.timemm.radoms(row)
                print('二星---前二直选---直选跨度')

                # 二星
                # 二星---前二直选---和值尾数
                self.timemm.star2_q2zhxhzws(row)
                self.timemm.radoms(row)
                print('二星---前二直选---和值尾数')

                # 二星
                # 二星---前二组选---复式
                self.timemm.star2_q2zuxfs(row)
                self.timemm.radoms(row)
                print('二星---前二组选---复式')

                # 二星
                # 二星---前二组选---单式
                self.timemm.star2_q2zuxds(row)
                self.timemm.radoms(row)
                print('二星---前二组选---单式')

                # 二星
                # 二星---前二组选---组选包胆
                self.timemm.star2_q2zuxbd(row)
                self.timemm.radoms(row)
                print('二星---前二组选---组选包胆')
                
                # 定位胆
                # 定位胆---定位胆---定位胆
                self.timemm.dwd(row)
                self.timemm.radoms(row)
                print('定位胆---定位胆---定位胆')

                # 五星
                # 五星---五星直选---复式
                self.timemm.star5_s5zhixfs(row)
                self.timemm.radoms(row)
                print('五星---五星直选---复式')

                # 五星
                # 五星---五星直选---单式
                self.timemm.star5_s5zhixds(row)
                self.timemm.radoms(row)
                print('五星---五星直选---单式')

                # 五星
                # 五星---五星直选---组合
                self.timemm.star5_s5zhixzuhe(row)
                self.timemm.radoms(row)
                print('五星---五星直选---组合')

                # 五星
                # 五星---五星组选---组选120
                self.timemm.star5_s5zuxz120(row)
                self.timemm.radoms(row)
                print('五星---五星组选---组选120')

                # 五星
                # 五星---五星组选---组选60
                self.timemm.star5_s5zuxz60(row)
                self.timemm.radoms(row)
                print('五星---五星组选---组选60')

                # 五星
                # 五星---五星组选---组选30
                self.timemm.star5_s5zuxz30(row)
                self.timemm.radoms(row)
                print('五星---五星组选---组选30')

                # 五星
                # 五星---五星组选---组选20
                self.timemm.star5_s5zuxz20(row)
                self.timemm.radoms(row)
                print('五星---五星组选---组选20')
'''
                # 五星
                # 五星---五星组选---组选10
                self.timemm.star5_s5zuxz10(row)
                self.timemm.radoms(row)
                print('五星---五星组选---组选10')

                # 五星
                # 五星---五星组选---组选10
                self.timemm.star5_s5zuxz5(row)
                self.timemm.radoms(row)
                print('五星---五星组选---组选5')

                # self.base_driver.forced_wait(10)
                # get_tips = self.timemm.get_tips()
                # print('获取的文字是：' + get_tips)
                # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')

    def test_fail_01(self):
        # 下注
        self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/24')
        # print("成功打开网址")
        self.base_driver.forced_wait(3)
        # 滑动浏览器右边滑动条
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注
        # # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.time()
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.timemm = TimeMinute(self.base_driver)

                # ---------------------------------------
                # 三星
                # 三星---后三直选---复式
                self.timemm.star3_h3zhxfs_error(row)
                print('三星---后三直选---复式')
                # self.logger.info('三星---后三直选---复式')
                
                # 三星
                # 三星---后三直选---单式
            
                self.timemm.star3_h3zhxds_error(row)
                print('三星---后三直选---单式')
                self.logger.info('三星---后三直选---单式')
                      
                # 三星
                # 三星---后三组选---组三
                
                self.timemm.star3_h3zuxz3_error(row)
                print('三星---后三组选---组三')
                self.logger.info('三星---后三组选---组三')              
                # 三星
                # 三星---后三组选---组六
                
                self.timemm.star3_h3zuxz6_error(row)
                print('三星---后三组选---组六')
                self.logger.info('三星---后三组选---组六')
                
                # 三星
                # 三星---后三组选---混合组选
                self.timemm.star3_h3zuxhhzhix_error(row)
                print('三星---后三组选---混合组选')
                self.logger.info('三星---后三组选---混合组选')
                # ---------------------------
                # ---------------------------
                # ---------------------------
                # #
                # 三星
                # 三星---中三直选---复式
                self.timemm.star3_z3zhxfs_error(row)
                print('三星---中三直选---复式')

                # 三星
                # 三星---中三直选---单式
                self.timemm.star3_z3zhxds_error(row)
                print('三星---中三直选---单式')

                # 三星
                # 三星---中三组选---组三
                self.timemm.star3_z3zuxz3_error(row)
                print('三星---中三组选---组三')
                #
                # 三星
                # 三星---中三组选---组六
                self.timemm.star3_z3zuxz6_error(row)
                print('三星---中三组选---组六')

                # 三星
                # 三星---后三组选---混合组选
                self.timemm.star3_z3zuxzx_error(row)
                print('三星---中三组选---混合组选')

                # ---------------------------
                # ---------------------------
                # ---------------------------

                # 三星
                # 三星---前三直选---复式
                self.timemm.star3_q3zhxfs_error(row)
                print('三星---前三直选---复式')

                # 三星
                # 三星---前三直选---单式
                self.timemm.star3_q3zhxds_error(row)
                print('三星---前三直选---单式')

                # 三星
                # 三星---前三组选---组三
                self.timemm.star3_q3zuxz3_error(row)
                print('三星---前三组选---组三')

                # 三星
                # 三星---前三组选---组六
                self.timemm.star3_q3zuxz6_error(row)
                print('三星---前三组选---组六')

                # 三星
                # 三星---前三组选---混合组选
                self.timemm.star3_q3zuxzx_error(row)
                print('三星---前三组选---混合组选')
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------

                # 四星
                # 四星---后四直选---复式
                self.timemm.star4_h4zhxfs_error(row)
                print('四星---后四直选---复式')

                # 四星
                # 四星---后四直选---单式
                self.timemm.star4_h4zhxds_error(row)
                print('四星---后四直选---单式')

                # 四星
                # 四星---后四直选---组合
                self.timemm.star4_h4zhxzuhe_error(row)
                print('四星---后四直选---组合')

                # 四星
                # 四星---后四组选---组选24
                self.timemm.star4_h4zuxz24_error(row)
                print('四星---后四组选---组选24')
               
                # 四星
                # 四星---后四组选---组选12
                self.timemm.star4_h4zuxz12_error(row)
                print('四星---后四组选---组选12')
                
                # 四星
                # 四星---后四组选--组选6
                self.timemm.star4_h4zuxz06_error(row)
                print('四星---后四组选---组选6')
                
                # 四星
                # 四星---后四组选---组选4
                self.timemm.star4_h4zuxz04_error(row)
                print('四星---后四组选---组选4')
                
                # 四星
                # 四星---前四直选---复式
                self.timemm.star4_q4zhxfs_error(row)
                print('四星---直四直选---直选4')
                #

                # 四星
                # 四星---前四直选---单式
                self.timemm.star4_q4zhxds_error(row)
                print('四星---直四直选---单式4')

                # 四星
                # 四星---前四直选---组合
                self.timemm.star4_q4zhxzuhe_error(row)
                print('四星---直四直选---组合')

                # 四星
                # 四星---前四直选---组合
                self.timemm.star4_q4zhxzuhe_error(row)
                print('四星---直四直选---组合')
                
                # 四星
                # 四星---前四组选---组选24
                self.timemm.star4_q4zuxz24_error(row)
                print('四星---前四组选---组选24')
               
                # 四星
                # 四星---前四组选---组选12
                self.timemm.star4_q4zuxz12_error(row)
                print('四星---前四组选---组选12')
                
                # 四星
                # 四星---前四组选---组选6
                self.timemm.star4_q4zuxz06_error(row)
                print('四星---前四组选---组选6')

                # 四星
                # 四星---前四组选---组选4
                self.timemm.star4_q4zuxz04_error(row)
                print('四星---前四组选---组选4')
                
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # # ---------------------------------
                # 任选
                #
                # 任选
                # 任选---任二---复式
                self.timemm.renxur2_fs_error(row)
                print('任选---任二---复式')
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # 任选
                # 任选---任二---单式
                self.timemm.renxur2_ds_error(row)
                # self.timemm.radoms(row)
                print('任选---任二---单式')
                #
                # # 任选
                # 任选---任二---组选
                self.timemm.renxur2_zux_error(row)
                print('任选---任二---组选')

                # 任选
                # 任选---任三---复式
                self.timemm.renxur3_fs_error(row)
                print('任选---任三---复式')
                
                # 任选
                # 任选---任三---单式
                self.timemm.renxur3_ds_error(row)
                print('任选---任三---单式')
                #
                # 任选
                # 任选---任三---组3
                self.timemm.renxur3_zux3_error(row)
                print('任选---任三---组3')

                # 任选
                # 任选---任三---组6
                self.timemm.renxur3_zux6_error(row)
                print('任选---任三---组6')

                # 任选
                # 任选---任三---混合组选
                self.timemm.renxur3_zuxhh_error(row)
                print('任选---任三---混合组选')

                # 任选
                # 任选---任四---复式
                self.timemm.renxur4_fs_error(row)
                print('任选---任四---复式')

                # 任选
                # 任选---任四---单式
                self.timemm.renxur4_ds_error(row)
                print('任选---任四---单式')

                # 不定位
                # 不定位---三星不定位---后三二码
                self.timemm.bdws3_h32_error(row)
                print('不定位---三星不定位---后三二码')
                #
                # 不定位
                # 不定位---三星不定位---中三二码
                self.timemm.bdws3_z32_error(row)
                print('不定位---三星不定位---中三二码')

                # 不定位
                # 不定位---三星不定位---前三二码
                self.timemm.bdws3_q32_error(row)
                print('不定位---三星不定位---前三二码')
                #

                # 不定位
                # 不定位---四星不定位---前四二码
                self.timemm.bdws4_q42_error(row)
                print('不定位---三星不定位---前四二码')

                # 不定位
                # 不定位---四星不定位---后四二码
                self.timemm.bdws4_h42_error(row)
                print('不定位---三星不定位---后四二码')

                # 不定位
                # 不定位---四星不定位---前四三码
                self.timemm.bdws4_q43_error(row)
                print('不定位---三星不定位---前四三码')

                # 不定位
                # 不定位---四星不定位---后四三码
                self.timemm.bdws4_h43_error(row)
                print('不定位---三星不定位---后四三码')

                # 不定位
                # 不定位---五星不定位---五星二码
                self.timemm.bdws5_s52_error(row)
                print('不定位---五星不定位---五星二码')
                #
                
                # 不定位
                # 不定位---五星不定位---五星三码
                self.timemm.bdws5_s53_error(row)
                print('不定位---五星不定位---五星三码')
                
                # 不定位
                # 不定位---五星不定位---五星四码
                self.timemm.bdws5_s54_error(row)
                print('不定位---五星不定位---五星四码')
                #
                # ----------------------------------------------
                # ----------------------------------------------
                # # ----------------------------------------------

                # 二星
                # 二星---后二直选---复式
                self.timemm.star2_h2zhxfs_error(row)
                print('二星---后二直选---复式')
                
                # 二星
                # 二星---后二直选---单式
                self.timemm.star2_h2zhxds_error(row)
                print('二星---后二直选---单式')
                #

                # 二星
                # 二星---后二组选---复式
                self.timemm.star2_h2zuxfs_error(row)
                print('二星---后二组选---复式')
                
                # 二星
                # 二星---后二组选---单式
                self.timemm.star2_h2zuxds_error(row)
                print('二星---后二组选---单式')

                #
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                # ---------------------------------
                #
                # 二星
                # 二星---前二直选---复式
                self.timemm.star2_q2zhxfs_error(row)
                print('二星---前二直选---复式')

                # 二星
                # 二星---前二直选---单式
                self.timemm.star2_q2zhxds_error(row)
                print('二星---前二直选---单式')

                # 二星
                # 二星---前二组选---复式
                self.timemm.star2_q2zuxfs_error(row)
                print('二星---前二组选---复式')

                # 二星
                # 二星---前二组选---单式
                self.timemm.star2_q2zuxds_error(row)
                print('二星---前二组选---单式')

                # -----------------------------------------
                # -----------------------------------------
                # -----------------------------------------
                #
                # 五星
                # 五星---五星直选---复式
                self.timemm.star5_s5zhixfs_error(row)
                print('五星---五星直选---复式')

                # 五星
                # 五星---五星直选---单式
                self.timemm.star5_s5zhixds_error(row)
                print('五星---五星直选---单式')
                #
                # 五星
                # 五星---五星直选---组合
                self.timemm.star5_s5zhixzuhe_error(row)
                print('五星---五星直选---组合')
                #
                # 五星
                # 五星---五星组选---组选120
                self.timemm.star5_s5zuxz120_error(row)
                print('五星---五星组选---组选120')

                # 五星
                # 五星---五星组选---组选60
                self.timemm.star5_s5zuxz60_error(row)
                print('五星---五星组选---组选60')

                # 五星
                # 五星---五星组选---组选30
                self.timemm.star5_s5zuxz30_error(row)
                print('五星---五星组选---组选30')
                #
                # 五星
                # 五星---五星组选---组选20
                self.timemm.star5_s5zuxz20_error(row)
                print('五星---五星组选---组选20')
                #
                # 五星
                # 五星---五星组选---组选10
                self.timemm.star5_s5zuxz10_error(row)
                print('五星---五星组选---组选10')

                # 五星
                # 五星---五星组选---组选10
                self.timemm.star5_s5zuxz5_error(row)
                print('五星---五星组选---组选5')

                # self.base_driver.forced_wait(10)
                # get_tips = self.timemm.get_tips()
                # print('获取的文字是：' + get_tips)
                # self.assertEqual(get_tips, row['tips'], '充值金额不符合！')
                # # self.base_driver.refresh()
                # print('刷新网页')
                # self.base_driver.forced_wait(1)
                # self.base_driver.quit()

        # 使用完csv文件后，关闭
        csv_file.close()
        print('test_fail_registered_01 运行完毕')
        # 日志
        self.logger.info('关闭CSV文件')


if __name__ == '__main__':

    unittest.main()
