# coding: utf-8

from runner import Runner


class Main(object):
    """
    自动化测试方案的唯一执行入口
    """
    @staticmethod
    def run_test():
        """
        静态的执行方法
        static method
        指的是 run_ranzhi() 运行的时候，不用实例化Main类
        直接用 Main.run_ranzhi()
        如果没有用 @staticmethod
        需要 Main().run_ranzhi()
        :return:
        """
        print("Start Test ...")
        Runner().run_test()


if __name__ == "__main__":
    Main().run_test()
