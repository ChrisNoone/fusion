from common.box import TestCase


class AgentCenter(TestCase):
    def dianziyouyi(self, dzyy_items):
        # 电子游艺
        if dzyy_items == '额度转换':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[1]')
        if dzyy_items == '转换记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]')
        if dzyy_items == '平台余额':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[3]')
