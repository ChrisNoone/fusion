import random

from common.box import BasePage, YamlHelper


class MinuteMarkSix(BasePage):
    # 分分六合彩
    config_dict_marksix = YamlHelper().get_config_dict('/fusion/yaml/lottery_marksix.yaml')['MarkSix']

    def menu(self):
        self.base_driver.click(self.config_dict_marksix['MENU'])

    # 两面-------------
    # -------------------------------------------------------------------
    # -------------------------------------------------------------------
    # -------------------------------------------------------------------

    def lm_fullin4(self, row):

        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.clicks(self.config_dict_marksix['FULLIN4'], '0')
        self.base_driver.forced_wait(1)
        print('进入四全中')
        # 随机抽取4个号码
        for i in range(100):
            s0 = random.choice(range(0, 7))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))
            s6 = random.choice(range(0, 5))
            s7 = random.choice(range(0, 5))
            s8 = random.choice(range(0, 5))
            
            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))

            # 随机四个号码
            if s0 == 0:
                if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                        or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                    if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    pass
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            
            # 随机五个号码
            if s0 == 1:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            
            # 随机六个号码
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                        or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5 \
                        or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 or b3 == b5 or b4 == b5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
           
            # 随机七个号码
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:

                    if a0 == a1 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
           
            # 随机八个号码
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1 or a2 == a3 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个号码')
                else:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            
            # 随机九个号码
            if s0 == 5:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:

                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('随机九个号码')

            # 随机十个号码
            if s0 == 6:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('随机十个号码')


        print('覆盖完毕------')

    def lm_fullin4_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)
        print('进入四全中')
        for i in range(100):
            s0 = random.choice(range(0, 4))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))

            c0 = random.choice(range(0, 10))
            c1 = random.choice(range(0, 10))
            c2 = random.choice(range(0, 10))
            c3 = random.choice(range(0, 10))
            c4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
            # 任意两个
            if s0 == 1:
                if s1 == s2:
                    pass
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)
            # 任意三个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], c0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], c1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], c2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], c3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], c4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意三个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], c0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], c1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], c2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], c3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], c4)

            # 任意11个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a1 == a2 or a2 == a3 or b0 == b1 or b2 == b3 or a4 == b4:
                    pass
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                print('随机11个号码')

        print('覆盖完毕------')

    def lm_full4_zfh(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---正/副号')

        for i in range(1000000):
            s0 = random.choice(range(0, 7))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机四个
            if s0 == 0:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 1:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 6:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

    def lm_full4_zfh_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---四全中---正/副号')

        for i in range(100):
            s0 = random.choice(range(0, 4))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))

            c0 = random.choice(range(0, 10))
            c1 = random.choice(range(0, 10))
            c2 = random.choice(range(0, 10))
            c3 = random.choice(range(0, 10))
            c4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 任意两个
            if s0 == 1:
                if s1 == s2:
                    pass
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                        
            # 任意三个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意三个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 特殊选择四个号码--- 选择五个，去掉正号
            if s0 == 3:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    # 去掉正
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('特殊选择四个号码--- 选择五个，去掉正号：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 任意11个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a1 == a2 or a2 == a3 or b0 == b1 or b2 == b3 or a4 == b4:
                    pass
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                print('随机11个号码')

    def lm_full4_xcws(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---肖串尾数')

        # 连码---二全中----12
        for i in range(20):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            if ss == 0:
                # 生肖---尾数各随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                print('随机二个：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_full4_xcws_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串--肖串尾数')

        # 连码---二全中----12
        for i in range(100):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            try:
                # 生肖随机一个
                if ss == 0:
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                # # 尾数随机一个
                if ss == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    print('尾数随机一个：  ' + ' ' + str(i))
            except Exception as e:
                print(e)
                # self.base_driver.forced_wait(1)
                self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
                self.base_driver.click(self.config_dict_marksix['TIPS04'])

        print('覆盖完毕------')

    def lm_full4_jcp(self, row):
        # 连码
        self.base_driver.click(self.config_dict_marksix['LIANMA'])
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.click(self.config_dict_marksix['FULLIN4'])
        self.base_driver.forced_wait(1)
        # 连码---四全中---交叉碰
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')

        # self.base_driver.forced_wait(3)

        # 新增柱列
        for i in range(20):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 8))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            c0 = random.sample(range(0, 5), 4)
            a0 = random.choice(range(0, 10))

            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 5))
            # 尾选四
            if s0 == 0:
                # 尾数
                if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a0)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a1)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a2)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN3'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数')
            # 数字选4
            if s0 == 1:
                if s2 == s3 or s2 == s4 or s2 == s5 or s3 == s4 or s3 == s5 or s4 == s5:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])

                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                    if s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN3'])

                    if s5 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s5 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s5 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s5 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s5 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('数字')
            # 生肖--色波
            if s0 == 2:
                if s1 == 0:
                    #四个生肖
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a0)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a1)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a2)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN3'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖--色波')
                if s1 == 2:
                    #三个生肖
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a0)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a1)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a2)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN3'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖--色波')

    '''
    def lm_full4_jcp_error(self, row):
        # 连码
        self.base_driver.click(self.config_dict_marksix['LIANMA'])
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.click(self.config_dict_marksix['FULLIN4'])
        self.base_driver.forced_wait(1)
        # 连码---四全中---交叉碰
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')

        # self.base_driver.forced_wait(3)

        # 新增柱列
        for i in range(2000000000):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 8))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            c0 = random.sample(range(0, 5), 4)
            a0 = random.choice(range(0, 10))

            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 5))
            # 数字选1
            if s0 == 0:
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                print('s111111:   ' + str(s2))
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.forced_wait(3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                print('s22222:    ' + str(s2))
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
            
            # 数学选2
            if s0 == 1:
                if s2 == s3:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---四全中---数学选2：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

            if s0 == 2:
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                if s3 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s3 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s3 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s3 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s3 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                if s4 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s4 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s4 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s4 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s4 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                if s3 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s3 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s3 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s3 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s3 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                if s4 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s4 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s4 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s4 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s4 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                print('数字')

            
    '''
    def lm_full4_dt(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(1000000):
            s0 = random.choice(range(0, 5))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == s2 or a0 == b0 or a1 == b1 or a2 == b2 or a3 == b3 or a4 == b4:
                    pass
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)

                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

        print('覆盖完毕------')

    def lm_full4_dt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(30):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
            if s0 == 1:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

        print('覆盖完毕------')

    def lm_full4_dtsb(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖色波')

        for i in range(5):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)

                self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            else:
                pass

        print('覆盖完毕------')

    def lm_full4_dtsb_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖色波')
        # 任意选择一个胆
        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
            print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
        # 任选一个色波
        c0 = random.choice(range(0, 3))
        self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('连码---特串---胆拖生肖：  ' + ' ' + str(s))
        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

        print('覆盖完毕------')

    def lm_full4_dtsx(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖生肖')

        for i in range(20):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，一个拖
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            # 任意选择一个胆，二个拖
            if s0 == 1:
                if s1 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                else:
                    pass
            else:
                pass

        print('覆盖完毕------')

    def lm_full4_dtsx_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '0')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖生肖')

        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
            # 任选一个拖
            if s0 == 1:
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)

                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
            # 任选二个拖
            if s0 == 2:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                else:
                    pass

        print('覆盖完毕------')

    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------

    def lm_full3qz(self, row):

        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.clicks(self.config_dict_marksix['FULLIN4'], '1')
        self.base_driver.forced_wait(1)
        print('进入四全中')
        # 随机抽取4个号码
        for i in range(100):
            s0 = random.choice(range(0, 8))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))
            s6 = random.choice(range(0, 5))
            s7 = random.choice(range(0, 5))
            s8 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            # 随机三个号码
            if s0 == 0:
                if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    pass
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机四个号码
            if s0 == 1:
                if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                        or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                    if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    pass
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机五个号码
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机六个号码
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                        or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5 \
                        or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 or b3 == b5 or b4 == b5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机七个号码
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:

                    if a0 == a1 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机八个号码
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1 or a2 == a3 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个号码')
                else:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机九个号码
            if s0 == 6:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:

                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('随机九个号码')

            # 随机十个号码
            if s0 == 7:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('随机十个号码')

        print('覆盖完毕------')

    def lm_full3qz_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)
        print('进入四全中')
        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))

            c0 = random.choice(range(0, 10))
            c1 = random.choice(range(0, 10))
            c2 = random.choice(range(0, 10))
            c3 = random.choice(range(0, 10))
            c4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
            # 任意两个
            if s0 == 1:
                if s1 == s2:
                    pass
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)

            # 任意11个
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a1 == a2 or a2 == a3 or b0 == b1 or b2 == b3 or a4 == b4:
                    pass
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                print('随机11个号码')

        print('覆盖完毕------')

    def lm_full3qz_zfh(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---三全中---正/副号')

        for i in range(1000000):
            s0 = random.choice(range(0, 8))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机三个
            if s0 == 0:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 7:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

    def lm_full3qz_zfh_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---四全中---正/副号')

        for i in range(100):
            s0 = random.choice(range(0, 4))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))

            c0 = random.choice(range(0, 10))
            c1 = random.choice(range(0, 10))
            c2 = random.choice(range(0, 10))
            c3 = random.choice(range(0, 10))
            c4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 任意两个
            if s0 == 1:
                if s1 == s2:
                    pass
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 特殊选择三个号码--- 选择四个，去掉正号
            if s0 == 3:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    # 去掉正
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('特殊选择四个号码--- 选择五个，去掉正号：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)

            # 任意11个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a1 == a2 or a2 == a3 or b0 == b1 or b2 == b3 or a4 == b4:
                    pass
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                print('随机11个号码')

    def lm_full3qz_xcws(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---三全中---肖串尾数')

        # 连码---三全中----12
        for i in range(20):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            if ss == 0:
                # 生肖---尾数各随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                print('随机二个：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_full3qz_xcws_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串--肖串尾数')

        # 连码---二全中----12
        for i in range(100):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            try:
                # 生肖随机一个
                if ss == 0:
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                # # 尾数随机一个
                if ss == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    print('尾数随机一个：  ' + ' ' + str(i))
            except Exception as e:
                print(e)
                # self.base_driver.forced_wait(1)
                self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
                self.base_driver.click(self.config_dict_marksix['TIPS04'])

        print('覆盖完毕------')

    def lm_full3qz_jcp(self, row):
        # 连码
        self.base_driver.click(self.config_dict_marksix['LIANMA'])
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.click(self.config_dict_marksix['FULLIN4'])
        self.base_driver.forced_wait(1)
        # 连码---四全中---交叉碰
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')

        # self.base_driver.forced_wait(3)

        # 新增柱列
        for i in range(20):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 8))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            c0 = random.sample(range(0, 5), 4)
            a0 = random.choice(range(0, 10))

            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 5))
            # 尾选三
            if s0 == 0:
                # 尾数
                if a0 == a1 or a0 == a2 or a1 == a2:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a0)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a1)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a2)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数')
            # 数字选4
            if s0 == 1:
                if s2 == s3 or s2 == s4 or s3 == s4:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])

                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                    if s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN3'])

                    print('数字')
            # 生肖--色波
            if s0 == 2:
                if s1 == 0:
                    # 三个生肖
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a0)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a1)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖--色波')
                if s1 == 2:
                    # 三个生肖
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a0)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a1)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖--色波')

    '''
    def lm_full4_jcp_error(self, row):
        # 连码
        self.base_driver.click(self.config_dict_marksix['LIANMA'])
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.click(self.config_dict_marksix['FULLIN4'])
        self.base_driver.forced_wait(1)
        # 连码---四全中---交叉碰
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')

        # self.base_driver.forced_wait(3)

        # 新增柱列
        for i in range(2000000000):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 8))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            c0 = random.sample(range(0, 5), 4)
            a0 = random.choice(range(0, 10))

            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 5))
            # 数字选1
            if s0 == 0:
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                print('s111111:   ' + str(s2))
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.forced_wait(3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                print('s22222:    ' + str(s2))
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

            # 数学选2
            if s0 == 1:
                if s2 == s3:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---四全中---数学选2：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

            if s0 == 2:
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                if s3 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s3 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s3 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s3 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s3 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                if s4 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s4 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s4 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s4 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s4 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                if s3 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s3 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s3 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s3 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s3 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                if s4 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s4 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s4 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s4 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s4 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                print('数字')


    '''

    def lm_full3qz_dt(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(100):
            s0 = random.choice(range(0, 5))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == s2 or a0 == b0 or a1 == b1 or a2 == b2 or a3 == b3 or a4 == b4:
                    pass
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)

                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

        print('覆盖完毕------')

    def lm_full3qz_dt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(30):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
            if s0 == 1:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

        print('覆盖完毕------')

    def lm_full3qz_dtsb(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖色波')

        for i in range(5):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)

                self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            else:
                pass

        print('覆盖完毕------')

    def lm_full3qz_dtsb_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖色波')
        # 任意选择一个胆
        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
            print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
        # 任选一个色波
        c0 = random.choice(range(0, 3))
        self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('连码---特串---胆拖生肖：  ' + ' ' + str(s))
        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

        print('覆盖完毕------')

    def lm_full3qz_dtsx(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖生肖')

        for i in range(20):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，一个拖
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            # 任意选择一个胆，二个拖
            if s0 == 1:
                if s1 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                else:
                    pass
            else:
                pass

        print('覆盖完毕------')

    def lm_full3qz_dtsx_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '1')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖生肖')

        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
            # 任选一个拖
            if s0 == 1:
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)

                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
            # 任选二个拖
            if s0 == 2:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                else:
                    pass

        print('覆盖完毕------')

    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    def lm_full3z2(self, row):

        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.clicks(self.config_dict_marksix['FULLIN4'], '2')
        self.base_driver.forced_wait(1)
        print('进入四全中')
        # 随机抽取4个号码
        for i in range(100):
            s0 = random.choice(range(0, 8))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))
            s6 = random.choice(range(0, 5))
            s7 = random.choice(range(0, 5))
            s8 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            # 随机三个号码
            if s0 == 0:
                if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                    if s1 == s2 or s1 == s3 or s2 == s3:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    pass
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机四个号码
            if s0 == 1:
                if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                        or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                    if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                        pass
                    else:
                        if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    pass
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机五个号码
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机六个号码
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a1 == a2 or a1 == a3 or a1 == a4 \
                        or a1 == a5 or a2 == a3 or a2 == a4 or a2 == a5 or a3 == a4 or a3 == a5 or a4 == a5 \
                        or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b2 == b3 or b2 == b4 or b2 == b5 or b3 == b4 or b3 == b5 or b4 == b5:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机七个号码
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:

                    if a0 == a1 or a2 == a3:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个号码')
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a5)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b6)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机八个号码
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1 or a2 == a3 or a4 == a5:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个号码')
                else:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        if a0 == a1:
                            pass
                        else:
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a1)
                            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

            # 随机九个号码
            if s0 == 6:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:

                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('随机九个号码')

            # 随机十个号码
            if s0 == 7:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('随机十个号码')

        print('覆盖完毕------')

    def lm_full3z2_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)
        print('进入四全中')
        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))

            c0 = random.choice(range(0, 10))
            c1 = random.choice(range(0, 10))
            c2 = random.choice(range(0, 10))
            c3 = random.choice(range(0, 10))
            c4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
            # 任意两个
            if s0 == 1:
                if s1 == s2:
                    pass
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], b0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], b1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], b2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], b3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], b4)

            # 任意11个
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a1 == a2 or a2 == a3 or b0 == b1 or b2 == b3 or a4 == b4:
                    pass
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], a0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], b4)
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF101_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF111_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF121_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF131_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZF141_49'], a4)
                print('随机11个号码')

        print('覆盖完毕------')

    def lm_full3z2_zfh(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---三全中---正/副号')

        for i in range(1000000):
            s0 = random.choice(range(0, 8))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机三个
            if s0 == 0:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 2:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 7:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

    def lm_full3z2_zfh_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---四全中---正/副号')

        for i in range(100):
            s0 = random.choice(range(0, 4))
            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))

            c0 = random.choice(range(0, 10))
            c1 = random.choice(range(0, 10))
            c2 = random.choice(range(0, 10))
            c3 = random.choice(range(0, 10))
            c4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 任意两个
            if s0 == 1:
                if s1 == s2:
                    pass
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意二个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)

            # 特殊选择三个号码--- 选择四个，去掉正号
            if s0 == 3:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    # 去掉正
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('特殊选择四个号码--- 选择五个，去掉正号：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)

            # 任意11个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a1 == a2 or a2 == a3 or b0 == b1 or b2 == b3 or a4 == b4:
                    pass
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('任意11个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], b1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], b3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], a4)
                print('随机11个号码')

    def lm_full3z2_xcws(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---三全中---肖串尾数')

        # 连码---三全中----12
        for i in range(20):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            if ss == 0:
                # 生肖---尾数各随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                print('随机二个：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_full3z2_xcws_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串--肖串尾数')

        # 连码---二全中----12
        for i in range(100):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            try:
                # 生肖随机一个
                if ss == 0:
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                # # 尾数随机一个
                if ss == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    print('尾数随机一个：  ' + ' ' + str(i))
            except Exception as e:
                print(e)
                # self.base_driver.forced_wait(1)
                self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
                self.base_driver.click(self.config_dict_marksix['TIPS04'])

        print('覆盖完毕------')

    def lm_full3z2_jcp(self, row):
        # 连码
        self.base_driver.click(self.config_dict_marksix['LIANMA'])
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.click(self.config_dict_marksix['FULLIN4'])
        self.base_driver.forced_wait(1)
        # 连码---四全中---交叉碰
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')

        # self.base_driver.forced_wait(3)

        # 新增柱列
        for i in range(20):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 8))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            c0 = random.sample(range(0, 5), 4)
            a0 = random.choice(range(0, 10))

            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 5))
            # 尾选三
            if s0 == 0:
                # 尾数
                if a0 == a1 or a0 == a2 or a1 == a2:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a0)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a1)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                    self.base_driver.clicks(self.config_dict_marksix['LMJXPWS'], a2)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数')
            # 数字选4
            if s0 == 1:
                if s2 == s3 or s2 == s4 or s3 == s4:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])

                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                    if s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN3'])

                    print('数字')
            # 生肖--色波
            if s0 == 2:
                if s1 == 0:
                    # 三个生肖
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3:
                        pass
                    else:
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a0)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a1)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖--色波')
                if s1 == 2:
                    # 三个生肖
                    if a0 == a1 or a0 == a2 or a1 == a2:
                        pass
                    else:
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a0)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a1)
                        self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                        self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], a2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖--色波')

    '''
    def lm_full4_jcp_error(self, row):
        # 连码
        self.base_driver.click(self.config_dict_marksix['LIANMA'])
        self.base_driver.forced_wait(1)
        # 连码---四全中
        self.base_driver.click(self.config_dict_marksix['FULLIN4'])
        self.base_driver.forced_wait(1)
        # 连码---四全中---交叉碰
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')

        # self.base_driver.forced_wait(3)

        # 新增柱列
        for i in range(2000000000):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 8))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            c0 = random.sample(range(0, 5), 4)
            a0 = random.choice(range(0, 10))

            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 5))
            # 数字选1
            if s0 == 0:
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                print('s111111:   ' + str(s2))
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.forced_wait(3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                print('s22222:    ' + str(s2))
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

            # 数学选2
            if s0 == 1:
                if s2 == s3:
                    pass
                else:
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---四全中---数学选2：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                    if s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                    self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                    if s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                    if s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                    if s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                    if s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                    if s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)

            if s0 == 2:
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                if s3 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s3 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s3 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s3 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s3 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                if s4 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s4 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s4 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s4 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s4 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
                if s2 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s2 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s2 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s2 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s2 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
                if s3 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s3 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s3 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s3 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s3 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                self.base_driver.click(self.config_dict_marksix['LMJXPXZLN2'])
                if s4 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
                if s4 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
                if s4 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a2)
                if s4 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a3)
                if s4 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], a5)
                print('数字')


    '''

    def lm_full3z2_dt(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(100):
            s0 = random.choice(range(0, 5))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == s2 or a0 == b0 or a1 == b1 or a2 == b2 or a3 == b3 or a4 == b4:
                    pass
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)

                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

        print('覆盖完毕------')

    def lm_full3z2_dt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(30):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
            if s0 == 1:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

        print('覆盖完毕------')

    def lm_full3z2_dtsb(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖色波')

        for i in range(5):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)

                self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            else:
                pass

        print('覆盖完毕------')

    def lm_full3z2_dtsb_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖色波')
        # 任意选择一个胆
        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
            print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
        # 任选一个色波
        c0 = random.choice(range(0, 3))
        self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('连码---特串---胆拖生肖：  ' + ' ' + str(s))
        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

        print('覆盖完毕------')

    def lm_full3z2_dtsx(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖生肖')

        for i in range(20):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，一个拖
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            # 任意选择一个胆，二个拖
            if s0 == 1:
                if s1 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                else:
                    pass
            else:
                pass

        print('覆盖完毕------')

    def lm_full3z2_dtsx_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖生肖')

        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
            # 任选一个拖
            if s0 == 1:
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)

                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
            # 任选二个拖
            if s0 == 2:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                else:
                    pass

        print('覆盖完毕------')

    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    def lm_fullin2qz(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(3)
        print('进入二全中---连码---特串')

        # 连码---二全中----12
        for i in range(1000000):
            s0 = random.choice(range(0, 9))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机二个
            if s0 == 0:
                if s1 == s2:
                    pass
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机二个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], '1')
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], '1')
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], '1')
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], '1')
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], '1')

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))
            # 随机三个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机三个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 7:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 8:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

        print('覆盖完毕------')

    def lm_fullin2qz_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串')

        for i in range(100):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
        print('覆盖完毕------')

    def lm_fullin2qz_zfh(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---正/副号')

        for i in range(1000000):
            s0 = random.choice(range(0, 9))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机二个
            if s0 == 0:
                if s1 == s2:
                    pass
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机二个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], '1')
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], '1')
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], '1')
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], '1')
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], '1')

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))
            # 随机三个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机三个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 7:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 8:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

    def lm_fullin2qz_zfh_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---正/副号')

        for i in range(100):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
        print('覆盖完毕------')

    def lm_fullin2qz_xcws(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---肖串尾数')

        # 连码---二全中----12
        for i in range(10):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            if ss == 0:
                # 生肖---尾数各随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                print('随机二个：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_fullin2qz_xcws_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串--肖串尾数')

        # 连码---二全中----12
        for i in range(10000):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            try:
                # 生肖随机一个
                if ss == 0:
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                    # self.base_driver.forced_wait(3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                # # 尾数随机一个
                if ss == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    print('尾数随机一个：  ' + ' ' + str(i))
            except Exception as e:
                print(e)
                # self.base_driver.forced_wait(1)
                self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
                self.base_driver.click(self.config_dict_marksix['TIPS04'])

        print('覆盖完毕------')

        # def lm_fullinntc_jcp(self, row):
        #     # 连码
        #     self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        #     self.base_driver.forced_wait(1)
        #     # 连码---特串---交叉碰
        #     self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        #     self.base_driver.forced_wait(1)
        #
        #     self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        #     self.base_driver.forced_wait(1)
        #     print('进入连码---特串---交叉碰')
        #
        #     # self.base_driver.forced_wait(3)
        #
        #     # 新增柱列
        #     for i in range(1000000000):
        #         s0 = random.choice(range(0, 6))
        #         s1 = random.choice(range(0, 5))
        #         s2 = random.choice(range(0, 2))
        #
        #
        #         # a0 = random.choice(range(0, 50))
        #         # a1 = random.choice(range(0, 50))
        #         # a2 = random.choice(range(0, 50))
        #         # a3 = random.choice(range(0, 50))
        #         a0 = random.choice(range(0, 10))
        #         a1 = random.choice(range(0, 10))
        #         a2 = random.choice(range(0, 10))
        #         a3 = random.choice(range(0, 10))
        #         a4 = random.choice(range(0, 10))
        #
        #         b0 = random.choice(range(0, 9))
        #         b1 = random.choice(range(0, 9))
        #
        #         c0 = random.choice(range(0, 5))
        #         # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #         if s0 == 0:
        #             # 每一柱列选择一个号码
        #             if s1 == s2:
        #                 pass
        #                 # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #                 # # 尾巴1---尾0 任意两个
        #                 # if s1 == 0:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a1)
        #                 # if s1 == 1:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
        #                 # if s1 == 2:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a1)
        #                 # if s1 == 3:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a1)
        #                 # if s1 == 4:
        #                 #     if b0 == b1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b1)
        #                 # self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        #             else:
        #                 self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #
        #                 #self.base_driver.forced_wait(1)
        #                 #
        #                 # if s1 == 0:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], '1')
        #                 # if s1 == 1:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], '1')
        #                 # if s1 == 2:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], '1')
        #                 # if s1 == 3:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], '1')
        #                 if s1 == 4:
        #                     print(b0)
        #                     # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #                     #self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b0)
        #                     self.base_driver.click(self.config_dict_marksix['aaaaa'])
        #                # self.base_driver.forced_wait(1)
        #                 self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
        #             #     #self.base_driver.forced_wait(1)
        #             #
        #                 if s2 == 0:
        #                     #self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], '1')
        #                     self.base_driver.click(self.config_dict_marksix['sssss'])
        #             #     if s2 == 1:
        #             #         self.base_driver.clicks(self.config_dict_marksix['LMJXPSX2'], '1')
        #             #     #self.base_driver.forced_wait(1)
        #             #    # # self.base_driver.forced_wait(0.5)
        #             self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        #             #self.base_driver.forced_wait(1)
        #                #  print('==========================')
        #             # except Exception as e:
        #             #     print(e)
        #             #     print('下注异常')
        #             #     print('异常的数组是:' + ' ' + str(a0) + ' ' + str(a1))
        #             #     self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
        #             #     self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #             #     self.base_driver.forced_wait(3)
        #             #     pass

    def lm_fullin2qz_dt(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(10):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
            if s0 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
            if s0 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
            if s0 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
            if s0 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)

            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

        print('覆盖完毕------')

    def lm_fullin2qz_dt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(10):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
            if s0 == 1:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

        print('覆盖完毕------')

    def lm_fullin2qz_dtsb(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖色波')

        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)

                self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            else:
                pass

        print('覆盖完毕------')

    def lm_fullin2qz_dtsb_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖色波')
        # 任意选择一个胆
        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
            print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
        # 任选一个色波
        c0 = random.choice(range(0, 3))
        self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('连码---特串---胆拖生肖：  ' + ' ' + str(s))
        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

        print('覆盖完毕------')

    def lm_fullin2qz_dtsx(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖生肖')

        for i in range(20):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，一个拖
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            # 任意选择一个胆，二个拖
            if s0 == 1:
                if s1 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                else:
                    pass
            else:
                pass

        print('覆盖完毕------')

    def lm_fullin2qz_dtsx_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '2')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '6')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖生肖')

        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
            # 任选一个拖
            if s0 == 1:
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)

                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
            # 任选二个拖
            if s0 == 2:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                else:
                    pass

        print('覆盖完毕------')

    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    def lm_fullin2zt(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(3)
        print('进入二全中---连码---特串')

        # 连码---二全中----12
        for i in range(1000000):
            s0 = random.choice(range(0, 9))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机二个
            if s0 == 0:
                if s1 == s2:
                    pass
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机二个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], '1')
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], '1')
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], '1')
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], '1')
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], '1')

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))
            # 随机三个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机三个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 7:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 8:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

        print('覆盖完毕------')

    def lm_fullin2zt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串')

        for i in range(100):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
        print('覆盖完毕------')

    def lm_fullin2zt_zfh(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---正/副号')

        for i in range(1000000):
            s0 = random.choice(range(0, 9))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机二个
            if s0 == 0:
                if s1 == s2:
                    pass
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机二个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], '1')
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], '1')
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], '1')
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], '1')
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], '1')

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))
            # 随机三个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机三个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 7:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 8:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

    def lm_fullin2zt_zfh_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---二中特---正/副号')

        for i in range(100):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
        print('覆盖完毕------')

    def lm_fullin2zt_sxdp(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---生肖对碰')

        # 连码---二全中----12
        for i in range(20):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            # 生肖左右随机一个
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a1)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('生肖左右随机一个-9：  ' + ' ' + str(i))
            # 生肖左随机两个
            if s0 == 1:
                if a0 == a1:
                    pass
                else:
                    print(a0)
                    print(a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('生肖左随机两个：  ' + ' ' + str(i))
            # 生肖后随机两个
            if s0 == 2:
                if a0 == a1:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('生肖后随机两个：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_fullin2zt_sxdp_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---尾数对碰')

        # 连码---特串---尾数对碰
        for i in range(100):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            # 生肖左随机一个
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('生肖左随机一个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
            # 生肖右随机一个
            if s0 == 1:
                self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('生肖右随机一个：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a0)

        print('覆盖完毕------')

    def lm_fullin2zt_wsdp(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---尾数对碰')

        # 连码---二全中----12
        for i in range(20):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 5))
            a1 = random.choice(range(0, 5))
            # 尾数各随机一个
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a1)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('尾数每边1个5-9：  ' + ' ' + str(i))
            # 生肖两个
            if s0 == 1:
                if a0 == a1:
                    pass
                else:
                    print(a0)
                    print(a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数两个5-9：  ' + ' ' + str(i))
            # 尾数两个
            if s0 == 2:
                if a0 == a1:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数两个5-9：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_fullin2zt_wsdp_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---尾数对碰')

        # 连码---特串---尾数对碰
        for i in range(100):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 5))
            a1 = random.choice(range(0, 5))
            # 尾数各随机一个
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('尾数每边1个5-9：  ' + ' ' + str(i))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
            # 生肖两个
            if s0 == 1:
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('尾数每边1个5-9：  ' + ' ' + str(i))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_marksix['LMDPN1'], a0)

        print('覆盖完毕------')

    def lm_fullin2zt_xcws(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---肖串尾数')

        # 连码---二全中----12
        for i in range(10):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            if ss == 0:
                # 生肖---尾数各随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                print('随机二个：  ' + ' ' + str(i))

        print('覆盖完毕------')

    def lm_fullin2zt_xcws_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串--肖串尾数')

        # 连码---二全中----12
        for i in range(10000):
            ss = random.choice(range(0, 2))
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 6))
            a1 = random.choice(range(0, 6))
            a2 = random.choice(range(0, 5))
            a3 = random.choice(range(0, 5))
            try:
                # 生肖随机一个
                if ss == 0:
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                    # self.base_driver.forced_wait(3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                # # 尾数随机一个
                if ss == 1:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    print('尾数随机一个：  ' + ' ' + str(i))
            except Exception as e:
                print(e)
                # self.base_driver.forced_wait(1)
                self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
                self.base_driver.click(self.config_dict_marksix['TIPS04'])

        print('覆盖完毕------')

        # def lm_fullinntc_jcp(self, row):
        #     # 连码
        #     self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        #     self.base_driver.forced_wait(1)
        #     # 连码---特串---交叉碰
        #     self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        #     self.base_driver.forced_wait(1)
        #
        #     self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        #     self.base_driver.forced_wait(1)
        #     print('进入连码---特串---交叉碰')
        #
        #     # self.base_driver.forced_wait(3)
        #
        #     # 新增柱列
        #     for i in range(1000000000):
        #         s0 = random.choice(range(0, 6))
        #         s1 = random.choice(range(0, 5))
        #         s2 = random.choice(range(0, 2))
        #
        #
        #         # a0 = random.choice(range(0, 50))
        #         # a1 = random.choice(range(0, 50))
        #         # a2 = random.choice(range(0, 50))
        #         # a3 = random.choice(range(0, 50))
        #         a0 = random.choice(range(0, 10))
        #         a1 = random.choice(range(0, 10))
        #         a2 = random.choice(range(0, 10))
        #         a3 = random.choice(range(0, 10))
        #         a4 = random.choice(range(0, 10))
        #
        #         b0 = random.choice(range(0, 9))
        #         b1 = random.choice(range(0, 9))
        #
        #         c0 = random.choice(range(0, 5))
        #         # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #         if s0 == 0:
        #             # 每一柱列选择一个号码
        #             if s1 == s2:
        #                 pass
        #                 # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #                 # # 尾巴1---尾0 任意两个
        #                 # if s1 == 0:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a1)
        #                 # if s1 == 1:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
        #                 # if s1 == 2:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a1)
        #                 # if s1 == 3:
        #                 #     if a0 == a1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a1)
        #                 # if s1 == 4:
        #                 #     if b0 == b1:
        #                 #         pass
        #                 #     else:
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b0)
        #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b1)
        #                 # self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        #             else:
        #                 self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #
        #                 #self.base_driver.forced_wait(1)
        #                 #
        #                 # if s1 == 0:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], '1')
        #                 # if s1 == 1:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], '1')
        #                 # if s1 == 2:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], '1')
        #                 # if s1 == 3:
        #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], '1')
        #                 if s1 == 4:
        #                     print(b0)
        #                     # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #                     #self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b0)
        #                     self.base_driver.click(self.config_dict_marksix['aaaaa'])
        #                # self.base_driver.forced_wait(1)
        #                 self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
        #             #     #self.base_driver.forced_wait(1)
        #             #
        #                 if s2 == 0:
        #                     #self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], '1')
        #                     self.base_driver.click(self.config_dict_marksix['sssss'])
        #             #     if s2 == 1:
        #             #         self.base_driver.clicks(self.config_dict_marksix['LMJXPSX2'], '1')
        #             #     #self.base_driver.forced_wait(1)
        #             #    # # self.base_driver.forced_wait(0.5)
        #             self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        #             #self.base_driver.forced_wait(1)
        #                #  print('==========================')
        #             # except Exception as e:
        #             #     print(e)
        #             #     print('下注异常')
        #             #     print('异常的数组是:' + ' ' + str(a0) + ' ' + str(a1))
        #             #     self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
        #             #     self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
        #             #     self.base_driver.forced_wait(3)
        #             #     pass

    def lm_fullin2zt_dt(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(10):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
            if s0 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
            if s0 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
            if s0 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
            if s0 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)

            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

        print('覆盖完毕------')

    def lm_fullin2zt_dt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(10):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
            if s0 == 1:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

        print('覆盖完毕------')

    def lm_fullin2zt_dtsb(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '7')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖色波')

        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)

                self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            else:
                pass

        print('覆盖完毕------')

    def lm_fullin2zt_dtsb_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '7')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖色波')
        # 任意选择一个胆
        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
            print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
        # 任选一个色波
        c0 = random.choice(range(0, 3))
        self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('连码---特串---胆拖生肖：  ' + ' ' + str(s))
        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])

        print('覆盖完毕------')

    def lm_fullin2zt_dtsx(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '8')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖生肖')

        for i in range(20):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，一个拖
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            # 任意选择一个胆，二个拖
            if s0 == 1:
                if s1 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                else:
                    pass
            else:
                pass

        print('覆盖完毕------')

    def lm_fullin2zt_dtsx_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '3')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '8')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖生肖')

        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
            # 任选一个拖
            if s0 == 1:
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)

                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
            # 任选二个拖
            if s0 == 2:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                else:
                    pass

        print('覆盖完毕------')

    # -------------------------------------------------------------
    # -------------------------------------------------------------
    # -------------------------------------------------------------
    def lm_fullinntc(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(3)
        print('进入二全中---连码---特串')

        # 连码---二全中----12
        for i in range(1000000):
            s0 = random.choice(range(0, 9))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机二个
            if s0 == 0:
                if s1 == s2:
                    pass
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机二个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], '1')
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], '1')
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], '1')
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], '1')
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], '1')

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))
            # 随机三个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机三个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 7:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 8:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

        print('覆盖完毕------')

    def lm_fullinntc_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串')

        for i in range(100):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
        print('覆盖完毕------')

    def lm_fullinntc_zfh(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---正/副号
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---正/副号')

        for i in range(1000000):
            s0 = random.choice(range(0, 9))

            s1 = random.choice(range(0, 5))
            s2 = random.choice(range(0, 5))
            s3 = random.choice(range(0, 5))
            s4 = random.choice(range(0, 5))
            s5 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 10))
            a5 = random.choice(range(0, 10))
            a6 = random.choice(range(0, 10))
            a7 = random.choice(range(0, 10))
            a8 = random.choice(range(0, 10))
            a9 = random.choice(range(0, 10))

            b0 = random.choice(range(0, 9))
            b1 = random.choice(range(0, 9))
            b2 = random.choice(range(0, 9))
            b3 = random.choice(range(0, 9))
            b4 = random.choice(range(0, 9))
            b5 = random.choice(range(0, 9))
            b6 = random.choice(range(0, 9))
            b7 = random.choice(range(0, 9))
            b8 = random.choice(range(0, 9))
            b9 = random.choice(range(0, 9))
            # 随机二个
            if s0 == 0:
                if s1 == s2:
                    pass
                    if a0 == a1 or b0 == b1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机二个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], '1')
                    if s1 == 1 or s2 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], '1')
                    if s1 == 2 or s2 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], '1')
                    if s1 == 3 or s2 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], '1')
                    if s1 == 4 or s2 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], '1')

                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))
            # 随机三个
            if s0 == 1:
                if s1 == s2 or s1 == s3 or s2 == s3:
                    pass
                    if a0 == a1 or a0 == a2 or a1 == a2 or b0 == b1 or b0 == b2 or b1 == b2:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机三个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机三个：  ' + ' ' + str(i))
            # 随机四个
            if s0 == 2:
                if s1 == s2 or s1 == s3 or s1 == s4 or s2 == s3 or s2 == s4 or s3 == s4:
                    if a0 == a1 or a0 == a2 or a0 == a3 or a1 == a2 or a1 == a3 or a2 == a3 or b0 == b1 or b0 == b2 \
                            or b0 == b3 or b1 == b2 or b1 == b3 or b2 == b3:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机四个：  ' + ' ' + str(i))
                else:
                    if s1 == 0 or s2 == 0 or s3 == 0 or s4 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    if s1 == 1 or s2 == 1 or s3 == 1 or s4 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    if s1 == 2 or s2 == 2 or s3 == 2 or s4 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    if s1 == 3 or s2 == 3 or s3 == 3 or s4 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    if s1 == 4 or s2 == 4 or s3 == 4 or s4 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机四个：  ' + ' ' + str(i))
            # 随机五个
            if s0 == 3:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a1 == a2 or a1 == a3 or a1 == a4 or a2 == a3 \
                        or a2 == a4 or a3 == a4 or b0 == b1 or b0 == b2 or b0 == b3 or b0 == b4 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b2 == b3 or b2 == b4 or b3 == b4:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机五个：  ' + ' ' + str(i))
            # 随机六个
            if s0 == 4:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机六个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机六个：  ' + ' ' + str(i))
            # 随机七个
            if s0 == 5:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a1 == a2 or a1 == a3 \
                        or a1 == a4 or a1 == a5 or a1 == a6 or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 \
                        or a3 == a4 or a3 == a5 or a3 == a6 or a4 == a5 or a4 == a6 or a5 == a6 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b1 == b2 or b1 == b3 \
                        or b1 == b4 or b1 == b5 or b1 == b6 or b2 == b3 or b2 == b4 or b2 == b5 or b2 == b6 \
                        or b3 == b4 or b3 == b5 or b3 == b6 or b4 == b5 or b4 == b6 or b5 == b6:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机七个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机七个：  ' + ' ' + str(i))
            # 随机八个
            if s0 == 6:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a1 == a2 \
                        or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a2 == a3 or a2 == a4 \
                        or a2 == a5 or a2 == a6 or a2 == a7 or a3 == a4 or a3 == a5 or a3 == a6 or a3 == a7 \
                        or a4 == a5 or a4 == a6 or a4 == a7 or a5 == a6 or a5 == a7 or a6 == a7 or b0 == b1 \
                        or b0 == b2 or b0 == b3 or b0 == b4 or b0 == b5 or b0 == b6 or b0 == b7 or b1 == b2 \
                        or b1 == b3 or b1 == b4 or b1 == b5 or b1 == b6 or b1 == b7 or b2 == b3 or b2 == b4 \
                        or b2 == b5 or b2 == b6 or b2 == b7 or b3 == b4 or b3 == b5 or b3 == b6 or b3 == b7 \
                        or b4 == b5 or b4 == b6 or b4 == b7 or b5 == b6 or b5 == b7 or b6 == b7:
                    if a0 == b0 or a1 == b0 or a2 == b0 or a3 == b0 or a4 == b0 or a5 == b0 or a6 == b0:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机八个：  ' + ' ' + str(i))
                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b7)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机八个：  ' + ' ' + str(i))
            # 随机九个
            if s0 == 7:
                if a0 == a1 or a0 == a2 or a0 == a3 or a0 == a4 or a0 == a5 or a0 == a6 or a0 == a7 or a0 == a8 \
                        or a1 == a2 or a1 == a3 or a1 == a4 or a1 == a5 or a1 == a6 or a1 == a7 or a1 == a8 \
                        or a2 == a3 or a2 == a4 or a2 == a5 or a2 == a6 or a2 == a7 or a2 == a8 or a3 == a4 \
                        or a3 == a5 or a3 == a6 or a3 == a7 or a3 == a8 or a4 == a5 or a4 == a6 or a4 == a7 \
                        or a4 == a8 or a5 == a6 or a5 == a7 or a5 == a8 or a6 == a7 or a6 == a8 or a7 == a8:
                    pass
                    if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('随机九个：  ' + ' ' + str(i))

                else:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a8)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a8)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a8)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a2)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a3)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a5)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a8)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机九个：  ' + ' ' + str(i))
            # 随机十个
            if s0 == 8:
                if a0 == a1 or a2 == a3 or a4 == a5 or a6 == a7 or b0 == b1:
                    if s1 == 0:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], j)
                    if s1 == 1:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], j)
                    if s1 == 2:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], j)
                    if s1 == 3:
                        for j in range(10):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], j)
                    if s1 == 4:
                        for j in range(9):
                            self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], j)
                        self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN01_10'], a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a2)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN11_20'], a3)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN21_30'], a5)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a6)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN31_40'], a7)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b0)
                    self.base_driver.clicks(self.config_dict_marksix['LMZFN41_49'], b1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('随机十个：  ' + ' ' + str(i))
            else:
                pass

    def lm_fullinntc_zfh_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '1')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---正/副号')

        for i in range(100):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['FULLIN4N41_49'], a4)
        print('覆盖完毕------')

    def lm_fullinntc_sxdp(self, row):
            # 连码
            self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
            self.base_driver.forced_wait(1)
            # 连码---特串
            self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
            self.base_driver.forced_wait(1)

            self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
            self.base_driver.forced_wait(1)
            print('进入二全中---连码---特串---生肖对碰')

            # 连码---二全中----12
            for i in range(20):
                s0 = random.choice(range(0, 3))
                s1 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                # 生肖左右随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('生肖左右随机一个-9：  ' + ' ' + str(i))
                # 生肖左随机两个
                if s0 == 1:
                    if a0 == a1:
                        pass
                    else:
                        print(a0)
                        print(a1)
                        self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖左随机两个：  ' + ' ' + str(i))
                # 生肖后随机两个
                if s0 == 2:
                    if a0 == a1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a0)
                        self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('生肖后随机两个：  ' + ' ' + str(i))

            print('覆盖完毕------')

    def lm_fullinntc_sxdp_error(self, row):
            # 连码
            self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
            self.base_driver.forced_wait(1)
            # 连码---特串
            self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
            self.base_driver.forced_wait(1)

            self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '2')
            self.base_driver.forced_wait(1)
            print('进入连码---特串---尾数对碰')

            # 连码---特串---尾数对碰
            for i in range(100):
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                # 生肖左随机一个
                if s0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('生肖左随机一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN0'], a0)
                # 生肖右随机一个
                if s0 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('生肖右随机一个：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['LMSXDPN1'], a0)

            print('覆盖完毕------')

    def lm_fullinntc_wsdp(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---尾数对碰')

        # 连码---二全中----12
        for i in range(20):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 5))
            a1 = random.choice(range(0, 5))
            # 尾数各随机一个
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a1)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                print('尾数每边1个5-9：  ' + ' ' + str(i))
            # 生肖两个
            if s0 == 1:
                if a0 == a1:
                    pass
                else:
                    print(a0)
                    print(a1)
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数两个5-9：  ' + ' ' + str(i))
            # 尾数两个
            if s0 == 2:
                if a0 == a1:
                    pass
                else:
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a0)
                    self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('尾数两个5-9：  ' + ' ' + str(i))

        print('覆盖完毕------')
        
    def lm_fullinntc_wsdp_error(self, row):
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '3')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---尾数对碰')

        # 连码---特串---尾数对碰
        for i in range(100):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 2))
            a0 = random.choice(range(0, 5))
            a1 = random.choice(range(0, 5))
            # 尾数各随机一个
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('尾数每边1个5-9：  ' + ' ' + str(i))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN0'], a0)
            # 生肖两个
            if s0 == 1:
                self.base_driver.clicks(self.config_dict_marksix['LMWSDPN1'], a0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('尾数每边1个5-9：  ' + ' ' + str(i))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                self.base_driver.clicks(self.config_dict_marksix['LMDPN1'], a0)

        print('覆盖完毕------')

    def lm_fullinntc_xcws(self, row):
            # 连码
            self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
            self.base_driver.forced_wait(1)
            # 连码---特串
            self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
            self.base_driver.forced_wait(1)

            self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
            self.base_driver.forced_wait(1)
            print('进入二全中---连码---特串---肖串尾数')

            # 连码---二全中----12
            for i in range(10):
                ss = random.choice(range(0, 2))
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                if ss == 0:
                    # 生肖---尾数各随机一个
                    if s0 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                    if s0 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                    print('随机二个：  ' + ' ' + str(i))



            print('覆盖完毕------')

    def lm_fullinntc_xcws_error(self, row):
            # 连码
            self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
            self.base_driver.forced_wait(1)
            # 连码---特串
            self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
            self.base_driver.forced_wait(1)

            self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '4')
            self.base_driver.forced_wait(1)
            print('进入二全中---连码---特串--肖串尾数')

            # 连码---二全中----12
            for i in range(10000):
                ss = random.choice(range(0, 2))
                s0 = random.choice(range(0, 2))
                s1 = random.choice(range(0, 2))
                a0 = random.choice(range(0, 6))
                a1 = random.choice(range(0, 6))
                a2 = random.choice(range(0, 5))
                a3 = random.choice(range(0, 5))
                try:
                    # 生肖随机一个
                    if ss == 0:
                        if s0 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMXCN0'], a0)
                        if s0 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMXCN1'], a1)
                        # self.base_driver.forced_wait(3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    # # 尾数随机一个
                    if ss == 1:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['LMXCWS0'], a2)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['LMXCWS1'], a3)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        print('尾数随机一个：  ' + ' ' + str(i))
                except Exception as e:
                    print(e)
                    # self.base_driver.forced_wait(1)
                    self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
                    self.base_driver.click(self.config_dict_marksix['TIPS04'])

            print('覆盖完毕------')


    # def lm_fullinntc_jcp(self, row):
    #     # 连码
    #     self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
    #     self.base_driver.forced_wait(1)
    #     # 连码---特串---交叉碰
    #     self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
    #     self.base_driver.forced_wait(1)
    #
    #     self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
    #     self.base_driver.forced_wait(1)
    #     print('进入连码---特串---交叉碰')
    #
    #     # self.base_driver.forced_wait(3)
    #
    #     # 新增柱列
    #     for i in range(1000000000):
    #         s0 = random.choice(range(0, 6))
    #         s1 = random.choice(range(0, 5))
    #         s2 = random.choice(range(0, 2))
    #
    #
    #         # a0 = random.choice(range(0, 50))
    #         # a1 = random.choice(range(0, 50))
    #         # a2 = random.choice(range(0, 50))
    #         # a3 = random.choice(range(0, 50))
    #         a0 = random.choice(range(0, 10))
    #         a1 = random.choice(range(0, 10))
    #         a2 = random.choice(range(0, 10))
    #         a3 = random.choice(range(0, 10))
    #         a4 = random.choice(range(0, 10))
    #
    #         b0 = random.choice(range(0, 9))
    #         b1 = random.choice(range(0, 9))
    #
    #         c0 = random.choice(range(0, 5))
    #         # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
    #         if s0 == 0:
    #             # 每一柱列选择一个号码
    #             if s1 == s2:
    #                 pass
    #                 # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
    #                 # # 尾巴1---尾0 任意两个
    #                 # if s1 == 0:
    #                 #     if a0 == a1:
    #                 #         pass
    #                 #     else:
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a0)
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], a1)
    #                 # if s1 == 1:
    #                 #     if a0 == a1:
    #                 #         pass
    #                 #     else:
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a0)
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], a1)
    #                 # if s1 == 2:
    #                 #     if a0 == a1:
    #                 #         pass
    #                 #     else:
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a0)
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], a1)
    #                 # if s1 == 3:
    #                 #     if a0 == a1:
    #                 #         pass
    #                 #     else:
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a0)
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], a1)
    #                 # if s1 == 4:
    #                 #     if b0 == b1:
    #                 #         pass
    #                 #     else:
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b0)
    #                 #         self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b1)
    #                 # self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
    #             else:
    #                 self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
    #
    #                 #self.base_driver.forced_wait(1)
    #                 #
    #                 # if s1 == 0:
    #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP01_10'], '1')
    #                 # if s1 == 1:
    #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP11_20'], '1')
    #                 # if s1 == 2:
    #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP21_30'], '1')
    #                 # if s1 == 3:
    #                 #     self.base_driver.clicks(self.config_dict_marksix['LMJXP31_40'], '1')
    #                 if s1 == 4:
    #                     print(b0)
    #                     # self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
    #                     #self.base_driver.clicks(self.config_dict_marksix['LMJXP41_49'], b0)
    #                     self.base_driver.click(self.config_dict_marksix['aaaaa'])
    #                # self.base_driver.forced_wait(1)
    #                 self.base_driver.click(self.config_dict_marksix['LMJXPXZLN1'])
    #             #     #self.base_driver.forced_wait(1)
    #             #
    #                 if s2 == 0:
    #                     #self.base_driver.clicks(self.config_dict_marksix['LMJXPSX1'], '1')
    #                     self.base_driver.click(self.config_dict_marksix['sssss'])
    #             #     if s2 == 1:
    #             #         self.base_driver.clicks(self.config_dict_marksix['LMJXPSX2'], '1')
    #             #     #self.base_driver.forced_wait(1)
    #             #    # # self.base_driver.forced_wait(0.5)
    #             self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
    #             #self.base_driver.forced_wait(1)
    #                #  print('==========================')
    #             # except Exception as e:
    #             #     print(e)
    #             #     print('下注异常')
    #             #     print('异常的数组是:' + ' ' + str(a0) + ' ' + str(a1))
    #             #     self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
    #             #     self.base_driver.click(self.config_dict_marksix['LMJXPXZLN0'])
    #             #     self.base_driver.forced_wait(3)
    #             #     pass

    def lm_fullinntc_dt(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(10):
            s0 = random.choice(range(0, 5))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
            if s0 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
            if s0 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
            if s0 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
            if s0 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)

            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

        print('覆盖完毕------')

    def lm_fullinntc_dt_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '5')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖')

        for i in range(10):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            b0 = random.choice(range(0, 10))
            b1 = random.choice(range(0, 10))
            b2 = random.choice(range(0, 10))
            b3 = random.choice(range(0, 10))
            b4 = random.choice(range(0, 9))
            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOD41_49'], a4)
            if s0 == 1:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT01_10'], b0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT11_20'], b1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT21_30'], b2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT31_40'], b3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DANTUOT41_49'], b4)

        print('覆盖完毕------')

    def lm_fullinntc_dtsb(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '7')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖色波')

        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，色波
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)

                self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            else:
                pass


        print('覆盖完毕------')

    def lm_fullinntc_dtsb_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖色波
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)

        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '7')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖色波')
        # 任意选择一个胆
        for i in range(10):
            s0 = random.choice(range(0, 1))
            s1 = random.choice(range(0, 5))

            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 2))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
            self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
            print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
            self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            if s1 == 0:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO01_10'], a0)
            if s1 == 1:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO11_20'], a1)
            if s1 == 2:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO21_30'], a2)
            if s1 == 3:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO31_40'], a3)
            if s1 == 4:
                self.base_driver.clicks(self.config_dict_marksix['DTSEBO41_49'], a4)
        # 任选一个色波
        c0 = random.choice(range(0, 3))
        self.base_driver.clicks(self.config_dict_marksix['DTSEBO'], c0)
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
        print('连码---特串---胆拖生肖：  ' + ' ' + str(s))
        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
            
            

        print('覆盖完毕------')

    def lm_fullinntc_dtsx(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)
        
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '8')
        self.base_driver.forced_wait(1)
        print('进入二全中---连码---特串---胆拖生肖')

        for i in range(20):
            s0 = random.choice(range(0, 2))
            s1 = random.choice(range(0, 5))
            
            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆，一个拖
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
            # 任意选择一个胆，二个拖
            if s0 == 1:
                if s1 == 0:
                    if s1 == 0:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                    if s1 == 1:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                    if s1 == 2:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                    if s1 == 3:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                    if s1 == 4:
                        self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])

                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        if s1 == 0:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                        if s1 == 1:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                        if s1 == 2:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                        if s1 == 3:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                        if s1 == 4:
                            self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i))
                else:
                    pass
            else:
                pass


                
        print('覆盖完毕------')
        
    def lm_fullinntc_dtsx_error(self, row):
        # 连码
        # 连码
        self.base_driver.clicks_by_text(self.config_dict_marksix['MENU'], '连码')
        self.base_driver.forced_wait(1)
        # 连码---特串---胆拖生肖
        self.base_driver.clicks(self.config_dict_marksix['FULLINN'], '4')
        self.base_driver.forced_wait(1)
        
        self.base_driver.clicks(self.config_dict_marksix['ZHENGFUN'], '8')
        self.base_driver.forced_wait(1)
        print('进入连码---特串---胆拖生肖')

        for i in range(100):
            s0 = random.choice(range(0, 3))
            s1 = random.choice(range(0, 5))
            
            b0 = random.choice(range(0, 3))
            b1 = random.choice(range(0, 2))
            c0 = random.choice(range(0, 6))
            c1 = random.choice(range(0, 6))

            a0 = random.choice(range(0, 10))
            a1 = random.choice(range(0, 10))
            a2 = random.choice(range(0, 10))
            a3 = random.choice(range(0, 10))
            a4 = random.choice(range(0, 9))

            # 任意选择一个胆
            if s0 == 0:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
                self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX01_10'], a0)
                if s1 == 1:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX11_20'], a1)
                if s1 == 2:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX21_30'], a2)
                if s1 == 3:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX31_40'], a3)
                if s1 == 4:
                    self.base_driver.clicks(self.config_dict_marksix['DTSX41_49'], a4)
            # 任选一个拖
            if s0 == 1:
                if b0 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('合肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)

                else:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
            # 任选二个拖
            if s0 == 2:
                if s1 == 0:
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                    self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                    s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                    print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                    self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                    self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                if s1 == 1:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS0'], c1)
                if s1 == 2:
                    if c0 == c1:
                        pass
                    else:
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
                        s = self.base_driver.get_text(self.config_dict_marksix['TIPS'])
                        print('连码---特串---胆拖生肖：  ' + ' ' + str(i) + ' ' + str(s))
                        self.base_driver.click(self.config_dict_marksix['TIPSBUTTON'])
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c0)
                        self.base_driver.clicks(self.config_dict_marksix['DTSXS1'], c1)
                else:
                    pass




                    
                
                
        print('覆盖完毕------')

    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------

    def addnote_button(self):
        # 点击添加注单按钮
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        print('点击添加注单按钮')
        self.base_driver.forced_wait(3)

    def radoms(self, row):

        # 随机5注
        self.base_driver.click(self.config_dict_marksix['RANDOM5'])
        self.base_driver.forced_wait(3)
        # 随机1注2元
        self.base_driver.click(self.config_dict_marksix['RANDOM1'])
        # 随机一注2角
        self.base_driver.click(self.config_dict_marksix['JIAO'])
        self.base_driver.click(self.config_dict_marksix['RANDOM1'])
        # 随机一注2分
        self.base_driver.click(self.config_dict_marksix['FEN'])
        self.base_driver.click(self.config_dict_marksix['RANDOM1'])
        # 随机20
        # self.base_driver.clear(self.config_dict_marksix['XIUGAI'])
        #
        # self.base_driver.forced_wait(20)
        self.base_driver.type(self.config_dict_marksix['XIUGAI'], row['xiugai'])
        self.base_driver.click(self.config_dict_marksix['RANDOM1'])
        print('随机')

        # 全部删除':
        # self.base_driver.click(self.config_dict_marksix['ALLDELETE'])
        self.base_driver.forced_wait(1)
        print('随机5注')

    def surebet(self):
        # 确认投注按钮
        surebet = self.base_driver.click(self.config_dict_marksix['SUREBET'])
        print('点击确认投注')
        self.base_driver.forced_wait(5)
        self.base_driver.refresh()
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

    def get_tips0000(self):

        # 合肖---鼠牛虎兔龙蛇马羊猴鸡11
        self.base_driver.click(self.config_dict_marksix['SHU'])
        self.base_driver.click(self.config_dict_marksix['NIU'])
        self.base_driver.click(self.config_dict_marksix['HU'])
        self.base_driver.click(self.config_dict_marksix['TUZI'])
        self.base_driver.click(self.config_dict_marksix['LONG'])
        self.base_driver.click(self.config_dict_marksix['SHE'])
        self.base_driver.click(self.config_dict_marksix['MA'])
        self.base_driver.click(self.config_dict_marksix['YANG'])
        self.base_driver.click(self.config_dict_marksix['HOU'])
        self.base_driver.click(self.config_dict_marksix['JI'])
        self.base_driver.click(self.config_dict_marksix['GOU'])
        self.base_driver.click(self.config_dict_marksix['ADDNOTE'])
        self.base_driver.forced_wait(0.5)
