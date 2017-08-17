#coding=utf-8
import unittest
import time
import test_linke_login_fail
from HTMLTestRunner import HTMLTestRunner

# 加载所有测试用例集
# suite = unittest.TestLoader().discover("testsuites")

# 加载单个测试用例
suite = unittest.TestSuite()
suite.addTest(test_linke_login_fail.Linke_Login_Fail("test_login_fail_001"))
suite.addTest(test_linke_login_fail.Linke_Login_Fail("test_login_fail_002"))
suite.addTest(test_linke_login_fail.Linke_Login_Fail("test_login_fail_003"))
# suite.addTest(test_linke_login_fail.Linke_Login_Fail("test_login_fail_004"))
# suite.addTest(test_linke_login_fail.Linke_Login_Fail("test_login_fail_005"))
# suite.addTest(test_linke_login_fail.Linke_Login_Fail("test_login_fail_006"))


if __name__ == '__main__':
    # 执行用例
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    fp = open('../logs/'+now + 'result.html','wb')
    runner = HTMLTestRunner(stream=fp, title=u'领客电商测试报告', description=u'用例执行情况')
    runner.run(suite)


# if __name__ == '__main__':
#     # 执行用例
#     runner = unittest.TextTestRunner()
#     runner.run(suite)