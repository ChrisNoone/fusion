from common.box import TestCase


class CaiWuCenter(TestCase):

    def caiwucenter_idem(self, cwcenter_idems):
        # 财务中心
        if cwcenter_idems == '充值':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[1]')
        if cwcenter_idems == '提现':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[2]')
        if cwcenter_idems == '充值记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[3]')
        if cwcenter_idems == '提现记录':
            self.base_driver.click('xpath,//*[@id="main"]/div/ul/li[2]/ul/li[4]')

    def hyzx_cwzx_idem_rk(self, hyzx_cwzx_idem_rk):
        # 充值入款方式
        if hyzx_cwzx_idem_rk == 'SUSU公司入款':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[1]')
        if hyzx_cwzx_idem_rk == '支付宝转账':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[2]')
        if hyzx_cwzx_idem_rk == '公司入款':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[3]')
        if hyzx_cwzx_idem_rk == 'VIP代理充值':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/ul/li[4]')

    def hyzx_cwzx_idem_rk_bank(self, hyzx_cwzx_idem_rk_bank):
        # 充值入款方式
        if hyzx_cwzx_idem_rk_bank == '中国工商银行_susu':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[1]')
        if hyzx_cwzx_idem_rk_bank == '中国工商银行我测试啊':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[2]')
        if hyzx_cwzx_idem_rk_bank == '中国工商银行李洁':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[3]')
        if hyzx_cwzx_idem_rk_bank == '中国光大银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[4]')
        if hyzx_cwzx_idem_rk_bank == '中国银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[5]')
        if hyzx_cwzx_idem_rk_bank == '江苏银行-123':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[6]')
        if hyzx_cwzx_idem_rk_bank == '恒丰银行':
            self.base_driver.click('xpath,//*[@id="main"]/div/section/div[2]/div/ul[2]/li[7]')

    def hyzx_cwzx_idem_rk_yuan(self, hyzx_cwzx_idem_rk_yuan):
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

    def cwbutton(self):
        # 下一步
        cwb = self.base_driver.click('x,//*[@id="main"]/div/section/div[2]/button')
        return cwb
