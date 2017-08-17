# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from framework.base_page import BasePage
from pageobjects.linke_loginpage import LoginPage
from pageobjects.linke_homepage import LinkeHomePage
from pageobjects.ds_homepage import DSPage
from pageobjects.ds_shipment import Shipment
import pageobjects


class ShipmentTemplate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_shipment(self):
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
        dshomepage.click_menu("运费模板")
        time.sleep(1)
        shipment = Shipment(self.driver)
        shipment.click_menu("添加运费模板")
        self.driver.switch_to.frame(shipment.add_frame)
        shipment.type_template_name("selenium0706")
        shipment.click_weight_fee()
        shipment.type_first_piece("1")
        shipment.type_first_fee("2")
        shipment.type_add_pieces("3")
        shipment.type_add_fee("4")
        time.sleep(1)
        self.driver.switch_to.default_content()
        shipment.click_add_submit()












if __name__ == '__main__':
    unittest.main()