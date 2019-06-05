import csv
import unittest
from selenium.webdriver.common.action_chains import ActionChains

from common.box import TestCase, BoxDriver, Browser
from marksix.lottery import Lottery
from marksix.marksix_minute import MinuteMarkSix


class MarkSixTest(TestCase):
    # 六合彩
    def set_up(self):
        # 启动浏览器
        self.base_driver = BoxDriver(Browser.Chrome)
        # 全屏浏览器
        self.base_driver.maximize_window()
        # 输入网址
        # self.base_driver.navigate('https://fusion.spmobileapi.net/#/home')
        # self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("打开网址")

        # 休眠
        # self.base_driver.forced_wait(3)

    def tear_down(self):
        self.base_driver.quit()

        # 测试用例
    def test_success_01(self):
        # 下注
        self.base_driver.navigate('https://online.baifu-tech.net/dglobby#/play/46')
        print("成功打开网址")
        self.base_driver.forced_wait(30)
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注
        # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.marksix()
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.base_driver.execute_js(js)
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.mmsix = MinuteMarkSix(self.base_driver)

                # 两面下注
                self.mmsix.twosidesall(row)
                self.mmsix.radoms(row)
                print("两面注单提交完毕")
                print('两面玩法下注完毕')

                # 七码五行--七码
                self.mmsix.sevenyards_qm(row)
                self.mmsix.radoms(row)
                print('七码五行--七码下注完毕')

                # # 七码五行--五行
                self.mmsix.sevenyards_wx(row)
                self.mmsix.radoms(row)
                print('七码五行--五行下注完毕')

                # 尾数--头尾数
                self.mmsix.tailnum_htnum(row)
                self.mmsix.radoms(row)
                print('尾数--头尾数')

                # 尾数--正特尾数
                self.mmsix.tailnum_potnum(row)
                self.mmsix.radoms(row)
                print('尾数--头尾数')

                # 色波---三色波
                self.mmsix.sebo_3(row)
                self.mmsix.radoms(row)
                print('色波---三色波')

                # # 色波---半波
                self.mmsix.sebo_h(row)
                self.mmsix.radoms(row)
                print('色波---半波')

                # 色波---半半波
                self.mmsix.sebo_hh(row)
                self.mmsix.radoms(row)
                print('色波---半半波')

                # 色波---七色波
                self.mmsix.sebo_7(row)
                self.mmsix.radoms(row)
                print('色波---七色波')

                # 合肖---
                self.mmsix.hexiao_1(row)
                self.mmsix.radoms(row)
                print('合肖---')

                # 生肖---生肖
                self.mmsix.shengxiao_zhx(row)
                self.mmsix.radoms(row)
                print('生肖---生肖')

                # 生肖---平特一肖
                self.mmsix.shengxiao_tex(row)
                self.mmsix.radoms(row)
                print('生肖---平特一肖')

                # 生肖---一肖
                self.mmsix.shengxiao_yix(row)
                self.mmsix.radoms(row)
                print('生肖---一肖')

                # 生肖---总肖
                self.mmsix.shengxiao_zongx(row)
                self.mmsix.radoms(row)
                print('生肖---总肖')

                # 自选不中---五不中
                self.mmsix.nochoice_5(row)
                self.mmsix.radoms(row)
                print('自选不中---五不中')

                # 自选不中---六不中
                self.mmsix.nochoice_6(row)
                self.mmsix.radoms(row)
                print('自选不中---六不中')

                # 自选不中---七不中
                self.mmsix.nochoice_7(row)
                self.mmsix.radoms(row)
                print('自选不中---七不中')

                # 自选不中---八不中
                self.mmsix.nochoice_8(row)
                self.mmsix.radoms(row)
                print('自选不中---八不中')

                # 自选不中---九不中
                self.mmsix.nochoice_9(row)
                self.mmsix.radoms(row)
                print('自选不中---九不中')

                # 自选不中---十不中
                self.mmsix.nochoice_10(row)
                self.mmsix.radoms(row)
                print('自选不中---十不中')

                # 自选不中---十一不中
                self.mmsix.nochoice_11(row)
                self.mmsix.radoms(row)
                print('自选不中---十一不中')

                # 自选不中---十二不中
                self.mmsix.nochoice_12(row)
                self.mmsix.radoms(row)
                print('自选不中---十二不中')
                

                # 连肖连尾---二连肖
                self.mmsix.lxlw_lx2(row)
                self.mmsix.radoms(row)
                print('连肖连尾---二连肖')

                # 连肖连尾---三连肖
                self.mmsix.lxlw_lx3(row)
                self.mmsix.radoms(row)
                print('连肖连尾---三连肖')

                # 连肖连尾---四连肖
                self.mmsix.lxlw_lx4(row)
                self.mmsix.radoms(row)
                print('连肖连尾---四连肖')

                # 连肖连尾---五连肖
                self.mmsix.lxlw_lx5(row)
                self.mmsix.radoms(row)
                print('连肖连尾---五连肖')

                # 连肖连尾---二连尾
                self.mmsix.lxlw_lw2(row)
                self.mmsix.radoms(row)
                print('连肖连尾---二连尾')

                # 连肖连尾---三连尾
                self.mmsix.lxlw_lw3(row)
                self.mmsix.radoms(row)
                print('连肖连尾---三连尾')

                # 连肖连尾---四连尾
                self.mmsix.lxlw_lw4(row)
                self.mmsix.radoms(row)
                print('连肖连尾---四连尾')

                # 连肖连尾---五连尾
                self.mmsix.lxlw_lw5(row)
                self.mmsix.radoms(row)
                print('连肖连尾---五连尾')

                # -----------------------------
                # -----------------------------
                # -----------------------------
                # 连码---四全中
                self.mmsix.lm_fullin4(row)
                self.mmsix.radoms(row)
                print('连码---四全中')

                # 连码---四全中---正/副号
                self.mmsix.lm_full4_zfh(row)
                self.mmsix.radoms(row)
                print('连码---四全中---正/副号')

                # 连码---四全中---肖串尾数
                self.mmsix.lm_full4_xcws(row)
                self.mmsix.radoms(row)
                print('连码---四全中---肖串尾数')
               
                # # 连码---四全中---交叉碰
                # self.mmsix.lm_full4_jcp(row)
                # self.mmsix.radoms(row)
                # print('连码---四全中---交叉碰')

                # 连码---四全中---胆拖
                self.mmsix.lm_full4_dt(row)
                self.mmsix.radoms(row)
                print('连码---四全中---胆拖')

                # 连码---四全中---胆拖色波
                self.mmsix.lm_full4_dtsb(row)
                self.mmsix.radoms(row)
                print('连码---四全中---胆拖色波')

                # 连码---四全中---胆拖生肖
                self.mmsix.lm_full4_dtsx(row)
                self.mmsix.radoms(row)
                print('连码---四全中---胆拖生肖')

                # -----------------------------
                # -----------------------------
                # -----------------------------

                # 连码---三全中
                self.mmsix.lm_full3qz(row)
                self.mmsix.radoms(row)
                print('连码---三全中')

                # 连码---三全中---正/副号
                self.mmsix.lm_full3qz_zfh(row)
                self.mmsix.radoms(row)
                print('连码---三全中---正/副号')

                # 连码---三全中---肖串尾数
                self.mmsix.lm_full3qz_xcws(row)
                self.mmsix.radoms(row)
                print('连码---三全中---肖串尾数')

                # # 连码---三全中---交叉碰
                # self.mmsix.lm_full3qz_jcp(row)
                # self.mmsix.radoms(row)
                # print('连码---四全中---交叉碰')

                # 连码---三全中---胆拖
                self.mmsix.lm_full3qz_dt(row)
                self.mmsix.radoms(row)
                print('连码---三全中---胆拖')

                # 连码---三全中---胆拖色波
                self.mmsix.lm_full3qz_dtsb(row)
                self.mmsix.radoms(row)
                print('连码---三全中---胆拖色波')

                # 连码---三全中---胆拖生肖
                self.mmsix.lm_full3qz_dtsx(row)
                self.mmsix.radoms(row)
                print('连码---三全中---胆拖生肖')

                # -----------------------------
                # -----------------------------
                # -----------------------------

                # 连码---三中二
                self.mmsix.lm_full3z2(row)
                self.mmsix.radoms(row)
                print('连码---三中二')
                #

                # 连码---三中二---正/副号
                self.mmsix.lm_full3z2_zfh(row)
                self.mmsix.radoms(row)
                print('连码---三中二---正/副号')

                # 连码---三中二---肖串尾数
                self.mmsix.lm_full3z2_xcws(row)
                self.mmsix.radoms(row)
                print('连码---三中二---肖串尾数')
                #
                # # 连码---三全中---交叉碰
                # self.mmsix.lm_full3z2_jcp(row)
                # self.mmsix.radoms(row)
                # print('连码---三中二---交叉碰')

                # 连码---三中二---胆拖
                self.mmsix.lm_full3z2_dt(row)
                self.mmsix.radoms(row)
                print('连码---三中二---胆拖')

                # 连码---三中二---胆拖色波
                self.mmsix.lm_full3z2_dtsb(row)
                self.mmsix.radoms(row)
                print('连码---三中二---胆拖色波')

                # 连码---三中二---胆拖生肖
                self.mmsix.lm_full3z2_dtsx(row)
                self.mmsix.radoms(row)
                print('连码---三中二---胆拖生肖')

                # ------------------------------------------
                # ------------------------------------------
                # ------------------------------------------

                # 连码---二全中
                self.mmsix.lm_fullin2qz(row)
                self.mmsix.radoms(row)
                print('连码---二全中')
                #

                # 连码---二全中---正/副号
                self.mmsix.lm_fullin2qz_zfh(row)
                self.mmsix.radoms(row)
                print('连码---二全中---正/副号')

                # 连码---二全中---肖串尾数
                self.mmsix.lm_fullin2qz_xcws(row)
                self.mmsix.radoms(row)
                print('连码---二全中---肖串尾数')

                # 连码---二全中---交叉碰
                # self.mmsix.lm_fullin2qz_jcp(row)
                # self.mmsix.radoms(row)
                # print('连码---二全中---交叉碰')

                # 连码---二全中---胆拖
                self.mmsix.lm_fullin2qz_dt(row)
                self.mmsix.radoms(row)
                print('连码---二全中---胆拖')

                # 连码---二全中---胆拖色波
                self.mmsix.lm_fullin2qz_dtsb(row)
                self.mmsix.radoms(row)
                print('连码---二全中---胆拖色波')

                # 连码---二全中---胆拖生肖
                self.mmsix.lm_fullin2qz_dtsx(row)
                self.mmsix.radoms(row)
                print('连码---二全中---胆拖生肖')

                # ---------------------------------------------
                # ---------------------------------------------
                # ---------------------------------------------
                # 连码---二中特
                self.mmsix.lm_fullin2zt(row)
                self.mmsix.radoms(row)
                print('连码---二中特')

                # 连码---二中特---正/副号
                self.mmsix.lm_fullin2zt_zfh(row)
                self.mmsix.radoms(row)
                print('连码---二中特---正/副号')

                # 连码---二中特---肖串尾数
                self.mmsix.lm_fullin2zt_xcws(row)
                self.mmsix.radoms(row)
                print('连码---二中特---肖串尾数')

                # 连码---二中特---交叉碰
                # self.mmsix.lm_fullin2qz_jcp(row)
                # self.mmsix.radoms(row)
                # print('连码---二中特---交叉碰')

                # 连码---二中特---胆拖
                self.mmsix.lm_fullin2zt_dt(row)
                self.mmsix.radoms(row)
                print('连码---二中特---胆拖')

                # 连码---二中特---胆拖色波
                self.mmsix.lm_fullin2zt_dtsb(row)
                self.mmsix.radoms(row)
                print('连码---二中特---胆拖色波')

                # 连码---二中特---胆拖生肖
                self.mmsix.lm_fullin2zt_dtsx(row)
                self.mmsix.radoms(row)
                print('连码---二中特---胆拖生肖')

                # ---------------------------------------------
                # ---------------------------------------------
                # ---------------------------------------------

                # 连码---特串
                self.mmsix.lm_fullinntc(row)
                self.mmsix.radoms(row)
                print('连码---特串')

                # 连码---特串---正/副号
                self.mmsix.lm_fullinntc_zfh(row)
                self.mmsix.radoms(row)
                print('连码---特串---正/副号')

                # 连码---特串---肖串尾数
                self.mmsix.lm_fullinntc_xcws(row)
                self.mmsix.radoms(row)
                print('连码---特串---肖串尾数')

                # 连码---特串---交叉碰
                # self.mmsix.lm_fullinntc_jcp(row)
                # self.mmsix.radoms(row)
                # print('连码---特串---交叉碰')

                # 连码---特串---胆拖
                self.mmsix.lm_fullinntc_dt(row)
                self.mmsix.radoms(row)
                print('连码---特串---胆拖')

                # 连码---特串---胆拖色波
                self.mmsix.lm_fullinntc_dtsb(row)
                self.mmsix.radoms(row)
                print('连码---特串---胆拖色波')

                # 连码---特串---胆拖生肖
                self.mmsix.lm_fullinntc_dtsx(row)
                self.mmsix.radoms(row)
                print('连码---特串---胆拖生肖')

                # ---------------------------------------------
                # ---------------------------------------------
                # ---------------------------------------------

                # 正码 过关
                self.mmsix.zm_zmgg(row)
                self.mmsix.radoms(row)
                print('正码 过关')

                # ---------------------------------------------
                # ---------------------------------------------
                # ---------------------------------------------
                # 正码-1-6
                self.mmsix.zm1_6(row)
                self.mmsix.radoms(row)
                print('正码-1-6')

                # 正码特
                # 正一特
                self.mmsix.zmt_1(row)
                self.mmsix.radoms(row)
                print('正码一特')

                # 正码特
                # 正二特
                self.mmsix.zmt_2(row)
                self.mmsix.radoms(row)
                print('正码特二特')

                # 正码特
                # 正三特
                self.mmsix.zmt_3(row)
                self.mmsix.radoms(row)
                print('正码特三特')

                # 正码特
                # 正四特
                self.mmsix.zmt_4(row)
                self.mmsix.radoms(row)
                print('正码特四特')

                # 正码特
                # 正五特
                self.mmsix.zmt_5(row)
                self.mmsix.radoms(row)
                print('正码特五特')

                # 正码特
                # 正六特
                self.mmsix.zmt_6(row)
                self.mmsix.radoms(row)
                print('正码特六特')

                # 正码
                self.mmsix.zmzm(row)
                self.mmsix.radoms(row)
                print('正码')

                # 特码
                self.mmsix.tm(row)
                self.mmsix.radoms(row)
                print('特码')

                # 中一
                # 五中一
                self.mmsix.choice_5(row)
                self.mmsix.radoms(row)
                print('中一---五中一')

                # 中一
                # 六中一
                self.mmsix.choice_6(row)
                self.mmsix.radoms(row)
                print('中一---六中一')

                # 中一
                # 七中一
                self.mmsix.choice_7(row)
                self.mmsix.radoms(row)
                print('中一---七中一')

                # 中一
                # 八中一
                self.mmsix.choice_8(row)
                self.mmsix.radoms(row)
                print('中一---八中一')

                # 中一
                # 九中一
                self.mmsix.choice_9(row)
                self.mmsix.radoms(row)
                print('中一---九中一')

                # 中一
                # 十中一
                self.mmsix.choice_10(row)
                self.mmsix.radoms(row)
                print('中一---十中一')
                #
                # self.base_driver.forced_wait(10)
                # get_tips = self.mmsix.get_tips()
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

        self.logger.example('正码过关下注两个号码：' + 'example')
