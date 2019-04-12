from common.box import TestCase


class TranRecord(TestCase):
    def tranrecord(self, trecord):
        # 交易记录
        if trecord == '数字彩投注记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div/div[1]/div/div/div/div/div[2]')
        if trecord == '体彩投注记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div/div[1]/div/div/div/div/div[3]')
        if trecord == '电子游艺投注记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div/div[1]/div/div/div/div/div[4]')
        if trecord == '帐变记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div/div[1]/div/div/div/div/div[5]')
