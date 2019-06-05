import time

from alltest.home.test_home_login import HomeLoginTest
from common.box import TestSuite, CsvHelper, TestRunner
from alltest.home.test_home_register import HomeRegisterTest
from marksix.test_choice115_mm import Choice115MnTest
from marksix.test_fast3_mm import Fast3MmTest
from marksix.test_lowfrequency_speed3d import Speed3DTest
from marksix.test_marksix import MarkSixTest
from marksix.test_pcdd_lucky28 import PcddLucky28Test
from marksix.test_pk10_mm import PK10MmTest
from marksix.test_time_mm import TimeMmTest


class Runner(object):
    def run_test(self):

        """
        运行测试
        :return:
        """

        '''
        
        方法1（自动搜索指定路径下的指定文件中的测试用例执行）
        
        # 测试存放文件夹位置
        cases_path = 'src\\testcase_runner\\case'
        
        test_suite = unittest.TestSuite()

        # 自动搜索目录下所有测试用例文件并添加到test_suite中
        discover = unittest.defaultTestLoader.discover(start_dir=cases_path, pattern='login_*.py', top_level_dir=None)
        for dir in discover:
            for suite in dir:
                test_suite.addTests(suite)
                
        '''

        '''
        方法2：单个指定添加
        '''
        # 实例化测试套件,用来装用例
        suite = TestSuite()
        # 读取要运行的用例所在的类和方法名称等，获取出来的形式是列表，列表里面有多个字典。如：
        # [{'a':'1','b':'2'},{'c':'3','d':'4'},{'e':'5','f':'6'}]
        csv_data = CsvHelper().read_data_as_dict("csv/TestAll.csv")
        # 获取一个本地时间，格式是年月日，时分秒

        test_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        # 创建一个新的日志文件
        logger_file = "/fusion/report_loggers/fusion_automate_log_%s.log" % test_time

        for row in csv_data:
            # row其实就是每一个字典
            test_class = row["class"]
            test_method = row["test"]
            # 从csv读取过来的数据都是字符串形式
            test_count = int(row["count"])

            for i in range(test_count):
                pass
                # 增加测试用例，这里要增加
                # 注册register用例
                # if test_class == "HomeRegisterTest":
                #     suite.add_test(HomeRegisterTest(test_method, logger_file))
                #
                # if test_class == "HomeLoginTest":
                #     suite.add_test(HomeLoginTest(test_method, logger_file))

                # Fusion Test测试用例
                # # 分分11选5
                # if test_class == "Choice115MnTest":
                #     suite.add_test(Choice115MnTest(test_method, logger_file))
                # # 分分六合彩
                # if test_class == "MarkSixTest":
                #     suite.add_test(MarkSixTest(test_method, logger_file))
                # # 分分时时彩
                # if test_class == "TimeMmTest":
                #     suite.add_test(TimeMmTest(test_method, logger_file))
                # # 分分PK10
                # if test_class == "PK10MmTest":
                #     suite.add_test(PK10MmTest(test_method, logger_file))
                # pc蛋蛋幸运28
                if test_class == "PcddLucky28Test":
                    suite.add_test(PcddLucky28Test(test_method, logger_file))
                # # 极速3D
                # if test_class == "Speed3DTest":
                #     suite.add_test(Speed3DTest(test_method, logger_file))
                # # 分分快3
                # if test_class == "Fast3MmTest":
                #     suite.add_test(Fast3MmTest(test_method, logger_file))

        # 创建测试报告的文件
        report_file = "/fusion/report_loggers/fusion_automate_report_%s.html" % test_time
        # 实例化TestRunner类，用来运行用例和生成测试报告
        runner = TestRunner(file_name=report_file,
                            verbosity=2,
                            title="FUSION系统自动化测试报告",
                            description="具体测试报告内容如下: ")
        runner.run(suite)

        # 发送测试报告到指定邮箱

        # Email().email_attachment(report_file)

