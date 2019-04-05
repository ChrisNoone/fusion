from common.box import TestCase


class ElectGame(TestCase):

    def electgame(self, agame):
        # 电子游艺
        if agame == '额度转换':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[4]/ul/li[1]')
        if agame == '转换记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[4]/ul/li[2]')
        if agame == '平台余额':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[4]/ul/li[3]')
