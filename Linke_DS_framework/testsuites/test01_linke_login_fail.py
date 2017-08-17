# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
import pageobjects



class Linke_Login_Fail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_fail_001(self):
        u""" 测试不输入用户名"""
        # self.login()
        loginpage = LoginPage(self.driver)
        # 不输入用户名
        loginpage.linke_login("", "123456", "HY7102$")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        # 断言
        BasePage.assert_page_source(self, u"您尚未输入用户名")

    def test_login_fail_002(self):
        u""" 测试不输入密码"""
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("htest", "", "HY7102$")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        BasePage.assert_page_source(self, u"a您11尚未输入密码")

    def test_login_fail_003(self):
        u""" 测试输入错误用户名"""
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("11221test", "12345", "HY7102$")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        BasePage.assert_page_source(self, u"帐号或密码错误")

    def test_login_fail_004(self):
        u""" 测试输入错误密码"""
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("htest", "123123", "HY7102$")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        # 断言
        BasePage.assert_page_source(self, u"帐号或密码错误")

    def test_login_fail_005(self):
        u""" 测试输入错误验证码"""
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("htest", "123123", "abc")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        # 断言
        BasePage.assert_page_source(self, u"验证码错误")

    def test_login_fail_006(self):
        u""" 测试没有输入验证码"""
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("htest", "123456", "")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        # 断言
        BasePage.assert_page_source(self, u"您尚未输入验证码")

if __name__ == '__main__':
    unittest.main()