# coding: utf-8

import time
from common.box import TestSuite, CsvHelper, TestRunner, TestLogger
from TestCase import *


class Runner(object):

    @staticmethod
    def run_test():
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
        TestLogger().info('================== 测试开始 ==================')
        suite = TestSuite()
        # 读取要运行的用例所在的类和方法名称等，获取出来的形式是列表，列表里面有多个字典。如：
        csv_data = CsvHelper().read_data_as_dict("./TestData/csv_test/all_test.csv")

        for row in csv_data:
            test_class = row['class']
            test_method = row['method']
            test_status = int(row['status'])
            if test_status == 1:
                if test_class == "RegisterTest":
                    suite.add_test(test_register.RegisterTest(test_method))
                elif test_class == "HomeLoginTest":
                    suite.add_test(test_home_login.HomeLoginTest(test_method))
            else:
                continue

        # 创建测试报告的文件
        report_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
        report_file = "./TestData/report/fusion_automate_report_%s.html" % report_time
        # 实例化TestRunner类，用来运行用例和生成测试报告
        runner = TestRunner(file_name=report_file,
                            verbosity=2,
                            title="FUSION系统自动化测试报告",
                            description="具体测试报告内容如下: ")
        runner.run(suite)

        # 发送测试报告到指定邮箱
        # Email().email_attachment(report_file)
