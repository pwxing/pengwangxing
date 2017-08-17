# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_attributepage import AttributePage
import pageobjects


class AttributePage1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_attribute001(self):
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
        dshomepage.click_menu("属性模板")
        time.sleep(1)
        attributepage = AttributePage(self.driver)
        attributepage.click_menu("模板列表")
        attributepage.click_menu("添加模板")

        attributepage.click_clothes_menu()
        attributepage.click_food_menu()
        attributepage.click_jewelry_menu()
        attributepage.click_shoe_menu()
        attributepage.click_cosmetic_menu()
        attributepage.click_custom_menu()
        attributepage.click_add_attr_btn()
        attributepage.type_attribute_name("seleniumA")
        attributepage.type_attr_option(1, "AAA")
        attributepage.type_attr_option(2, "BBB")
        attributepage.type_attr_option(3, "CCC")
        # attributepage.click_add_attr_submit()

        attributepage.click_menu("模板列表")
        time.sleep(1)
        attributepage.click_edit_attr_btn(1)
        attributepage.type_edit_attr(2,"ZZZ")
        time.sleep(1)
        attributepage.click_edit_attr_submit()












if __name__ == '__main__':
    unittest.main()