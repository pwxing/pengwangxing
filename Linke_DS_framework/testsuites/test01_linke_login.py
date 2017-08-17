# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
import pageobjects


class Linke_Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_linke_login001(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("htest","123456", "HY7102$")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        loginpage.assert_page_source(self, u"昨日新增粉丝")
        loginpage.logout()

    def test_linke_login002(self):
        loginpage = LoginPage(self.driver)
        loginpage.linke_login("ytest", "hy2017", "HY7102$")
        time.sleep(1)
        loginpage.get_windows_img()  # 调用基类截图方法
        loginpage.assert_page_source(self, u"昨日新增粉丝")
        loginpage.logout()


if __name__ == '__main__':
    unittest.main()