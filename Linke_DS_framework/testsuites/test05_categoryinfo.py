# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_categorymanage import CategoryManage
import pageobjects


class CategoryInfoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_category_info001(self):
        # self.login()
        loginpage = LoginPage(self.driver)
        loginpage.login()
        time.sleep(1)
        # loginpage.get_windows_img()  # 调用基类截图方法
        # 点击电商按钮
        linkehomepage = LinkeHomePage(self.driver)
        time.sleep(1)
        linkehomepage.send_ds_link_btn()
        time.sleep(1)

        dshomepage = DSPage(self.driver)
        dshomepage.click_menu("分类管理")
        time.sleep(1)
        categorymanage = CategoryManage(self.driver)
        # categorymanage.click_menu("添加新分类")
        time.sleep(1)
        categorymanage.click_category1_by_index(1)
        time.sleep(1)
        categorymanage.click_category1_by_index(2)
        time.sleep(1)
        categorymanage.click_category1_by_index(3)




if __name__ == '__main__':
    unittest.main()