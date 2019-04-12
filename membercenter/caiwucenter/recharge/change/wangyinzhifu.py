from common.box import TestCase


class SuSuDeposit1(TestCase):


    def hyzx_cwzx_idem_rk_yuan(self, hyzx_cwzx_idem_rk_yuan):

        # 充值金额
        if hyzx_cwzx_idem_rk_yuan == '充值金额':
            self.base_driver.get_text('x,// *[ @ id = "main"] / div / section / div[2] / div / input')
        # 50,100,300,500,800,1000,2000,3000
        if hyzx_cwzx_idem_rk_yuan == '50':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[1]')
        if hyzx_cwzx_idem_rk_yuan == '100':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[2]')
        if hyzx_cwzx_idem_rk_yuan == '300':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[3]')
        if hyzx_cwzx_idem_rk_yuan == '500':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[4]')
        if hyzx_cwzx_idem_rk_yuan == '800':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[5]')
        if hyzx_cwzx_idem_rk_yuan == '1000':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[6]')
        if hyzx_cwzx_idem_rk_yuan == '2000':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[7]')
        if hyzx_cwzx_idem_rk_yuan == '3000':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[1]/li[8]')

    def yunshanfu(self,ysf):
        if ysf == '云闪付':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li')

    def next_buttion(self):
        # 下一步按钮
        nt = self.base_driver.click('x,//*[@id="main"]/div/section/div[2]/div/div[2]/button')
        return nt
    def youhuijuan(self):
        # 优惠劵
        youhuijuan = self.base_driver.click('x,//*[@id="main"]/div/section/div[2]/div/div[1]')
        return youhuijuan