'''
    def test_fail_01(self):
        # 下注
        self.base_driver.navigate('https://fusion.spmobileapi.net/dglobby#/play/46')
        print("成功打开网址")
        self.base_driver.forced_wait(3)
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)
        # 下注
        # 指定某一个用户登陆
        # self.lottery = Lottery(self.base_driver)
        # # 登陆
        # self.lottery.login()
        # # 点击六合彩
        # self.lottery.marksix()
        # js = "var q=document.documentElement.scrollTop=100000"
        # self.base_driver.execute_js(js)
        # 打开csv文件
        csv_file = open('/fusion/csv/marksix.csv', 'r', encoding='utf8')
        # 读取csv文件
        csv_date = csv.DictReader(csv_file)
        print('打开csv')
        for row in csv_date:
            if row['msg'] == 'succ01':
                print('进入数据循环succ01')
                # 登陆模块，调用CommonRecharge中的login()
                self.mmsix = MinuteMarkSix(self.base_driver)

                #
                #
                # 合肖---
                self.mmsix.twosidesall(row)
                print('合肖---')

                # 合肖---
                self.mmsix.hexiao_1_error(row)
                print('合肖---')

                # 自选不中---五不中
                self.mmsix.nochoice_5_error(row)
                print('自选不中---五不中')

                # 自选不中---六不中
                self.mmsix.nochoice_6_error(row)
                print('自选不中---六不中')

                # 自选不中---七不中
                self.mmsix.nochoice_7_error(row)
                print('自选不中---七不中')

                # 自选不中---八不中
                self.mmsix.nochoice_8_error(row)
                print('自选不中---八不中')
                
                # 自选不中---九不中
                self.mmsix.nochoice_9_error(row)
                print('自选不中---九不中')

                # 自选不中---十不中
                self.mmsix.nochoice_10_error(row)
                print('自选不中---十不中')

                # 自选不中---十一不中
                self.mmsix.nochoice_11_error(row)
                print('自选不中---十一不中')
                #
                # 自选不中---十二不中
                self.mmsix.nochoice_12_error(row)
                print('自选不中---十二不中')

                # 连肖连尾---二连肖
                self.mmsix.lxlw_lx2_error(row)
                print('连肖连尾---二连肖')
                #
                # 连肖连尾---三连肖
                self.mmsix.lxlw_lx3_error(row)
                print('连肖连尾---三连肖')

                # 连肖连尾---四连肖
                self.mmsix.lxlw_lx4_error(row)
                print('连肖连尾---四连肖')

                # 连肖连尾---五连肖
                self.mmsix.lxlw_lx5_error(row)
                print('连肖连尾---五连肖')

                # 连肖连尾---二连尾
                self.mmsix.lxlw_lw2_error(row)
                print('连肖连尾---二连尾')

                # 连肖连尾---三连尾
                self.mmsix.lxlw_lw3_error(row)
                print('连肖连尾---三连尾')

                # 连肖连尾---四连尾
                self.mmsix.lxlw_lw4_error(row)
                print('连肖连尾---四连尾')
               
                # 连肖连尾---五连尾
                self.mmsix.lxlw_lw5_error(row)
                print('连肖连尾---五连尾')

                # -----------------------------------------------------
                # -----------------------------------------------------
                # -----------------------------------------------------
                # -----------------------------------------------------
                #
                # 连码---四全中
                self.mmsix.lm_fullin4_error(row)
                print('连码---四全中')

                # 连码---四全中---正/副号
                self.mmsix.lm_full4_zfh_error(row)
                print('连码---四全中---正/副号')

                # 连码---四全中---肖串尾数
                self.mmsix.lm_full4_xcws_error(row)
                print('连码---四全中---肖串尾数')

                # # 连码---四全中---交叉碰
                # self.mmsix.lm_full4_jcp_error(row)
                # print('连码---四全中---交叉碰')

                # 连码---四全中---胆拖
                self.mmsix.lm_full4_dt_error(row)
                print('连码---四全中---胆拖')

                # 连码---四全中---胆拖色波
                self.mmsix.lm_full4_dtsb_error(row)
                print('连码---四全中---胆拖色波')

                # 连码---四全中---胆拖生肖
                self.mmsix.lm_full4_dtsx_error(row)
                print('连码---四全中---胆拖生肖')

                # # # ---------------------------------------------
                # # # ---------------------------------------------
                # # # ---------------------------------------------
                #
                # 连码---三全中
                self.mmsix.lm_full3qz_error(row)
                print('连码---三全中')

                # 连码---三全中---正/副号
                self.mmsix.lm_full3qz_zfh_error(row)
                print('连码---三全中---正/副号')

                # 连码---三全中---肖串尾数
                self.mmsix.lm_full3qz_xcws_error(row)
                print('连码---三全中---肖串尾数')

                # # 连码---三全中---交叉碰
                # self.mmsix.lm_full3qz_jcp_error(row)
                # print('连码---三全中---交叉碰')

                # 连码---三全中---胆拖
                self.mmsix.lm_full3qz_dt_error(row)
                print('连码---三全中---胆拖')

                # 连码---三全中---胆拖色波
                self.mmsix.lm_full3qz_dtsb_error(row)
                print('连码---三全中---胆拖色波')

                # 连码---三全中---胆拖生肖
                self.mmsix.lm_full3qz_dtsx_error(row)
                print('连码---三全中---胆拖生肖')

                # ------------------------------------------------
                # ------------------------------------------------
                # ------------------------------------------------

                # 连码---三中二
                self.mmsix.lm_full3z2_error(row)
                print('连码---三中二')

                # 连码---三中二---正/副号
                self.mmsix.lm_full3z2_zfh_error(row)
                print('连码---三中二---正/副号')

                # 连码---三中二---肖串尾数
                self.mmsix.lm_full3z2_xcws_error(row)
                print('连码---三中二---肖串尾数')

                # # 连码---三中二---交叉碰
                # self.mmsix.lm_full3z2_jcp_error(row)
                # print('连码---三中二---交叉碰')

                # 连码---三中二---胆拖
                self.mmsix.lm_full3z2_dt_error(row)
                print('连码---三中二---胆拖')

                # 连码---三中二---胆拖色波
                self.mmsix.lm_full3z2_dtsb_error(row)
                print('连码---三中二---胆拖色波')

                # 连码---三中二---胆拖生肖
                self.mmsix.lm_full3z2_dtsx_error(row)
                print('连码---三中二---胆拖生肖')

                # # # ---------------------------------------------
                # # # ---------------------------------------------
                # # # ---------------------------------------------
                # 连码---二全中
                self.mmsix.lm_fullin2qz_error(row)
                print('连码---二全中')
                
                # 连码---二全中---正/副号
                self.mmsix.lm_fullin2qz_zfh_error(row)
                print(' 连码---二全中---正/副号')

                # 连码---二全中---肖串尾数
                self.mmsix.lm_fullin2qz_xcws_error(row)
                print(' 连码---二全中---肖串尾数')

                # # 连码---二全中---交叉碰
                # # # self.mmsix.lm_fullin2qz_dt_error(row)
                # # # print(' 连码---二全中---交叉碰')
                
                # 连码---二全中---胆拖
                self.mmsix.lm_fullin2zt_dt_error(row)
                print(' 连码---二全中---胆拖')

                # 连码---二全中---胆拖色波
                self.mmsix.lm_fullin2zt_dtsb_error(row)
                print(' 连码---二全中---胆拖色波')

                # 连码---二全中---胆拖生肖
                self.mmsix.lm_fullin2zt_dtsx_error(row)
                print(' 连码---二全中---胆拖生肖')
                # # # ---------------------------------------------
                # # # ---------------------------------------------
                # # # ---------------------------------------------
                
                # 连码---二中特
                self.mmsix.lm_fullin2zt_error(row)
                print('连码---二中特')

                # 连码---二中特---正/副号
                self.mmsix.lm_fullin2zt_zfh_error(row)
                print(' 连码---二中特---正/副号')
                
                # 连码---二中特---生肖对碰
                self.mmsix.lm_fullin2zt_sxdp_error(row)
                print(' 连码---二中特---生肖对碰')
                
                # 连码---二中特---尾数对碰
                self.mmsix.lm_fullin2zt_wsdp_error(row)
                print(' 连码---二中特---尾数对碰')

                # 连码---二中特---肖串尾数
                self.mmsix.lm_fullin2zt_xcws_error(row)
                print(' 连码---二中特---肖串尾数')

                # # # 连码---二中特---交叉碰
                # # self.mmsix.lm_fullin2zt_dt_error(row)
                # # print(' 连码---二中特---交叉碰')
                
                # 连码---二中特---胆拖
                self.mmsix.lm_fullin2zt_dt_error(row)
                print(' 连码---二中特---胆拖色波')

                # 连码---二中特---胆拖色波
                self.mmsix.lm_fullin2zt_dtsb_error(row)
                print(' 连码---二中特---胆拖色波')

                # 连码---二中特---胆拖生肖
                self.mmsix.lm_fullin2zt_dtsx_error(row)
                print(' 连码---二中特---胆拖生肖')
                # # # ---------------------------------------------
                # # # ---------------------------------------------
                # # # ---------------------------------------------
                # # 连码---特串
                self.mmsix.lm_fullinntc_error(row)
                print('连码---特串')

                # 连码---特串---正/副号
                self.mmsix.lm_fullinntc_zfh_error(row)
                print(' 连码---特串---正/副号')

                # 连码---特串---生肖对碰
                self.mmsix.lm_fullinntc_sxdp_error(row)
                print(' 连码---特串---尾数对碰')

                # 连码---特串---尾数对碰
                self.mmsix.lm_fullinntc_wsdp_error(row)
                print(' 连码---特串---尾数对碰')

                # 连码---特串---肖串尾数
                self.mmsix.lm_fullinntc_xcws_error(row)
                print(' 连码---特串---肖串尾数')

                # # # 连码---特串---交叉碰
                # self.mmsix.lm_fullinntc_dt_error(row)
                # # print(' 连码---特串---交叉碰')
                
                # 连码---特串---胆拖
                self.mmsix.lm_fullinntc_dt_error(row)
                print(' 连码---特串---胆拖色波')

                # 连码---特串---胆拖色波
                self.mmsix.lm_fullinntc_dtsb_error(row)
                print(' 连码---特串---胆拖色波')

                # 连码---特串---胆拖生肖
                self.mmsix.lm_fullinntc_dtsx_error(row)
                print(' 连码---特串---胆拖生肖')
                # ---------------------------------------------
                # ---------------------------------------------
                # ---------------------------------------------

                # 正码过关--正码过关
                self.mmsix.zm_zmgg_error(row)
                print('正码过关--正码过关')

                # ---------------------------------------------
                # ---------------------------------------------
                # ---------------------------------------------

                # 中一
                # 中一---五中一
                self.mmsix.choice_5_error(row)
                print('中一---五中一')

                # 中一
                # 中一---六中一
                self.mmsix.choice_6_error(row)
                print('中一---六中一')

                # 中一
                # 中一---七中一
                self.mmsix.choice_7_error(row)
                print('中一---七中一')

                # 中一
                # 中一---八中一
                self.mmsix.choice_8_error(row)
                print('中一---八中一')

                # 中一
                # 中一---九中一
                self.mmsix.choice_9_error(row)
                print('中一---九中一')

                # 十中一
                # 中一---十中一
                self.mmsix.choice_10_error(row)
                print('中一---十中一')
                #
                # self.base_driver.forced_wait(10)
                # get_tips = self.mmsix.get_tips()
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

        self.logger.example('正码过关下注两个号码：' + 'example')
'''

if __name__ == '__main__':

    unittest.main()
