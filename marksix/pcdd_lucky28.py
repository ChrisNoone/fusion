import random
import time

from common.box import BasePage, YamlHelper, drag_and_drop_by_offset, ActionChainss


class PcddLucky28(BasePage):
    # 幸运28
    config_dict_pclk28 = YamlHelper().get_config_dict('/fusion/yaml/lottery_pcdd_lucky28.yaml')['LUCKY28']

    def tema(self, row):
        # 特码
        try:
            for i in range(0, 7):
                s0 = random.choice(range(1, 100))
                s1 = [1, 5, 10, 20, s0]
                s2 = random.choice(range(0, 5))
                s3 = random.choice(range(0, 5))
                s4 = random.choice(range(0, 5))
                s5 = random.choice(range(0, 5))
                self.base_driver.types(self.config_dict_pclk28['L28TAN0'], s1[s2], i)
                self.base_driver.types(self.config_dict_pclk28['L28TAN1'], s1[s3], i)
                self.base_driver.types(self.config_dict_pclk28['L28TAN2'], s1[s4], i)
                self.base_driver.types(self.config_dict_pclk28['L28TAN3'], s1[s5], i)
            self.base_driver.click(self.config_dict_pclk28['ADDNOTE'])
        except Exception as e:
            print(e)
            now_Time = time.strftime("%Y%m%d.%H.%M.%S")
            ss = '/fusion/pictures/luck28/' + '%s-特码.png' % now_Time
            self.base_driver.save_window_snapshot_by_io(ss)
            # self.logger.infos('特码下注异常')
            self.base_driver.refresh()
            self.base_driver.forced_wait(4)
            print('特码')

    def tema_bao3(self, row):
        # 特码包三
        print('特码包三')
        for i in range(100):
            a = random.choice(range(0, 27))
            b = random.choice(range(0, 27))
            c = random.choice(range(0, 27))
            self.base_driver.type(self.config_dict_pclk28['L28TAB3'], '1')
            self.base_driver.forced_wait(2)
            if a == b or a == c or b == c:
                pass
            else:
                print('选择的号码是：' + str(a) + str(b) + str(c))
                s1 = self.base_driver.clicks(self.config_dict_pclk28['L28TAB30'], a)
                self.base_driver.select_by_visible_text(self.config_dict_pclk28['L28TAB30'], a)
                self.base_driver.select_by_value(self.config_dict_pclk28['L28TAB31'], b)
                self.base_driver.select_by_visible_text(self.config_dict_pclk28['L28TAB32'], c)
                self.base_driver.type(self.config_dict_pclk28['L28TAB3'], '1')



    def tema_bao31(self, row):
        # 特码包三
        print('特码包三')
        s0 = random.choice(range(5, 10))
        s1 = random.choice(range(0, 10))
        self.base_driver.select_by_visible_text(self.config_dict_pclk28['L28TAB30'], 10)
        self.base_driver.forced_wait(2)
        # self.base_driver.select_by_visible_text(self.config_dict_pclk28['L28TAB30'], '每页显示20条')
        # self.base_driver.forced_wait(2)
        # self.base_driver.select_by_visible_text(self.config_dict_pclk28['L28TAB30'], '每页显示10条')
        #s = self.base_driver.select_and_click(self.config_dict_pclk28['L28TAB30'], s0)

        self.base_driver.forced_wait(2)





    def hsb(self, row):
        # 混合
        s0 = random.choice(range(1, 100))
        s1 = [1, 5, 10, 20, s0]
        s2 = random.choice(range(0, 5))
        s3 = random.choice(range(0, 5))
        s4 = random.choice(range(0, 5))
        s5 = random.choice(range(0, 5))
        self.base_driver.type(self.config_dict_pclk28['L28HHDA'], s1[s2])
        self.base_driver.type(self.config_dict_pclk28['L28HHDAN'], s1[s2])
        self.base_driver.type(self.config_dict_pclk28['L28HHDDD'], s1[s2])
        self.base_driver.type(self.config_dict_pclk28['L28HHDSS'], s1[s2])
        self.base_driver.type(self.config_dict_pclk28['L28HHJID'], s1[s2])
        print('混合大：' + str(s1[s2]))
        print('混合单：' + str(s1[s2]))
        print('混合大单：' + str(s1[s2]))
        print('混合大双：' + str(s1[s2]))

        self.base_driver.type(self.config_dict_pclk28['L28HHX'], s1[s3])
        self.base_driver.type(self.config_dict_pclk28['L28HHSS'], s1[s3])
        self.base_driver.type(self.config_dict_pclk28['L28HHXD'], s1[s3])
        self.base_driver.type(self.config_dict_pclk28['L28HHXS'], s1[s3])
        self.base_driver.type(self.config_dict_pclk28['L28HHJIX'], s1[s3])
        print('混合小：' + str(s1[s3]))
        print('混合双：' + str(s1[s3]))
        print('混合小单：' + str(s1[s3]))
        print('混合小双：' + str(s1[s3]))

        # 色波
        self.base_driver.type(self.config_dict_pclk28['L28SBR'], s1[s4])
        self.base_driver.type(self.config_dict_pclk28['L28SBG'], s1[s4])
        self.base_driver.type(self.config_dict_pclk28['L28SEB'], s1[s4])
        print('混合红波：' + str(s1[s4]))
        print('混合绿波：' + str(s1[s4]))
        print('混合蓝波：' + str(s1[s4]))

        # 豹子
        self.base_driver.type(self.config_dict_pclk28['L28BZ'], s1[s5])
        print('混合豹子：' + str(s1[s5]))
        print('混合---色波---豹子')

    def drag_element1(self):
        # self.base_driver.drag_element(self.config_dict_pclk28['TTT1'], 10)
        # self.base_driver.get_selected()
        # target = self.base_driver.clicks(self.config_dict_pclk28['TTT'], 0.5)
        # self.base_driver.execute_js("arguments[0].scrollIntoView();", target)
        js = "var q=document.documentElement.scrollTop=100000"
        self.base_driver.execute_js(js)

    def move_to_gap(self, row):
        # 得到滑块标签

        self.base_driver.drag_and_drop_by_offset(
            self.config_dict_pclk28['SLIDER'], 10, 0).perform()

        '''
        slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gt_slider_knob')))
        # 使用click_and_hold()方法悬停在滑块上，perform()方法用于执行
        ActionChains(browser).click_and_hold(slider).perform()
        for x in self:
            # 使用move_by_offset()方法拖动滑块，perform()方法用于执行
            ActionChains(browser).drag_and_drop_by_offset(xoffset=x, yoffset=0).perform()
           
        self.base_driver.forced_wait(0.5)
        # 释放滑块
        ActionChains(browser).release().perform()
        '''


    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_pclk28['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(3)

    def radoms(self, row):

        # 随机5注
        self.base_driver.click(self.config_dict_pclk28['RANDOM5'])
        self.base_driver.forced_wait(3)
        # 随机1注2元
        self.base_driver.click(self.config_dict_pclk28['RANDOM1'])
        # 随机一注2角
        self.base_driver.click(self.config_dict_pclk28['JIAO'])
        self.base_driver.click(self.config_dict_pclk28['RANDOM1'])
        # 随机一注2分
        self.base_driver.click(self.config_dict_pclk28['FEN'])
        self.base_driver.click(self.config_dict_pclk28['RANDOM1'])
        # 随机20
        s = random.choice(range(0, 1000))
        self.base_driver.type(self.config_dict_pclk28['XIUGAI'], "\b" + str(s))
        self.base_driver.click(self.config_dict_pclk28['RANDOM1'])
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        print('随机1注')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        self.base_driver.forced_wait(1)
        print('随机5注')

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_pclk28['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
        self.base_driver.forced_wait(3)
        return surebet

    def get_tips(self):
        tips = self.base_driver.get_text(self.config_dict_pclk28['TIPS'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips01(self):
        # 提示请先添加投注内容
        tips = self.base_driver.get_text(self.config_dict_pclk28['TIPS01'])
        print('捕捉到的信息是：' + tips)
        return tips

    def get_tips02(self):
        # 提示下注成功
        tips = self.base_driver.get_text(self.config_dict_pclk28['TIPS02'])
        print('捕捉到的信息是：' + tips)
        return tips